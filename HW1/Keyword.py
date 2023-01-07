# -*- coding: utf-8 -*-
"""
@author: Anıl Bayram
"""

class Node(object):
    def __init__(self, label):
        self.label = label
        self.children = {}
        self.ID = None
        
class KeywordTree(object):
    
    def __init__(self, patterns):
        self.root = Node(None)
        self.patterns = patterns
        
        for pat in self.patterns: #patterns is list, pat is string "apple" or "banana"
            search_node = self.root
        
            for letter in pat: #letter is a letter in string "a", "p"
                MATCH = False
                for nodes in search_node.children:
                    if letter == nodes:
                        search_node = search_node.children[nodes]
                        MATCH = True
                        break
                    
                if not MATCH:
                    search_node.children[letter] = Node(letter)
                    search_node = search_node.children[letter]
            search_node.ID = pat

    def get_root(self):
        return self.root
    
    def find_in_text(self, text):
        results_dic = {}
        results = []
        for patt in self.patterns:
            results_dic[patt] = []
        for i in range(len(text)): 
            MATCH = True
            j = 0
            search_node = self.root
            while search_node.ID == None and MATCH and (i+j)<len(text):
                
                for nodes in search_node.children:
                    
                    if text[i+j] == nodes:
                        search_node = search_node.children[nodes]
                        MATCH = True
                        break
                        
                    else:
                        MATCH = False
                j += 1
            if search_node.ID != None and MATCH:
                results_dic[search_node.ID] += [i+1]
                # print(search_node.ID, i)
        for i in range(len(self.patterns)):
            if self.patterns[i] in results_dic:
                results.append(results_dic[self.patterns[i]])
            else:
                results.append([])
        return results, results_dic


