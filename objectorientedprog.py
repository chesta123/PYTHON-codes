class Student:
    @staticmethod
    def printgood(string):
        print("this is a good " + string)
        return "taste it!"
karan= Student()
print(karan.printgood("vegetable"))

                       # DIFF BETWEEN USING SELF AND NOT USING IT...PREFERABLE IS STATICMETHOD
class Student:
    def printfood(self,string):
        print("this is good "+string)
        return "try it!"
karan = Student()
print(karan.printfood("sanskar"))
