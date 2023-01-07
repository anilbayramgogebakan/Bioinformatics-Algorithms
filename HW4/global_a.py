"""
Global Alignment
Anıl Bayram Göğebakan
"""
import numpy as np
# import pandas as pd

def go_horizontal(res_text, res_pattern, text, pattern, btrack_col, btrack_row ):
    # Go horizontal
    # Decide string values
    res_text = text[btrack_col-1] + res_text
    res_pattern = "_" + res_pattern
    # Move to other cell
    btrack_col -= 1
    return res_text, res_pattern, btrack_col, btrack_row

def go_vertical(res_text, res_pattern, text, pattern, btrack_col, btrack_row):
    # Go vertical
    # Decide string values
    res_text = "_" + res_text
    res_pattern = pattern[btrack_row-1] + res_pattern
    # Move to other cell
    btrack_row -= 1
    return res_text, res_pattern, btrack_col, btrack_row

def go_diagonal(res_text, res_pattern, text, pattern, btrack_col, btrack_row):
    # Go diagonal
    # Decide string values
    res_text = text[btrack_col-1] + res_text
    res_pattern = pattern[btrack_row-1] + res_pattern
    # Move to other cell
    btrack_col -= 1; btrack_row -= 1    
    return res_text, res_pattern, btrack_col, btrack_row


# match = 10
# mismatch = -2 
# gap = -5

# text = "CTCGCAGC"
# pattern = "CATTCAC"

def global_alignment(text,pattern, match, mismatch, gap, BACKTRACK=True):
    score_ar = np.zeros((len(pattern)+1, len(text)+1 ), dtype=np.int32)
    direction_ar = np.zeros((len(pattern)+1, len(text)+1 ))
    # 1: right,  2: down,  4:diagonal
    
    # Fill the initial row and column
    for i in range(1, score_ar.shape[1]):
        score_ar[0][i] = score_ar[0][i-1] + gap 
        direction_ar[0][i] = 1
        
    for i in range(1, score_ar.shape[0]):
        score_ar[i][0] = score_ar[i-1][0] + gap 
        direction_ar[i][0] = 2
    
    # Fill the rest of the arrays
    for col in range(1, score_ar.shape[1]):
        for row in range(1, score_ar.shape[0]):
            # First, calculate all possible results
            hor_sc = score_ar[row][col-1] + gap
            ver_sc = score_ar[row-1][col] + gap
            if text[col-1] == pattern[row-1]:
                dia_sc = score_ar[row-1][col-1] + match
            else:
                dia_sc = score_ar[row-1][col-1] + mismatch
                
            # Decide which score is max
            scores = [hor_sc, ver_sc, dia_sc]
            
            if max(scores) == hor_sc:
                direction_ar[row][col] += 1
                score_ar[row][col] = hor_sc
                
            if max(scores) == ver_sc:
                direction_ar[row][col] += 2
                score_ar[row][col] = ver_sc
                
            if max(scores) == dia_sc:
                direction_ar[row][col] += 4
                score_ar[row][col] = dia_sc
    
    if not BACKTRACK:
        return score_ar[-1][-1]
                
    # Backtrack
    btrack_row = score_ar.shape[0]-1
    btrack_col = score_ar.shape[1]-1
    
    res_text = ""
    res_pattern = ""
    # 1: left,  2: up,  4:diagonal
    
    # iterate it until reach source
    while btrack_row != 0 or btrack_col != 0:
        direction = direction_ar[btrack_row][btrack_col]
        
        if direction == 4: # Diagonal move
            res_text, res_pattern, btrack_col, btrack_row = go_diagonal(res_text, res_pattern, text, pattern, btrack_col, btrack_row)        
            
        elif direction == 1: # Horizontal move
            res_text, res_pattern, btrack_col, btrack_row = go_horizontal(res_text, res_pattern, text, pattern, btrack_col, btrack_row)
            
        elif direction == 2: # Vertical move
            res_text, res_pattern, btrack_col, btrack_row = go_vertical(res_text, res_pattern, text, pattern, btrack_col, btrack_row)
            
        elif direction == 3: # Either horizontal or vertical
            if score_ar[btrack_row-1][btrack_col] >= score_ar[btrack_row][btrack_col-1]:
                res_text, res_pattern, btrack_col, btrack_row = go_vertical(res_text, res_pattern, text, pattern, btrack_col, btrack_row)
            else:
                res_text, res_pattern, btrack_col, btrack_row = go_horizontal(res_text, res_pattern, text, pattern, btrack_col, btrack_row)
                
        elif direction == 5: # Either horizontal or diagonal
            if score_ar[btrack_row-1][btrack_col-1] >= score_ar[btrack_row][btrack_col-1]:
                res_text, res_pattern, btrack_col, btrack_row = go_diagonal(res_text, res_pattern, text, pattern, btrack_col, btrack_row)
            else:
                res_text, res_pattern, btrack_col, btrack_row = go_horizontal(res_text, res_pattern, text, pattern, btrack_col, btrack_row)
    
        elif direction == 6: # Either vertical or diagonal
            if score_ar[btrack_row-1][btrack_col-1] >= score_ar[btrack_row-1][btrack_col]:
                res_text, res_pattern, btrack_col, btrack_row = go_diagonal(res_text, res_pattern, text, pattern, btrack_col, btrack_row)
            else:
                res_text, res_pattern, btrack_col, btrack_row = go_vertical(res_text, res_pattern, text, pattern, btrack_col, btrack_row)
    
        elif direction == 7: # Either vertical, horiazontal or diagonal
            if score_ar[btrack_row-1][btrack_col] == max(score_ar[btrack_row-1][btrack_col],score_ar[btrack_row-1][btrack_col-1],score_ar[btrack_row][btrack_col-1]):
                res_text, res_pattern, btrack_col, btrack_row = go_vertical(res_text, res_pattern, text, pattern, btrack_col, btrack_row)
                
            elif score_ar[btrack_row][btrack_col-1] == max(score_ar[btrack_row-1][btrack_col],score_ar[btrack_row-1][btrack_col-1],score_ar[btrack_row][btrack_col-1]):
                res_text, res_pattern, btrack_col, btrack_row = go_horizontal(res_text, res_pattern, text, pattern, btrack_col, btrack_row)
                
            else:
                res_text, res_pattern, btrack_col, btrack_row = go_diagonal(res_text, res_pattern, text, pattern, btrack_col, btrack_row)
         
    score = int(score_ar[-1][-1])
    # print(res_pattern)
    # print(res_text)
    # print("Score = {}".format(score))

    return res_text, res_pattern, score
    
# res_t, res_p, sc = global_alignment(text, pattern, match, mismatch, gap)