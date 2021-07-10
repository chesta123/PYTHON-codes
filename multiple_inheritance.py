class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.salary= aname
        self.name=asalary
        self.role = arole


    def printdetails(self):
        return f"the name is {self.name}, salary is {self.salary}, role is {self.role}"

class Player:
    no_of_games = 5
    def __init__(self,name,game):
        self.name = name
        self.game = game
    def gamedetails(self):
        return f"the name of player is {self.name},the game is {self.game}"

class Coolprog(Employee,Player):
    languages="cpp"

harry = Employee("harry",455,"instructor")
chesta = Employee("Chesta",255,"student")
harsh = Player("harsh",["chess"])
karan = Coolprog("karan",67890,"cool programmer")
det = karan.printdetails()
print(det)
print(Coolprog.languages)