Results: 

	31631 out of 32853 tags correct
	  accuracy: 96.28
	8378 groups in key
	8621 groups in response
	7689 correct groups
	  precision: 89.19
	  recall:    91.78
	  F1:        90.46


SHORT VERSION

Requirements:

	python2, python3 and java

In the following:

	python3 is for python3
	python is for python2

Instructions:

In the terminal

(1) create features
	
	The output are training.feature and test.feature

	python3 create_features.py train_file test_24.pos test_file

	For example

	python3 create_features.py WSJ_02-21.pos-chunk WSJ_24.pos

(2) create models
	
	For Linux, Apple and other Posix systems, do:

		javac -cp maxent-3.0.0.jar:trove.jar *.java ### compiling
		java -cp .:maxent-3.0.0.jar:trove.jar MEtrain training.feature model.chunk ### creating the model of the training data
		java -cp .:maxent-3.0.0.jar:trove.jar MEtag test.feature model.chunk response.chunk ### creating the system output

	For Windows Only -- Use semicolons instead of colons in each of the above commands, i.e., the command for Windows would be:
	
		javac -cp maxent-3.0.0.jar;trove.jar *.java ### compiling
		java -cp .:maxent-3.0.0.jar;trove.jar MEtrain training.feature model.chunk ### creating the model of the training data
		java -cp .:maxent-3.0.0.jar;trove.jar MEtag test.feature model.chunk response.chunk ### creating the system output

(3) score models (python 2 only)

	python score.chunk.py answer_key.chunk response.chunk

	For example

	python score.chunk.py WSJ_24.pos-chunk response.chunk


LONG VERSION

This is a Noun Group tagger, using similar data that you used for Homework 3. However, for this program we will focus more on feature selection than on an algorithm.

This folder includes the following data files
	WSJ_02-21.pos-chunk -- the training file
	WSJ_24.pos  -- the development file that you will test your system on
	WSJ_24.pos-chunk -- the answer key to test your system output against
	WSJ_23.pos -- the test file, to run your final system on, producing system output

This folder also includes the following program files (using the OpenNLP package):
maxent-3.0.0.jar,  MEtag.java. MEtrain.java  and trove.jar -- Java files for running the maxent training and classification programs

score.chunk.py -- A python scoring script

The program that takes a file like WSJ_02-21.pos-chunk as input and produces a file consisting of feature value pairs for use with the maxent trainer and classifier. As this step represents the bulk of the assignment, there will be more details below, including the format information, etc. This program creates two output files. From the training corpus (WSJ_02-21.pos-chunk), create a training feature file (training.feature). From the development corpus (WSJ_24.pos), create a test feature file (test.feature). See details below.

Compile and run MEtrain.java, giving it the feature-enhanced training file as input; it will produce a MaxEnt model. MEtrain and MEtest use the maxent and trove packages, so you must include the corresponding jar files, maxent-3.0.0.jar and trove.jar, on the classpath when you compile and run. Assuming all java files are in the same directory, the following command-line commands will compile and run these programs -- these commands are slightly different for posix systems (Linux or Apple), than for Microsoft Windows.

For Linux, Apple and other Posix systems, do:

	javac -cp maxent-3.0.0.jar:trove.jar *.java ### compiling
	java -cp .:maxent-3.0.0.jar:trove.jar MEtrain training.feature model.chunk ### creating the model of the training data
	java -cp .:maxent-3.0.0.jar:trove.jar MEtag test.feature model.chunk response.chunk ### creating the system output

For Windows Only -- Use semicolons instead of colons in each of the above commands, i.e., the command for Windows would be:

	javac -cp maxent-3.0.0.jar;trove.jar *.java ### compiling
	java -cp .:maxent-3.0.0.jar;trove.jar MEtrain training.feature model.chunk ### creating the model of the training data
	java -cp .:maxent-3.0.0.jar;trove.jar MEtag test.feature model.chunk response.chunk ### creating the system output


Score the results with the python script as follows:
	python score.chunk.py WSJ_24.pos-chunk response.chunk ### WSJ_24.pos-chunk is the answer key and response.chunk is your output file

This pipeline is set up so you can write the code for producing the feature files in any programming language you wish. You have the alternative of using any Maxent package you would like, provided that the scoring script works on your output.
As mentioned in section 1.3, you are primarily responsible for a program that creates sets of features for the Maximum Entropy system.

Format Information:
1. There should be 1 corresponding line of features for each line in the input file (training or test)
If the input and feature files have different numbers of lines, you have a bug
2. Blank lines in the input file should correspond to blank lines in your feature file
3. Each line corresponding to text should contain tab separated values as follows:
	1. the first field should be the token (word, puncutation, etc.)
	2. this should be followed by as many features as you want (but no feature should contain white space). Typically, features are recommended to have the form attribute=value, e.g., POS=NN
		- This makes the features easy for humans to understand, but is not actually required by the program, e.g., the code does not look for the = sign.
	3. for the training file only, the last field should be the BIO tag (B-NP, I-NP or O)
	4. for the test file, there should be no final BIO field (as there is none in the .pos file that you would be training from)
	5. A sample training file line (where \t represents tab):'fish\tPOS=NN\tprevious_POS=DT\tprevious_word=the\tI-NP ## actual lines will probably be longer. There is a special symbol '@@' that you can use to refer to the previous BIO tag, e.g., Previous_BIO=@@
4. This allows you to simulate a (bigram) MEMM because you can refer to the previous BIO tag



Suggested features:
1. Features of the word itself: POS, the word itself, stemmed version of the word
2. Similar features of previous and/or following words (suggestion: use the features of previous word, 2 words back, following word, 2 words forward)
3. Beginning/Ending Sentence (at the beginning of the sentence, omit features of 1 and 2 words back; at end of sentence, omit features of 1 and 2 words forward) 
4. capitalization, features of the sentence, your own special dictionary, etc.


Understanding the scoring:
1. Accuracy = (correct BIO tags)/Total BIO Tags
2. Precision, Recall and F-measure measure Noun Group performance: A noun group is correct if it in both the system output and the answer key.
	1. Precision = Correct/System_Output
	2. Recall = Correct/Answer_key
	3. F-measure = Harmonic mean of Precision and Recall