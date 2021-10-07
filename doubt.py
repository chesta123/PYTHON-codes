#changed
class b:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "variable testing"
class a(b):
    classvar2 = "I am in class B"
    def __init__(self):
        
a = b()
b = a()

print(b.classvar1)
