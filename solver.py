#!/usr/bin/env python
# coding: utf-8

# In[12]:



import csv
import os
import sys
from docplex.mp.progress import *
from docplex.mp.progress import SolutionRecorder
import docplex.mp.model as cpx
import numpy as np
import networkx as nx
import time
import random
from config import get_config
from network import *
from work_load import *

# In[8]:


class Solver:
    def __init__(self):
        pass
    def request_service_delay_minimization(self,network,work_load,life_time,iteration,cyclic_workload,feasibility_flag):        

        import docplex.mp.model as cpx
        opt_model = cpx.Model(name="Storage problem model"+str(iteration))
        w_vars = {}
        u_vars = {}
        
        w_vars  = {(k,p,t): opt_model.continuous_var(lb=0, ub= network.max_edge_capacity,
                                  name="w_{0}_{1}_{2}".format(k,p,t))  for t in work_load.T 
                   for k in work_load.each_t_user_pairs[t]+network.storage_pairs 
                   for p in network.each_request_real_paths[k]+network.each_request_virtual_paths[k]}
#         print("w_vars",w_vars)
        u_vars  = {(j,b,t): opt_model.continuous_var(lb=0, ub= network.storage_capacity,
                                      name="u_{0}_{1}_{2}".format(j,b,t))  for t in work_load.T 
                       for j in network.storage_pairs for b in network.each_storage_blocks[j] 
                   }   
    
#         opt_model.add_constraint(opt_model.sum(u_vars[1,0,19]) == 10000 
#             , ctname="static_const{0}_{1}".format(19,1))
#         print("u_vars",u_vars)
        if life_time ==1000:
            #inventory evolution constraint
            for t in work_load.T[1:]:
                for j in network.storage_pairs:
                    for b in network.each_storage_blocks[j]:
#                         for p_s in network.each_request_real_paths[j,b]:
                        if cyclic_workload:
                            opt_model.add_constraint(u_vars[j,b,t] == u_vars[j,b,(t-1)]/network.get_each_storage_block_freshness(j,b)-
                            opt_model.sum(w_vars[k,p,(t-1)] *
                            network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,b,t))
                            for k in work_load.each_t_requests[t] if k!=j 
                            for p in network.each_request_each_storage_each_block_paths[k][j][b])*network.delta_value
                            +opt_model.sum(w_vars[j,p2,(t-1)] for p2 in network.each_storage_block_paths[j][b])*network.delta_value
                                                 ,ctname="inventory_evolution_{0}_{1}_{2}".format(t,j,b))
