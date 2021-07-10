print("provide the value of number of rows")
n=int(input())
print("press 1 if you want the pattern to be in increasing order and 0 if you want pattern to be in reverse order")
a = int(input())
if a==1 :
    i = 0
    while i<n+1 :
        print("*"*i)
        i = i+1
else :
    i = n
    while i>0:
        print("*"*i)
        i = i - 1
