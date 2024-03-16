print("hello")
#square if the numbers
for i in range(1, 501):
    if i ** 0.5 == int(i ** 0.5):
        print(i)

#1234
#234
#34
#4

for i in range(4):
    for j in range(i+1,6):
        print(j, end ="")
    print()

#APQR
#ABQR
#ABCR
#ABCD
# Number of rows
# n = 4

# # Outer loop for rows
# for i in range(n):
#     # Print '#' at the beginning of each row
#     print("#", end="")

#     # Inner loop for columns
#     for j in range(n):
#         # Print character based on position
#         if j == 1 and i != 0:
#             print("P", end="")
#         elif j <= i:
#             print(chr(65 + j), end="")
#         else:
#             print(chr(65 + 3), end="")
    
#     # Move to the next line after printing each row
#     print()

#print a prime number otherwise its not a prime number
#How to find a prime number in efficent way.
# num = 13
# for i in range(2, num):
#     if num % i == 0:
#         print("not a prime")
#         break
# else:
#     print("prime number")

# num= int(input("enter the number:"))
# if num % 2 == 0:
#     print("prime number")
# else:
#     print("not a prime number")
      

# Array are similar to list but in array all the
#values in same type. we need to import array
# is its a integer, string, booleon we need to mention
#import array 
from array import *
# from below list we can put -5 but need use i
# when use I need to +1 dont use -1
# vals = array('i', [5,6,7,8,9])
# vals.reverse()
# for i in range(4):
#     print(vals[i])

# arr= array('i', [])
# n = int(input("enter the length of list:"))
# i = 1
# while i in range(n):
#     x= int(input("enter the value of list:"))
#     arr.append(x)
#     i+=1
# print(arr)
# num = int(input("enter the number you need to fetch"))
# k = 0
# for i in arr:
#     if i == num:
#         print(k)
#         break
#     k+=1
# print(arr.index(val))
    

# from numpy import *

# # arr = array([1,2,3,4,5],float)
# # print(arr.dtype)
# # arr = linspace(0,15,20)
# # arr1 = arange(1,15,2)
# #arr2= logspace(1,40,5)
# #arr = zeros(5)
# # arr = ones(5)
# # print(arr)

# #vectorized opereation
# a= array([1,2,3,4])
# # b= array([6,7,8,9])
# # c = a+b
# # print(c)
# print(sum(a))
# print(cos(a))
# print(log(a))
# print(sqrt(a))
# print(max(a))
# #b= a.view()  # shallow copy
# b=a.copy()   #deep copy
# print(id(a))
# print(id(b))

# def vijay(**b):
    
#     for i,j in b.items():
#         print(i,j)
    
# vijay(name= "vijay", age =28,city="akvd", num=9989067385)


# a= 6
# b = 5
# c= 10

# def vijay():
#    # global a
#     globals()['a'],['b']
#   #  b= 4
#     c = a+b
#     print(c)
    
# vijay()   
    
# list = [12,3,4,5,6,19]

# def even_odd(list):
#     even_list= []
#     odd_list = []
#     even = 0
#     odd = 0 
#     for i in list:
#         if i %2 ==0:
#             even +=1
#             even_list.append(i)

#         else:
#             odd +=1
#             odd_list.append(i)
#     return even,odd,even_list,odd_list

# even,odd,even_list,odd_list=even_odd(list)
# print(f"odd{odd},even{even}, even_list{even_list}, odd{odd_list}")

#Fibonic series:

# def fibonic_series(n):
#     if n <= 0:
#         print("need to give the correct input")
#     else:
#         a=0
#         b=1
#         for i in range(2,n):
#             c= a+b
#             a=b
#             b=c
#             print(c)
    
# fibonic_series(n=10)    

#Factorial of number

# def fact_number(n):
#     f=1
#     for i in range(1,n+1):
#         f = f*i
#     print(f)

# fact_number(10)

#Recursion function:
# import sys

# sys.setrecursionlimit(10)
# print(sys.getrecursionlimit(), "limit")

# i = 0
# def recurssive():
#     global i 
#     i +=1
#     print("Hello", i)
#     recurssive()
    
# recurssive()

#Factorial using recurssion#

# def fact_recurssive(n):
#     if n==0:
#         return 1        
#     return n*fact_recurssive(n-1)

# result =fact_recurssive(8)
# print(result)


#Lambda, In lambda there are three concepts filter,map,reduce

# from functools import reduce
# lst= [1,2,3,4,5,6,7]

# even = list(filter(lambda x : x%2 ==0, lst))

# map = list(map(lambda x : x+2, even))

