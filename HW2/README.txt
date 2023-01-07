Anıl Bayram Göğebakan-21802687
bayram.gogebakan@ug.bilkent.edu.tr
CS481-HW2

This is my submission for Homework 2.

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
	numpy 1.23.3
	pandas 1.2.4

	Note that numpy is used for matrix operations such as calculation scoring matrix and so on. Pandas is not use to calculate allignments. 
Instead, it is only used while printing output in the desired format.

Files:
	main.py: This script is for the main operations. In this script, global_a.py and local_a.py are imported and used for given pattern and 
text. It gives the output as result file and print the results. Followings are the arguments of main.py script.
	-g: Flag for global allignment. If exist, Global allignment has been run.
	-l: Flag for local allignment. If exist, Local allignment has been run.
	-p: Pattern file path. This file must be .fasta file as given in the instructions.
	-t: Text file path. This file must be .fasta file as given in the instructions.
	-s: match, mismatch and gap scores. It includes 3 numbers seperated with ",". Note that in the instruction, numbers are seperated by 
vertical pipe("|"). However, pipe is a command in ubuntu console. In order to prevent any unnecessary bug, comma (",") symbol will be used.
	
	-o: Output file path. It should be in .txt format.

	global_a.py: Takes file pathes and scores as input. It prints the results and dump the output file accordingly.

	local_a.py: Takes file pathes and scores as input. It prints the results and dump the output file accordingly.

Before run the script, the there shouldn't a .txt type file with the same name as new output in order to prevent overlap. Also, text and pattern files must be in the .fasta type 
whose first line is the name and second line is the sequence.