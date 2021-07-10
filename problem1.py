a = int(input("please enter your age or year of birth \n"))
if 2021>a>=1000:
    print("you have entered your year of birth")
    print(f"your age will be 100 years in the year {a + 100}")
elif a<100:
    print("you have entered your age")
    print(f"you will be 100 year old in {99 - a + 2021}")
elif a == 100:
    print("congrats! you completed century")
elif a > 2021:
    print("you are not yet born")
else:
    print("invalid input!try again")
response = input("do you want to know your age in any particular year . please give your ans in 'yes' or 'no'\n")
if response == "yes" :
    year = input("enter the year \n ")
    diff = int(year)- 2021
    print(f"your age will be {diff + a}")
    ans = input('do you want to continue')
    while ans == "ya":
        year = input("enter the year \n ")
        diff = int(year)- 2021
        print(f"your age will be {diff + a}")
        continue

elif response == "no":
    print("Okay! Thanks for using my program")
else:
    print("invalid input")



