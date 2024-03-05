#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
from itertools import islice
import random
from itertools import groupby
import time
import math
import csv
import numpy as np
import os
import random
import pdb
from network import *
from work_load import *
from solver import *

# In[2]:


#paths: 0:(0,1),(1,2),(2,3),(3,4),(4,5),
        #1:(1,2),(2,3),(3,4),
        #2:(0,1),(1,4),(4,5)
        
# 0:(0,1),1:(1,2),2:(2,3),3:(3,4),4:(4,5),5:(5,6)
network = Network()
network.set_of_paths = {0:[0,1,2,3,4,5],1:[1,2,3],2:[0,5]}
network.each_edge_fidelity = {0:0.94,1:0.94,2:0.94,3:0.94,4:0.94,5:0.94}
network.max_edge_capacity =800
network.each_request_real_paths = {0:[0],1:[1]}
network.each_request_virtual_paths = {0:[2],1:[]}
network.each_request_each_storage_each_block_paths = {0:
                                                      {1:
                                                       {0:[2]}
                                                      }}


network.storage_pairs = [1]
network.each_storage_blocks ={1:[0]} 
network.each_storage_block_paths = {1:{0:[1]}}

#Edge constraint
network.set_E = [0,1,2,3,4,5]
network.each_edge_capacity = {0:600,1:200,2:200,3:200,4:200,5:600}

work_load = Work_load()
  


# In[3]:


results_file_path = "../QSN_results_final_maximizing_rate.csv"
τ_coh_list = np.logspace(1,2,20)
instance_counter = 0
number_of_experiments = 1
request_fidelity_thresholds = [0.6,0.7,0.9,0.8,0.94]
storage_block_thresholds  = [0.7,0.9,0.95,0.8,0.85]
storage_capacities = [i for i in range(100,500,100)]
t_max_list = [t for t in range(10,50,10)]
delta_values = [d for d in range(2,20,2)]
demand_max = 50
feasibility_flag = False
all_instances = (len(t_max_list)*number_of_experiments*
                 len(request_fidelity_thresholds)*
                 len(storage_block_thresholds)*len(storage_capacities)*
                 len(τ_coh_list)*len(delta_values))
start_time = time.time()
for t_max in t_max_list:
    for i in range(number_of_experiments):
        for request_fidelity_threshold in request_fidelity_thresholds:
            if request_fidelity_threshold not in network.fidelity_threshold_values:
                network.fidelity_threshold_values.append(request_fidelity_threshold)
                    
            work_load.each_t_user_pairs={}
            work_load.T = []
            work_load.each_t_requests={}
            for t in range(0,t_max):
                work_load.each_t_user_pairs[t]=[0]
                work_load.T.append(t)
                work_load.each_t_requests[t]=[0,1]
                try:
                    work_load.each_request_each_time_threshold[0][t]=request_fidelity_threshold
                except:
                    work_load.each_request_each_time_threshold[0]={}
                    work_load.each_request_each_time_threshold[0][t]=request_fidelity_threshold
                work_load.each_t_real_requests[t] = [0]

            for storage_block_threshold in storage_block_thresholds:
                for t in range(0,t_max):
                    try:
                        network.each_storage_block_time_treshold[1][0][t]=storage_block_threshold
                    except:
                        try:
                            network.each_storage_block_time_treshold[1][0][t]=storage_block_threshold
                            network.each_storage_block_time_treshold[1][0][t]=storage_block_threshold
                        except:
                            network.each_storage_block_time_treshold[1]={}
                            network.each_storage_block_time_treshold[1][0]={}
                            network.each_storage_block_time_treshold[1][0][t]=storage_block_threshold
                if storage_block_threshold not in network.fidelity_threshold_values:
                    network.fidelity_threshold_values.append(storage_block_threshold)
                
                network.set_each_path_basic_fidelity(t_max,storage_block_threshold)
                network.oracle_for_target_fidelity = {}
#                 for path,b_f in network.each_path_basic_fidelity.items():
#                     print(path,b_f)
                        
                network.set_required_EPR_pairs_for_each_path_each_fidelity_threshold()

                # Demand constriant
                work_load.each_t_each_request_demand = {}
                work_load.set_each_user_pair_demands(len(work_load.T),work_load.each_t_user_pairs,demand_max,2)
