my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def return_string (dict):
    # return a string of info in the dictionary called
    return f"The title of the book is {dict['title']}, the author is {dict['author']}" 

# print(return_string(my_book))


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def book_rating(dict):
    return f"The rating was {dict['rating']}."

def year_published(dict):
    return f"The year it was published was {dict['year']}."

def book_pages(dict):
    return f"It has {dict['pages']} pages."

# print(book_rating(my_book))
# print(year_published(my_book))
# print(book_pages(my_book))



# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def organize_by_year(dict):
    if dict['year'] >= 2000:
        return f"The book {dict['title']} is new"
    else:
        return f"The book is old"

def determine_quality(dict):
    if dict['rating'] >= 4:
        return f"{dict['title']} is a good book"
    elif dict['rating'] < 3.9 and dict['rating'] >= 2.5:
        return f"{['title']} is a decent book"
    else: 
        return f"{dict['title']} is not a good book"

def organize_by_pagecount(dict):
    if dict['pages'] > 300:
        return f"{dict['title']} is a long book"
    elif dict['pages'] >= 150 and dict['pages'] <= 299:
        return f"{dict['title']} is a medium-length book"
    else:
        return f"{dict['title']} is a short book"