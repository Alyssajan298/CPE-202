from Stacks import StackArray

def infix_to_postfix(infixexpr):
    """Converts an infix expression to an equivalent postfix expression """

    """Signature:  a string containing an infix expression where tokens are space separated is
       the single input parameter and returns a string containing a postfix expression
       where tokens are space separated"""
    
    newStack = StackArray(30)
    postfixList= []
    tokenList = infixexpr.split()
    x = 0
    par = 0 
    while x < len(tokenList): 
        if tokenList[x] is ('('):
            newStack.push(tokenList[x])
            par = x+1
            while par < len(tokenList) and tokenList[par] not in (')'):
                if tokenList[par] not in ('*','-','/','+','^'):
                    postfixList.append(tokenList[par])
                elif tokenList[par] in ('^'):
                    if newStack.peek() in ('('):
                        newStack.push(tokenList[par])
                    elif newStack.peek() in '^':
                        newStack.push(tokenList[par])
                    elif newStack.peek() in ('*','/'):
                        newStack.push(tokenList[par])
                    elif newStack.peek() in ('+','-'):
                        newStack.push(tokenList[par])
                elif tokenList[par] in ('*','/'):
                    if newStack.peek() in ('('):
                        newStack.push(tokenList[par])
                    elif newStack.peek() in ('^'):
                        postfixList.append(newStack.pop())
                        newStack.push(tokenList[par])
                    elif newStack.peek() in ('+','-'):
                        newStack.push(tokenList[par])
                    elif newStack.peek() in ('*','/'):
                        postfixList.append(newStack.pop())
                        newStack.push(tokenList[par])
                elif tokenList[par] in ('+','-'):
                    if newStack.peek() in ('('):
                        newStack.push(tokenList[par])
                    elif newStack.peek() in ('^','*','/'):
                        while newStack.peek() in ('^','*','/') and newStack.peek() not in ('(') :
                            postfixList.append(newStack.pop())
                        newStack.push(tokenList[par])
                    elif newStack.peek() in ('+','-'):
                        while newStack.peek() in ('+','-'):
                            postfixList.append(newStack.pop())
                        newStack.push(tokenList[par])
                par+=1
            while newStack.peek() not in ('('):
                postfixList.append(newStack.pop())
            newStack.pop()

                
            x = par

                     
        
        elif tokenList[x] not in ('*','-','/','+','^','(',')'):
            postfixList.append(tokenList[x])
        elif tokenList[x] in ('^'):
            if newStack.is_empty():
                newStack.push(tokenList[x])
            elif newStack.peek() in '^':
                newStack.push(tokenList[x])
            elif newStack.peek() in ('*','/'):
                newStack.push(tokenList[x])
            elif newStack.peek() in ('+','-'):
                newStack.push(tokenList[x])
        elif tokenList[x] in ('*','/'):
            if newStack.is_empty():
                newStack.push(tokenList[x])
            elif newStack.peek() in ('^'):
                    postfixList.append(newStack.pop())
                    newStack.push(tokenList[x])
            elif newStack.peek() in ('+','-'):
                    newStack.push(tokenList[x])
            elif newStack.peek() in ('*','/'):
                    postfixList.append(newStack.pop())
                    newStack.push(tokenList[x])
        elif tokenList[x] in ('+','-'):
             if newStack.is_empty():
                newStack.push(tokenList[x])
             elif newStack.peek() in ('^','*','/'):
                while newStack.peek() in ('^','*','/') or not newStack.is_empty():
                    postfixList.append(newStack.pop())
                newStack.push(tokenList[x])
             elif newStack.peek() in ('+','-'):
                while newStack.peek() in ('+','-'):
                    postfixList.append(newStack.pop())
                newStack.push(tokenList[x])
        x+=1
    while not newStack.is_empty():
        postfixList.append(newStack.pop())
    return " ".join(postfixList)


def postfix_eval(postfixExpr):
    """ Takes in Postfix Expression and evaluates"""
    newStack = StackArray(30)
    postfix = postfixExpr.split()
    for x in postfix:
        if x not in ('*','-','/','+','^'):
            newStack.push(x)
        elif x in ('*','-','/','+','^'):
            newStack.push(doMath(x,float(newStack.pop()),float(newStack.pop())))
    return newStack.pop()


def doMath(op, op1, op2):
    """ Evaluates Math Expressions for postfix_eval """
    if op == '*':
        return  op2 * op1
    elif op == '-':
        return  op2 - op1
    elif op == '/':
        if op1 == 0:
            raise ValueError
        return  op2 / op1
    elif op == '+':
        return  op2 + op1
    elif op == '^':
        return (op2**op1)


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
                           