#                 print("work_load.each_t_each_request_demand",work_load.each_t_each_request_demand)
                for storage_capacity in storage_capacities:
                    for idx,τ_coh in enumerate(τ_coh_list):
                        network.τ_coh = τ_coh
                        for delta_value in delta_values:
                            network.delta_value  =delta_value
                            network.set_required_EPR_pairs_each_storage_block_freshness()
#                             for path,b_f in network.each_path_basic_fidelity.items():
#                                 print(path,b_f,network.oracle_for_target_fidelity[path])
                            
                            solver =Solver()
                            service_delay = solver.request_service_delay_minimization(network,work_load,
                                                                      1000,i,True,storage_capacity,delta_value,
                                                                                     feasibility_flag)
                            line_items = [t_max,i,request_fidelity_threshold,
                                          storage_block_threshold,
                                          storage_capacity,τ_coh,delta_value,service_delay,
                                          network.each_edge_capacity[1],demand_max,
                                          feasibility_flag
                                         ]
                            with open(results_file_path, 'a') as newFile:                                
                                            newFileWriter = csv.writer(newFile)
                                            newFileWriter.writerow([item for item in line_items])
                                        
                            instance_counter+=1
                            end_time = time.time()
                            duration = round(end_time -start_time,4)
                            start_time = time.time()
                            print("%s / %s d = %s k for t_max %s exp %s req.Fth %s S.Blk.Fth %s stg_C %s τ_coh %s dlta %s "%(instance_counter,
                                                                        all_instances/1000,duration,t_max,
                                                                          i,request_fidelity_threshold,
                                                                        storage_block_threshold,
                                                                        storage_capacity,
                                                                    round(τ_coh,3),delta_value
                                                                         ),end="\r")
                            
#                             time.sleep(30)


# In[4]:




# In[ ]:


# network = Network()

# work_load = Work_load()

# network.computing_blocks_of_qubits() 
# for i in range(100):
#      for edge_fidelity_range in edge_fidelity_ranges:
#         for network_topology,file_path in each_network_topology_file.items():
#             for spike_mean in each_topology_mean_value_spike[network_topology]:
#                 work_load.generat_demands()
#                 each_storage_each_path_number_value = {}
#                 network = Network(config,file_path,False,edge_fidelity_range,max_edge_capacity_value,fidelity_threshold_ranges)
#                 for T in T_values:
#                     for i in range(experiment_repeat):
#                         for storage_capacity in storage_capacities:
#                             for fidelity_threshold_range in fidelity_threshold_ranges:
#                                 for storage_node_selection_scheme in storage_node_selection_schemes:
#                                     selected_storage_nodes = []
#                                     selected_storage_pairs = []
#                                     for num_paths in [1]:
#                                         for number_of_storages in [0,2,4,8,10]:
#                                             """with new storage pairs, we will check the solution for each number of paths(real and virtual)"""
#                                             pairs = []
#                                             network.setup_network()
#                                             for delat_value in delat_values:
#                                                 for life_time in given_life_time_set:
#                                                     for purificaion_scheme in purification_schemes:
#                                                         objective_value=-1
#                                                         if network.path_existance_flag:
#                                                             try:
#                                                                 solver.request_service_delay_minimization()
#                                                             except:
#                                                                 objective_value = -1
#                                                         else:
#                                                             print("oops we do not have even one path for one k at a time!!")
#                                                             objective_value = -1


#                                                     print("for purificaion %s topology %s iteration %s from %s spike mean %s capacity %s  fidelity range %s  life time %s storage %s and path number %s objective_value %s"%
#                                                     (purificaion_scheme,network_topology,i,experiment_repeat, spike_mean,storage_capacity,fidelity_threshold_range,life_time, number_of_storages,num_paths, objective_value))  

#                                                     with open(results_file_path, 'a') as newFile:                                
#                                                         newFileWriter = csv.writer(newFile)
#                                                         newFileWriter.writerow([network_topology,number_of_storages,num_paths,
#                                                                                 life_time,
#                                                                                 objective_value,spike_mean,num_spikes,i,
#                                                                                 storage_node_selection_scheme,
#                                                                                 fidelity_threshold_range,cyclic_workload,
#                                                                                 distance_between_users,storage_capacity,edge_fidelity_range,delat_value,purificaion_scheme]) 
                                            


# In[ ]:


# def EGR_for_dynamic_population(each_network_topology_file,spike_mean,num_spikes,experiment_repeat,storage_node_selection_scheme):
#     for spike_mean in spike_means:
#         for network_topology,file_path in each_network_topology_file.items():
#             import pdb
#             each_storage_each_path_number_value = {}
#             network = Network(file_path)
            
