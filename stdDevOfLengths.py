#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 22:18:34 2019

@author: kevinhowlett
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L == []:
        return float('NaN')
    lengths = []
    for string in L:
        lengths.append(len(string))
    mean = sum(lengths)/len(lengths)
    num = 0
    for x in lengths:
        num += (x - mean)**2
    return (num/len(lengths))**0.5