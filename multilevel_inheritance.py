class Grandfather:
    basketball = 1

class Father(Grandfather):
    dance =1
    basketball = 4
    def candance(self):
        return f"Yes i can dance{self.dance} times"

class Son(Father):
    dance = 6
    def candance(self):
        return  f"yes i can dance very beautifullly {self.dance} times"

carry =Grandfather()
larry = Father()
darry = Son()
print(darry.basketball)