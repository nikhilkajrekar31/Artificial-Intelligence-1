import sys
from copy import copy

def check_true_false(knowledge_base, statement, negation, dict1):
    
    try:
        output_file = open('result.txt', 'w')
    except:
        print('failed to create output file')
    
    # Storing all the knowledge_base symbols.
    knowledge_base_symbols = []
    # Storing all the sentence variables
    # NOTE: not_setence and sentence will have the same variables.
    s_symbols = []

    # Making a shallow copy of the dict1 and storing the values
    # in the model
    model = dict1.copy(); 

    # extracting all the symbols from the KB
    retrieve_symbols(knowledge_base, knowledge_base_symbols)
    retrieve_symbols(statement, s_symbols)

    # removing the repeated ones
    knowledge_base_symbols = list(set(knowledge_base_symbols))
    s_symbols = list(set(s_symbols))

    # Extending the kb_list with the alpha symbol list
    knowledge_base_symbols.extend(s_symbols)
    # Removing the duplicates
    symbols = list(set(knowledge_base_symbols))

    # removing the symbols I know are true
    for key in model.keys():
        try:
            symbols.remove(key)
        except Exception:
            # would be handled in the PL_FUNCTION itself.
            # just added here so that the code doesn't crash
            pass

    # Doing the TT check for alpha
    result_alpha = TT_CHECKS_ALL(knowledge_base, statement, symbols, model)

    # Doing the TT check for negation of alpha
    result_not_alpha = TT_CHECKS_ALL(knowledge_base, negation, symbols, model)
    
    print                 
    print 'ANSWER: ', 

    # Different answers depending on the values of alpha and not alpha
    if result_alpha == True and result_not_alpha == False:
        output_file.write('definitely true') 
        print 'definitely true'
    elif result_alpha == False and result_not_alpha == True:
        output_file.write('definitely false')
        print 'definitely false'
    elif result_alpha == False and result_not_alpha == False:
        output_file.write('possibly true, possibly false')
        print 'possibly true, possibly false'
    elif result_alpha == True and result_not_alpha == True:
        output_file.write('both true and false')
        print 'both true and false'
    else:
        output_file.write('Error in the code')    
        
    print 
    output_file.close()
    
class logical_expression:
    """X logical statement/sentence/expression class"""
    # All types need to be mutable, so we don't have to pass in the whole class.
    # We can just pass, for example, the symbol variable to a function, and the
    # function's changes will actually alter the class variable. Thus, lists.
    def __init__(self):
        self.symbol = ['']
        self.connective = ['']
        self.subexpressions = []


def print_expression(expression, separator):
    """Prints the given expression using the given separator"""
    if expression == 0 or expression == None or expression == '':
        print '\nINVALID\n'

    elif expression.symbol[0]: # If it is a base case (symbol)
        sys.stdout.write('%s' % expression.symbol[0])

    else: # Otherwise it is a subexpression
        sys.stdout.write('(%s' % expression.connective[0])
        for subexpression in expression.subexpressions:
            sys.stdout.write(' ')
            print_expression(subexpression, '')
            sys.stdout.write('%s' % separator)
        sys.stdout.write(')')


def read_expression(input_string, counter=[0]):
    """Reads the next logical expression in input_string"""
    # Note: counter is a list because it needs to be a mutable object so the
    # recursive calls can change it, since we can't pass the address in Python.
    
    result = logical_expression()
    length = len(input_string)
    while True:
        if counter[0] >= length:
            break

        if input_string[counter[0]] == ' ':    # Skip whitespace
            counter[0] += 1
            continue

        elif input_string[counter[0]] == '(':  # It's the beginning of a connective
            counter[0] += 1
            read_word(input_string, counter, result.connective)
            read_subexpressions(input_string, counter, result.subexpressions)
            break

        else:  # It is a word
            read_word(input_string, counter, result.symbol)
            break
    return result


def read_subexpressions(input_string, counter, subexpressions):
    """Reads a subexpression from input_string"""
    length = len(input_string)
    while True:
        if counter[0] >= length:
            print '\nUnexpected end of input.\n'
            return 0

        if input_string[counter[0]] == ' ':     # Skip whitespace
            counter[0] += 1
            continue

        if input_string[counter[0]] == ')':     # We are done
            counter[0] += 1
            return 1

        else:
            expression = read_expression(input_string, counter)
            subexpressions.append(expression)


