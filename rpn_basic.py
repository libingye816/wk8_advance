#!/usr/bin/env python3

# vim: tabstop=4 shiftwidth=4 softtabstop=4 expandtab
#
# This is a "modeline", which tells vim how to handle tabs an spaces (many other
# editors will also respect vim modelines). By default, vim ignores modelines,
# however, if you add "set modeline" to your .vimrc it will pay attention to
# this line.



import logging
import math
import operator



OPERATORS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        #'/': operator.div,
        }


def calculate(expression):
    '''Takes a valid RPN expression as a string and computes the result

    RPN is Reverse Polish Notation, essentially a stack based calculator.
    The simplest example is "1 1 +", which returns 2.
    '''
    stack = []

    for operand in expression.split():
        logging.debug("Stack: {} || Operand: {}".format(stack, operand))
        try:
            stack.append(float(operand))
        except ValueError:
            operator_fn = OPERATORS[operand]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = operator_fn(arg1, arg2)
            stack.append(result)

    if len(stack) != 1:
        raise RuntimeError("Malformed expression")
    return stack.pop()



def main():
    while True:
        try:
            to_calculate = input("rpn calc> ")

            # 'q'uit
            if to_calculate[0] == 'q':
                break

            answer = calculate(to_calculate)
            print(answer)

        except RuntimeError as e:
            print("Error:", e)

# This lets your program act as both a _script_ and a _module_
if __name__ == '__main__':
    main()

