# exception handling is the process of responding to unwanted or unexpected events when program runs. exception handling deals with this events to avoid program crashing.
#If you are feeling that your code is going to give you error then you can use exception handling concept.

#try except - exception handling
#syntax - 

#try:
   #code

#except exception as e:             - use exception as e only when you using e while printing in next line 
#print or next code


# try:
#     num = int(input("Enter an integer: "))       # here user will enter the non int input 

# except:
#     print("Enter number is not integer")         # since user entered non int input so try except will trigger and it will print this line



# a = 5
# b = 0

# try:
#     print (a/b)             # here im priting a divide by b which is not divisible 

# except:
#     print("it is not divisible by zero")        # since 2 numbers are not divisible so it will go to except block and print next line of code


# print("End of program")                   # it will execute the print statement without throwing any error since we using exception handling here



#Note - except block will only work or it will jump to except block only when if try block gives some error. if try block works fine then except block will not execute.



#finally block 
#finally block will execute if we get the error or if we did not get the error. no matter what the result it will print anything comes under finally.

# a = 5
# b = 0

# try:
#     print (a/b)             

# except:
#     print("it is not divisible by zero")      

# finally:
#     print("End of program")  # using finally it will print whatever inside of this block no matter what's the outcome.





# handling multiple error messages

a = 5
b = 2

try:
    print (a/b)
    k = int((input("Enter a number: ")))  
    print(k)          

except ZeroDivisionError as e:
    print("it is not divisible by zero")  

except ValueError as e:                      # here im handling another error message using another except block.
    print("this is value error")