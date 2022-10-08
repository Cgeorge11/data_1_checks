# A program to take input of user names, birthdays and favorite hobby and writes them to a file

file = open("users.csv", mode="w")

last_input = ""

while last_input != "Quit":

    # add a header to the file
    file.write("first_name, last_name, birth_year, favorite_hobby\n")

    print("Please input user's first name. 'Quit' to exit the program")
    last_input = input()
    first = last_input

    print("Please input users last name 'Quit' to exit the program")
    last_input = input()
    second = last_input

    print("Please input users birthday_year. 'Quit' to exit the program")
    last_input = int(input())
    third = last_input
    
    print("Please input users favorite hobby. 'Quit' to exit the program")
    last_input = input()
    fourth = last_input

    #use a format string to write an input to our file
    file.write(first + "," + second + "," + third + "," + fourth)

file.close()