#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:20:20 2019

@author: kevinhowlett
"""

#Program generates a random even number between 0 and 100

import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    even_numbers = []
    for i in range(100):
        if i % 2 == 0:
            even_numbers.append(i)
    return random.choice(even_numbers)