#                         else:
#                             opt_model.add_constraint(u_vars[t,j,b,p_s] == u_vars[t-1,j,b,p_s]/network.get_each_storage_block_freshness(j,b)-
#                             opt_model.sum(w_vars[t-1,k,p] *
#                             network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(k,t))
#                             for k in work_load.each_t_requests[t] if k!=j 
#                             for p in network.each_request_virtual_paths_include_subpath[k][p_s])*network.delta_value
#                             +opt_model.sum(w_vars[t-1,j,p_s])*network.delta_value
#                                                  , ctname="inventory_evolution_{0}_{1}".format(t,j,p_s))
        else:
            #inventory evolution constraint
            for t in work_load.T[1:]:
                for j in network.storage_pairs:
                    for b in network.each_storage_blocks[j]:
                        for p_s in network.each_request_real_paths[j,b]:

                            if cyclic_workload:
                                opt_model.add_constraint(u_vars[j,b,t] == -
                                opt_model.sum(w_vars[k,p,(t-1)] *
                                network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,b,t))
                                for k in work_load.each_t_requests[t] if k!=j 
                                for p in network.each_request_each_storage_each_block_paths[k][j][b] 
                                )*network.delta_value
                                + opt_model.sum(w_vars[j,p_s,(t-1)])*network.delta_value
                                                     , ctname="inventory_evolution_{0}_{1}".format(t,j,p_s))
                            else:
                                opt_model.add_constraint(u_vars[j,b,t] == -
                                opt_model.sum(w_vars[k,p,t-1] *
                                network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,b,t))
                                for k in work_load.each_t_requests[t] if k!=j 
                                for p in network.each_request_each_storage_each_block_paths[k][j][b] 
                                )*network.delta_value
                                + opt_model.sum(w_vars[j,p_s,t-1])*network.delta_value
                                                     , ctname="inventory_evolution_{0}_{1}".format(t,j,p_s))

        # serving from inventory constraint
        for t in work_load.T[1:]:
            for j in network.storage_pairs:
                for b in network.each_storage_blocks[j]:
                    opt_model.add_constraint(opt_model.sum(w_vars[k,p,t]*
                    network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,b,t))
                    for k in work_load.each_t_user_pairs[t] if k!=j 
                    for p in network.each_request_each_storage_each_block_paths[k][j][b]
                    )*network.delta_value<=u_vars[j,b,t]
                                         , ctname="inventory_serving_{0}_{1}_{2}".format(t,j,b))  


        if feasibility_flag:
            # Demand constriant
            for t in work_load.T[1:]:
                for k in  work_load.each_t_user_pairs[t]:
                    opt_model.add_constraint(opt_model.sum(w_vars[k,p,t]
                    for p in network.each_request_real_paths[k]+network.each_request_virtual_paths[k]) >= 
                            work_load.each_t_each_request_demand[t][k], ctname="constraint_{0}_{1}".format(t,k))

        #Edge constraint
        for t in work_load.T:
            for edge in network.set_E:
                opt_model.add_constraint(
                    opt_model.sum(w_vars[k,p,t]*
                    network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,b,t)) 
                    for k in work_load.each_t_user_pairs[t]+network.storage_pairs
                    for p in network.each_request_real_paths[k]+network.each_request_virtual_paths[k] if network.check_path_include_edge(edge,p))

                     <= network.each_edge_capacity[edge], ctname="edge_capacity_{0}_{1}".format(t,edge))

        # storage servers capacity constraint
    #     storage_capacity = storage_capacity/delta_value
        for t in work_load.T:
            #for s1 in network.storage_nodes:
            for j in network.storage_pairs:
                opt_model.add_constraint(opt_model.sum(u_vars[j,b,t]
                    for b in network.each_storage_blocks[j]) <= network.storage_capacity 
            , ctname="storage_capacity_constraint_{0}_{1}".format(t,j))

        # constraints for serving from storage at time zero and 1 should be zero
#         if not cyclic_workload:
#             for t in [0,1]:
#                 opt_model.add_constraint(opt_model.sum(w_vars[t,k,p]
#                         for k in work_load.each_t_requests[t] for p in network.each_request_virtual_paths[k] 
#                         )<=0, ctname="serving_from_inventory_{0}".format(t))

#         # constraints for putting in storage at time zero  should be zero
#         """this is becasue we start the formulation from 1 and not from zero and we have t-1 in our formulation"""
#         for t in [0]:
#             opt_model.add_constraint(opt_model.sum(w_vars[t,k,p]
#                     for k in work_load.each_t_requests[t] for p in network.each_request_real_paths[k] 
#                     )<=0, ctname="storing_in_inventory_{0}".format(t))   


#         # constraint for inventory is zero at time zero 
#         if not cyclic_workload:
        for t in [0]:
            for j in network.storage_pairs:
                 for b in network.each_storage_blocks[j]:
                        opt_model.add_constraint(u_vars[j,b,t] <=0, ctname="storage_capacity_constraint_{0}_{1}_{2}".format(j,b,t))

        """defining an objective, which is a linear expression"""
        if feasibility_flag:
            objective = opt_model.sum(1/len(work_load.T[1:])*1/len(work_load.each_t_real_requests[t])
                                      *1/work_load.each_t_each_request_demand[t][k]
                                      *(w_vars[k,p,t] * network.get_path_length(p)) for t in work_load.T[1:]
                                      for k in work_load.each_t_user_pairs[t] 
                                      for p in network.each_request_real_paths[k]+network.each_request_virtual_paths[k]
                                      )
            opt_model.minimize(objective)
        else:
            objective = opt_model.sum((w_vars[k,p,t]) for t in work_load.T[-1:]
                                      for k in work_load.each_t_user_pairs[t] 
                                      for p in network.each_request_real_paths[k]+network.each_request_virtual_paths[k]
                                      )
            opt_model.maximize(objective)


        

