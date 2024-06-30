# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 02:12:22 2024

@author: User
"""

def divide(numerator, denominator):
  """Divides two numbers and handles ZeroDivisionError.

  Args:
      numerator: The number to be divided.
      denominator: The divisor.

  Returns:
      The result of the division.
  """
  try:
    result = numerator / denominator
  except ZeroDivisionError:
    print("Error: Cannot divide by zero")
  else:
    # This block executes only if no exception occurs in the try block
    print(f"Result: {result}")
  finally:
    # This block always executes, even if an exception occurs
    print("Cleaning up...")

# Example usage
divide(10, 2)  # Output: Result: 5.0
divide(10, 0)  # Output: Error: Cannot divide by zero
                  #        Cleaning up...
