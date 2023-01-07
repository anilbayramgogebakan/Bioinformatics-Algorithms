# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 19:48:57 2022

@author: Anıl Bayram
"""

import argparse
import global_a as G
import numpy as np
import UPGMA

parser = argparse.ArgumentParser(description='hw4')

parser.add_argument('-t', type=str, help='tree type, upgma or nj')
parser.add_argument('-i', type=str, help='input file')
parser.add_argument('-s', type=str,  help="score string e.g. '+1: -1: -2'")
parser.add_argument('-o', type=str,  help='output file')

args = parser.parse_args()

TREE = args.t
INP_PATH = args.i
scores = args.s
OUT_PATH = args.o

scores_list = scores.split(":")
match, mismatch, gap = int(scores_list[0]), int(scores_list[1]), int(scores_list[2])

def create_distance_arr(inp_list):
    
    genes = []
    names = []
    
    match = 1
    mismatch = -1
    gaps = -2
    
    
    for i in range(len(inp_list)): # Read from fasta file to list objects
        
        if inp_list[i][0] == ">":
            names.append(inp_list[i][1:].strip())
        else:
            if len(names) != len(genes):
                genes.append(inp_list[i].strip())
            else:
                genes[-1] = genes[-1]+inp_list[i].strip()
    # print(genes)
    # print(names)

    
    d = np.zeros((len(genes),len(genes)))
    
    for i in range(len(genes)):
        
        for col in range(i):
            
            if i == col:
                d[i][col] = 0
            else:
                d[i][col] = G.global_alignment(genes[i], genes[col], match, mismatch, gaps, BACKTRACK=False)
                
    d = d + d.T
    return d, names

# INP_PATH = "inp.fasta"
# OUT_PATH = "out.txt"

f = open(INP_PATH, 'r')
lines = f.readlines()

d, labels = create_distance_arr(lines)

if TREE == "upgma":
    h_dic = UPGMA.UPGMA(d)
else:
    print("nj solution does not exist")

out = open(OUT_PATH, 'w')
out.writelines(str(h_dic))
out.writelines('\n')
out.writelines(str(labels))
out.close()




 