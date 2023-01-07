Anıl Bayram Göğebakan-21802687
bayram.gogebakan@ug.bilkent.edu.tr
CS481-HW3

This is my submission for Homework 3.

In this homework Python3 is used. Although Python3 doesn't require compilation process,
there are some libraries which must be installed before run the program. These libraries 
are mentioned in the "Requirements" section.

In order to run the program, execute the following steps.
	$ make install
		This step will install the required libraries.
	$ make run
		This step will run the code.
	$ make clean
		This step will clear the .pyc files that might be created after running the program.

Requirements:
	numpy==1.20.1

	Note that numpy is used for matrix operations such as calculation scoring matrix and so on.

Files:
	main.py: This script is for the main operations. In this script, global_a.py and star.py are imported and used 
for given pattern and text. It gives the output as result file. Followings are the arguments of main.py script.
	-i: Pattern file path. This file must be .fasta file as given in the instructions.
	-s: match, mismatch and gap scores. It includes 3 numbers seperated with ":".
	-o: Output file path. It should be in .txt format.

	global_a.py: Takes texts and scores as input. Then, gives the alignment and its score.

	star.py: Takes pattern list, pattern ids, output path and scores as input. It dumps the output file accordingly.

Before run the script, the there shouldn't a .txt type file with the same name as new output in order to prevent overlap. 
Also, text and pattern files must be in the .fasta type whose first line is the name and second line is the sequence.