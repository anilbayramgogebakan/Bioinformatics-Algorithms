# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 17:19:17 2022

@author: Anıl Bayram
"""

class Node(object):
    def __init__(self, label, ID):
        self.label = label
        self.children = {}
        self.ID = ID # exist only in leafs, gives the starting index
        
class SuffixTree(object):
        
    def __init__(self, text):
        """ Takes text as input and generates Suffix Tree.
        """
        self.root = Node(None,None)
        self.text = text
        self.text += "$"
        self.root.children[self.text] = Node(self.text, 0 ) #whole string added
      
        
        for ID in range(1, len(self.text)): #each iteration correspond to each suffix(ID=index)
            suffix = self.text[ID:]
            match = False
            label = "$"
            search_node = self.root
            label_idx = 0
            for idx_suff in range(len(suffix)):
                
                
                if not match or label_idx == len(label):
                    match = False
                    # we should find matching node  
                    for children_label in search_node.children: #children_label = "banana$, anana$...."
                    
                        if suffix[idx_suff] == children_label[0]:
                            match = True
                            label = children_label
                            parent_node = search_node
                            search_node = search_node.children[children_label] #matching branch/node updated.
                            label_idx = 1
                            break # since we found our branch
                    if match:
                        continue
                
                if not match: # no more match, new leaf added
                    new_node = Node(suffix[idx_suff:], ID)
                    search_node.children[suffix[idx_suff:]] = new_node
                    break
                
                    
                else: # we found matching branch, start to compare
        
                    
                    if len(label) < label_idx:
                        match = False
                    
                    elif suffix[idx_suff] == label[label_idx]:
                        label_idx +=1
                    
                    else:
                        new_node = Node(suffix[idx_suff:], ID) #new node created
                        
                        update_node = Node(label[label_idx:], parent_node.children[label].ID)
                        update_node.children = parent_node.children[label].children
                        
                        inter_node = Node(label[:label_idx], None)
                        inter_node.children[new_node.label] = new_node
                        inter_node.children[update_node.label] = update_node
        
                        del parent_node.children[label]
                        parent_node.children[label[:label_idx]] = inter_node # inter node created
                        break

    
    def get_root(self):
        return self.root
    
    def get_ID(node):
    
        ID_list = []
        
        if node.ID != None:
            ID_list.append(node.ID+1)
        
        for child in node.children:
            
            if node.children[child].ID == None:
                children_ID = SuffixTree.get_ID(node.children[child])
                ID_list += children_ID
            else:
                ID_list.append(node.children[child].ID+1)
        
        return ID_list
    
    def find_pattern(self, pattern):
        FOUND = False
        label_idx = 0
        label = "$"
        search_node = self.root
        
        for find_idx in range(len(pattern)):
            if not FOUND or label_idx == len(label):
                FOUND = False
                    # we should find matching node  
                for children_label in search_node.children: #children_label = "banana$, anana$...."
                    
                    if pattern[find_idx] == children_label[0]:
                        FOUND = True
                        label = children_label
                        search_node = search_node.children[children_label] #matching branch/node updated.
                        label_idx = 1
                        break # since we found our branch
                if FOUND:
                    continue
                    
            if not FOUND: # no more match, new leaf added
                #print("Matching index: ", find_idx)
                break
            else:
                
                if len(label) < label_idx:
                    FOUND = False
                    
                elif pattern[find_idx] == label[label_idx]:
                    label_idx +=1
                else:
                    FOUND = False
                  
        if FOUND:
            results = SuffixTree.get_ID(search_node)
            return results
        else:
            # print("No match!!")
            return []
    def find_pattern_from_list(self, lis):
        res_list = []
        for pat in lis:
            res = SuffixTree.find_pattern(self, pat)
            res_list.append(res)
        return res_list
        
 
        