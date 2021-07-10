# imporatant gyaan about reverse of list function in video https://youtu.be/tx7VofKNnAA from 7:30 approx
# lst = ["a","b","c"]
# for rtyu in lst:
#     print(rtyu)
    # here rtyu are just random words.

# list1 = [["chesta",1],["carry",2],["larry",3]]
# dict1 = dict(list1)
# for items,lolypop in list1:
#     print(items, "eats", lolypop ,"lollypop")
mylist = ["hey",1,"three","hello",6,7,"red",3,567]
for items in mylist:
    if str(items).isnumeric() and items>6:
        print(items)

# very important thing about lists.try the below code
list1 = [1,5,2,8,3,9,4]
list_sorted = list1.sort()
print(list_sorted)
# it will give none as output..but printing the below code will work
list1 = [1,5,2,8,3,9,4]
list1.sort()
print(list1)
# this is because list.sort() function changes the original list without returning anyhtinhg.

# adding anything in lists. use of append
list1.append(34)

# to find sum of numbers in a list
l1=[34,45,76]
print(l1[0]+l1[1]+l1[2])
print(sum(l1))