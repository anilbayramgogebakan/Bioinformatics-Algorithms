Anıl Bayram Göğebakan-21802687
bayram.gogebakan@ug.bilkent.edu.tr
CS481-HW1

This is my submission for Homework 1.

In this homework Python3 is used. Although Python3 doesn't require compilation process,
there are some libraries which must be installed before run the program. These libraries 
are mentioned in the "Requirements" section.

In order to run the program, execute the following steps.
	$ make run
		This step will run the code.
	$ make clean
		This step will clear the .pyc files that might be created after running the program.

Requirements:
	None except Python and its default modules

Files:
	main.py: This script is for the main operations. In this script, Keyword.py and Suffix.py are imported and used for given patterns and text. It gives the output as results file. 

	Keyword.py: In this script, Keyword Tree with Naive Threading is implemented as based on the information
given in lectures. No additional library is used. Two object is created: Node() and KeywordTree(). 

Node is used for each node on the tree. Every node has 3 features. Label feature for the letter of node, 
Children represent the children nodes of existing node (no children on the leafs) and ID for the leaf that gives the keyword.

KeywordTree is for the tree-like algorithm. It is created by default with root node and by using given patterns, children roots 
added accordingly. In order to the find keywords in given text, find_in_text() function can be used.

	Suffix.py: In this script, Suffix Tree is implemented as based on the information given in lectures.
No additional library is used. Two object is created: Node() and SuffixTree(). 

Node is used for each edge. Every node has 3 features. Label feature for the label of node, Children represent the 
children nodes of existing node (no children on the leafs) and ID for the leaf that gives the starting index

SuffixTree is for the tree-like algorithm. It is created by default with root node and by using given text, children
 roots added accordingly. In order to the find keywords in given text, find_pattern_from_list()(for input as list) 
and find_pattern()(for individual string input) functions can be used.