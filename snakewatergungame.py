# this code has some error now
import random
randnum=random.randint(1,2)
if randnum == 1:
    comp == 's'
elif randnum == 2:
    comp == 'w'
else :
    comp == "g"
def gamewon(comp,a):
    if a==comp:
        return false
    else:
        if comp=='s':
            if a=='w':
                return false
            elif a=='g':
                return true
        elif comp == 'w':
            if a=='g':
                return false
            elif a == 's':
                return true
        elif comp == 'g':
            if a=='s':
                return false
            elif a == 'w':
                return true
import random
randnum=random.randint(1,2)
if randnum == 1:
    comp == 's'
elif randnum == 2:
    comp == 'w'
else :
    comp == "g"
 a = input("choose anyone from snake(s),water(w),gun(g) \n")
 n=gamewon(comp,a)
 if n==none:
     print("the game is tie")
 elif n:
     print("you win")
 else:
     print("you loose")