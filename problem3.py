# important gyaan about reverse of list function in video https://youtu.be/tx7VofKNnAA from 7:30 approx

size = int(input("Enter the size of list\n"))
mylist = []
for i in range(size):
    mylist.append(int(input("enter the elements of the list one by one \n")))
print(f"List you entered is {mylist}")
# mylist = [1,23,45,76]
print(f"your list is {mylist}")
reverse1 = mylist[:]
reverse1.reverse()
reverse2 = mylist[::-1]
print(f"the first reverse list is {reverse1}")
print(f"the second reverse list is {reverse2}")
reverse3 = mylist[:]
for i in range(len(reverse3) // 2):
    reverse3[i] , reverse3[len(reverse3)-i-1] =  reverse3[len(reverse3)-i-1] , reverse3[i]
print(f"the third reverse list is {reverse3}")
if reverse1 == reverse2 and reverse2 == reverse3 :
    print("all the methods give same results")