#         opt_model.print_information()
        opt_model.solve()
        print("docplex.mp.solution",opt_model.solution)
        for t in work_load.T[-1:]:
            for k in work_load.each_t_user_pairs[t]:
                for p in network.each_request_real_paths[k]+network.each_request_virtual_paths[k]:
                    print("path %s basic fidleity %s g function %s==%s rate is %s "%(p,
                                                                                 network.each_path_basic_fidelity[p],
                                                                                 network.oracle_for_target_fidelity[p][work_load.get_each_request_threshold(network,k,10,t)],
                                                                                 network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,10,t)),
                                                                                 w_vars[k,p,t].solution_value))

                    
        for t in work_load.T[-1:]:
            for edge in network.set_E:
                edge_sum = 0
                for k in work_load.each_t_user_pairs[t]:
                    for p in network.each_request_real_paths[k]+network.each_request_virtual_paths[k]:
                        if network.check_path_include_edge(edge,p):
                            edge_sum+= w_vars[k,p,t].solution_value* network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,10,t))
                            print("for path %s rate is %s distillation %s product %s "%(p,w_vars[k,p,t].solution_value,network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,10,t)),w_vars[k,p,t].solution_value* network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,10,t))))
                

                print("for edge %s we have load %s its capacity is %s "%(edge,edge_sum,network.each_edge_capacity[edge]))
                    
                    
                    
        for t in work_load.T[1:]:
            for j in network.storage_pairs:
                for b in network.each_storage_blocks[j]:
                    sum_served_from_storage = 0
                    for k in work_load.each_t_user_pairs[t]:
                        
                        for p in network.each_request_each_storage_each_block_paths[k][j][b]:
                            sum_served_from_storage +=w_vars[k,p,t].solution_value* network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,b,t))
                            if sum_served_from_storage>0:
                                print("virtual path %s has rate %s g() %s with distillation %s "%(p,w_vars[k,p,t].solution_value,
                                                                                                  network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,b,t)),
                                                                                      w_vars[k,p,t].solution_value* network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,b,t))))
                    if sum_served_from_storage>0:
                        print("served from storage %s cannot be higher than %s with fr() = %s "%(sum_served_from_storage*network.delta_value,
                                                                                                 u_vars[j,b,t].solution_value,
                                                                                                network.each_storage_block_delat_value_required_EPRs[j][b][network.delta_value]))

                        
                        
                    
#         time.sleep(10)
#         import pdb
#         pdb.set_trace()
        objective_value = -1
        try:
            if opt_model.solution:
                objective_value =opt_model.solution.get_objective_value()
        except ValueError:
            print(ValueError)

            #print("******************************** end *************************************")   



        opt_model.clear()
        return objective_value


    def request_service_delay_minimization_discret(self,network,work_load,life_time,iteration,cyclic_workload,storage_capacity,delat_value,feasibility_flag):        

        import docplex.mp.model as cpx
        opt_model = cpx.Model(name="Storage problem model"+str(iteration))
        w_vars = {}
        u_vars = {}
        
        w_vars  = {(t,k,p): opt_model.integer_var(lb=0, ub= network.max_edge_capacity,
                                  name="w_{0}_{1}_{2}".format(t,k,p))  for t in work_load.T 
                   for k in work_load.each_t_user_pairs[t]+network.storage_pairs 
                   for p in network.each_request_real_paths[k]+network.each_request_virtual_paths[k]}
