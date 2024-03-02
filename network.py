#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

# In[ ]:


class Network:
    def __init__(self):
        self.global_each_basic_fidelity_target_fidelity_required_EPRs  = {}
        self.oracle_for_target_fidelity = {}
        self.each_path_basic_fidelity = {}
        self.fidelity_threshold_values = []
        self.set_of_paths  ={}
        self.each_storage_block_paths ={}
        self.each_storage_block_time_treshold = {}
        self.τ_coh = 10
    def each_storage_block_freshness(self,j,b,delat_value):
        return 1/2*(1-np.exp(-delat_value/self.τ_coh))
    def check_path_include_edge(self,edge,p):
        if edge in self.set_of_paths[p]:
            return True
        elif edge not  in self.set_of_paths[p]:
            return False
    def set_each_path_basic_fidelity(self,storage_block_threshold):
        
        self.each_path_basic_fidelity = {}
        for path,path_edges in self.set_of_paths.items():
            if path in [0,1]:
                if path_edges:
                    basic_fidelity = 1/4+(3/4)*(4*self.each_edge_fidelity[path_edges[0]]-1)/3
                    for edge in path_edges[1:]:
                        basic_fidelity  = (basic_fidelity)*((4*self.each_edge_fidelity[edge]-1)/3)
                    basic_fidelity = basic_fidelity
                else:
                    print("Error")
                    break
            else:
                basic_fidelity = 1/4+(3/4)*(4*self.each_edge_fidelity[path_edges[0]]-1)/3
                basic_fidelity  = (basic_fidelity)*((4*max(storage_block_threshold,self.each_path_basic_fidelity[1])-1)/3)
                basic_fidelity  = (basic_fidelity)*((4*self.each_edge_fidelity[5]-1)/3)
                basic_fidelity = basic_fidelity
            self.each_path_basic_fidelity[path]= round(basic_fidelity,3)
    def T_sequential_no_cutoff(τ_coh, mu_link, F_link,links):
        """ Calculate performance metrics for asynchronous sequential scheme using analytical formulas
        inputs:
            τ_coh: coherence time of quantum memories
            mu_link: parameter in 2qubit depolarizing channel describing noisy link-level entanglement and
            entanglement swapping error
            F_link: fidelity of link level entanglement (i.e.,quality of locally generated Bell pairs)
            links: list of segment (link) lengths in km
        outputs:
            Raw_rate: 1/ expected value of total time for e2e entanglement delivery
            *** application specific quantities:
            skr: secret key rate for qkd (does not include idle times of end memories)
            F_e2e: e2e entanglement fidelity for entanglement distrubtion (does include idle times of end memories)
        """
        if type(links) != np.ndarray:
            links = np.array(links)
        τs = links/c
        T_tot = 2* np.sum( τs / (p_link*Trans(links)) )

        raw_rate = 1/T_tot
        N_links = len(links) # number of links, i.e. no. of repeaters + 1
        mu_e2e = mu_link**(2*N_links-1)
        # secret key rate calculations
        f_memory_qkd = np.prod( p_link*Trans(links[1:])*np.exp(-4*τs[1:]/τ_coh)/(1- (1-p_link*Trans(links[1:]))*np.exp(-2*τs[1:]/τ_coh) )  )
        f_e2e_qkd = 0.5 + 0.5 * (2*F_link-1)**N_links *f_memory_qkd
        ex = (1 - mu_e2e)/2
        ez = (1 + mu_e2e)/2 - mu_e2e * f_e2e_qkd
        skr = raw_rate * (1-h([ex])-h([ez]))
        #  fidelity of e2e Bell pairs
        Le2e = np.sum(links)
        τe2e = Le2e/c
        f_memory_bell = np.exp(-3*τe2e/τ_coh) *np.prod(p_link*Trans(links[1:])*np.exp(-4*τs[1:]/τ_coh)/(1- (1-p_link*Trans(links[1:]))*np.exp(-4*τs[1:]/τ_coh) ) )
        f_e2e_bell = 0.5 + 0.5 * (2*F_link-1)**N_links *f_memory_bell
        F_e2e = mu_e2e * f_e2e_bell + (1-mu_e2e)/4

        return raw_rate, skr, F_e2e
    def get_path_length(self,p):
        return len(self.set_of_paths[p])
    def get_required_purification_EPR_pairs(self,p,threshold):
#         print("we are getting the required EPR pairs for path %s to reach threshold %s"%(p,threshold))
        return self.oracle_for_target_fidelity[p][threshold]
    def set_required_EPR_pairs_for_each_path_each_fidelity_threshold(self):
        targets = []
        for t in self.fidelity_threshold_values:
            targets.append(t)
        targets.append(0.6)
        targets.sort()
        for path,path_basic_fidelity in self.each_path_basic_fidelity.items():
            #print("for path %s with lenght %s fidelity %s"%(path,self.each_path_legth[path],path_basic_fidelity))
            try:
                if path_basic_fidelity in self.global_each_basic_fidelity_target_fidelity_required_EPRs:
                    
                    for target in targets:
                        
                        #print("getting required rounds for initial F %s to target %s path length %s"%(path_basic_fidelity,target,self.each_path_legth[path]))
                        n_avg = self.global_each_basic_fidelity_target_fidelity_required_EPRs[path_basic_fidelity][target]
                        #print("we got ",n_avg)
                        try:
                            self.oracle_for_target_fidelity[path][target] = n_avg
                            
                        except:
                            self.oracle_for_target_fidelity[path] = {}
                            self.oracle_for_target_fidelity[path][target] = n_avg
                            
                else:
                    
                    for target in targets:
                        
                        #print("getting required rounds for initial F %s to target %s path lenght %s "%(path_basic_fidelity,target,self.each_path_legth[path]))
