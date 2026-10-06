#python list are container to store value of any datatype.
#List is mutable in python
#syntax -  Value = [a, 2, good, 6.7]



# List example
friends = ["apple", "orange", 5, 4.5, False, "Rahul"]
print(friends[0])


# changing the list - making list mutable - we can change the value in list 
friends = ["apple", "orange", 5, 4.5, False, "Rahul"]
friends[0] = "papaya"
print(friends[0])


# list indexing - we can indexed a list just like string
friends = ["apple", "orange", 5, 4.5, False, "Rahul"]
print (friends[1:4])


#list methods - append method - this method will add new value in list at last
friends = ["apple", "orange", 5, 4.5, False, "Rahul"]
friends.append("Jio")
print(friends)


# list methods - sort method - this will sort the value from list in ascending order
number = [6,2,8,3,8,6,1]
number.sort()
print(number)


# list methods - reverse method - this will reverse the value from list
number = [6,2,8,3,8,6,1]
number.reverse()
print(number)


# list methods - insert method - this will insert the value in list at specific index
number = [6,2,8,3,8,6,1]
number.insert(3, 1)   # this will add 1 at index 3 
print(number)



# list methods - pop method - this will pop out the value in list from specific index
number = [6,2,8,3,8,6,1]
number.pop(3)   # this will pop out the value at index 3
print(number)


# list methods - remove method - this will remove the value in list 
number = [6,2,8,3,8,6,1]
number.remove(2)   # this will remove the given value
print(number)