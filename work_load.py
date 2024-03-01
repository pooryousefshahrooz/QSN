#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Work_load:
    def __init__(self):
        self.each_t_each_request_demand = {}
    def get_each_request_threshold(self,k,t):
        return self.each_request_threshold[k][t]
