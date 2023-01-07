# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:47:21 2022

@author: Anıl Bayram
"""
import numpy as np

def find_min_coor(d):
    sorted_array = np.unravel_index(np.argsort(np.tril(d), axis=None), d.shape)
    K = d.shape[0]
    nonzero_ind = int(K*K-((K*K-K)/2))    
    min_coor = sorted_array[0][nonzero_ind], sorted_array[1][nonzero_ind]
    return min_coor

def UPGMA(d):
    h_dic = {}
    
    label = [str(x) for x in range(d.shape[0])]
    # col_label = [x for x in range(d.shape[0])]
    
    while d.shape[0] != 1:
        row, col = find_min_coor(d)
        
        h = d[row][col]/2
        h_dic[(label[row],label[col])] = h
        
        
        new_dist = np.copy(d)
        new_dist = np.delete(new_dist, (col, row), axis=0)
        new_dist = np.delete(new_dist, (col, row), axis=1)
        
        new_label = list(label)
        new_label.append(label[row]+label[col]); new_label.remove(label[row]); new_label.remove(label[col])
        
        new_dvec = np.zeros((new_dist.shape[0],1))
        
        dvec_ind = -1
        for el in range(new_dist.shape[0]+2):
            
            if el==col or el==row:
                continue
            else:
                dvec_ind += 1
            
            new_dvec[dvec_ind] = (d[el][col]*len(label[col]) + d[el][row]*len(label[row]))/(len(label[row])+len(label[col]))
        
        new_dist = np.vstack((new_dist, new_dvec.T))
        new_dist = np.hstack((new_dist, np.vstack((new_dvec, np.array([[0]])))))
        
        # Update label and distance matrices
        label = new_label
        d = new_dist
        
    return h_dic

    
# d = np.array([[0,19,27,8,33,18],
#               [19,0,31,18,36,1],
#               [27,31,0,26,41,32],
#               [8,18,26,0,31,17],
#               [33,36,41,31,0,35],
#               [18,1,32,17,35,0]])

# d_2 = np.array([[0,2,4,6,6,8],
#                 [2,0,4,6,6,8],
#                 [4,4,0,6,6,8],
#                 [6,6,6,0,4,8],
#                 [6,6,6,4,0,8],
#                 [8,8,8,8,8,0]])
# dic = UPGMA(d_2)