#             for i in range(experiment_repeat):
        
#                 network = Network(file_path)
#                 network.get_user_pairs_over_dynamicly_chaning_population(number_of_user_pairs,distance_between_users,number_of_time_slots)

#                 work_load = Work_load(number_of_time_slots,"time_demands_file.csv")

#                 objective_values = []
#                 selected_storage_nodes = []
#                 selected_storage_pairs = []

#                 #nx.draw(network.g,with_labels=True)
#                 # plt.show()
#                 network.reset_pair_paths()
#                 pairs = []
#                 print("network.each_t_user_pairs",network.each_t_user_pairs)
#                 for t,user_pairs in network.each_t_user_pairs.items():            
#                     for user_pair in user_pairs:
#                         if user_pair not in pairs:
#                             pairs.append(user_pair)
#                 network.get_each_user_pair_real_paths(pairs)

#                 import pdb
#                 #pdb.set_trace()


#                 """select and add new storage pairs"""

#                 for number_of_storages in range(7):
#                     print("for number of storages round  ",number_of_storages)
#                     network.get_new_storage_pairs(number_of_storages,storage_node_selection_scheme)
#                     work_load.reset_variables()
#                     work_load.set_each_time_requests(network.each_t_user_pairs,network.storage_pairs)
#                     work_load.set_each_time_real_requests(network.each_t_user_pairs)
#                     """with new storage pairs, we will check the solution for each number of paths(real and virtual)"""
#                     for num_paths in range(3,4):

#                         path_counter_id = 0
#                         #print("network.storage_pairs",network.storage_pairs)
#                         #import pdb
#                         #pdb.set_trace()
#                         network.get_each_user_pair_real_paths(network.storage_pairs)
#                         if number_of_storages==1:
#                             number_of_storages = 2

#                         """first we add the real paths between storage pairs"""

#                         print("for iteration %s storage %s and path number %s"%(i,number_of_storages,num_paths))
#                         for storage_pair in network.storage_pairs:
#                             #print("going to get real paths between storage pair ",storage_pair)
#                             paths = network.get_real_path(storage_pair,num_paths)
#                             #print("got paths",paths)
#                             for path in paths:
#                                 network.set_each_path_length(path_counter_id,path)
#                                 network.set_of_paths[path_counter_id] = path
#                                 network.each_path_path_id[tuple(path)] = path_counter_id
#                                 try:
#                                     network.each_request_real_paths[storage_pair].append(path_counter_id)
#                                 except:
#                                     network.each_request_real_paths[storage_pair]=[path_counter_id]
#                                 try:
#                                     network.each_storage_real_paths[storage_pair].append(path)
#                                 except:
#                                     network.each_storage_real_paths[storage_pair]=[path]
#                                 #print("*** we used path_counter_id",path_counter_id)
#                                 path_counter_id+=1

#                         across_all_time_slots_pairs = []
#                         for t,user_pairs in network.each_t_user_pairs.items():
#                             for user_pair in user_pairs:
#                                 if user_pair not in across_all_time_slots_pairs:
#                                     across_all_time_slots_pairs.append(user_pair)
#                         all_sub_paths = []
#                         for user_pair in across_all_time_slots_pairs:
#                             paths = network.get_real_path(user_pair,num_paths)
#                             #print("we got real paths for user pair",user_pair,paths)
#                             for path in paths:
#                                 network.set_of_paths[path_counter_id] = path
#                                 network.set_each_path_length(path_counter_id,path)
#                                 network.each_path_path_id[tuple(path)] = path_counter_id
#                                 try:
#                                     network.each_request_real_paths[user_pair].append(path_counter_id)
#                                 except:
#                                     network.each_request_real_paths[user_pair]=[path_counter_id]
                                
#                                 path_counter_id+=1
    
#                             for storage_pair in network.storage_pairs:
#                                 """add one new path to the previous paths"""
#                                 for real_sub_path in network.each_storage_real_paths[storage_pair]:
                                    
#                                     paths = network.get_paths_to_connect_users_to_storage(user_pair,real_sub_path,num_paths)
#     #                               
#                                     this_sub_path_id = network.each_path_path_id[tuple(real_sub_path)]
                                    

