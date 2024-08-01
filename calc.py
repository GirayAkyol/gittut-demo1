#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: calc.py <expression>")
        return

    expression = ''.join(sys.argv[1:]).replace(" ", "")

    if '+' in expression:
        # addition
        num1, num2 = expression.split('+')
        result = float(num1) + float(num2)
    elif '-' in expression:
        num1, num2 = expression.split('-')
        result = float(num1) - float(num2)
    elif '*' in expression:
        num1, num2 = expression.split('*')
        result = float(num1) * float(num2)
    elif '/' in expression:
        num1, num2 = expression.split('/')
        if float(num2) == 0:
            print("Error: Division by zero.")
            return
        result = float(num1) / float(num2)
    else:
        print("Unsupported operator. Use +, -, *, or /.")

    print(result)

if __name__ == "__main__":
    main()