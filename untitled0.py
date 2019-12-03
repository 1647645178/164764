# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:16:49 2019

@author: 16476
"""
import numpy as np
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item 
            seen.add(item)
a=np.random.randint(10,size=10)
list(dedupe(a))
s=slice(2,4)
a[s]