class Library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lendDict={}

    def displaybooks(self):
        print(f"we have following books in our library : {self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("The book is added in list of already lended books")
        else:
            print(f"Sorry! currently the book is with {self.lendDict[book]}")

    def addbook(self,book):
        self.booklist.append(book)
        print("Thanks! This book is now added to the library")

    def returnbook(self,book):
        self.lendDict.remove(book)
        print("Your book is returned.Hope you enjoyed the book")

if __name__ == '__main__':
    chesta = Library(["You can Win","Harry Potter","Theory of everything","Shreemad bhagwat geeta","Learn Python"],"Smart book")

    while(True):
        print(f"Welcome to the {chesta.name} library.Enter your choice to continue")
        print("1.Display the books")
        print("2.Lend a book")
        print("3.Add a book")
        print("4.Return a book")
        user_choice = int(input())

        if user_choice == 1:
            chesta.displaybooks()

        elif user_choice == 2:
            book = print("Enter the name of the book you want to lend ")
            user = print("Enter your name")
            chesta.lendbook(user, book)

        elif user_choice == 3:
            book = print("Enter the name of the book you want to add ")
            chesta.addbook(book)


        elif user_choice == 4:
            book = print("Enter the name of the book you want to return")
            chesta.returnbook(book)

        else:
            print("Invalid input")

        print("Press 'q' to quit and 'c' to continue")
        user_choice2 = ""
        while(user_choice2!= "c" and user_choice2 != "q"):
            # print("not a valid option")
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue
