#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Work_load:
    def __init__(self):
        self.each_t_each_request_demand = {}
        self.each_request_each_time_threshold = {}
        self.each_t_real_requests = {}
    def get_each_request_threshold(self,network,k,b,t):
        if k in self.each_t_user_pairs[t]:
            print("this is user pair %s all user pairs %s and time %s all data structure %s "%(k,self.each_t_user_pairs,t,self.each_request_each_time_threshold))
            return self.each_request_each_time_threshold[k][t]
        else:
            return network.each_storage_block_time_treshold[k][b][t]