def read_word(input_string, counter, target):
    """Reads the next word of an input string and stores it in target"""
    word = ''
    while True:
        if counter[0] >= len(input_string):
            break

        if input_string[counter[0]].isalnum() or input_string[counter[0]] == '_':
            target[0] += input_string[counter[0]]
            counter[0] += 1

        elif input_string[counter[0]] == ')' or input_string[counter[0]] == ' ':
            break

        else:
            print('Unexpected character %s.' % input_string[counter[0]])
            sys.exit(1)


def valid_expression(expression):

    # print expression

    """Determines if the given expression is valid according to our rules"""
    if expression.symbol[0]:
        return valid_symbol(expression.symbol[0])

    if expression.connective[0].lower() == 'if' or expression.connective[0].lower() == 'iff':
        if len(expression.subexpressions) != 2:
            print('Error: connective "%s" with %d arguments.' %
                        (expression.connective[0], len(expression.subexpressions)))
            return 0

    elif expression.connective[0].lower() == 'not':
        if len(expression.subexpressions) != 1:
            print('Error: connective "%s" with %d arguments.' %
                        (expression.connective[0], len(expression.subexpressions)))
            return 0

    elif expression.connective[0].lower() != 'and' and \
         expression.connective[0].lower() != 'or' and \
         expression.connective[0].lower() != 'xor':
        print('Error: unknown connective %s.' % expression.connective[0])
        return 0

    for subexpression in expression.subexpressions:
        if not valid_expression(subexpression):
            return 0
    return 1


def valid_symbol(symbol):
    """Returns whether the given symbol is valid according to our rules."""
    if not symbol:
        return 0

    for s in symbol:
        if not s.isalnum() and s != '_':
            return 0
    return 1

# Function for retrieving all the symbols from the expression.
def retrieve_symbols(expression, symbols):

    if expression.symbol[0]:
        symbols.append(expression.symbol[0])

    for subexpression in expression.subexpressions:
        retrieve_symbols(subexpression, symbols)


# Function for performing the tt_check_all algorithm. 
def TT_CHECKS_ALL(KB, a, symbols, model):

    if not symbols:
        # If true in KB
        if PL_TRUE(KB, model):
            return PL_TRUE(a, model)
        else:
            return True
    
    # Storing first symbol
    p = symbols[0]
    # Storing rest of the symbols
    rest = symbols[1:]

    return TT_CHECKS_ALL( KB, a, rest, extend_model(model, p, True) ) \
           and TT_CHECKS_ALL( KB, a, rest, extend_model(model, p, False) )


# Function for performing the pl_true algorithm.
def PL_TRUE(expression, model):
    # Check for connective AND
    if expression.connective[0].lower() == 'and':
        # A boolean value that will return the value for this expression
        boolean = True
        # Going over all the subexpressions and AND-ing them.
        for i, subexpression in enumerate(expression.subexpressions):
            # Finding the inital value of the bool.
            if(i == 0):
                boolean = PL_TRUE(subexpression, model)
                continue;
            boolean = boolean and PL_TRUE(subexpression, model)
        # Returning the value of all the AND subexpressions.
        return boolean

    # Check for connective OR
    elif expression.connective[0].lower() == 'or':
        boolean = True
        for i, subexpression in enumerate(expression.subexpressions):
            if(i == 0):
                boolean = PL_TRUE(subexpression, model)
                continue;
            boolean = boolean or PL_TRUE(subexpression, model)
        return boolean

    # Check for the connective NOT
    elif expression.connective[0].lower() == 'not':
        # A boolean value that will return the value for this expression
        # Here, we are just concerned with the not of the value.
        boolean = not PL_TRUE(expression.subexpressions[0], model)
        return boolean

    # Check for the connective XOR
    elif expression.connective[0].lower() == 'xor':
        boolean = True
        for i, subexpression in enumerate(expression.subexpressions):
            if(i == 0):
                boolean = PL_TRUE(subexpression, model)
                continue;
            # taking the XOR
            boolean = boolean ^ PL_TRUE(subexpression, model)
        return boolean

    elif expression.connective[0].lower() == 'if':
        # Getting the values of the two expressions I want to if.
        X = PL_TRUE(expression.subexpressions[0], model)
        Y = PL_TRUE(expression.subexpressions[1], model)
        # returing the if values for both the expressions
        return ( (not X) or Y )

    elif expression.connective[0].lower() == 'iff':
        # Getting the values of the two expressions I want to iff.
        X = PL_TRUE(expression.subexpressions[0], model)
        Y = PL_TRUE(expression.subexpressions[1], model)
        # returing the iff values for both the expressions
        return ( (not X) or Y ) and ( (not Y) or X )
    
    # return the value of the symbol from the model dictionary
    return model[expression.symbol[0]]

# Required for tt_check_all algorithm.
def extend_model(model, key, value):
    model[key] = value
    return model
