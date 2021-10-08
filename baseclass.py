#classes
class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employeee is {self.fname} {self.lname}"
    def email(self):
        pass
chesta_gupta = Employee("chesta" ,"gupta")
harry_ji  = Employee("harry","ji")
print(chesta_gupta.explain())
