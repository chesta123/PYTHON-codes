n = input("enter the number of apples chesta have\n")
mn =input("enter the minimum no of people in which apples are supposed to be distributed\n")
mx =input("enter the maximum possible no of people in which apples are to be distributed\n")
if mn>mx:
    print("minimum number can't be greater than maximum")
for i in range(int(mn),int(mx)+1):
    if int(n)%i == 0 :
        print(f"{i} is divisor of {int(n)}")
    else :
        print(f"{i} is not a divisor of {int(n)}")
    i +=1