#                         n_avg = self.get_avg_epr_pairs(path_basic_fidelity ,target)
                        n_avg = self.get_avg_epr_pairs_DEJMPS(path_basic_fidelity ,target)
                        #print("we got ",n_avg)
                        try:
                            self.global_each_basic_fidelity_target_fidelity_required_EPRs[path_basic_fidelity][target] =n_avg 
                        except:
                            self.global_each_basic_fidelity_target_fidelity_required_EPRs[path_basic_fidelity]={}
                            self.global_each_basic_fidelity_target_fidelity_required_EPRs[path_basic_fidelity][target] =n_avg 
                            
                        try:
                            self.oracle_for_target_fidelity[path][target] = n_avg
                            
                        except:
                            self.oracle_for_target_fidelity[path] = {}
                            self.oracle_for_target_fidelity[path][target] = n_avg
                            
            except:
                
                for target in targets:
                    n_avg = self.get_avg_epr_pairs(path_basic_fidelity ,target)
                    try:
                        self.global_each_basic_fidelity_target_fidelity_required_EPRs[path_basic_fidelity][target] =n_avg 
                    except:
                        self.global_each_basic_fidelity_target_fidelity_required_EPRs[path_basic_fidelity]={}
                        self.global_each_basic_fidelity_target_fidelity_required_EPRs[path_basic_fidelity][target] =n_avg                     
                    try:
                        self.oracle_for_target_fidelity[path][target] = n_avg
                        
                    except:
                        self.oracle_for_target_fidelity[path] = {}
                        self.oracle_for_target_fidelity[path][target] = n_avg
                        
    def get_avg_epr_pairs_DEJMPS(self,F_init,F_target):
        F_curr = F_init
        F2 = F3 = F4 = (1-F_curr)/3
        n_avg = 1.0
        while(F_curr < F_target):
            F_curr,F2, F3, F4, succ_prob = self.get_next_fidelity_and_succ_prob_DEJMPS(F_curr, F2, F3, F4)
            n_avg = n_avg*(2/succ_prob)
        return  n_avg
    def get_next_fidelity_and_succ_prob_DEJMPS(self,F1,F2,F3,F4):
        succ_prob = (F1+F2)**2 + (F3+F4)**2
        output_fidelity1 = (F1**2 + F2**2)/succ_prob
        output_fidelity2 = (2*F3*F4)/succ_prob
        output_fidelity3 = (F3**2 + F4**2)/succ_prob
        output_fidelity4 = (2*F1*F2)/succ_prob

        return output_fidelity1, output_fidelity2, output_fidelity3, output_fidelity4, succ_prob
    def setup_network(self,number_of_user_pairs,distance_between_users,number_of_time_slots,
                      number_of_storages,spike_mean,num_spikes,storage_capacity,
                      fidelity_threshold_range,storage_node_selection_scheme,
                      num_paths
                     ):
        self.reset_variables()
        self.get_user_pairs(number_of_user_pairs,distance_between_users,number_of_time_slots)
        #work_load = Work_load(number_of_time_slots,"time_demands_file.csv")
        """we set the demands for each user pair"""
        if setting_demands=="python_library":
            self.set_each_user_pair_demands(number_of_time_slots,network.each_t_user_pairs,spike_mean,num_spikes)
        else:
            self.set_each_user_pair_demands_randomly(number_of_time_slots,network.each_t_user_pairs,spike_mean,num_spikes)
        """we set at least one demand for each time to avoid divided by zero error"""
        self.check_demands_per_each_time(network.each_t_user_pairs)
        for storage_capacity in storage_capacities:
            for fidelity_threshold_range in fidelity_threshold_ranges:
                self.fidelity_threshold_range = fidelity_threshold_range
                self.set_each_request_fidelity_threshold()
#                             print("self.each_request_threshold ",network.each_request_threshold)
                for storage_node_selection_scheme in storage_node_selection_schemes:
                    selected_storage_nodes = []
                    selected_storage_pairs = []
                    for num_paths in [1]:
                        self.reset_storage_pairs()
                        for number_of_storages in [0,2,4,8,10]:
                            try:
                                """with new storage pairs, we will check the solution for each number of paths(real and virtual)"""

                                pairs = []
                                """select and add new storage pairs"""
                                available_flag = network.get_new_storage_pairs(number_of_storages,storage_node_selection_scheme)
                                self.set_each_storage_fidelity_threshold()
                                self.set_paths_in_the_network()
                            except:
                                pass

