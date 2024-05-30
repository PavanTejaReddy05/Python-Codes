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
# Student2.display()

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
