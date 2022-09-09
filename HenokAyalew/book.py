# Create a class called Book that stores the information for each of the books in a library.
#The class should keep: the title of the book, author, number of copies of the book
#and number of lend copies.
#Method Loan: that increases the corresponding attribute each time a loan is made from the book.
#No books may be borrowed if no copies are available to lend.
#Returns true if the operation was successful and false otherwise.
#Method Returned: that decrements the corresponding attribute when a book is returned.
#No books can be returned that have not been lend.
#Returns true if the operation was successful and false otherwise.	
#Method Display: to display data from books. (with pretty formatting) 

#---------------------------------------------------------------------------------------------------


# Create a class called Book that stores the information for each of the books in a library.
#The class should keep: the title of the book, author, number of copies of the book
#and number of lend copies.
class Book:

    def __init__(self,title,author,number_of_copies,lend_copies):
        self.title = title
        self.author = author
        self.number_of_copies = number_of_copies
        self.lend_copies = lend_copies


    def loan_book(self):
        if(self.number_of_copies > 0):
            self.lend_copies += 1
            self.number_of_copies -= 1
            return True
        else:
            print("No more copies left")
            return False
    
    def return_book(self):
        if(self.lend_copies > 0):
            self.lend_copies -= 1
            self.number_of_copies +1
            return True
        else:
            print("none were borrowed")
            return False
    


    def display(self):
        print("======Books======")
        print("Title: ",self.title)
        print("Author: ",self.author)
        print("Number of copies:",self.number_of_copies)
        print("Lend copies: ",self.lend_copies)

    
    
                
    

b1 = Book("Harry potter","J.K Rowling",50,20)
b2 = Book("Lord of the rings","J.R.R Tolkien",40,12)
b3 = Book("Twilight saga","Stephenie mayer",20,17)

b1.display()
b2.display()
b3.display()

b1.loan_book()
b2.loan_book()
b3.loan_book()




