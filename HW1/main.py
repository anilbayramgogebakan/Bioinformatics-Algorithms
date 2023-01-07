# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:15:50 2022

@author: Anıl Bayram
"""
import argparse

import Keyword as k
import Suffix as s

parser = argparse.ArgumentParser(description='hw1')
parser.add_argument('-p', type=str, help='pattern file')
parser.add_argument('-t', type=str,  help='text file')
parser.add_argument('-o', type=str,  help='output file')

args = parser.parse_args()



PATTERN_PATH = args.p
TEXT_PATH = args.t
OUTPUT_PATH = args.o


pattern_file = open(PATTERN_PATH, "r")
pattern_list = pattern_file.read().split("\n")
pattern_file.close()

text_file = open(TEXT_PATH, "r")
txt_str = text_file.read()
text_file.close()

tree = k.KeywordTree(pattern_list)
index = tree.find_in_text(txt_str)

tree = s.SuffixTree(txt_str)
index = tree.find_pattern_from_list(pattern_list)

out_file = open(OUTPUT_PATH, "w")

for p_idx in range(len(pattern_list)):
    
    # out_file.write(pattern_list[p_idx])
    out_file.write(" ")
    for ind in index[p_idx]:
        out_file.write(str(ind)+" ")
    out_file.write("\n")
out_file.close()



