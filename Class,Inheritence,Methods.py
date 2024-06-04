# class Pavan:
#     def Greet(name):
#         print("Hello",name)
# a=Pavan
# a.Greet("Teja")

# print("----------------------------------------------------------------------------------------")

# class data:
#     college="SRM"

#     def __init__(self,name,Roll_No):
#         self.name=name
#         self.Reg_No=Roll_No

#     def display(self):
#         print("Student Name is: ",self.name)
#         print("Student Reg_No is: ",self.Reg_No)
#         print("Student Belongs to",data.college,"University")

# name=input("Enter the Student Name: ")
# Reg_No=int(input("Enter the Reg_No: "))
# student1=data(name,Reg_No)
# student1.display()

# name=input("Enter the Student Name: ")
# Reg_No=int(input("Enter the Reg_No: "))
# Student2=data(name,Reg_No)
# Student2.display()                                #The code is to print data from single class and multiple def's

''' defines a class data which models student information, 
including the student's name, registration number, and the college they belong to.'''
class Student:                                    #The code is to print the data from multiple classes and multiple def's
    college="SRM University"
    def __init__(self,name=None,Reg_No=None):
        self.name=name
        self.Reg_No=Reg_No
    def set_Stud(self):
        self.Studname=input("Enter The Student Name: ")
        self.StudReg_No=input("Enter the student Reg No.: ")
    def DispStud(self):
        print("Name of the Student is ",self.Studname)
        print("Student Reg No: ",self.StudReg_No)
class Department:
    def __init__(self,DeptName=None,DeptID=None):
        self.DeptName=DeptName
        self.DeptID=DeptID
        self.Dept=Student()
    def set_Dept(self):
        self.DeptName=input("Enter the Department Name: ")
        self.DeptID=input("Enter The Department ID: ")
        self.Dept.set_Stud()
    def DispDept(self):
        print("Department Name is: ",self.DeptName)
        print("Department ID is: ",self.DeptID)
        self.Dept.DispStud()
d=Department()
d.set_Dept()
d.DispDept()

# print("----------------------------------------------------------------------------------------")

# ||||Inheritence||||
# class Animal:                          # class Animal:                    BaseClass -> Derived Class==Inheritence
#     def eating(self):                  #     def eating(self):
#         print("Eating")                #         print("eating")

# class Dog:                             # class Dog(Animal):
#     def eating(self):                  #    def barking(self):
#         print("Eating")                #       print("Barking")        
#     def barking(self):                 #Output:Same Output=eating Barking
#         print("Barking")

# d = Dog()
# d.eating()
# d.barking()

# print("----------------------------------------------------------------------------------------")

# |||||MultiLevel_Inheritence||||                                          BaseClass  ->  DerivedClass  ->  DerivedClass2
# class Office:                                                            Class"Office"  Class"Branch1"    Class"Branch2"
#     Comp="AxiomIO"
#     def Head(self):
#         print("Head of AxiomIO is: A",Office.Comp)
# class Branch1(Office):
#     def Head1(self):
#         print("Head of Branch1 is: B")
# class Branch2(Branch1):
#     def Head2(self):
#         print("Head of Branch2 is: C")

# P=Branch2()
# P.Head()
# P.Head1()
# P.Head2()

# print("----------------------------------------------------------------------------------------")

# ||||MULTIPLE INHERITENCE||||
# class land_Animal:
#     def land(self):
#         print("The Animal which can live on Land")     #LandClass+WaterClass=Frog
# class Water_Animal:                                    #Frog is the result class of different claases
#     def water(self):
#         print("The Living Being that can live in Water too")
# class Frog(land_Animal,Water_Animal):
#     pass 

# P=Frog()
# P.land()
# P.water()

# print("----------------------------------------------------------------------------------------")
# |||||Method Override||||

# class A:                       #class A:
#     def B(self):                   def B(self):
#         print("Hello")    <--          Print("hello")
# class C(A):                    #class C(A):
#     def B(self):                   pass
#         print("Teja")
#          #To Override Here from There
# e=C()
# e.B()
# print("----------------------------------------------------------------------------------------")

# ||||||Polymorphism|||||
class Male:
    def dress(self):
        print("Shirt, Pant")
class Female:
    def dress(self):
        print("Saree","HalfSaree")
def clothes(dresstype):
    dresstype.dress()

m=Male()
f=Female()
clothes(m)
clothes(f)
################################################################################################3
def printit( ) : # global function
    print('Opener')
class Message :
    def display(self, msg) : # instance method
        printit( )
        print(msg)
    def show( ) : # class method
        printit( )
        print('Hello')
        # display( )  # this call will result in an error
printit( ) # call global function
m = Message( )
m.display('Good Morning') # call instance method
Message.show( )
######################################################################################################
# class Department():
#     def Dep(self):
#         self.__DepID=input("Enter the Department ID: ")
#         self.__DepNm=input("Enter the Department Name: ")
#     def Dep_Dsp(self):
#         print(self.__DepID)
#         print(self.__DepNm)
# class Employee():        
#     def emp(self):
#         self.__empID=input("Enter the Employee ID: ")
#         self.emNM=input("Enter the Employee Name: ")
#         emDep=Department()
#     def emp_Dsp(self):
#         print(self.__empID)
#         print(self.__emNM)
# e=Employee()
# e.emp()|||||||||||||||||||||||||||||||||wrong code||||||||||||||||||||||||||||||||||||||||||||||
# ------------------------------------------------------------------------------------------------------#