#sometimes we want to repeat a set of statements in our program. Here loops make it easy what to repeat and how 
#there are 2 types of loops which are: for loop and while loop

#for loop
#for loop is used to iterate through a swquence like list, tuple or string
for i in range(1,6):     # here range function will give you numbers from 1 to 5 
    print(i)


l = [1,2,3,4,5]
for i in l:       # here i in l means it will print element present in l 
    print (i)





# while loop
#in while loop -> conditions is checked first. if it evaluates to true, body will execute else not
#if the loop is entered, the process of condition check and execution is continued until the condition become false
#syntax 
#while (condition) - it will keep executing until condition is true
   #body of loop


i = 1
while(i<6):     #while loop will only execute until condition is true(once the condition get false then it will exit the loop) - if condition is always true then it will become infinite loop
    print(i)
    i+=1


l = [1, "rahul", "shital", False]
i = 0
while(i<len(l)):  # here value for i is zero and we have 4 values so in while loop condition we added lenght of i is less than lenght of l (lenght of l is 4)
    print(l[i])   # here value of i is zero and it is less than 4 then it will print 0 
    i+=1          # at the end when value of i becomes 4 then it will break the loop because condtion got false 



i = int(input("Enter the value: "))    # here we need to initialize the value - very imp
while(i<50):                           # here you have given condition in while loop that value of i should be less than 50
    i = int(input("Enter the value: "))   # here you will be entering the input
    print(i)                            # if value is less than 50 it will print given input value

print("you are good to go")            # the moment value is greater than 50 loop will end and it will print this line



# Break statement
#Break stement is used to come out of the loop when encountered. it basically the program to exit the loop

for i in range(100):
    if(i==34):      # here i added the condition that if i value is equal to 34 then it should break the loop
        break   # here it will break the loop
    print(i)



# continue statement
# it is used to skip the iteration 
for i in range(100):
    if(i==34):      # here continue statement will skip 34 value and print from 0 to 100 except 34
        continue      # here it will skip the value 34 because continue statement will always skip the iteration (ieration is 34)
    print(i)



# pass statement

for i in range(100):
    pass       # if you have incomplete for loop and you wanted to execute while loop  but during execution you got indentation error then you can use pass inside for loop to execute only while loop
               # here pass statement will pass it - skip the for loop
i = 0
while(i<45):
    print(i)
    i+=1


#imp note: 
#You can use for loop when you know exactly how many times you want to execute the loop
#You can use while loop when you don't know how many times you need to execute the loop