#Write a python program to take 2 inputs from user and perform arithmetic operations
#based onthe choice of the user.(using Function is optional)

# print("Choose an operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = input("Enter choice (1/2/3/4): ")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if choice == '1':
#     result = num1 + num2
#     print(num1, " + ", num2, " = ", result)
# elif choice == '2':
#     result = num1 - num2
#     print(num1, " - ", num2, " = ", result)
# elif choice == '3':
#     result = num1 * num2
#     print(num1, " X ", num2, " = ", result)
# elif choice == '4':
#     if num2 != 0:
#         result = num1 / num2
#         print(num1, " / ", num2, " = ", result)
#     else:
#         print("Division by zero is not possible")
# else:
#     print("Invalid input")
    
    
    
    
# # using function

def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x,y):
    if y == 0:
        return "Error! Can not divide by zero."
    else:
        return x/y

print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice =='1':
    print(num1, " + ", num2, " =", add(num1, num2))
elif choice =='2':
    print(num1, " - ", num2, " =", subtract(num1, num2))
elif choice =='3':
    print(num1, " X ", num2, " =", multiply(num1, num2))
elif choice =='4':
    print(num1, " / ", num2, " =", divide(num1, num2))
else:
    print("Invalid input")