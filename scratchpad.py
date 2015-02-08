# -*- coding: utf-8 -*-
"""
scratchpad for spread builder
"""


import numpy as np
import pandas as pd



def fakeData(shape=(250,3)):
    
    r = np.random.randn(shape[0],shape[1])
    df = pd.DataFrame(np.cumsum(r,0))
    
    return df
    
    
