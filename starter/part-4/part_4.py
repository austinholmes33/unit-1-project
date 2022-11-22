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

def new_book ():
    title = input("What is the book title? ")
    author = input("Who is the book's author? ")
    try:
        year = int(input("What year was the book published? "))
    except:
        year = int(input("Please type a number for the year? - "))
    rating = input("What is the book's rating? ")
    pages = input("How many pages does the book have? ")


    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary

print(new_book())


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

def main_menu():
    if:
        return
    elif:
        return
    else:


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

