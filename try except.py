print("enter num1")
num1 =  input()
print("enter num2")
num2=input()
try:
    print ("sum of these two is", int(num1) + int(num2))
except Exception as error:
    print(error)

print("useful line..must be printed")