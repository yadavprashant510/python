
class Library:
    def __init__(self, list, name):
        self.name = name
        self.book_list = list
        self.lendDict = {}

    def display_book(self):
        print(f"We have following book in our library:{self.name}")
        for book in self.book_list:
            print(book)

    def lend_book(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-book database has been updated.You can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self,book):
        self.book_list.append(book)
        print("Book has been added to the book list.")

    def return_book(self,book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    prashant = Library(["Python","Rich Dad and Poor Dad","How to win friends and influence people"
                     ,"C++ Basics","Harry Potter","Monk who sold his ferrari"], "Prashant")
    while True:
        print(f"Welcome to the {prashant.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Enter valid option.")
        else:
            user_choice = int(user_choice)
        if user_choice == 1:
            prashant.display_book()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name:")
            prashant.lend_book(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            prashant.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            prashant.return_book(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while user_choice2 != "c" and user_choice2 != "q":
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue
