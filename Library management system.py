Books = []
Issued_books = []


def add_book():
    book_id = input("Enter book ID -> ").lower()
    book_title = input("Enter book TItle -> ").lower()
    book_author = input("Enter book Author Name -> ").lower()
    quantity = int(input("Enter book Quantity -> "))

    if quantity>0:
        if Books:
            for i in Books:
                if not book_id in i:
                    Books.append([book_id,book_title,book_author,quantity])        
                    print("\nBook added successfully............!")
                else:
                    print("\nThis book already exist we can not add it........!")
        else:
            Books.append([book_id,book_title,book_author,quantity])        
            print("\nBook added successfully............!") 
    else:
        print("\nBook quantity must be a positive whole number....!")
    

def View_all_books():
    varify = False
    for index,i in enumerate(Books,start=1):
        print("\n")
        print("Book -> ",index)
        for j in i:
            varify=True
            print("\t-> ",j)
    if not varify:
        print("There is no any Books......!")
    
def Search_Book():
    book_id = input("\nEnter book ID/Title/ -> ").lower()
    varify = False
    for i in Books:
        if book_id in i:
            varify=True
            for value in i:
                print(f" -> {value}")

    if not varify:    
        print("\nSorry i have not this book......!")

def Issue_book():
    book_id = input("\nPlease Enter book ID -> ")
    quantity = int(input("\nPlease Enter quantity -> "))
    varify = False
    for index,i in enumerate(Books):
        if book_id in i:
            if i[3]==quantity:
                Issued_books.append(i)
                Books.remove(i)
                print(f"\nBook ({book_id}) issued successfully.......!")
                varify=True
            elif i[3]<quantity:
                print(f"\nDear i have7 only ({i[3]}) books......!")
                varify=True
            else:
                issued = []
                for ind,j in enumerate(i):
                    if ind==3:
                        issued.append(quantity)
                        break
                    issued.append(j)

                Issued_books.append(issued)

                Books[index][3]-=quantity
                print(f"\nBook ({book_id}) issued successfully.......!")
                varify=True

    if not varify:
        print(f"\nThis ({book_id}) book is not available.........!")

def Return_book():
    book_id = input("Enter book ID -> ").lower()
    quantity = int(input("Enter book quantity -> "))

    for index,i in enumerate(Issued_books):
        if book_id in i:
            if Issued_books[index][3]==quantity:
                for ind,j in enumerate(Books):
                    if book_id in j:
                        Books[ind][3]+=quantity
                        Issued_books.pop(index)
                        print(f"\nThis ({book_id}) Book returned successfully......!")
                        break
                    else:
                        Books.append(i)
                        Issued_books.pop(index)
                        print(f"\nThis ({book_id}) Book returned successfully......!")
                        break
            elif Issued_books[index][3]<quantity:
                print(f"\nDear i had only {Issued_books[index][3]} books, recheak it.......!")
            else:
                print(f"\nDear i gave you {Issued_books[index][3]} books, where is other book/books ?")
        else:
            print("\nDear i have not this book.......!")

    
def Delete_book():
    varify = False
    book_id = input("\nPlease Enter book_id to delete -> ")
    for i in Issued_books:
        if book_id in i:
            print("\nI can not delete this book because copy of this book has been issued.....!")
        else:
            for i in Books:
                if book_id in i:
                    varify=True
                    Books.remove(i)
                    print(f"\nThis ({book_id}) book has been deleted.......!")
            
    if not varify:
        print(f"\nThis ({book_id}) is not available.......!")


def View_issued_books():
    if Issued_books:
        for index,i in enumerate(Issued_books,start=1):
                print("\n")
                print("Book -> ",index)
                for j in i:
                    print("   ",j)
    else:
        print("No any issued book right now.......!")
    

def Main():
    while True:
        print("""
        <<<<<<<<<<- LIBRARY MANAGEMENT SYSTEM ->>>>>>>>>>

        1. Add Book
        2. View All Books
        3. Search Book
        4. Issue Book
        5. Return Book
        6. Delete Book
        7. View Issued Books
        8. Exit
""")
        choice = input("Please Enter your choice -> ")
        if choice=="1":
            add_book()
        elif choice=="2":
            View_all_books()
        elif choice=="3":
            Search_Book()
        elif choice=="4":
            Issue_book()
        elif choice=="5":
            Return_book()
        elif choice=="6":
            Delete_book()
        elif choice=="7":
            View_issued_books()
        elif choice=="8":
            break
        else:
            print("\nInvalid choice please enter(1-8)........!")

Main()