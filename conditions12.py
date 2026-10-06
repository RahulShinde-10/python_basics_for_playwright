# explaining condition with help of example - sometime we order ice cream if the day is sunny 
# here the decision is depend on condition being met
# in python as well, we must able to execute the instructions on condition being met.

# if else condition
a = int(input("Enter your age: "))

if(a>18):
    print("You are above the age: ")

else:
    print("your are below the age: ")



# elif condition
a = int(input("Enter your age: "))

if(a>18):
    print("You are above the age: ")

elif(a<0):
    print("You are entering wrong age")

else:
    print("your are below the age: ")



# Relational Operators - Relational operators used to evaluate condition inside the if statements
# eg: == , >= , <= 

# Logical operators - logical operators operates condition statements
# and - true if both operand is true else false
# or - true if one of the operant is true or else false
# not - invert true to false and false to true


# practice set
marks1 = int(input("Enter the marks1: "))
marks2 = int(input("Enter the marks2: "))
marks3 = int(input("Enter the marks3: "))

total_percentage = (100*(marks1 + marks2 + marks3))/300

if (total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are pass", total_percentage)

else:
    print("you are fail", total_percentage)


# practice set
p1 = "click on it"
p2 = "buy this"
p3 = "use this"

message = input("enter the input: ")

if (p1 in message or p2 in message or p3 in message):
    print("this is spam")

else:
    print("this is not spam")


# practice set
list = ["rahul", "shital", "shubham"]

message = input("enter the name: ")

if (message in list):
    print("true")

else:
    print("false")
