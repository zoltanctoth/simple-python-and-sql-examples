#!/usr/bin/env python3

# Global variable
global_var = "I am a global variable"

def calculate_sum(a, b):
    """A simple function to demonstrate stepping into during debugging."""
    local_var = "I am a local variable"
    result = a + b
    print(f"Global variable: {global_var}")
    print(f"Local variable: {local_var}")
    return result

if __name__ == "__main__":
    # Main code execution
    x = 10
    y = 20
    print("About to call calculate_sum function")
    sum_result = calculate_sum(x, y)
    print(f"The sum is: {sum_result}")
    print("Program completed") 