#!/usr/bin/env python3

# vim: tabstop=4 shiftwidth=4 softtabstop=4 expandtab
#
# This is a "modeline", which tells vim how to handle tabs an spaces (many other
# editors will also respect vim modelines). By default, vim ignores modelines,
# however, if you add "set modeline" to your .vimrc it will pay attention to
# this line.

import logging
logging.basicConfig()

import math
import operator
import sys



class Calculator:
    def __init__(self):
        self.OPERATORS = {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                '/': operator.truediv,
                }

    def coerce_number(self, operand):
        return float(operand)

    def calculate(self, expression):
        stack = []

        for operand in expression.split():
            logging.debug("Stack: {} || Operand: {}".format(stack, operand))
            try:
                stack.append(self.coerce_number(operand))
            except ValueError:
                operator_fn = self.OPERATORS[operand]
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = operator_fn(arg1, arg2)
                stack.append(result)

        if len(stack) != 1:
            raise RuntimeError("Malformed expression")
        return stack.pop()


class IntegerCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.OPERATORS['/'] = operator.floordiv

    def coerce_number(self, operand):
        return int(operand)

def main():
    calculator = Calculator()
    integer_calculator = IntegerCalculator()

    while True:
        try:
            to_calculate = input("rpn calc> ")

            # 'q'uit
            if to_calculate[0] == 'q':
                sys.exit()

            print("Float Answer:", calculator.calculate(to_calculate))
            print("  Int Answer:", integer_calculator.calculate(to_calculate))

        except RuntimeError as e:
            print("Error:", e)

        # Let the user press Ctrl-d to quit
        except EOFError:
            break

# This lets your program act as both a _script_ and a _module_
if __name__ == '__main__':
    main()

