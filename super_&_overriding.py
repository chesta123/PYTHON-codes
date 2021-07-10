class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "variable testing"
        self.special = "this is special variable"
class B(A):
        classvar1 = "I am in class B"
        def __init__(self):
            super().__init__()
            self.var1 = "I am inside class B's construction"
            self.classvar1 = "this is instance variable of class B"

a = A()
b = B()
print(b.classvar1)
print(b.var1)

# sabse pehele compliler class B me jaega ...vaha dekhega ki super constructor h isliye class A me chala jaega . vaha var1 aur classvar1 ki
# value classs A ke according ho jaegi , par ab super constructor ke baad vala code i.e. line 11 aur 12 run hogi...to var1 aur classvar1
# ki value class B ke acc print ho jaegi.

#                                              CASE 2

class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "variable testing"
        self.special = "this is special variable"
class B(A):
        classvar1 = "I am in class B"
        def __init__(self):
            self.var1 = "I am inside class B's construction"
            self.classvar1 = "this is instance variable of class B"
            super().__init__()

a = A()
b = B()
print(b.special,b.classvar1)
print(b.var1)

# this time compiler will take value of var1 and classvar1 from instance variable os class B  but when it wiil reach super constructor it
# will go to class A and the values of var1 and classvar1 will be updated acc to class A.