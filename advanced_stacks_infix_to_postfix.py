def infixToPostfix(A):
    Priority = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities of Operators 

    stack = [] # initialization of empty stack

    output = '' 

    

    for character in A:

        if character.isalpha():  # if an operand append in postfix expression

            output+= character

        elif character=='(':  # else Operators push onto stack

            stack.append('(')

        elif character==')':

            while stack and stack[-1]!= '(':

                output+=stack.pop()

            stack.pop()

        else: 

            while stack and stack[-1]!='(' and Priority[character]<=Priority[stack[-1]]:

                output+=stack.pop()

            stack.append(character)

    while stack:

        output+=stack.pop()

    return output


print(infixToPostfix("x^y/(a*z)+b"))
         
    