# red = reduce(lambda a,b : a+b, map)

# print(even)
# print(map)
# print(red)

#swap the number

# def swap_number(a,b):
#     if a<b:
#         a=b
#         b=a
#         print(a,"a")
#         c= a%b
#         print(c)
#     else:
#         c= a%b
#         print(c)
        
# swap_number(a=4, b=6)

#Decorators :

#divisible the number need to use inside a function in another function

# def div(a,b):
#     print(a/b)
    
# def smart_variable(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
            
#         return func(a,b)
#     return inner
   
# def div(a, b):
#     print(a/b)

# def smart_variable(func, a, b):
#     if a < b:
#         a, b = b, a

#     return func(a, b)

# div1 = smart_variable(div, 4, 5)

#Modules in python 
#it's nothing but we need to create like any project need to
#break into a diferent modules

#if __name__ == "__main__"

#Object Oriented Programming language(OPPs)
#Attributes, Behaviour
#Object, Class, Encapsulation, Abstraction, Polymorphism

# class Computer:
    
#     def __init__(self, cpu, ram):
#         self.cpu = cpu
#         self.ram = ram        
            
#     def name_v(self):
#         print("config is", self.cpu, self.ram)
        
        
    # def age(self):
    #     self.name_v()
        
    # def update(self):
    #     self.age
    #     self.name
        
# vi = Computer("dell", "i7")
# vi.name_v()

#Let us take a example CAR:

# class Car:
    
#     def __init__(self):
#         self.car = "Benz"
#         self.millage = 5
#         self.colour = "red"

# class Student:
#     school = "sarada"
    
#     def __init__(self, m1,m2,m3) -> None:
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     def avg(self):
#         c = (self.m1 + self. m2 + self.m3)/3
#         return c
    
#     @classmethod
#     def info(cls):
#         return cls.school

# vi = Student(25,24,25)
# v2 = Student(25,24,25)
# print(vi.avg())
# print(Student.info())

# Now we can discuss about the class inside the class

# class Student:
    
#     def __init__(self,name,age,rollno):
#         self.name= name
#         self.age = age
#         self.rollno = rollno
#         self.lap = self.Laptop()
        
#     def show(self):
#         print(self.name, self.rollno, self.age)
#         self.lap.show()
    
#     class Laptop:
#         def __init__(self):
#             self.brand ="Hp"
#             self.cpu = "i7"
#             self.ram = 8
            
#         def show(self):
#             print(self.brand, self.ram, self.cpu)        

# v1 = Student('vijay', 24, 22)
# v2 = Student('sam', 30, 24)   

# v1.show()

#Inheritance
#2 types one in class and single level,multilevel, multi pl

# class A:
#     def features1(self):
#         print("vijay")

#     def features2(self):
#             print("vijay")

# class B:
#     def features3(self):
#         print("vijay")
        
#     def features4(self):
#         print("vijay")
    
# class C(A,B):
#     def features5(self):
#         print("vijay")

# v1 = A()
# v1.features1()
# c1 = C()
# c1.features3()

#Constructor in Inheritance(super().__init__())
#Method resolution Order in Class c we are print intfunction but output will print A and C because
#it will periority to left first
# class A:
    
#     def __init__(self):
#          print("vijay A")
         
#     def features1(self):
#         print("vijay")

#     def features2(self):
#             print("vijay")

# class B():
#     def __init__(self):
#         super().__init__()
#         print("vijay B")
         
#     def features3(self):
#         print("vijay")
        
#     def features4(self):
#         print("vijay")
        
# class C(A,B):
#     def __init__(self):
#         super().__init__()
#         print("vijay C")
        
#     def features5(self):
#         print("vijay")
# a1 = C()

#POLY MORPHISM:
#In this method we can use 4 types
#1.Duck typing, 2.Operator Overloading, 3.Method Overloading, 4.Method Overriding

#Duck typing(Dyanamic typing)

# class Pycharm:
#     def execute(self):
#         print("compling")
#         print("running")
        
# class Vijay:
#     def execute(self):
#         print("vijay")
#         print("is a good boy")

# class Laptop:  
#     def code(self,ide):
#         ide.execute()
    
#ide = Pycharm() " ide refer a duck typing because basically we can use the class function in any type"
# ide = Vijay()
# lap= Laptop()
# lap.code(ide)

#Operator Overloading. 

# class Student:
    
#     def __init__(self,m1,m2):
#         self.m1= m1
#         self.m2= m2
        
#     def __add__(self, other):
#         s1= self.m1 + other.m1
#         s2 = self.m2 + other.m2
#         s3 = Student(s1,s2)
#         return s3
    
