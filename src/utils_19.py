#!/usr/bin/env python3
"""
Calculator utility.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Calculator module loaded")


# Update 51
def new_function_51():
    """New function added in update 51."""
    return 51
