# Tuple is immutable just like string, you cannot make changes in existing Tuple but you can make new tuple.
# syntax - value = (3,5,7, "rahul", false)



a = (1,2,3,5)
print (type(a))


# tuple methods

#tuple methods - count method - it will count how many values are in tuple
a = (1,2,3,5)
b = a.count(2)
print(b)


#tuple methods - index method - it will index in tuple
a = (1,2,3,5)
b = a.index(2)
print(b)



# practice questions for list and tuple

fruits = []
f1 = input("enter the fruit name: ")
fruits.append(f1)
f2 = input("enter fruit name: ")
fruits.append(f2)

print(fruits)


# practice questions for list and tuple
marks = []
f1 = input("enter the marks: ")
marks.append(f1)
f2 = input("enter the marks: ")
marks.append(f2)
marks.sort()

print(marks)



