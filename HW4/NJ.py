# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 21:16:13 2022

@author: Anıl Bayram
"""
import numpy as np

d = np.array([[0,4,10,9],
              [4,0,8,7],
              [10,8,0,9],
              [9,7,9,0]])

# d = np.array([[0,2,8,7],
#               [2,0,6,5],
#               [8,6,0,7],
#               [7,5,7,0]])


def find_deg_trip(d):
    t = np.tril(d)
    
    for row in range(d.shape[0]):
        for col in range(d.shape[0]):
            
            if row <= col: # iterate through lower triangle
                continue
            
            el = t[row][col]
            
            for row_2 in range(d.shape[0]):
                for col_2 in range(d.shape[0]):
            
                    if row_2 <= col_2 or ((row_2 == row) and (col_2 == col)): # iterate through lower triangle
                        continue
                    
                    el_2 = t[row_2][col_2]
                    
                    if el + el_2 in t:
                        ind = np.where(t == el + el_2)
                        return [(row,col), (row_2,col_2), (int(ind[0]),int(ind[1]))]
        
    return []
hist = []
while d.shape[0] != 2:
    
    ind_list = find_deg_trip(d)
    
    if ind_list == []: # no degenerate, shorten tree
        d -= 2
        np.fill_diagonal(d, 0)
        hist.append(-1)
    else:
        deleted = tuple(set(ind_list[0]) & set(ind_list[1]))
        d = np.delete(d,deleted[0], axis=0)
        d = np.delete(d,deleted[0], axis=1)
        hist.append(deleted[0])

print(hist)
        

        
        
                