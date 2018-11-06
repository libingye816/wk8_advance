#!/usr/bin/env python3

import operator
import readline
from termcolor import colored,cprint

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
    '<<': operator.lshift,
    '>>': operator.rshift,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        #print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        arg=input("rpn calc> ")
        cprint("Input: ",end='')
        for token in arg.split():
            try:
                token=int(token)
                if token<0:
                    cprint(str(token),'red',attrs=['bold'],end=' ')
                else:
                    cprint(str(token),end=' ')
            except ValueError:
                if token=='+' or token=='-' or token=='*' or token=='/':
                    cprint(token,'green',end=' ')
                else:
                    cprint(token, 'blue', end=' ')
        result = calculate(arg)
        print('')
        print("Result: ", result)

if __name__ == '__main__':
    main()
