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


selection = None
while selection != "exit":
	selection = input("Would you like to add a book (add) view books (view) or exit (exit)?")
	if selection not in ["add","view","exit"]:
		print("not a valid selection")
		continue
	if selection == "add":
		title = input("What is the book title?")
		author = input("Who is the author?")
		year = int(input("What year was it published?"))
		rating = float(input("What is the book's rating?"))
		pages = int(input("How many pages does the book have?"))
		f = open(test.txt, "a")
		f.write(f"{title} {author} {year} {rating} {pages}\n")
		f.close()
	if selection == "view":
		f = open(test.txt, "r")
		for line in f.readlines():
			title, author, year, rating, pages = line.strip().split(' ')
			print(f"{title} {author} {year} {rating} {pages}")
			f.close()
	elif selection == "exit":
		break