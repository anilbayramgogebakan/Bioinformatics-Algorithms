# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:08:44 2022

@author: Anıl Bayram
"""
import argparse
import star as SC

parser = argparse.ArgumentParser(description='hw3')


parser.add_argument('-i', type=str, help='input file')
parser.add_argument('-s', type=str,  help="score string e.g. '+1: -1: -2'")
parser.add_argument('-o', type=str,  help='output file')

args = parser.parse_args()


PATTERN_PATH = args.i
scores = args.s
OUT_PATH = args.o

 
# scores = '+1: -1: -2'
scores_list = scores.split(":")
match, mismatch, gap = int(scores_list[0]), int(scores_list[1]), int(scores_list[2])


# PATTERN_PATH = "inp.fasta"
pattern_file = open(PATTERN_PATH, "r")
lines = pattern_file.readlines()
pattern_list = []
pattern_id = []
for i in range(len(lines)): # Read from fasta file to list objects
    
    if lines[i][0] == ">":
        pattern_id.append(lines[i][1:].strip())
    else:
        if len(pattern_id) != len(pattern_list):
            pattern_list.append(lines[i].strip())
        else:
            pattern_list[-1] = pattern_list[-1]+lines[i].strip()
# print(pattern_list)
# print(pattern_id)

# read_file = pattern_file.read().split("\n")
pattern_file.close()

        
SC.center_star(pattern_list, pattern_id, OUT_PATH,match, mismatch, gap)