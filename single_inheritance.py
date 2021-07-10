class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.salary= aname
        self.name=asalary
        self.role = arole
    # we r making a constructor using this __init__

    def printdetails(self):
        return f"the name is {self.name}, salary is {self.salary}, role is {self.role}"


    @classmethod
    def ammend(cls,updatedleaves):
        cls.no_of_leaves = updatedleaves

harry = Employee("harry",455,"instructor")
chesta = Employee("Chesta",255,"student")

class Programmer(Employee):
        no_of_leaves = 5
        def __init__(self,aname,asalary,arole,language):
            self.salary = aname
            self.name = asalary
            self.role = arole
            self.language=language

        def progdetails(self):
            return f"the name of programmer is {self.name}, salary is {self.salary}, role is {self.role},languages is{self.language}"

rohan = Programmer("Rohan",467,"programmer",["python"])
sohan =Programmer("Sohan",672,"programmer",["javascript"])
# print(rohan.role)
# print(rohan.language)
# print(sohan.progdetails())
print(chesta.no_of_leaves)
# print(chesta.role)