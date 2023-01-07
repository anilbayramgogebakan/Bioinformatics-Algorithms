# -*- coding: utf-8 -*-
"""
Main.py
Anıl Bayram Göğebakan
"""
import argparse

import global_a as g
import local_a as l

parser = argparse.ArgumentParser(description='hw2')

parser.add_argument('-g', action='store_true', help='global allignment')
parser.add_argument('-l', action='store_true', help='local allignment')
parser.add_argument('-p', type=str, help='pattern file')
parser.add_argument('-t', type=str,  help='text file')
parser.add_argument('-s', type=str,  help="score string e.g. '+1| -1| -2'")

parser.add_argument('-o', type=str,  help='output file')

args = parser.parse_args()

GLOBAL_FLAG = args.g
LOCAL_FLAG = args.l
PATTERN_PATH = args.p
TEXT_PATH = args.t
scores = args.s

OUTPUT_PATH = args.o

 

scores_list = scores.split(",")
match, mismatch, gap = int(scores_list[0]), int(scores_list[1]), int(scores_list[2])

pattern_file = open(PATTERN_PATH, "r")
pattern = pattern_file.readlines()[1]
pattern_file.close()

text_file = open(TEXT_PATH, "r")
text = text_file.readlines()[1]
text_file.close()

if GLOBAL_FLAG:
    g.global_allignment(text, pattern, match, mismatch, gap, OUTPUT_PATH)
    
if LOCAL_FLAG:
    l.local_allignment(text, pattern, match, mismatch, gap, OUTPUT_PATH)
