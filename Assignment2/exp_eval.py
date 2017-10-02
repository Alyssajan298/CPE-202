from Stacks import StackArray

# def infix_to_postfix(infixexpr):
#     """Converts an infix expression to an equivalent postfix expression """

#     """Signature:  a string containing an infix expression where tokens are space separated is
#        the single input parameter and returns a string containing a postfix expression
#        where tokens are space separated"""
    
#     ????? = StackArray(30)
# ...
#     tokenList = infixexpr.split()
# ...
#     return " ".join(postfixList)


def postfix_eval(postfixExpr):
    """ Takes in Postfix Expression and evaluates"""
    newStack = StackArray(30)
    postfix = postfixExpr.split()
    for x in postfix:
        if x not in ('*','-','/','+','^'):
            newStack.push(int(x))
        elif x in ('*','-','/','+','^'):
            newStack.push(doMath(x,newStack.pop(),newStack.pop()))
    return newStack.pop()


def doMath(op, op1, op2):
    """ Evaluates Math Expressions for postfix_eval """
    if op == '*':
        return float(op2) * op1
    elif op == '-':
        return float(op2) - op1
    elif op == '/':
        if op1 == 0:
            raise ValueError
        return float(op2) / op1
    elif op == '+':
        return float(op2) + op1
    elif op == '^':
        return float(op2) ** op1


def postfix_valid(postfixexpr):
    """ Tests to see that an input is a solvable postfix expressiojn"""
    counter = 0
    if postfixexpr == "":
        return False
    tokenList= postfixexpr.split()
    if tokenList[0] in ('*','-','/','+','^'):
        return False
    for x in tokenList:
            if x not in ('*','-','/','+','^'):
                counter+=1
            else:
                counter-=1
    return counter == 1
                           
