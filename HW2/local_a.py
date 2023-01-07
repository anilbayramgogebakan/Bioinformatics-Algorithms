"""
Local Allignment
Anıl Bayram Göğebakan
"""
import numpy as np
import pandas as pd

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

def mul_step(x):
    # if x value is greater than zero, return it directly; else return zero.
    return x * (x>0)



# match = 1
# mismatch = -1 
# gap = -2

# pattern = "ACGCGA"
# text = "CGAGTGA"

def local_allignment(text, pattern, match, mismatch, gap, output_file):
    score_ar = np.zeros((len(pattern)+1, len(text)+1 ), dtype=np.int32)
    direction_ar = np.zeros((len(pattern)+1, len(text)+1 ), dtype=np.int32)
    # 1: right,  2: down,  4:diagonal
    
    # Fill arrays
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
                score_ar[row][col] = mul_step(hor_sc)
                
            if max(scores) == ver_sc:
                direction_ar[row][col] += 2
                score_ar[row][col] = mul_step(ver_sc)
                
            if max(scores) == dia_sc:
                direction_ar[row][col] += 4
                score_ar[row][col] = mul_step(dia_sc)
                
    # Backtrack
    btrack_ind = np.where(score_ar == np.max(score_ar))
    for i in range(len(btrack_ind[0])):
        btrack_row = btrack_ind[0][i]
        btrack_col = btrack_ind[1][i]
        
        res_text = ""
        res_pattern = ""
        # 1: left,  2: up,  4:diagonal
        
        # iterate it until reach source
        while score_ar[btrack_row][btrack_col] != 0:
            # print(btrack_row)
            # print(btrack_col)
            # print()
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
             
                
        print(res_pattern)
        print(res_text)
    print("Score = {}".format(int(np.max(score_ar))))
    print("Number of local allignments: {}".format(len(btrack_ind[0])))
    
    col_head = []
    col_head[:0] = " " + text
    
    row_head = []
    row_head[:0] = " " + pattern
    df = pd.DataFrame(score_ar, columns=col_head, index=row_head)
    df.to_csv(output_file, sep='\t', mode='a')

# local_allignment(text, pattern, match, mismatch, gap, "local.txt")