#         print("w_vars",w_vars)
        u_vars  = {(j,b,t): opt_model.integer_var(lb=0, ub= network.max_edge_capacity,
                                      name="u_{0}_{1}_{2}".format(j,b,t))  for t in work_load.T 
                       for j in network.storage_pairs for b in network.each_storage_blocks[j] 
                   }   
#         print("u_vars",u_vars)
        if life_time ==1000:
            #inventory evolution constraint
            for t in work_load.T[1:]:
                for j in network.storage_pairs:
                    for b in network.each_storage_blocks[j]:
#                         for p_s in network.each_request_real_paths[j,b]:
                        if cyclic_workload:
                            opt_model.add_constraint(u_vars[j,b,t] == u_vars[j,b,(t-1)%len(work_load.T)]/network.get_each_storage_block_freshness(j,b)-
                            opt_model.sum(w_vars[(t-1)%len(work_load.T),k,p] *
                            network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,b,t))
                            for k in work_load.each_t_requests[t] if k!=j 
                            for p in network.each_request_each_storage_each_block_paths[k][j][b])*delat_value
                            +opt_model.sum(w_vars[(t-1)%len(work_load.T),j,p2] for p2 in network.each_storage_block_paths[j][b])*delat_value
                                                 ,ctname="inventory_evolution_{0}_{1}_{2}".format(t,j,b))
#                         else:
#                             opt_model.add_constraint(u_vars[t,j,b,p_s] == u_vars[t-1,j,b,p_s]/network.get_each_storage_block_freshness(j,b)-
#                             opt_model.sum(w_vars[t-1,k,p] *
#                             network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(k,t))
#                             for k in work_load.each_t_requests[t] if k!=j 
#                             for p in network.each_request_virtual_paths_include_subpath[k][p_s])*delat_value
#                             +opt_model.sum(w_vars[t-1,j,p_s])*delat_value
#                                                  , ctname="inventory_evolution_{0}_{1}".format(t,j,p_s))
        else:
            #inventory evolution constraint
            for t in work_load.T[1:]:
                for j in network.storage_pairs:
                    for b in network.each_storage_blocks[j]:
                        for p_s in network.each_request_real_paths[j,b]:

                            if cyclic_workload:
                                opt_model.add_constraint(u_vars[j,b,t] == -
                                opt_model.sum(w_vars[(t-1)%len(work_load.T),k,p] *
                                network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,b,t))
                                for k in work_load.each_t_requests[t] if k!=j 
                                for p in network.each_request_each_storage_each_block_paths[k][j][b] 
                                )*delat_value
                                + opt_model.sum(w_vars[(t-1)%len(work_load.T),j,p_s])*delat_value
                                                     , ctname="inventory_evolution_{0}_{1}".format(t,j,p_s))
                            else:
                                opt_model.add_constraint(u_vars[j,b,t] == -
                                opt_model.sum(w_vars[t-1,k,p] *
                                network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,b,t))
                                for k in work_load.each_t_requests[t] if k!=j 
                                for p in network.each_request_each_storage_each_block_paths[k][j][b] 
                                )*delat_value
                                + opt_model.sum(w_vars[t-1,j,p_s])*delat_value
                                                     , ctname="inventory_evolution_{0}_{1}".format(t,j,p_s))

        # serving from inventory constraint
        for t in work_load.T[1:]:
            for j in network.storage_pairs:
                for b in network.each_storage_blocks[j]:
                    opt_model.add_constraint(opt_model.sum(w_vars[t,k,p]*
                    network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,b,t))
                    for k in work_load.each_t_user_pairs[t] if k!=j 
                    for p in network.each_request_each_storage_each_block_paths[k][j][b]
                    )*delat_value<=u_vars[j,b,t]
                                         , ctname="inventory_serving_{0}_{1}_{2}".format(t,j,b))  


        if feasibility_flag:
            # Demand constriant
            for t in work_load.T[1:]:
                for k in  work_load.each_t_user_pairs[t]:
                    opt_model.add_constraint(opt_model.sum(w_vars[t,k,p]
                    for p in network.each_request_real_paths[k]+network.each_request_virtual_paths[k]) >= 
                            work_load.each_t_each_request_demand[t][k], ctname="constraint_{0}_{1}".format(t,k))

        #Edge constraint
        for t in work_load.T:
            for edge in network.set_E:
                opt_model.add_constraint(
                    opt_model.sum(w_vars[t,k,p]*
                    network.get_required_purification_EPR_pairs(p,work_load.get_each_request_threshold(network,k,b,t)) 
                    for k in work_load.each_t_user_pairs[t]+network.storage_pairs
                    for p in network.each_request_real_paths[k]+network.each_request_virtual_paths[k] if network.check_path_include_edge(edge,p))

                     <= network.each_edge_capacity[edge], ctname="edge_capacity_{0}_{1}".format(t,edge))

        # storage servers capacity constraint
    #     storage_capacity = storage_capacity/delat_value
        for t in work_load.T:
            #for s1 in network.storage_nodes:
            for j in network.storage_pairs:
                opt_model.add_constraint(opt_model.sum(u_vars[j,b,t]
                    for b in network.each_storage_blocks[j]) <= storage_capacity 
            , ctname="storage_capacity_constraint_{0}_{1}".format(t,j))

        # constraints for serving from storage at time zero and 1 should be zero
