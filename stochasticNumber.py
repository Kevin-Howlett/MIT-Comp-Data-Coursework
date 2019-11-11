#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:31:24 2019

@author: kevinhowlett
"""

#Program stochastically returns uniformly distributed even numbers
#between 9 and 21

import random
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    random.seed()
    return random.choice([10,12,14,16,18,20])
