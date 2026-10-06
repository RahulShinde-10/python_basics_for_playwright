# function is a group of statements performing a specific task
# syntax is:
# def func():
      # print("Hello")

# function can be called any number of time at anywhere in program


# if you want to do a sametask for multiple users then you can't do it same thing multiple times. here you will use functions.

def avg():          # here you will use standard syntax to define a function
    a = int(input("Enter your number: "))       #here you will write a code
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    average = (a+b+c)/3
    print(average)   # this piece of code is called function definition

avg()    # this step is nessesary to give because this line will print actual code. if this line is not present then it will not execute the code
avg()       # if you want to print it for 2 times then use same line in next line or n times.
# this is also called as function call


# function calling
#whenever we want to call a function, we put the name of function folloed by paranthesis -  func1()


#types of funtions: 
#built in function - already present in python  - eg: len(), print(), range()
#user define function - define by user   - eg: func1() - created by user



# function with argument
def func(name):        # here i have passed argument as name in function
    print("Good day " + name)  # here im printing name along with good day

func("Harry")  # here im passing Harry as a value in defined argument name
# As a final output it will print Good Day Harry - harry value will go in name and we are printing the name - this is how functions with argument is working



# How to return value in function
def func():      # function is defined
    print("Good day")     # priting good day
    return "done"         # here i added return with some value as "Done" - so basically it will pick done value and assigned it to below value a

a = func()    # defined a 
print(a)       # printing a - here it will pick Done value and assinged to a and then it will print a as Done