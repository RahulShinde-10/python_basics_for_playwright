# Set are mutable in python, you can change the value of a set.
# syntax - value = set()  - this is empty set
# syntax - value = {1,2,3,4}   - set with value (set do not contains key value pair) but set uses curly braces same as dict.
# if set contains repeated value then it will only take it as one value it will not give repeated value.

# set and dictionary both uses curly braces, so here how u will create empty set? see below

s = set()  #this is the empty set
s = {}  # this empty dictionary
s = {1,2,3,4,4,4}  # this is set with value - to diffrentiate it remember dictonary comes with key value pair but set not.

print(s)  # set will not repeat the repeated value - it will take it as only one


# set methods 

#add method - s.add()  - this method will add the value - very imp method
s = {1,2,3,4,4,4}
s.add(10)
print (s)


# operation in set

#union and intersection operation - union will return all items from 2 set and intersection will return common value from 2 set
s = {1,2,3,4,5}
s2 = {6,7,8,9,1}

print(s.union(s2))
print(s.intersection(s2))


# practice set for set and dictionay 

s = {
    "madat": "help",
    "billi": "cat"
}

a = input("enter the word you want: ")
print(s[a])

# practice set for set and dictionary 
s = set()
n = input("enter the number: ")
s.add(int(n))
n = input("enter the number: ")
s.add(int(n))
n = input("enter the number: ")
s.add(int(n))
n = input("enter the number: ")
s.add(int(n))
print(s)


# practice set for set and dictionary - adding 18 as string and int
s = set()
s.add(18)
s.add("18")
print(s)


# practice set for set and dictionary - creating dic with key value pair

d = {}
name = input("Enter the name: ")
lang = input("Ente the lang: ")
d.update({name:lang})

name = input("Enter the name: ")
lang = input("Ente the lang: ")
d.update({name:lang})

print(d)
