a = "rahul"  # this is string which comes in double quote

#string is immutable we cannot make changes in string instead it will create new string.
#syntax - value = "Rahul"

shortname = a[0:3] # here it will print till 3 but will not include 3 so it will print rah
shortname1 = a[1]  # here im trying to print index 1 which is a, so it will print only a
print (shortname1)
print (shortname)


# string negative slicing
name = "Rahul"

shortname = name[-4:-1]  # here i did negative slicing of string
print (shortname)


# string slicing with SKIP
a = "0123456789"
b = a[1:8:3]
print (b)   # here 1:8:3 means it will start counting from 1 to 8 then :3 means from 1 to 8 it will jump/SKIP by 3


