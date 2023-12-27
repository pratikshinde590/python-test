# Import the programs
# from program1 import add_numbers
from program2 import multiply_numbers
# from program3 import divide_numbers

# # Test Program 1: Addition
# num1_add = 5
# num2_add = 7
# sum_result = add_numbers(num1_add, num2_add)
# assert sum_result == num1_add + num2_add, f"Program 1 Test failed! Expected {num1_add + num2_add}, got {sum_result}"
# print("Program 1 Test passed!")

# Test Program 2: Multiplication
num1_mul = 3
num2_mul = 4
product_result = multiply_numbers(num1_mul, num2_mul)
assert product_result == num1_mul * num2_mul, f"Program 2 Test failed! Expected {num1_mul * num2_mul}, got {product_result}"
print("Program 2 Test passed!")

# # Test Program 3: Division
# num1_div = 8
# num2_div = 2
# quotient_result = divide_numbers(num1_div, num2_div)
# assert quotient_result == num1_div / num2_div, f"Program 3 Test failed! Expected {num1_div / num2_div}, got {quotient_result}"
# print("Program 3 Test passed!")
