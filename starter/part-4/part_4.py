### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

# def new_book ():
#     title = input("What is the book title? ")
#     author = input("Who is the book's author? ")
#     year = input("What year was the book published? ")
#     rating = input("What is the book's rating? ")
#     pages = input("How many pages does the book have? ")

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

# print(new_book())

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# def new_book ():
#     title = input("What is the book title? ")
#     author = input("Who is the book's author? ")
#     year = int(input("What year was the book published? "))
#     rating = float(input("What is the book's rating? "))
#     pages = int(input("How many pages does the book have? "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

# print(new_book())

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# def new_book ():
#     title = input("What is the book title? - ")
#     author = input("Who is the book's author? - ")
#     try:
#         year = int(input("What year was the book published? - "))
#     except:
#         year = int(input("Please type a number for the year - "))
#     try:
#         rating = float(input("What is the book's rating? "))
#     except:
#         rating = float(input("Please type a number for the rating - "))
#     try:
#         pages = int(input("How many pages does the book have? - "))
#     except:
#         pages = int(input("Please type a number for the amount of pages - "))


#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

# print(new_book())


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

# fav_books = [
#     {
#         "title": "The Crossing",
#         "author": "Cormac McCarthy",
#         "year": 1994
#         "rating": 4.1
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
#     }
    
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
#     },
# ]

# def main_menu(books):
#     select = input("Select 1 to add a book. Select 2 to see all books. Select 3 to exit the program. - ")

#     if select == "1":
#         books.append(create_new_book())
#     elif select == "2":
#         print_all_books(books)
#     elif select == "3":
#         print("\nExiting")
#         active = False
#     else:
#         print("\nPlease enter a number.\n")


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

fav_books = [
    {
        "title": "The Crossing",
        "author": "Cormac McCarthy",
        "year": 1994
        "rating": 4.1
        "pages": 425
    },

    {
        "title": "Lonesome Dove",
        "author": "Larry McMurtry",
        "year": 1985,
        "rating": 4.5,
        "pages": 843
    },

    {
        "title": "Suttree",
        "author":  "Cormac McCarthy",
        "year": 1979,
        "rating": 4.2,
        "pages": 471
    },
    
    {
        "title": "The Shape of the Journey",
        "author": "Jim Harrison",
        "year": 1998,
        "rating": 4.3,
        "pages": 484
    },
    
    {
        "title": "What About This",
        "author": "Frank Stanford",
        "year": 2015,
        "rating": 4.7,
        "pages": 764
    }
]


def new_book ():
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


    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary

def all_books(book_list):

    print("\nAll of your books...\n")

    for book in book_list:
        title = book["title"]
        author = book["author"]
        year = book["year"]
        rating = book["rating"]
        pages = book["pages"]

        print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")

def main_menu(books):

    active = True

    while active:
        
        select = input("Select 1 to add a book. Select 2 to see all books. Select 3 to exit the program. - ")
        
        if select == "1":
            books.append(new_book())
        elif select == "2":
            all_books(books)
        elif select == "3":
            print("\nExiting")
            active = False
        else:
            print("\nPlease enter a number.\n")

main_menu(fav_books)