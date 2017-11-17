Name : Nikhil Lavoo Kajrekar

UTA ID : 1001552488

Programming Language : Python2.4.3

Code Structure : 

(1)check_true_false.py
	-Main : Function to convert the input string into expression and pass to check_true_false function.  
		
	 
(2)logical_expression.py
	-check_true_false: Function for checking if the statement and its negation entail from the knowledge base. It uses TT_CHECKS_ALL(), which in-turn uses PL_TRUE() and extend.
	
	-class logical_expression for storing all the variables and expressions.	
	
	-retrieve_symbols:
		Function for retrieving all the symbols from the expression.
	
	-tt_check_all:
		Function for performing the tt_check_all algorithm.
	
	-pl_true:
		Function for performing the pl_true algorithm.
	
	-extend model:
		Required for tt_check_all algorithm.

		 	
How to run the code : 

python check_true_false.py wumpus_rules.txt additional_knowledge.txt statement.txt
