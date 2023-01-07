# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:53:42 2022

@author: Anıl Bayram
"""
import global_a as GA
# from skbio import Alignment, DNA


# match = 10
# mismatch = -3
# gap = -5

# text = "AACCTT"
# pattern = "AATGCC"
# pattern2 = "AGACCGT"

# pattern_list = ['MEPSLLMWRFFVFIVVPGCVTEACHDDPPSLRNAMFKVLRYEVGTMVGTM', 
#  'MEPRLLMLGFLSLTIVPSCRAELCLYDPPEVPNATFKALSYKNGTI', 
#  'MEPSLLLWGILTFVVVHGHVTELCDENPPDIQHATFKALTYKTGTM', 
#  'MDSYLLMWGLLTFIMVPGCQAELCDDDPPEIPHATFKAMAYKEGTM']
# pattern_id = ['SHEEP', 'MOUSE', 'FELCA', 'HUMAN']
# pattern_list = ["AACCTT","AATGCC", "AGACCGT"]
# pattern_id = ["1","2", "3"]
# pattern_list = ["MPE","MKE", "MSKE", "SKE"]


def get_star_score_list(pattern_list, match, mismatch, gap):
    #Takes pattern list and score parameters, return star_score_list
    score_list = []    
    for i in range(len(pattern_list)):
        
        current_sc = 0
        
        for j in range(len(pattern_list)):
            # Calculate score for each pair (More memory efficient solution exist!)
            _, _, sc = GA.global_allignment(pattern_list[i], pattern_list[j], match, mismatch, gap)
            current_sc += sc
        
        score_list.append(current_sc)
    return score_list



def find_center(pattern_list,match, mismatch, gap):
    #Takes pattern list, return 
    score_list = get_star_score_list(pattern_list, match, mismatch, gap)
    star_ind = score_list.index(max(score_list))
    star_text = pattern_list[star_ind]
    return star_ind, star_text

def insert_gap(text, index):
    if index > len(text):
        return text + "-"
    else:
        return text[:index] + '-' + text[index:]

def center_star(pattern_list, pattern_id, OUT_PATH, match, mismatch, gap):
    star_ind, star_text = find_center(pattern_list,match, mismatch, gap)
    
    star_al = []
    left_al = []
    
    for i in range(len(pattern_list)):
        if i == star_ind:
            continue
        star_text_al, left_text_al, _ = GA.global_allignment(star_text, pattern_list[i], match, mismatch, gap)
        
        star_al.append(star_text_al)
        left_al.append(left_text_al)
    
    # Example intermediate inputs
    # sc1 = "AA__CCTT"
    # s1 = "AATGCC__"
    
    # sc2 = "A_ACC_TT"
    # s2 = "AGACCGT_"
    
    # star_al = [sc1, sc2]
    # left_al = [s1, s2]
    
    
    i = 0
    
    while True:
        GAP = False
        
        st_al_id = 0
        for st_al in star_al:
            if st_al[i] == "-":
                GAP = True
                break
            st_al_id += 1
        
        if GAP:
            le_al_id = 0
            for le_al_ind in range(len(left_al)):
                if le_al_id != st_al_id:
                    left_al[le_al_ind] = insert_gap(left_al[le_al_ind], i)
                le_al_id += 1
            
            for st_al_ind in range(len(star_al)):
                if len(star_al[st_al_ind]) == i or star_al[st_al_ind][i] != "-":
                    star_al[st_al_ind] = insert_gap(star_al[st_al_ind], i)
    
        i +=1
        if len(max(star_al, key=len)) == i:
            break
        
    left_al.insert(star_ind, star_al[0])
    result = left_al
    seq = []
    f = open(OUT_PATH, "w")

    for i in range(len(result)):
        seq.append(pattern_id[i] + "__" + result[i])

    
    for line in seq: 
        f.write(line)
        f.write("\n")

    f.close()
    return result
# OUT_PATH = "new_out.txt"
# res = center_star(pattern_list, pattern_id, OUT_PATH,match, mismatch, gap)
    
    