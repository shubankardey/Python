#Take n as an input from the user and write a program to print the table of n.

inputValue=int(input("Enter a number of your choice :"))
print("Table of",inputValue,"is :")
for p in range (1,11) :
    print (inputValue, "x",p, "=",p* inputValue)