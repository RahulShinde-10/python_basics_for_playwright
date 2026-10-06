# Dictionary are mutable in python, you can change the value in dictionary
# Dictornary comes in key value pair
#syntax - value = {"rahul": 200, "yoyo": 56}
# if you want to print value then you have to always enter key in print statement then it will print value in output
# Dictionary cannot contains duplicate keys, although it can contain duplicate values but not the keys.


# Writing dictionary syntax and print required output from dictionary
marks = {
    "Rahul":100,
    "Adi":20,
    "Shubham":70
}

print(marks, type(marks))
print(marks["Rahul"])


# dictionary methods - a.items() - it will return key value pairs in form of tuple
marks = {
    "Rahul":100,
    "Adi":20,
    "Shubham":70
}
print(marks.items())


# dictionary methods - a.keys() - it will return key in response
marks = {
    "Rahul":100,
    "Adi":20,
    "Shubham":70
}
print(marks.keys())


# dictionary methods - a.update() - it will update the value in dictionary
marks = {
    "Rahul":100,
    "Adi":20,
    "Shubham":70
}
marks.update({"Rahul":99})
print(marks)


# dictionary methods - a.get() - it will give the value of given input
marks = {
    "Rahul":100,
    "Adi":20,
    "Shubham":70
}
print(marks.get("Rahul"))