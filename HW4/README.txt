Anıl Bayram Göğebakan-21802687
bayram.gogebakan@ug.bilkent.edu.tr
CS481-HW4

This is my submission for Homework 4.

In this homework Python3 is used. Although Python3 doesn't require compilation process,
there are some libraries which must be installed before run the program. These libraries 
are mentioned in the "Requirements" section.

In order to run the program, execute the following steps.
	$ make install
		This step will install the required libraries.
		In this step, scikit-bio module is installed. However, up-to-date version and 0.2.3 version (which is given in HW3 pdf) have 
installation problems. Thus, 0.2.0 version is used. Due to some errors in scikit-bio module, future module installed and re-installed again.
	$ make run
		This step will run the code.
	$ make clean
		This step will clear the .pyc files that might be created after running the program.

Requirements:
	numpy==1.20.1

Files:
	main.py: This script is for the main operations. In this script, global_a.py and UPGMA.py scriptes are imported.
It gives the output as result file. Result file format is not Newick format. Instead, it is a dictionary that shows the relationship between labels in terms of their height.
Note that in dictionary, every label is represented their corresponding index. Label list can be found in the second line of output file.
Followings are the arguments of main.py script.
	-t: Tree type. Only valid tree argument is "upgma". Note that "nj" is not implemented.
	-i: Pattern file path. This file must be .fasta file as given in the instructions.
	-s: match, mismatch and gap scores. It includes 3 numbers seperated with ":".
	-o: Output file path. It should be in .txt format.

	global_a.py: Takes file pathes and scores as input. Then, gives alignment score. It is used while constructing distance matrix.

	UPGMA.py: Takes distance matrix and return resulting dictionary.

	NJ.py: Takes distance matrix and return resulting dictionary. Since code is not completed, it is not used in the main script. However, it can calculate the degenerate
 triples and shorten the hanging edges. However, constracting tree with recovering function is not working.
