#!/usr/bin/env python
# coding: utf-8

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
    def each_storage_block_freshness(self,j,b,delat_value):
        return 1
    def check_path_include_edge(self,edge,p):
        if edge in self.set_of_paths[p]:
            return True
        elif edge not  in self.set_of_paths[p]:
            return False
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

