statement = "please try again"
a = 23
print("guess the 2 digit integral number...make sure you have only 5 rounds")
i=1
while(i<5):
    b = input()
    if int(b)<=5 :
        print("your number is very less than actual.")
        print(statement)
    elif 20<=int(b)<23:
        print("you r very close...try again a slightly bigger number.")
        print(statement)
    elif 6<=int(b)<20:
        print("plz enter a bigger number.")
        print(statement)

    elif int(b)>=60:
        print("the number is much smaller than this.")
        print(statement)

    elif 23<int(b)<60:
        print("the actual number is less than this.")
        print(statement)

    else:
        print("CONGRATS...YOU WON!!")

    i=i+1
print("oops!! number of trials are finished")
