#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# from tmgen.models import uniform_tm,spike_tm,modulated_gravity_tm,random_gravity_tm,gravity_tm,exp_tm
import random

# In[ ]:


class Work_load:
    def __init__(self):
        self.each_t_each_request_demand = {}
        self.each_request_each_time_threshold = {}
        self.each_t_real_requests = {}
    def get_each_request_threshold(self,network,k,b,t):
        if k in self.each_t_user_pairs[t]:
            return self.each_request_each_time_threshold[k][t]
        else:
            return network.each_storage_block_time_treshold[k][b][t]
        
        
    def set_each_user_pair_demands(self,number_of_time_slots,each_t_user_pairs,spike_mean,num_spikes):
        self.each_t_each_request_demand = {}
        num_of_pairs= len(list(each_t_user_pairs[0]))
#         tm = spike_tm(num_of_pairs+1,num_spikes,spike_mean,number_of_time_slots)
        for time in range(number_of_time_slots):
#             traffic = tm.at_time(time)
#             print("traffic",traffic)
            demand = random.randint(1,spike_mean)
            try:
                self.each_t_each_request_demand[time][0] = demand
            except:
                self.each_t_each_request_demand[time] = {}
                self.each_t_each_request_demand[time][0] = demand
                                

                
        for request in each_t_user_pairs[time]:
            try:
                self.each_t_each_request_demand[0][request] = 0
            except:
                self.each_t_each_request_demand[0]={}
                self.each_t_each_request_demand[0][request] = 0