#         if not cyclic_workload:
#             for t in [0,1]:
#                 opt_model.add_constraint(opt_model.sum(w_vars[t,k,p]
#                         for k in work_load.each_t_requests[t] for p in network.each_request_virtual_paths[k] 
#                         )<=0, ctname="serving_from_inventory_{0}".format(t))

#         # constraints for putting in storage at time zero  should be zero
#         """this is becasue we start the formulation from 1 and not from zero and we have t-1 in our formulation"""
#         for t in [0]:
#             opt_model.add_constraint(opt_model.sum(w_vars[t,k,p]
#                     for k in work_load.each_t_requests[t] for p in network.each_request_real_paths[k] 
#                     )<=0, ctname="storing_in_inventory_{0}".format(t))   


#         # constraint for inventory is zero at time zero 
#         if not cyclic_workload:
#             for t in [0]:
#                 for j in network.storage_pairs:
#                      for p_s in network.each_request_real_paths[j]:
#                             opt_model.add_constraint(u_vars[t,j,p_s] <=0, ctname="storage_capacity_constraint_{0}_{1}_{2}".format(t,j,p_s))

        """defining an objective, which is a linear expression"""
        if feasibility_flag:
            objective = opt_model.sum(1/len(work_load.T[1:])*1/len(work_load.each_t_real_requests[t])
                                      *1/work_load.each_t_each_request_demand[t][k]
                                      *(w_vars[t,k,p] * network.get_path_length(p)) for t in work_load.T[1:]
                                      for k in work_load.each_t_user_pairs[t] 
                                      for p in network.each_request_real_paths[k]+network.each_request_virtual_paths[k]
                                      )
            opt_model.minimize(objective)
        else:
            objective = opt_model.sum(1/len(work_load.T[1:])*1/len(work_load.each_t_real_requests[t])
                                      
                                      *(w_vars[t,k,p]) for t in work_load.T[1:]
                                      for k in work_load.each_t_user_pairs[t] 
                                      for p in network.each_request_real_paths[k]+network.each_request_virtual_paths[k]
                                      )
            opt_model.maximize(objective)


        

#         opt_model.print_information()

        opt_model.solve()


#         print('docplex.mp.solution',opt_model.solution)
#         import pdb
#         pdb.set_trace()
        objective_value = -1
        try:
            if opt_model.solution:
                objective_value =opt_model.solution.get_objective_value()
        except ValueError:
            print(ValueError)

            #print("******************************** end *************************************")   



        opt_model.clear()
        return objective_value
    
    
    

# In[9]:




# In[ ]:




# In[ ]:




# In[ ]:



