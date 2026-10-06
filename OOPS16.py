#class and object
# class is like empty form and there is no data available
# object is like content filled in form
# once u created the object that means you created a template
# you need to instantiate the object in order to allocate memory



#syntax to create a class
# class Employee:               # this is class which i have defined
#     language = "Python"       # cand this is class attributes which i defined under class
#     salary = 500000




# how to create object
class Employee:             #class is defined
    language = "python"     # attributes created under class
    salary = "70000"

rahul = Employee()                       # object is created
print(rahul.language, rahul.salary)      # printing values given in attributes




# showing how to create attributes under class and under object
class Employee:                 #class is defined
    language = "python"         # attributes created under class
    salary = "70000"

rahul = Employee()             # object is created
rahul.name = "addy"            # attibutes created under object which we can still refer/ we can call it instance attributes as well
print(rahul.name, rahul.language, rahul.salary)        # printing the values




# attribute created under object will override the attribute created under class
class Employee:             #class is defined
    language = "python"     # attributes created under class
    salary = "70000"

rahul = Employee()                       # object is created
rahul.language = "Java"                  #here i created another same attribute under object (which was present in class as well)
print(rahul.language, rahul.salary)      # while printing object attribute will override class attribute



# self parameter - self refer to object of the class. it will automatically pass with function call from object
class Employee:             #class is defined
    language = "python"     # attributes created under class
    salary = "70000"

    def getInfo(self):             # here i have created a funtion but if i did not give self in that then will will throw an error
        print("Hello brother")
        print(f"The language is {self.language} and salary is {self.salary}")   # here using f string im printing language and salary. in inside {} if u give only laguage then it will take it as self.language

rahul = Employee()                       # object is created
rahul.language = "Java"                  #here i created another same attribute under object (which was present in class as well)
print(rahul.language, rahul.salary)
rahul.getInfo()                         # here getInfo is part of class but rahul = Employee so i will do rahul.getInfo() to print get info function




# Static method - sometimes we need function which should not use self parameter so we can use static method by doing like @static Method
class Employee:             
    language = "python"     
    salary = "70000"

    def getInfo(self):            
        print(f"The language is {self.language} and salary is {self.salary}")

    @staticmethod               # this is how u should define static method so it will tell that function will not use any parameter 
    def greet():
        print("Hello world") 

rahul = Employee()                       
rahul.language = "Java"                  
print(rahul.language, rahul.salary)
rahul.getInfo()
rahul.greet()



#__init__() Constructor - 
#__init__() is a special method which is first run as soon as object is created
#__init__() method is also known as constructor
# it can take self argument and can take further arguments as well

class Employee:             
    language = "python"     
    salary = "70000"

    def __init__(self):                 # here i have created __init__ method. now even if i did not call this method at the end to print it will print it. that's why it is call special function method
        print("Hey my brother")

    
rahul = Employee()                                       
print(rahul.language, rahul.salary)




# How to pass values directly in __init__ method
class Employee:             
    language = "python"     
    salary = "70000"

    def __init__(self, language, salary, name):     # here im passing values in init method directly and it will overide already defined values        
        self.language = language              # assigning values inside init function
        self.salary = salary
        self.name = name

    
rahul = Employee("java", 850000, "goblin")             # assigning values                                
print(rahul.language, rahul.salary, rahul.name)          # printing




