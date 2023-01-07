# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 19:38:13 2022

@author: Anıl Bayram
"""

import numpy as np
import argparse

parser = argparse.ArgumentParser(description='hw0')
parser.add_argument('--n', type=int, help='dimension')
parser.add_argument('--s', type=int,  help='config file')

args = parser.parse_args()

print("n: ",args.n)
print("s: ",args.s)


n = args.n
s = args.s

a = np.random.randint(-100, 100,size=(n,n))
b = np.random.randint(-100, 100,size=(n,n))

c = a + b

print("A:")
print(a)
print("B:")
print(b)
print("C:")
print(c)

print("s: ",s)

a = np.random.randint(100,size=(n,n))
print("A:")
print(a)

print("C:")
print(s*a)

a = np.random.randint(100,size=(n,n))
print("A:")
print(a)

print("A.T:")
print(np.transpose(a))