#                                     for path in paths:
#                                         network.set_each_path_length(path_counter_id,path)
#                                         """we remove the sub path that is connecting two storage pairs 
#                                         from the path because we do not want to check the edge capacity for the edges of this subpath"""
#     #                                     print("we set length %s for path %s having sub path %s with ID %s"%(len(path),path,real_sub_path,this_sub_path_id))
#                                         try:
#                                             network.each_request_virtual_paths_include_subpath[user_pair][this_sub_path_id].append(path_counter_id)
#                                         except:
#                                             try:
#                                                 network.each_request_virtual_paths_include_subpath[user_pair][this_sub_path_id]=[path_counter_id]
#                                             except:
#                                                 network.each_request_virtual_paths_include_subpath[user_pair]={}
#                                                 network.each_request_virtual_paths_include_subpath[user_pair][this_sub_path_id]=[path_counter_id]
#                                         if this_sub_path_id not in all_sub_paths:
#                                             all_sub_paths.append(this_sub_path_id)
#                                         path = network.remove_storage_pair_real_path_from_path(real_sub_path,path)
#                                         #print("and after removing sub path we have ",path,real_sub_path,len(path))
#                                         network.set_of_paths[path_counter_id] = path
#                                         try:
#                                             network.each_request_virtual_paths[user_pair].append(path_counter_id)
#                                         except:
#                                             network.each_request_virtual_paths[user_pair]=[path_counter_id]
#                                         #print("*** we used path_counter_id",path_counter_id)
#                                         path_counter_id+=1


#                                     for pair in network.storage_pairs:
#                                         network.each_request_virtual_paths[pair]=[]

#                                     #print("for user pair %s to storage pair %s we got real paths and it is:"%(user_pair,storage_pair))

#                         if number_of_storages==0:
#                             for t,pairs in network.each_t_user_pairs.items():
#                                 for pair in pairs:
#                                     network.each_request_virtual_paths[pair]=[]

#                         for j in network.storage_pairs:
#                             for sub_path_id in all_sub_paths:
#                                 try:
#                                     network.each_request_virtual_paths_include_subpath[j][sub_path_id] = []
#                                 except:
#                                     network.each_request_virtual_paths_include_subpath[j]={}
#                                     network.each_request_virtual_paths_include_subpath[j][sub_path_id] = []
#                         for t in range(number_of_time_slots):
#                             for k in work_load.each_t_requests[t]:
#                                 try:
#                                     if k in list(network.each_request_virtual_paths_include_subpath.keys()):
#                                         pass
#                                     else:
#                                         network.each_request_virtual_paths_include_subpath[k]= {}
#                                 except:
#                                     network.each_request_virtual_paths_include_subpath[k]= {}

#                         """we set the capacity of each storage node"""

#                         network.set_storage_capacity()

#                         """we add new storage pairs as our user pairs and set the demand for them zero"""

#                         work_load.set_storage_pairs_as_user_pairs(network.storage_pairs)

#                         """we print all variables to check the variables and values"""

#                         life_time_set = [1000,2]
#                         for life_time in life_time_set:
#                             """solve the optimization"""        
#                             try:
#                                 objective_value=0
#                                 try:
#                                     objective_value,each_inventory_per_time_usage = CPLEX_maximizing_entanglement_generation(network,work_load,life_time,i)
#                                 except ValueError:
#                                     print(ValueError)
#                                     pass
#                                 objective_values.append(objective_value)
#                                 if 0<objective_value<distance_between_users-1:
                                    

#                                 print("the objective value for %s storage nodes and %s paths between each pair of nodes is %s"%(number_of_storages,num_paths,objective_value))

#     #                             print(each_inventory_per_time_usage)
#                                 #time.sleep(10)
#                                 for storage_pair,t_saved_EPRs in each_inventory_per_time_usage.items():
#                                     for t ,EPRs in t_saved_EPRs.items():
#                                         with open(inventory_utilization_results_file_path, 'a') as newFile:                                
#                                             newFileWriter = csv.writer(newFile)
#                                             newFileWriter.writerow([topology,number_of_storages,num_paths,i,life_time,storage_pair,t,EPRs,storage_node_selection_scheme]) 

#                                 with open(results_file_path, 'a') as newFile:                                
#                                     newFileWriter = csv.writer(newFile)
#                                     newFileWriter.writerow([topology,number_of_storages,num_paths,life_time,objective_value,i,storage_node_selection_scheme]) 

#                             except ValueError:
#                                 #pass
#                                 print(ValueError)
#                 print("until the %s th iteration we have %s"%(i,each_storage_each_path_number_value)) 

# In[ ]:



