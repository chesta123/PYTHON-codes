class Employee:
    def __init__(self,aname,asalary,arole):
        self.salary= asalary
        self.name= aname
        self.role = arole

    def __add__(self, other):
        return self.salary - other.salary
emp1 = Employee("chesta",456,"prorammer")
emp2 = Employee("gupta",345,"engineer")
print(emp1+emp2)

# 7th line and 11th line should have same command here(addition) irrespective of what the function is returning , but the output will be
# obviously acc to what the function got from return (here subtraction of both)

    def __repr__(self):
        return f"Employee('{self.name}')"
    def __str__(self):
        return f"the name of guy is {self.name}"

emp1 = Employee("chesta",456,"prorammer")


print(emp1)
print(repr(emp1))
print(str(emp1))
