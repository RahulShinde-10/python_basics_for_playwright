# Inheritance - Inheritance is a way of creating a new class from an existing class.

# Syntax
# Class Employee    -- # base class
      #code

#Class Programmer (Employee)    -- # Derived or child class

# here we can use the method and attribute of "Employee" in "Programmer" class also we can add or override new attribute and method directly in Programmer class
# Types of Inheritance - Single/ Multiple/ Multilevel Inheritance


class Employee:
    company = "ITC"
    name = "Rahul"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")


# class programmer:
#     company = "TCS"
#     name = "Rahul"
#     def show(self):
#         print(f"The name is {self.name} and language is {self.language}")

#     def showLanguage(self):
#         print(f"language is {self.showLanguage}")

    


# here above we created 2 classes with objects in it and we are printing the object inside it pretty straight forward.


# But here we are doing same thing using inheritance

class programmer(Employee):           # Inheriting base class to child class
    company = "TCS"
    language = "Python"
    def showLanguage(self):
         print(f"language is {self.language}")


a = Employee()
b = programmer()
b.show()
b.showLanguage()



#Multiple inheritance
# Multiple inheritance occurs when the child class inherits from more than one parent classes

class Employee:
    company = "ITC"
    name = "Rahul"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

class coder:
    language = "Python"
    def showLanguage(self):
        print(f"language is {self.language}")


class programmer(Employee, coder):
    company = "ITC"
    def showLanguage(self):
        print(f"language is {self.language}")

a = Employee()
c = coder()
b = programmer()
b.show()
b.showLanguage()





# Multilevel inheritance
# multilevel inheritance means when child class is became a parent class for another child class
# for eg - parent -> child1 -> child2   --- here child class for parent is child 1 but for child2 it's parent class is child1
# syntax--

class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)           #it will print attribute a because a belongs to class Employee

o = Programmer()
print(o.a, o.b)      #it will print a and b because b belongs to class Programmer and Programmer class inherited from Employee class

o = Manager()
print(o.a, o.b, o.c)   # it will print a, b and c because c belongs to class Manager and Manager class inherited from Programmer class and Programmer class inerited from Employee class




#class method
# class method is a method which is bound to class and not object of class

class Employee:           # here in this program is created a class
    a = 1                 # defined a value for a
    def show(self):       # created a method
        print(f"the value of a is {self.a}")    

value = Employee()
value.a = 45         # here i assigned value for a is 45 then it will print 45 value 
value.show()         # but i wanted to print a = 1


# in above example i wanted to print value of a which is 1 and not 45 so i will use class method here
class Employee:           
    a = 1 
    @classmethod         # here is added class method so it will pick value from class only even if i given another value to print in object           
    def show(cls):      
        print(f"the value of a is {cls.a}")    

value = Employee()
value.a = 45          
value.show() 

