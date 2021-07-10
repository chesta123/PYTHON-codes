# def fibbonaci(n):
#     """fibbonaci no. 0 1 1 2 3 5 8 13 21......"""
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibbonaci(n-1) + fibbonaci(n-2)
# num= int(input("enter the no."))
# print(fibbonaci(num))


# no_of_guesses = 0
# while(no_of_guesses <=9):
#     no_of_guesses = no_of_guesses + 1
#     guess = int(input("guess the no.:\n"))
#     if guess< 36:
#         print("enter greater no.")
#         print(" tries taken are",no_of_guesses)
#         print(10- no_of_guesses, "tries left")
#
#     elif guess>36:
#         print("enter smaller no.")
#         print(" tries taken are",no_of_guesses)
#         print(10 - no_of_guesses, "tries left")
#
#     else:
#         print("winner")
#         print(" tries taken are",no_of_guesses)
#         break
# if(no_of_guesses>9):
#     print("lost")
#

# a=int(input("enter the marks of 1st subject\n"))
# b=int(input("enter the marks of 2nd subject\n"))
# c=int(input("enter the marks of 3rd subject\n"))
# sum = a + b + c
# if(sum>120):
#     if(a>33 and b>33 and c>33):
#         print("you r passed")
#     else:
#         print("you are failed")
# else:
#     print("u r failed")


# username = input("enter your name \n")
# if(len(username)>=10):
#     print("no the username does not contain less than 10 letters")
# else:
#     print("yes the username contains less than 10 characters")



# mylist = ["chesta","harsh","sneha","rohan","sonu","mohit"]
# name = input("enter your name \n")
# if(name in mylist):
#     print("yes,your name is in the list")
# else:
#     print("no,the list does not have your name")



#
# n=4
# product = 1
# for i in range(n):
#      product = product*(i+1)
# i=i+1
# print(product)


# def factorial(number):
#     product = 1
#     for i in range(number ):
#         product = product * (i + 1)
#     return product
# print(factorial(5))


#
# def chesta(n):
#     if n==1 or n==0:
#         return 1
#     return n * chesta(n-1)
# print(chesta(5))


# def addition(n):

#     return n + addition(n-1)
# print(addition(5))



# # 1 1 2 3 5 8 13 21
# def series(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return series(n-1)+series(n-2)
# print(series(15))


# f_term=1
# s_term = 1
# sum = 1
# n=400
# for i in range(3,n+1):
#
#     sum = f_term + s_term
#     f_term = s_term
#     s_term = sum
#
# print(sum)
#                                                  OBJECT ORIENTED PROGRAMMING
# class Shops:
#     def __init__(self,number,colony,type):
#         self.no = number
#         self.location = colony
#         self.typ = type
# bakery = Shops(45,"vasundhara","retailer")
# cloth = Shops(34,"malviya nagar", "wholesaler")
# toy =Shops(46,"gopalpura","retailer")
# patanjali = Shops(345,"railway bridge","retailer")
# print(patanjali.typ)

#
# class Employee:
#     def __init__(self,aname,asalary,arole):
#         self.salary= aname
#         self.name=asalary
#         self.role = arole
#
#     @classmethod
#     def randomly(cls,whatever):
#         hello = whatever.split("-")
#         print(hello)
#         return cls(hello[0],hello[1],hello[2])
# harry = Employee.randomly("harry-457-student")
# print(harry.salary)

#
# class Dog:
#     def bark(self):
#         print("abcd")
# d= Dog()
# Dog.bark(d)



# print("choose 'a' for add book")
# class Library:
#     def __init__(self,name_of_book,your_name):
#         self.name_of_book = name_of_book
#         self.your_name = your_name
# # books = ["you can win,","harry potter,","theory of everything"]
# val = input("choose an option from 'a','d','r','l'\n")
# if val=="d":
#     file1 = open('books.txt','r')
#     # print(books[0],books[1],books[2])
#     print(file1.read())
#     # file1.close()
# elif val == "a":
#     file1 = open('books.txt','r+')
#     new_book = input("name the book you want to add \n")
#     file1.write(new_book)
#     for data in file1:
#         print(data)
# elif val == "l":
#     student_name = input('enter your name')
#     book_name = input("enter book name which you want from library")


#
# a = int(input("enter any number"))
# print(f"sum is {a + 100}")
#
# size = int(input())
# for i in range(size):
#     print("hello")

# Python practice problem 3 solution

# Take the size of the list from the user
print("Enter the numbers of the list one by one\n")
size = int(input("Enter size of list\n"))

# Initialize a blank list
mylist = []

# Take the input from the user one by one
for i in range(size):
    mylist.append(int(input("Enter list element\n")))

# mylist = [7,3,2, 34, 1,0]
print(f"Your list is {mylist}\n")

reverse1 = mylist[:]
reverse1.reverse()

reverse2 = mylist[::-1]
print(f"My First reversed list of {mylist} is {reverse1}")
print(f"My Second reversed list of {mylist} is {reverse2}")

reverse3 = mylist[:]
for i in range(len(reverse3) // 2):
    reverse3[i], reverse3[len(reverse3) - i - 1] = reverse3[len(reverse3) - i - 1], reverse3[i]
    # print(f"the reversed list at i={i} is {reverse3}")

print(f"My Third reversed list of {mylist} is {reverse3}")
if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three methods give same result\n")