#     def __mul__(self, other):
#         s1= self.m1 * other.m1
#         s2= self.m2 * other.m2
#         s3 = Student(s1,s2)
#         return s3
        
#     def __sub__(self, vijay):
#         m1 = self.m1 - vijay.m1
#         m2 = self.m2 - vijay.m2
#         m3 = Student(m1,m2)
#         return m3    
    
# s1 = Student(10,20)
# s2 = Student(15,45)

# s3 = s1 - s2
# print(s3.m2)

#Method overloading: bascially in a,b,c variable when give more ots give error that is calledd the overriding,
#on that scenerio we need to use none
# class Student:
    
#     def __init__(self):
#         pass
    
#     def marks(self, a=None, b=None, c=None):
#         s= 0
#         if a!=None and b!=None and c!=None:
#             s= a+b+c
#         elif a!=None and b!=None:
#             s = a+b
#         else:
#             s= a
#         return s

# s1 = Student()
# result = s1.marks(1,2,3)
# print(result)

#Method overriding:
#Method overding in B
# class A:
    
#     def vijay(self):
#         print("vijay")
        
# class B(A):
#     def vijay(self):
#         print("vijay11")
        
# a1=B()
# a1.vijay()

# class Student:  
#     def Laptop(self):
#         print("it's running")
        
# class working:
#     def desktop(self):
#         print("working!!!")
#         s1.Laptop()
#         s3.using()
        
# class some:
#     def using(self):
#         print("someone was using the laptop!!")
        
# s1 = Student()
# s2 = working()
# s3 = some()
# s2.desktop()

#iterator :

# class incresing:
#     def __init__(self):
#         self.num = 1
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.num <= 10:
#             c = self.num
#             self.num +=1
#             return c
#         else:
#             raise StopIteration
     
# v1 = incresing()
# Generators: we need to yield function
# def squares():
#     n=0 
#     while n <= 20:
#         v= n*n
#         yield v
#         n +=1
    
# v1 = squares()
# for i in v1:
#     print(i)

#Errors: Compli time error(syntax errors), logical error(wrong output),run time error()
# try except, finally:
# x = 5
# y = 0

# try:
#     print("open the door")
#     c = x/y
#     print(c, "value")
# except Exception as e: # this will except all the errors
#     print("exeception error", e)
# except ZeroDivisionError:
#     print("error")
# except ValueError:
#     print("error")
# finally:
#     print("closed the door") 

#Threads, Multithreads: OUTPUT will simultaneously 

# from threading import *
# from time import sleep
# class Vijay(Thread):
    
#     def run(self):
#         for i in range(5):
#             print("hi")
#             sleep(1)
# class V1(Thread):   
#     def run(self):
#         for i in range(5):
#             print("vijay")
#             sleep(1)
        
# t1 = Vijay()
# t2 = V1()
# t1.start()
# sleep(0.2)
# t2.start()
# t1.join()
# t2.join()
# print("bye")

#open any file data.
#read a data
# f = open('vijay.c', 'r')#read the file
# print(f.readline())
#f = open('vijay.c', 'a') #append
#f = open('vijay.c', 'w') #write

# f = open("IMG_6309.JPG","rb")
# f = open("my pic","wb")
#for i in f:
#   f1.write(i)

# list = [1,2,3,5]
# n = 5

# def find(list,n):
#     i = 0
#     while i< len(list):
#         if list[i] == n:
#             return True
#         i+=1
#     return False
    
# if find(list,n):
#     print("found")
# else:
#     print("not found")

#Bubble sort: comparing and swaping:
# def sort(nums):
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j]>nums[j+1]:
#                 temp=nums[j]
#                 nums[j]=nums[j+1]
#                 nums[j+1]=temp
                    
# nums =[3,2,1,5,78,90]
# sort(nums)
# print(nums)
#selection sorting :
# num = [1,7,5,6,8,4]

# def sort(num):
#     for i in range(5):
#         minposition = i
#         for j in range(i,6):
#             if num[j] < num[minposition]:
#                 minposition = j
                
#         temp = num[i]
#         num[i] = num[minposition]
#         num[minposition] = temp
    
# sort(num) 
# print(sort) 

# list = [3,5,7,12,67,87,98,90]

# def sort(list):
#     #print(list)
#     for i in range(7):
#         min = i
#         for j in range(i,8):
#             if list[j] > list[min]:
#                 min = j
    
#         temp = list[i]
#         list[i] = list[min]
#         list[min] = temp
        
# sort(list)
# print(list)
