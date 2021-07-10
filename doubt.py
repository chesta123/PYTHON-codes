class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "variable testing"
class B(A):
    classvar2 = "I am in class B"
    def __init__(self):
        self.classvar2 = "this is instance variable of clas B"

a = A()
b = B()

print(b.classvar1)