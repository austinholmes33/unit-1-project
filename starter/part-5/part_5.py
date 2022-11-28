### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

# selection = None
# while selection != "exit":
# 	selection = input("would you like to add a book (add), view books (view), or exit (exit)?")
# 	if selection not in ["add","view","exit"]:
# 		print("not a valid selection")
# 		continue
# 	if selection == "add":
# 		title = input("What is your first nam?")
# 		author = input("What is your last name?")
# 		year = int(input("What is your age?"))
#         rating = float(input("What is your age?"))
#         pages = int(input("What is your age?"))
# 		f = open("test.txt", "a")
# 		f.write(f"{title} {author} {year} {rating} {pages}\n")
# 		f.close()




### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here


# selection = None
# while selection != "exit":
# 	selection = input("would you like to add a book (add), view books (view), or exit (exit)?")
#     if selection == "view":
# 	    f = open("test.txt", "r")
# 	    for line in f.readlines():
# 		    title, author, year, rating, pages = line.strip().split(" ")
# 		    print(f"{title} {author} {year} {rating} {pages}")
#         f.close()
# 	elif selection == "exit":
#         break

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!


def new_book (books):

    title = input("What is the book title? - ")
    author = input("Who is the book's author? - ")
    try:
        year = int(input("What year was the book published? - "))
    except:
        year = int(input("Please type a number for the year - "))
    try:
        rating = float(input("What is the book's rating? "))
    except:
        rating = float(input("Please type a number for the rating - "))
    try:
        pages = int(input("How many pages does the book have? - "))
    except:
        pages = int(input("Please type a number for the amount of pages - "))

    with open(books, "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")
        f.close()


def book_dictionary (books):
    book_list = []
    with open(books, "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
        book_list.append({
            "title": title,
            "author": author,
            "year": int(year),
            "rating": float(rating),
            "pages": int(pages)
        })
    return book_list
    


# def all_books(book_list):

#     print("\nAll of your books...\n")

#     for books in book_list:
#         title = books["title"]
#         author = books["author"]
#         year = books["year"]
#         rating = books["rating"]
#         pages = books["pages"]

#         print(f"{books['title']} {books['author']} {books['year']} {books['rating']} {books['pages']}")


def organize_by_year(books):
    if books['year'] >= 2000:
        return f"The book {books['title']} is new"
    else:
        return f"The book is old"


def determine_quality(books):
    if books['rating'] >= 4:
        return f"{books['title']} is a good book"
    elif books['rating'] < 3.9 and books['rating'] >= 2.5:
        return f"{['title']} is a decent book"
    else: 
        return f"{books['title']} is not a good book"


def organize_by_pagecount(books):
    if books['pages'] > 300:
        return f"{books['title']} is a long book"
    elif books['pages'] >= 150 and books['pages'] <= 299:
        return f"{books['title']} is a medium-length book"
    else:
        return f"{books['title']} is a short book"


def main_menu(books):

    active = True

    while active:

        selection = input("Select (1) to add a book. Select (2) to view books. Select (3) to organize by page count. Select (4) to sort by rating. Select (5) to organize by year. Select (exit) to exit.")
        if selection not in ["1", "2", "3", "4", "5", "exit"]:
            print("not a valid selection")
            continue
        elif selection == "1":
            new_book(books)        
        elif selection == "2":
            book_dictionary(books)         
        elif selection == "3":
            organize_by_pagecount(books) 
        elif selection == "4":
            determine_quality(books)
        elif selection == "5":
            organize_by_year(books)
        elif selection == "exit":
            break

if __name__ == "__main__":
    main_menu("test.txt")






    # title = input("What is the book title?")
            # author = input("Who is the author?")
            # year = int(input("What year was it published?"))
            # rating = float(input("What is the book's rating?"))
            # pages = int(input("How many pages does the book have?"))
            # f = open("test.txt", "a")
            # f.write(f"{title} {author} {year} {rating} {pages}\n")
            # f.close()

               # all_books(books)
            # f = open("test.txt", "r")
            # for line in f.readlines():
            #     title, author, year, rating, pages = line.split(", ")
            #     print(f"{books['title']} {books['author']} {books['year']} {books['rating']} {books['pages']}")
            #     f.close()

                      # f = open("test.txt", "r")
            # for line in f.readlines():
            #     title, author, year, rating, pages = line.split(' ')

                      # f = open("test.txt", "r")
            # for line in f.readlines():
            #     title, author, year, rating, pages = line.split(' ')

              # f = open("test.txt", "r")
            # for line in f.readlines():
            #     title, author, year, rating, pages = line.split(' ')


# def view_all_books (books):
#     for book in book_dictionary(books):
#         print(all_books(book))

            # select = input("Select 1 to add a book. Select 2 to see all books. Select 3 to organize by page count. Select 4 to determine quality by rating. Select 5 to organize by year.\
        # Select exit to exit the program. - ")
        
        # if select == "1":
        #     books.append(new_book())
        # elif select == "2":
        #     all_books(books)
        # elif select == "3":
        #     organize_by_pagecount(books)
        # elif select == "4":
        #     determine_quality(books)
        # elif select == "5":
        #     organize_by_year(books)
        # elif select == "exit":
        #     print("\nExiting")
        #     active = False
        # else:
        #     print("\nPlease enter a number.\n")

    # main_menu(fav_books)

# selection = None
# while selection != "exit":

# fav_books = [
#     {
#         "title": "The Crossing",
#         "author": "Cormac McCarthy",
#         "year": 1994,
#         "rating": 4.1,
#         "pages": 425
#     },

#     {
#         "title": "Lonesome Dove",
#         "author": "Larry McMurtry",
#         "year": 1985,
#         "rating": 4.5,
#         "pages": 843
#     },

#     {
#         "title": "Suttree",
#         "author":  "Cormac McCarthy",
#         "year": 1979,
#         "rating": 4.2,
#         "pages": 471
#     },
    
#     {
#         "title": "The Shape of the Journey",
#         "author": "Jim Harrison",
#         "year": 1998,
#         "rating": 4.3,
#         "pages": 484
#     },
    
#     {
#         "title": "What About This",
#         "author": "Frank Stanford",
#         "year": 2015,
#         "rating": 4.7,
#         "pages": 764
#     }
# ]