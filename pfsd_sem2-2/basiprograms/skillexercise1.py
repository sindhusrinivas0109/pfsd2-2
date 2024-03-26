"""n = int(input("enter the number:"))
if n==0:
    print("wrong input")
else:
    for i in range(n,n+1):
        val = n*(n*1)
        print(val) """

"""x = 0
str1 = "thisismycountryindia"
for i in str1:
    x = x+1
    print(str[0:x])"""

# program to print stars
"""
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")"""

#format - predefined function
#decimal -> binary
"""a1 = 1024
a2 = format(a1,'b')
print(a2)

a1 = 1045
a3 = "10100"
a2 = int(format(int(a3,2),'d'))
print(a2)

a4 = 1023
a5 = format(a4,'x')
print(a5)"""

# converting the string to integer
"""
a = input("enter the string:")
print(type(a))
a1 = int(a)
print(type(a1))"""

"""# sum of complex numbers

complex_number1 = complex(input("Enter the first complex number (in the form a+bj): "))
complex_number2 = complex(input("Enter the second complex number (in the form a+bj): "))
float_number1 = float(input("Enter the first float number: "))
float_number2 = float(input("Enter the second float number: "))
integer_number1 = int(input("Enter the first integer number: "))
integer_number2 = int(input("Enter the second integer number: "))
result_complex = complex_number1 + complex_number2
print(f"Sum of complex numbers: {result_complex}")
result_float = float_number1 + float_number2
print(f"Sum of float numbers: {result_float}")
result_integer = integer_number1 + integer_number2
print(f"Sum of integer numbers: {result_integer}")"""

""""
# Integer
integer_value = 42

# Convert to float
float_value = float(integer_value)
print(f"Integer: {integer_value}")
print(f"Float: {float_value}")
"""
""""
# List of numbers
numbers = [5, 10, 15, 20, 25]
total = 0
for number in numbers:
    total += number
average = total / len(numbers)
print(f"The average is: {average}")
"""

"""
# String and integer
string_number = "42"
integer_number = 10
converted_number = int(string_number)
result = converted_number + integer_number
print(f"The sum of {string_number} and {integer_number} is: {result}")
"""
"""
integer_number = int(input("Enter an integer: "))
float_number = float(integer_number)
print(f"The integer {integer_number} as a float: {float_number}")"""


input_string = input("Enter a string: ")
input_integer = int(input("Enter an integer: "))
string_as_integer = int(input_string)
result = string_as_integer + input_integer
print(f"The sum of {input_string} and {input_integer} is: {result}")

