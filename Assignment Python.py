# Function that allow user to read and view the room data only

def view_room_detail():
    print("Welcome to Hotel Reservation System. Here are all the room details in the hotel: \n")
    with open("room.txt", "r") as file:
        room_detail = file.readlines()

    # after change the data in txt file into list, read the data in the list according to index number

    for i in range(0, len(room_detail), 7):
        room_type = room_detail[i].strip()
        room_bed_size = room_detail[i+1].strip()
        room_size = room_detail[i+2].strip()
        room_occupants = room_detail[i+3].strip()
        room_price = room_detail[i+4].strip()
        room_availability = room_detail[i+5].strip()

        # Print the from the above parts

        print("Type of the room: ", room_type)
        print("Size of the beds: ", room_bed_size)
        print("Size of the room: ", room_size)
        print("Occupants of room: ", room_occupants)
        print("The price of the room: RM", room_price , "per night")
        print("The availability of the room: ", room_availability)
        print()



# A function that allow admin to add details of rooms

def add_room_detail():
    print("Welcome Admin! Here is the page for you to add new room details. "
          "Please enter the information of the room.\n")

    # Ask user to enter the new data for room

    room_type = input("Enter the room type: ").upper()
    room_bed_size = input("Enter the size of the beds: ").upper()
    room_size = input("Enter the room size: ").upper()
    room_occupants = input("Enter the room occupants: ").upper()

    # Need to ensure that the input for room price is number only, if the input is not number
    # then the "show bills" part will be very hard

    while True:
        room_price = input("Enter the price of the room: ")
        if room_price.isdigit():
            room_price = int(room_price)
            break
        else:
            print("Please enter digit number only. ")

    room_availability = input("Enter the availability of room: ")

    # write all the data into room.txt

    file = open("room.txt", "a")
    file.write(f"{room_type}\n{room_bed_size}\n{room_size}\n{room_occupants}\n{room_price}\n{room_availability}\n\n")

    print("Data added successfully! ")



# def a function that allow user to edit the specific line in room.txt file

def edit_specific_line_in_room(line_number, content):
    with open("room.txt", "r") as file:
        lines = file.readlines()

    # Put the new data into the list, according to index number (line_number is index number)

    if line_number >= 0 and line_number < len(lines):
        lines[line_number] = content + "\n"

    # Write the new data into the room.txt file.

    with open("room.txt", 'w') as file:
        file.writelines(lines)



# def a function that will search for the row number of data entered

def find_row_number_in_room(data):
    with open("room.txt", "r") as file:
        for number, line in enumerate(file, start=1):
            if data in line: #if the data is in the line, then the system will return the row number in txt file
                return number



# def a function that will print all the room names only

def show_all_room_name():
    with open("room.txt", "r") as file:
        lines = file.readlines()
        for i in range (0, len(lines), 7): # only print the specific row numbers which contain the room name
            print(lines[i].strip())



# def a function that allow user to update and modify the rooom details

def update_room_detail():
    print("Welcome Admin! Here is the page for you to update and modify the room details.\n")
    print("Please enter the room name you would like to update and modify.\n\n"
          "All the room names are here: \n")

    # Show all the room name as a reference for users

    show_all_room_name()

    # Make sure the room name that is entered by the users is in the room.txt file, avoid error

    while True:
        with open("room.txt", "r") as file:
            content = file.read()
            room_name = input("\nPlease enter the room name you would like to modify: ").upper()
            if room_name in content:
                break
            else:
                print("Room not found.")

    # After user key in the room name that they would like to edit, use the function defined above to check
    # the row number of the room name, so that the data of the room can be edited based on the row number

    room_position = find_row_number_in_room(room_name)

    print("\nChoose the part you would like to change: "
          "\n1. Room bed size"
          "\n2. Room size"
          "\n3. Room occupants"
          "\n4. Room price"
          "\n5. Room availability")

    # Ask user to choose the part that they would like to change, and make sure that the input is valid

    while True:
        decision = input("Please select: ")
        if decision.isdigit():
            decision = int(decision)
            if decision in range (1,6):
                break
            else:
                print("Please enter a valid value. ")
        else:
            print("Please enter digit number only")

    # use the function defined "edit_specific_line_in_room" edit the information in the row
    # New content is a variable, to ask user to key in the new information
    # edit_specific_line_in_room(), the content in the () is the row number of the data that need to be edited,
    # use mathematical method to find the row numbers of the specific data


    if decision == 1:
        new_content = input("Please enter the bed size in the room: ").upper()
        edit_specific_line_in_room(room_position, new_content)

    elif decision == 2:
        new_content = input("Please enter the room size: ").upper()
        edit_specific_line_in_room(room_position + 1, new_content)

    elif decision == 3:
        new_content = input("Please enter the room occupants: ").upper()
        edit_specific_line_in_room(room_position + 2, new_content)

    # Need to make sure that the price entered is digit number only

    elif decision == 4:
        while True:
            new_content = input("Please enter the price of the room: ")
            if new_content.isdigit():
                edit_specific_line_in_room(room_position + 3, new_content)
                break
            else:
                print("Only digit number is allowed. ")

    elif decision == 5:
        new_content = input("Please enter the room availability: ")
        edit_specific_line_in_room(room_position + 4, new_content)

    print("Data changed. ")


# def a function that will stop user from not entering any value

def limit_data_not_null(data_name):
    while True:
        data = input(f"Please enter your {data_name}: ")
        if data.strip() == "":
            print("Please enter a valid value, the value cannot be null.")
        else:
            break
    return data



#def a function that allow new members to do registration

def registration():
    print("Welcome to registration page. Please enter your information to join as our members !")

    # ask the users to key in their basic information, need to make sure that the information key in is not null (empty)

    name = limit_data_not_null("name").upper()
    address = limit_data_not_null("address")
    email = limit_data_not_null("Email_ID")

    # limit the data type of the contact number, only digit number is allowed

    while True:
        contact_number = limit_data_not_null("contact number")
        if contact_number.isdigit():
            break
        else:
            print("Only digit number is allowed. Please re-enter your contact number.")

    # limit the input for gender, only "m" and "f" are allowed, where m represent male and f represent female

    while True:
        gender = limit_data_not_null("gender").lower()

        if gender == "m" or gender == "f":
            break
        else:
            print("Please re-enter your gender. Only male(m) or female(f) is allowed.")

    date_birth = limit_data_not_null("date of birth")

    # limit the data type of age, only digit number is allowed

    while True:
        age = limit_data_not_null("age")
        if age.isdigit():
            break
        else:
            print("Only digit number is allowed. Please re-enter your age. ")

    # ask user to enter their username
    # if username is taken, then the user have to choose a different username
    # ".username" is added automatically, to allow the system to identify which one is username

    with open("account.txt", "r") as files:
        files = files.readlines()
        while True:
            user = limit_data_not_null("User ID")
            if user not in [line.strip() for line in files]:
                user = user + ".username"
                break
            else:
                print("The username have been taken, please try another username. ")

    # ask user to enter the password
    # ".password" is added automatically to allow the system identify the password

    password = limit_data_not_null("password")
    password = password + ".password"

    # ask user to reenter the password again, if the password is not match, then the system will ask the user to reenter

    while True:
        repassword = input("Please enter your password again: ")
        repassword = repassword + ".password"
        if password != repassword:
            print("Your password does not match, please rewrite your password again!")
        else:
            break

    # the role of the customers is automatically assigned, this is very important because it is the key to let the system
    # identify who is admin and who is customers

    role = "customer"

    # write all the data into account.txt file

    file = open("account.txt", "a")
    file.write(f"{name}\n{address}\n{email}\n{contact_number}\n{gender}\n{date_birth}\n{age}\n{user}\n{password}\n{role}\n\n")

    print("Account created! Now you can login to this system! ")



# def a function that can determine the row number of data entered in account.txt file

def find_row_number_in_account(data):
    with open("account.txt", "r") as file:
        for number, line in enumerate(file, start=1):
            if data in line:
                return number



# def a function that allow user to edit the specific line of data in account.txt

def edit_specific_line_in_account(line_number, content):
    with open("account.txt", "r") as file:
        lines = file.readlines()

    if line_number >= 0 and line_number < len(lines): # edit the list based on the index number given
        lines[line_number] = content + "\n"

    with open("account.txt", 'w') as file: # write the new list into the account.txt file
        file.writelines(lines)



# def a function that will print all the name of user only

def show_all_name():
    with open("account.txt", "r") as file:
        lines = file.readlines()
        for i in range (0, len(lines), 11): # this function will print the specific row numbers that contain the user name only
            print(lines[i].strip())



# def a function that allow admin to make changes for all the data in account.txt file

def login_access_system():
    print("Welcome admin. Here is the interface for you to update the access and data for all the users.")
    print("Here are all the names of users:\n")

    # show all name of user, to facilitate the admin when they wanna search for a specific user name

    show_all_name()

    with open("account.txt", "r") as file:
        line = file.read()

    # ask the user to enter the user name that they would like to edit, if the user name is not in the account.txt file
    # it will repeat the loop, until the user enter the name that in the txt file

    while True:
        choose = input("\nPlease enter the user name you would like to edit: ").upper()
        if choose in line:
            break
        else:
            print("Please enter a valid name.")

    # identify the row number of the user name entered, so that the data for that users can be edited
    # the data is edited based on row number

    row_number = find_row_number_in_account(choose)

    print("Please select the data you would like to change:\n"
          "1. User Name\n"
          "2. User Address\n"
          "3. User Email\n"
          "4. User Contact Number\n"
          "5. User Gender\n"
          "6. User Date of Birth\n"
          "7. User Age\n"
          "8. User Password\n"
          "9. User Role\n")

    # ask user to choose the data that they would like to edit
    # if the data is not a digit number, or the data is out of the range, then the system will request the users to reenter

    while True:
        choose2 = input("Please select: ")
        if choose2.isdigit():
            choose2 = int(choose2)
            if choose2 in range (1, 11):
                break
            else:
                print("Please enter a valid value. ")
        else:
            print("Please enter a valid value")

    # edit the data based on row number, the row number is identified based on mathematical method

    if choose2 == 1:
        name = limit_data_not_null("name").upper()
        edit_specific_line_in_account(row_number + choose2 - 2, name)
        print("Data changed successfully!")

    elif choose2 == 2:
        address = limit_data_not_null("address")
        edit_specific_line_in_account(row_number + choose2 - 2, address)
        print("Data changed successfully!")

    elif choose2 == 3:
        email = limit_data_not_null("Email_ID")
        edit_specific_line_in_account(row_number + choose2 - 2, email)
        print("Data changed successfully!")

    # only digit number is allowed for contact number

    elif choose2 == 4:
        while True:
            contact_number = limit_data_not_null("contact number")
            if contact_number.isdigit():
                edit_specific_line_in_account(row_number + choose2 - 2, contact_number)
                print("Data changed successfully!")
                break
            else:
                print("Only digit number is allowed. Please re-enter your contact number.")

    # only m and f are allowed for gender

    elif choose2 == 5:
        while True:
            gender = limit_data_not_null("gender").lower()
            if gender == "m" or gender == "f":
                edit_specific_line_in_account(row_number + choose2 - 2, gender)
                print("Data changed successfully!")
                break
            else:
                print("Please re-enter your gender. Only male(m) or female(f) is allowed.")

    elif choose2 == 6:
        date_birth = limit_data_not_null("date of birth")
        edit_specific_line_in_account(row_number + choose2 - 2, date_birth)
        print("Data changed successfully!")

    # only digit number is allowed for age

    elif choose2 == 7:
        while True:
            age = limit_data_not_null("age")
            if age.isdigit():
                edit_specific_line_in_account(row_number + choose2 - 9, age)
                print("Data changed successfully!")
                break
            else:
                print("Only digit number is allowed. Please re-enter your age.")

    # ".password" will be added automatically, to allow system identify the password

    elif choose2 == 8:
        password = limit_data_not_null("password")
        password = password + ".password"
        edit_specific_line_in_account(row_number + choose2 + 1 - 2, password)
        print("Data changed successfully!")

    # let admin to adjust the permissions for the user, based on "admin" and "customer"
    # admin will have more permissions compared to customer

    elif choose2 == 9:
        while True:
            content2 = input("Please enter the new role of the user (admin/customer): ").lower()
            if content2 == "admin" or content2 == "customer":
                edit_specific_line_in_account(row_number + choose2 + 1 - 2, content2)
                print("Role changed successfully!")
                break
            else:
                print("Please enter either 'admin' or 'customer'.")



# def a function that allow user to make changes of the information of its account only

def update_personal_info(username):

    # the system are able to identify the row number based on username, the username is given automatically

    num1 = find_rows_with_username_in_account(username)
    num = num1[0] # num1 is in list form, while num is in integer form

    print("Welcome user! Here is the interface for you to edit your account information!")
    print("Here is your account information: "
          "\n1. User Name"
          "\n2. User Address"
          "\n3. User Email"
          "\n4. User Contact Number"
          "\n5. User Gender"
          "\n6. User Date of Birth"
          "\n7. User Age"
          "\n8. User Password")

    # limit the decision type, only digit number, and 1 - 8 is allowed

    while True:
        select = input("Please select the information you want to change: ")
        if select.isdigit():
            select2 = int(select)
            if select2 in range (1,9):
                break
            else:
                print("Please enter a valid value")
        else:
            print("Please enter a valid value")

    # replace the data in account.txt by new content, based on row number, the row number is identified based on mathematical formula

    if select == "1":
        name = limit_data_not_null("name").upper()
        edit_specific_line_in_account(num + select2 - 9, name)
        print("Data changed successfully!")

    elif select == "2":
        address = limit_data_not_null("address")
        edit_specific_line_in_account(num + select2 - 9, address)
        print("Data changed successfully!")

    elif select == "3":
        email = limit_data_not_null("Email_ID")
        edit_specific_line_in_account(num + select2 - 9, email)
        print("Data changed successfully!")

    # only digit number is allowed for contact number

    elif select == "4":
        while True:
            contact_number = limit_data_not_null("contact number")
            if contact_number.isdigit():
                edit_specific_line_in_account(num + select2 - 9, contact_number)
                print("Data changed successfully!")
                break
            else:
                print("Only digit number is allowed. Please re-enter your contact number.")

    # only m and f is allowed for gender

    elif select == "5":
        while True:
            gender = limit_data_not_null("gender").lower()
            if gender == "m" or gender == "f":
                edit_specific_line_in_account(num + select2 - 9, gender)
                print("Data changed successfully!")
                break
            else:
                print("Please re-enter your gender. Only male(m) or female(f) is allowed.")

    elif select == "6":
        date_birth = limit_data_not_null("date of birth")
        edit_specific_line_in_account(num + select2 - 9, date_birth)
        print("Data changed successfully!")

    # only digit number is allowed for age

    elif select == "7":
        while True:
            age = limit_data_not_null("age")
            if age.isdigit():
                edit_specific_line_in_account(num + select2 - 9, age)
                print("Data changed successfully!")
                break
            else:
                print("Only digit number is allowed. Please re-enter your age.")

    # ".password" is added automatically to allow the system identify that it is a password

    elif select == "8":
        password = limit_data_not_null("password")
        password = password + ".password"

        while True:
            repassword = input("Please enter your password again: ")
            repassword = repassword + ".password"
            if password != repassword:
                print("Your password does not match. Please re-enter your password.")
            else:
                edit_specific_line_in_account(num + 9 - 9, password)
                print("Data changed successfully!")
                break



# def a function that can return a specific line of data in account.txt

def return_specific_line_in_account(number):
    with open("account.txt", "r") as file:
        for line, lines in enumerate(file, start=1):
            if line == number:
                return lines.strip() # return the value for that specific row



# def a function that can print the user account information

def print_user_account_info(username):
    print("Welcome User, here is your account information: \n")

    # open account.txt file and determine the row number of the username, the username is given automatically

    with open("account.txt", "r") as file:
        count = find_row_number_in_account(username)
        count = int(count) # turn the row number of the username into integer

    # read all the data for that user, and the data read is based on row number

    with open('account.txt', 'r') as file:
        lines = file.readlines()
        start_line = count - 7
        user = return_specific_line_in_account(start_line)
        address = return_specific_line_in_account(start_line + 1)
        email = return_specific_line_in_account(start_line + 2)
        contact = return_specific_line_in_account(start_line + 3)
        gender = return_specific_line_in_account(start_line + 4)
        birth = return_specific_line_in_account(start_line + 5)
        age = return_specific_line_in_account(start_line + 6)
        acc_name = return_specific_line_in_account(start_line + 7).removesuffix(".username")
        password = return_specific_line_in_account(start_line + 8).removesuffix(".password")

        # print all the data read

        print("User Name: ", user)
        print("User Address: ", address)
        print("User Email: ", email)
        print("User Contact Number: ", contact)
        print("User Gender: ", gender)
        print("User Date of Birth: ", birth)
        print("User Age: ", age)
        print("User Account Name: ", acc_name)
        print("User Password: ", password)



# def a function that are able to clear the data in specific role in account.txt

def clear_row_data_in_account(row_number):
    with open("account.txt", "r") as file:
        lines = file.readlines()

    if 1 <= row_number <= len(lines):
        lines[row_number - 1] = "\n" # write a empty data into the list, based on the index number given

        with open("account.txt", "w") as file:
            file.writelines(lines)



# def a function that allow normal users to delete their specific information

def delete_specific_information_of_account(username):

    # identify the row number of the username in account.txt file, the username is given automatically

    row_for_account = find_row_number_in_account(username)

    print("Welcome user. Here is the interface for you to delete the specific information of your account"
          "\n\nHere are all the choices:"
          "\n1. User Name"
          "\n2. User Address"
          "\n3. User Gmail"
          "\n4. User Contact Number"
          "\n5. User Gender"
          "\n6. User Date of Birth"
          "\n7. User Age")

    # ask the user to choose the data that they would like to delete, username and password are not allowed to delete
    # limit the data, only integer and 1 - 7 is allowed

    while True:
        decision_for_delete_specific_info = input("Please select the information you would like to delete: ")
        if decision_for_delete_specific_info.isdigit():
            decision_for_delete_specific_info = int(decision_for_delete_specific_info)
            if decision_for_delete_specific_info in range (1,8):
                break
            else:
                print("You entered an invalid value. Please enter the value in between 1 to 7.")
        else:
            print("You need to enter digit number only. ")

    # identify the row number of the data that need to be deleted

    row_value = row_for_account + decision_for_delete_specific_info - 8

    # delete the data for the specific row

    clear_row_data_in_account(row_value)

    print("Data delected")



# def a complete interface for users to manage their account

def personal_information_interface(username):
    print("Welcome User. Here is the page for you to manage your account. Please select one: "
          "\n\n1. View Personal Information"
          "\n2. Update/Modify Personal Information"
          "\n3. Delete Personal Information")

    # ask user to choose one of the following
    # only digit number and 1 - 3 is allowed

    while True:
        decision_personal_info = input("Please select: ")
        if decision_personal_info.isdigit():
            decision_personal_info = int(decision_personal_info)
            if decision_personal_info in range (1,4):
                if decision_personal_info == 1:
                    print_user_account_info(username)
                    break
                elif decision_personal_info == 2:
                    update_personal_info(username)
                    break
                elif decision_personal_info == 3:
                    delete_specific_information_of_account(username)
                    break
            else:
                print("Please enter a valid value")
        else:
            print("You entered an invalid value. Please enter only digit number.")



# def a function that can return the value of specific line in room.txt

def return_specific_line_in_room(number):
    with open("room.txt", "r") as file:
        for line, lines in enumerate(file, start=1):
            if line == number:
                return lines.strip() # return the value in the row number given



# A function that are able to count the number of rows in room.txt

def count_all_lines_in_room():
    count = 0
    with open("room.txt","r") as file:
        for i in file:
            count +=1
    return count



# A function that can print the data in a specific line in room.txt file

def print_specific_line_in_room(number):
    with open("room.txt", "r") as file:
        for line, lines in enumerate(file, start=1):
            if line == number:
                print(lines)



# def a function that allow user to book the rooms in hotel, it will add the data into a txt file

def booking_interface(username):
    print("Welcome user. Here is the interface for you to make bookings for our rooms. "
          "\n\nHere are all the rooms available:")

    # show all the room name, with numbers

    total_lines = count_all_lines_in_room()
    count = 0
    x = 0

    while x < total_lines:
        room = return_specific_line_in_room(1 + count * 7)
        count += 1
        x += 7
        print(count, ". ", room)

    # ask user to choose one of the room, only digit number and number in range is allowed

    while True:
        decision = input("\nPlease select the room you would like to book: ")
        if decision.isdigit():
            if int(decision) in range (1, count + 1):
                break
            else:
                print("Please choose a valid number. ")
        else:
            print("Please enter digit number only. ")

    # change the data type of decision into integer

    decision = int(decision)

    # the room booked will be automatically added into txt file, based on the "decision"

    room_book = return_specific_line_in_room(1 + (decision - 1) * 7)

    # ask user to enter the basic information

    name = input('Please enter the name of the person who will stay in the room: ')
    date = input("Please enter the date you would like to stay: ")

    # limit the data type of time, only digit number is allowed

    while True:
        time = input("Please enter how many nights you would stay in the hotel (X nights): ")
        if time.isdigit():
            break
        else:
            print("Please enter only digit. ")

    # ask user if they have any additional request

    comment = input("Please enter additional request: ")

    # write all the data into the file called booking.txt

    with open("booking.txt", "a") as file:
        file.write(f"{room_book}\n{name}\n{date}\n{time}\n{username}\n{comment}\n")

    print("Room Booked! ")



# def a function that allow admin to view and read all the room bookings only

def view_all_bookings():
    print("Welcome! Here are all the bookings informations.")

    # open the file booking.txt and change all the data in the txt file into a list
    with open("booking.txt", 'r') as file:
        booking_details = file.readlines()

    # read all the data from the list based on index number

    for i in range(0, len(booking_details), 6):
        room_book = booking_details[i].strip()
        name = booking_details[i+1].strip()
        book_date = booking_details[ i + 2 ].strip()
        day = booking_details[ i + 3 ].strip()
        id = booking_details[i+4].strip()
        comment = booking_details[i+5].strip()

        # print the data read

        print("Room booked: ", room_book)
        print("Name of the person who booked the room: ", name)
        print("The date booked: ", book_date)
        print("The nights stay in the rooms: ", day)
        print("User ID who booked the rooms: ", id)
        print("Additional Request: ", comment)
        print()



# def a function that can show the specific row numbers in booking, depends on username

def find_rows_with_username_and_words(words_to_check):
    matching_rows = []
    with open("booking.txt", 'r') as file:
        for row_number, row in enumerate(file, 1):
            row_lower = row.lower()
            if '.username' in row_lower and all(word.lower() in row_lower for word in words_to_check): # only the row that contain ".username"
                matching_rows.append(row_number)

    return matching_rows



# def a function that can return specific line in booking.txt

def return_specific_line_in_booking(number):
    with open("booking.txt", "r") as file:
        for line, lines in enumerate(file, start=1):
            if line == number:
                return lines.strip()


# def a function that allow admin to search for specific booking

def search_bookings():
    print("Welcome Admin! Here is an interface for you to search for the specific booking details of customer. ")

    # ask the user to enter the username that they would lke to search
    # ".username" is added automatically to allow the system identify the row number in booking.txt file

    username = input("\n\nPlease enter the username of the user: ")
    username_check = username.strip() + ".username"

    # find the row number based on the username

    list = find_rows_with_username_and_words(username)

    # print the data in the list
    # if the username is not in the list, then print "no booking found for username {username}

    if list:
        print(f"Bookings found for username '{username}':")
        for row_number in list:
            room = return_specific_line_in_booking(row_number - 4)
            person = return_specific_line_in_booking(row_number - 3)
            date = return_specific_line_in_booking(row_number - 2)
            day = return_specific_line_in_booking(row_number - 1)
            username = return_specific_line_in_booking(row_number).removesuffix(".username")
            comment = return_specific_line_in_booking(row_number + 1)

            print("Room booked: ", room)
            print("Name of the person who booked the room: ", person)
            print("The date booked: ", date)
            print("The nights stay in the rooms: ", day)
            print("User ID who booked the rooms: ", username)
            print("Additional comment of user: ", comment)
            print()

    else:
        print(f"No bookings found for username '{username}'.")



# def a function that allow user to view his/her own booking

def view_own_booking(username):
    print("Welcome! Here is an interface for you to view for your own bookings. . ")

    # find the row number of the username given

    list = find_rows_with_username_and_words(username)

    # print the specific data in the list
    # if the username is not in the list, then print "no booking found for username {username}

    if list:
        print(f"Bookings found for username '{username}':")
        for row_number in list:
            room = return_specific_line_in_booking(row_number - 4)
            person = return_specific_line_in_booking(row_number - 3)
            date = return_specific_line_in_booking(row_number - 2)
            day = return_specific_line_in_booking(row_number - 1)
            username = return_specific_line_in_booking(row_number).removesuffix(".username")
            comment = return_specific_line_in_booking(row_number +1)

            print("Room booked: ", room)
            print("Name of the person who booked the room: ", person)
            print("The date booked: ", date)
            print("The nights stay in the rooms: ", day)
            print("User ID who booked the rooms: ", username)
            print("Additional request of user: ", comment)
            print()

    else:
        print(f"No bookings found for username '{username}'.")



# def a function that allow user to delete specific line in booking.txt

def delete_rows_in_booking(row_number):
    with open("booking.txt", 'r') as file:
        lines = file.readlines()

    if row_number <= 0 or row_number > len(lines):
        print(f"Invalid row number: {row_number}")
        return

    updated_lines = [line for i, line in enumerate(lines, 1) if i != row_number]

    with open('booking.txt', 'w') as file:
        file.writelines(updated_lines)



# def a function that can get the value from a list, based on the index number given

def get_value_by_index(lst, index):
    if index >= 0 and index < len(lst):
        return lst[index]
    else:
        return None



# def a function that allow user to delete

def delete_booking(username):
    print("Here is the interface for you to delete your booking."
          "\n\nPlease select the booking you would like to delete: ")

    row_number = find_rows_with_username_and_words(username)

    # if user made any of the bookings

    if row_number:
        list_row = row_number
        row_number = [int(num) for num in row_number]
        count = 0

        # print all the bookings made by the user

        for row in row_number:
            count = count + 1

            room_name = return_specific_line_in_booking(row - 4)
            print(count, ". ", room_name)

        # ask the user which bookings he would likee to delete

        while True:
            decision = input("Please enter: ")
            if decision.isdigit():
                decision = int(decision)
                while True:
                    if decision in range(1, count + 1):
                        break
                    else:
                        print("Please enter a valid number.")
                        decision = int(input("Please enter: "))
                break
            else:
                print("Please enter digit number only.")


        value = get_value_by_index(list_row, decision - 1)


        # delete the specific rows

        delete_rows_in_booking(value + 1)
        delete_rows_in_booking(value)
        delete_rows_in_booking(value - 1)
        delete_rows_in_booking(value - 2)
        delete_rows_in_booking(value - 3)
        delete_rows_in_booking(value - 4)

        print("Booking cancel.")

    # if user did not make any of the bookings

    else:
        print("You did not make any of the bookings")



#A function that replace the content in booking.txt

def replace_value_in_booking(row_number, new_contents):
    with open("booking.txt", 'r') as file:
        lines = file.readlines()

    lines[row_number - 1] = new_contents + "\n"

    with open("booking.txt", 'w') as file:
        file.writelines(lines)



#A function that allow user to update booking information

def update_booking(username):
    print("Here is the interface for you to update your booking information."
          "\n\nPlease select the booking you would like to update: ")

    row_number = find_rows_with_username_and_words(username)

    # if user make any of the bookings

    if row_number:
        list_row = row_number
        row_number = [int(num) for num in row_number]
        count = 0

        # print all the bookings made by user

        for row in row_number:
            count = count + 1

            room_name = return_specific_line_in_booking(row - 4)
            print(count, ". ", room_name)

        # ask user which booking he would like to make changes

        while True:
            decision = input("Please enter: ")
            if decision.isdigit():
                decision = int(decision)
                while True:
                    if decision in range(1, count + 1):
                        break
                    else:
                        print("Please enter a valid number.")
                        decision = int(input("Please enter: "))
                break
            else:
                print("Please enter digit number only.")

        value = get_value_by_index(list_row, decision - 1)

        # ask user which information for that booking he would like to make changes

        print("\nPlease select the information you would like to update/modify: "
              "\n1. Name of the person who booked the room"
              "\n2. Date Booked"
              "\n3. Nights Stay"
              "\n4. Additional Request")

        # only digit number and number in range is allowed

        while True:
            choose = input("Please select: ")
            if choose.isdigit():
                choose = int(choose)
                if choose in range(1, 5):
                    break
                else:
                    print("Please enter a valid number")
            else:
                print("Please enter digit number only")

        # replace the value in specific row by new value
        # the row number is identified by using mathematical mathod

        if choose == 1:
            new_content = input("Please enter the new name of the person who booked the room: ")
            replace_value_in_booking(value - 3, new_content)

        elif choose == 2:
            new_content = input("Please enter the new date: ")
            replace_value_in_booking(value - 2, new_content)

        elif choose == 3:
            while True:
                new_content = input("Please enter the nights you will stay in the room (X nights): ")
                if new_content.isdigit():
                    break
                else:
                    print("Please enter digit number only. ")
            replace_value_in_booking(value - 1, new_content)

        elif choose == 4:
            new_content = input("Please enter your additional request: ")
            replace_value_in_booking(value + 1, new_content)

        print("Data changed! ")

    # if user did not make any of the bookings

    else:
        print("You did not make any of the bookings. ")



# def a function to show the row number in account.txt (for generate report purpose only)

def find_rows_with_username_in_account(words_to_check):
    matching_rows = []
    with open("account.txt", 'r') as file:
        for row_number, row in enumerate(file, 1):
            row_lower = row.lower()
            if '.username' in row_lower and all(word.lower() in row_lower for word in words_to_check):
                matching_rows.append(row_number)

    return matching_rows



# def a function that generate report

def generate_report():
    print("Welcome Admin. Here is the interface to generate the report. ")

    # make sure that the username entered is valid

    while True:
        decision = input("Please enter the username of the user: ")
        decision = decision + ".username"
        with open("account.txt", "r") as file:
            lines = [line.strip() for line in file.readlines()]
            if decision in lines:
                break
            else:
                print("Please enter a valid username")

    # check the row number of the username in account.txt

    row_number = find_rows_with_username_in_account(decision)

    # change row number into integer

    int_row = row_number[0]

    # read the data based on the row number

    name = return_specific_line_in_account(int_row- 7)
    address = return_specific_line_in_account(int_row - 6)
    gmail = return_specific_line_in_account(int_row - 5)
    contact = return_specific_line_in_account(int_row - 4)
    gender = return_specific_line_in_account(int_row - 3)
    birth = return_specific_line_in_account(int_row - 2)
    age = return_specific_line_in_account(int_row - 1)
    username = return_specific_line_in_account(int_row).removesuffix(".username")
    password = return_specific_line_in_account(int_row + 1).removesuffix(".password")

    # print the data read

    print("\n\n\n\t\tMEMBER REPORT")
    print()
    print("Name: ", name)
    print("Address: ", address)
    print("Email: ", gmail)
    print("Contact Number: ", contact)
    print("Gender: ", gender)
    print("Date of Birth: ", birth)
    print("Age: ", age)
    print("Username: ", username)
    print("Password: ", password)



# define a new funtion that allows admin to add room service menu

def add_room_service_menu():
    print("Welcome Admin. Here is the interface for you to add room service menu. ")
    print("\nPlease enter the information of the menu. ")


    # ask user to enter all the information of the food

    food = input("Please enter the name of the food: ")

    # limit the data type of the price, only digit number is allowed

    while True:
        price = input('Please enter the price of the food: ')
        if price.isdigit():
            break
        else:
            print("Only digit number is allowed")

    rest = input("Please enter the restaurant name ordered from: ")

    # only "vegetarian" and "all people" is allowed for people

    while True:
        people = input("This menu is suitable for (vegetarian/all people): ")
        if people == "vegetarian" or people == "all people":
            break
        else:
            print("Please enter a valid value (vegetarian/all people).")

    # write all the data into menu.txt

    with open("menu.txt", "a") as file:
        file.write(f"{food}\n{price}\n{rest}\n{people}\n")

    print("Menu added.")



# define a new function to show all the service menu

def view_service_menu():
    print("Here are the menu of the foods: \n\n")
    with open("menu.txt", "r") as file:
        line = file.readlines()  # read the data in menu.txt file and turn it into list

    # read the data from the list based on index number

    for i in range (0, len(line), 4):
        food = line[i].strip()
        price = line[i+1].strip()
        restaurant = line[i+2].strip()
        people = line[i+3].strip()

        # print all the data read

        print("Food Name: ", food)
        print("Food Price: RM", price)
        print("Order From: ", restaurant)
        print("Suitable for: ", people)
        print()



# def a function that can return specific line from menu.txt

def return_specific_line_in_menu(row_number):
        with open("menu.txt", "r") as file:
            for line, lines in enumerate(file, start=1):
                if line == row_number:
                    return lines.strip()



# define a new function to count all the line in menu.txt

def count_all_lines_in_menu():
    count = 0
    with open("menu.txt","r") as file:
        for i in file:
            count +=1
    return count



# define a new function which can search menu

def search_menu():
    print("Here is the interface for you to search for the room service menu. ")
    print("Here is all the foods name. ")

    # print all the foods in menu, with numbers

    total_line = count_all_lines_in_menu()
    count = 0
    x = 0

    while x < total_line:
        food = return_specific_line_in_menu(1 + count * 4)
        count += 1
        x += 4
        print(count, ". ", food)

    # ask user to enter the food (represent by a number) that they would like to search
    # only digit number and number in range accepted

    while True:
        decision = input("Please enter the food number you would like to search: ")
        if decision.isdigit():
            decision = int(decision)
            if decision in range (1, count +1):
                break
            else:
                print("You should enter a valid value. ")
        else:
            print("You should enter a valid value.")

    # read the data in menu.txt based on row number

    food = return_specific_line_in_menu(1 + 4 * (decision - 1))
    price = return_specific_line_in_menu(2 + 4 * (decision - 1))
    restaurant = return_specific_line_in_menu(3 + 4 * (decision - 1))
    people = return_specific_line_in_menu(4 + 4 * (decision -1))

    # print the data read

    print("Food: ", food)
    print("Price: RM", price)
    print("Restaurant: ", restaurant)
    print("Suitable for: ", people)


# def a function that can delete specific rows in menu.txt
def delete_rows_in_menu(row_number):
    with open("menu.txt", 'r') as file:
        lines = file.readlines()

    if row_number <= 0 or row_number > len(lines):
        print(f"Invalid row number: {row_number}")
        return

    updated_lines = [line for i, line in enumerate(lines, 1) if i != row_number]

    with open('menu.txt', 'w') as file:
        file.writelines(updated_lines)



# Define a new function to allow admin delete room service information
def delete_menu():
    print("Here is the interface for you to delete the room service menu. ")
    print("Here is all the foods name. ")

    # show all the food name, with a number

    total_line = count_all_lines_in_menu()
    count = 0
    x = 0

    while x < total_line:
        food = return_specific_line_in_menu(1 + count * 4)
        count += 1
        x += 4
        print(count, ". ", food)

    # ask the user which food that they would like to delete
    # only digit number and number in range can be accepted

    while True:
        decision = input("Please enter the food number you would like to delete: ")
        if decision.isdigit():
            decision = int(decision)
            if decision in range (1, count +1):
                break
            else:
                print("You should enter a valid value. ")
        else:
            print("You should enter a valid value.")

    decision = decision - 1

    # delete the row in menu.txt, the row number is identified based on mathematical method

    delete_rows_in_menu(1 + 4 * decision)
    delete_rows_in_menu(1 + 4 * decision)
    delete_rows_in_menu(1 + 4 * decision)
    delete_rows_in_menu(1 + 4 * decision)

    print("Menu deleted. ")



# def a function that can replace the value in specific row in menu

def replace_value_in_menu(row_number, new_contents):
    with open("menu.txt", 'r') as file:
        lines = file.readlines()

    lines[row_number - 1] = new_contents + "\n"

    with open("menu.txt", 'w') as file:
        file.writelines(lines)



# def a function that allow admin to edit the information in menu

def edit_menu():
    print("Here is the interface to edit and update the menu information. ")
    print("Here is the name of all the foods: ")
    total_line = count_all_lines_in_menu()
    count = 0
    x = 0

    # print all the food name with number

    while x < total_line:
        food = return_specific_line_in_menu(1 + count * 4)
        count += 1
        x += 4
        print(count, ". ", food)

    # ask the decision of the user, determine which food he would like to edit

    while True:
        decision = input("Please enter the food number you would like to edit: ")
        if decision.isdigit():
            decision = int(decision)
            if decision in range(1, count + 1):
                break
            else:
                print("You should enter a valid value. ")
        else:
            print("You should enter a valid value.")

    print("Please select the information you would like to update: " )
    print("1. Food Price")
    print("2. Restaurant Name")
    print("3. Suitable for who")

    # ask the user which information for that food he would like to change
    # only digit number and number in range allowed

    while True:
        decision2 = input("Please enter: ")
        if decision2.isdigit():
            decision2 = int(decision2)
            if decision2 in range (1, 4):
                break
            else:
                print("Please enter a valid number. ")

        else:
            print("Please enter a valid number. ")

    decision = decision - 1
    # replace the value in the specific row with new value

    if decision2 == 1:
        while True:
            new_content = input("Please enter the new price of the food: ")
            if new_content.isdigit():
                replace_value_in_menu(2 + 4 * decision, new_content)
                break
            else:
                print("Please enter digit number only. ")

    elif decision2 == 2:
        new_content = input("Please enter the restaurant name of the food: ")
        replace_value_in_menu(3 + 4 * decision, new_content)

    elif decision2 == 3:
        while True:
            new_content = input("This food is suitable for (vegetarian/all people): ")
            if new_content == "vegetarian" or new_content == "all people":
                replace_value_in_menu(4 + 4 *decision, new_content)
                break
            else:
                print("Please enter a valid value. ")

    print("Data changed. ")


# define a new function that can identify and list out all the row number for vegetarian foods

def find_row_numbers_vegetarian():
    row_numbers = []
    with open('menu.txt', 'r') as file:
        for row_number, line in enumerate(file, 1):
            if "vegetarian" in line.lower():
                row_numbers.append(row_number)
    return row_numbers


# def a new function to allow customer to make order

def make_order(username):
    print("Welcome user. Here is the interface for you to make order. ")

    # ask if user is a vegetarian or not
    # only y and n is allowed

    while True:
        ask = input("Are you a vegetarian? (y/n): ").lower()
        if ask == "y" or ask == "n":
            break
        else:
            print("Please enter a valid value. ")

    # if y, print all the vegetarian food only

    if ask == "y":
        print("Here is the menu for vegetarian: ")
        count = 0
        list = find_row_numbers_vegetarian()
        x = 0

        for i in list:
            count += 1
            number = list[x]
            word = return_specific_line_in_menu(number - 3)
            x += 1
            print(count, ". ",word)

        # ask user which food that would like to order

        while True:
            decision = input("Please enter the food number you would like to order: ")
            if decision.isdigit():
                decision = int(decision)
                if decision in range (1, count +1):
                    break
                else:
                    print("Please enter a valid value.")
            else:
                print("Please enter a valid value. ")

        # ask user to enter the information, such as room number

        decision = decision - 1
        choose_food_row = list[decision]
        food_order = return_specific_line_in_menu(choose_food_row - 3)
        room = input("Please enter your room number: ")

        # write the data into order.txt file

        with open("order.txt", "a") as file:
            file.writelines(f"{food_order}\n{room}\n{username}\n\n")

        print("We will send the food to your room as fast as possible. ")

    # if n, print all the food name

    elif ask == "n":
        total_line = count_all_lines_in_menu()
        count = 0
        x = 0

        while x < total_line:
            food = return_specific_line_in_menu(1 + count * 4)
            count += 1
            x += 4
            print(count, ". ", food)

        # ask user which food they would like to order

        while True:
            decision = input("Please enter the food number you would like to order: ")
            if decision.isdigit():
                decision = int(decision)
                if decision in range(1, count + 1):
                    break
                else:
                    print("You should enter a valid value. ")
            else:
                print("You should enter a valid value.")

        decision = decision - 1

        # ask user to enter the information

        food_order = return_specific_line_in_menu(1 + 4 * decision)
        room_id = input("Please enter your room ID: ")

        # write the data into order.txt file

        with open("order.txt", "a") as file:
            file.write(f"{food_order}\n{room_id}\n{username}\n\n")

        print("We will send the food to your room as fast as possible. ")




# A function that allow user to read the order

def view_order():
    print("Welcome admin. Here is page for you to view all the orders. \n")
    with open("order.txt", "r") as file: # read the data in order.txt and turn all into the list
        line = file.readlines()

        # read the data in the list based on index number

        for i in range (0, len(line), 4):
            food = line[i].strip()
            room = line[i + 1].strip()
            username = line[i + 2].strip()

            # print all the data read

            print("Food ordered: ", food)
            print("Room Number/ID: ", room)
            print("Username: ", username)
            print()


# define a new function that will return the price of the room, by providing the room name

def return_room_price(room_name):
    with open("room.txt", "r") as file:
        row_number = find_row_number_in_room(room_name)
        price = return_specific_line_in_room(row_number + 4)
        return price



# A function that find the rows number depend on the given words

def find_rows_with_username_in_order(words_to_check):
    matching_rows = []
    with open("order.txt", 'r') as file:
        for row_number, row in enumerate(file, 1):
            row_lower = row.lower()
            if '.username' in row_lower and all(word.lower() in row_lower for word in words_to_check):
                matching_rows.append(row_number)

    return matching_rows



# return the data in the line in order.txt based on the row number given

def return_specific_line_in_order(row_number):
    with open("order.txt", "r") as file:
        for line, lines in enumerate(file, start=1):
            if line == row_number:
                    return lines.strip()



# def a function that are able to find the row number in menu.txt based on the data entered

def find_row_number_in_menu(data):
    with open("menu.txt", "r") as file:
        for number, line in enumerate(file, start=1):
            if data in line:
                return number



# a function that are able to return the food price in menu.txt

def return_food_price(food_name):
    with open("menu.txt", "r") as file:
        row_number = find_row_number_in_menu(food_name)
        price = return_specific_line_in_menu(row_number + 1)
        return price



# Define a function that will show the bills of each customers

def show_bills():
    print("Welcome admin. Here is the interface for you to view the bills of the customer. ")

    # ask user to enter the username
    # if the username is not in account.txt, ask user to enter again

    while True:
        username = input("Please enter the username of the customer: ")
        username = username + ".username"
        with open("account.txt", "r") as file:
            line = file.readlines()
            if username + "\n" in line:
                break
            else:
                print("Please enter a valid username. ")

    print("\nPlease enter the bills you would like to check: "
          "\n1. Room Booking Bills"
          "\n2. Restaurant Bills"
          "\n3. Total Bills")

    # ask user to enter the bills that the user would like to check
    # only digit number and 1 - 3 is allowed

    while True:
        decision = input("Please enter: ")
        if decision.isdigit():
            decision = int(decision)
            if decision in range (1, 4):
                break
            else:
                print("Please enter a valid value. ")
        else:
            print("Please enter a valid value. ")

    # calculate the bills based on mathematical formula

    if decision == 1:
        price1 = 0
        with open("booking.txt", "r") as booking_file:
            lines = booking_file.readlines()
            if username + "\n" in lines:
                list = find_rows_with_username_and_words(username)
                for i in list:
                    room_name = str(return_specific_line_in_booking(i - 4))
                    one_night = int(return_room_price(room_name))
                    night_stay = int(return_specific_line_in_booking(i -1))
                    price1 += one_night * night_stay
                print("Total Bills for Room Bookings is RM", price1)
            else:
                print("The username you entered does not make any bookings.")

    if decision == 2:
        price2 = 0
        with open("order.txt", "r") as order_file:
            readfile = order_file.readlines()
            if username + "\n" in readfile:
                lists = find_rows_with_username_in_order(username)
                for x in lists:
                    food = str(return_specific_line_in_order(x - 2))
                    food_price = int(return_food_price(food))
                    price2 += food_price
                print("Total Bills for Room Service is RM" , price2)
            else:
                print("The username you entered does not place any order or call room service. ")

    if decision == 3:
        price1 = 0
        with open("booking.txt", "r") as booking_file:
            lines = booking_file.readlines()
            if username + "\n" in lines:
                list = find_rows_with_username_and_words(username)
                for i in list:
                    room_name = str(return_specific_line_in_booking(i - 4))
                    one_night = int(return_room_price(room_name))
                    night_stay = int(return_specific_line_in_booking(i - 1))
                    price1 += one_night * night_stay
                print("Total Bills for Room Bookings is RM", price1)
            else:
                print("The username you entered does not make any bookings.")

        price2 = 0
        with open("order.txt", "r") as order_file:
            readfile = order_file.readlines()
            if username + "\n" in readfile:
                lists = find_rows_with_username_in_order(username)
                for x in lists:
                    food = str(return_specific_line_in_order(x - 2))
                    food_price = int(return_food_price(food))
                    price2 += food_price
                print("Total Bills for Room Service is RM", price2)
            else:
                print("The username you entered does not place any order or call room service. ")

        total_bills = price1 + price2
        print("Total Bills is RM", total_bills)



# Make the full login page

def complete_system():
    print("Welcome to Hotel Reservation System.")

    # ask user if they are the member of the system
    # only y and n allowed

    while True:
        decision = input("Are you the member of our system? (y/n): ").lower()

        if decision == "y":
            break
        elif decision == "n":
            break
        else:
            print("You should enter 'y' or 'n' only.")

    # if y, then the system will ask the user to login

    if decision == "y":
        print("Please proceed to login. ")

        # ask the user to enter his username
        # check if the user is in the account.txt, if it is not in the txt file, then the system will ask the user to use a valid username

        while True:
            while True:
                with open("account.txt", "r") as file:
                    line = file.readlines()
                    username = input("Please enter your username: ")
                    username = username + ".username"
                    if username + "\n" in line:
                        break
                    else:
                        print("The username you entered has not been registered. ")

            # ask the user to enter the password

            username_row = find_rows_with_username_in_account(username)
            pass_num = username_row[0]
            correct_password = return_specific_line_in_account(pass_num + 1)
            password = input("Please enter your password: ")
            password = password + ".password"
            if password == correct_password:
                break
            else:
                print("Your password is wrong, Please try again.")

        # determine the role of the user, and give a right permissions

        role = return_specific_line_in_account(pass_num + 2)

        # if the role of the user is admin, then list out the permissions of admin, and ask admin to choose one of the following

        if role == "admin":
            while True:
                print("Welcome. Please select one of the following: "
                      "\n1. Login to Access System"
                      "\n2. View all the detail of the rooms"
                      "\n3. Add/upload new room details"
                      "\n4. Update/modify room information"
                      "\n5. View all room service menu"
                      "\n6. View all room service order"
                      "\n7. Add new room service menu"
                      "\n8. Delete room service information"
                      "\n9. Edit room service menu"
                      "\n10. Search room service menu"
                      "\n11. View all bookings of customers"
                      "\n12. Generate bills for customers"
                      "\n13. Search bookings for specific customer"
                      "\n14. Generate customer details report."
                      "\n15. Exit")

                # make sure only digit number and number in range is allowed

                while True:
                    decision_admin = input("Please select: ")
                    if decision_admin.isdigit():
                        decision_admin = int(decision_admin)
                        if decision_admin in range(1, 16):
                            break
                        else:
                            print("Please enter a valid value. ")
                    else:
                        print("Please enter a valid value. ")

                if decision_admin == 1:
                    login_access_system()

                elif decision_admin == 2:
                    view_room_detail()

                elif decision_admin == 3:
                    add_room_detail()

                elif decision_admin == 4:
                    update_room_detail()

                elif decision_admin == 5:
                    view_service_menu()

                elif decision_admin == 6:
                    view_order()

                elif decision_admin == 7:
                    add_room_service_menu()

                elif decision_admin == 8:
                    delete_menu()

                elif decision_admin == 9:
                    edit_menu()

                elif decision_admin == 10:
                    search_menu()

                elif decision_admin == 11:
                    view_all_bookings()

                elif decision_admin == 12:
                    show_bills()

                elif decision_admin == 13:
                    search_bookings()

                elif decision_admin == 14:
                    generate_report()

                elif decision_admin == 15:
                    break

                # ask user if user want to continue or not
                # only y and n allowed

                while True:
                    decision_to_continue = input("Do you wish to continue? (y/n): ").lower()
                    if decision_to_continue == "y" or decision_to_continue == "n":
                        break
                    else:
                        print("You should enter a valid value. ")

                if decision_to_continue == "y":
                    continue

                elif decision_to_continue == "n":
                    break

            print("Thanks for using the hotel reservation system.")

        # if the system detect the role of the user is "customer", then give the correct permissions
        # print all the permissions of the customer

        if role == "customer":
            while True:
                print("Welcome. Please select one of the following: "
                      "\n1. View all room details"
                      "\n2. Booking room"
                      "\n3. View your own bookings"
                      "\n4. Update your own bookings information"
                      "\n5. Cancel bookings"
                      "\n6. Personal information interface"
                      "\n7. View room service menu"
                      "\n8. Order the foods"
                      "\n9. Exit")

                # ask user to choose one of the following
                # only digit number and number in range is allowed

                while True:
                    decision_customer = input("Please choose: ")
                    if decision_customer.isdigit():
                        decision_customer = int(decision_customer)
                        if decision_customer in range(1, 10):
                            break
                        else:
                            print("Please enter a valid value.")
                    else:
                        print('Please enter a valid value')

                if decision_customer == 1:
                    view_room_detail()

                elif decision_customer == 2:
                    booking_interface(username)

                elif decision_customer == 3:
                    view_own_booking(username)

                elif decision_customer == 4:
                    update_booking(username)

                elif decision_customer == 5:
                    delete_booking(username)

                elif decision_customer == 6:
                    personal_information_interface(username)

                elif decision_customer == 7:
                    view_service_menu()

                elif decision_customer == 8:
                    make_order(username)

                elif decision_customer == 9:
                    break

                while True:
                    decision_to_continue = input("Do you wish to continue? (y/n): ").lower()
                    if decision_to_continue == "y" or decision_to_continue == "n":
                        break
                    else:
                        print("You should enter a valid value. ")

                if decision_to_continue == "y":
                    continue

                elif decision_to_continue == "n":
                    break

            print("Thanks for using the hotel reservation system.")

    # if user is not a registered member, then print all the permission that can be accessed for non registered member

    elif decision == "n":
        while True:
            print("Welcome. Please select one of the following: "
                  "\n1. View Room Detail"
                  "\n2. Registration"
                  "\n3. Exit")

            # ask user to choose one of the following
            # only digit number and number in range is allowed

            while True:
                choose_non_member = input("Please select: ")
                if choose_non_member.isdigit():
                    choose_non_member = int(choose_non_member)
                    if choose_non_member in range(1, 4):
                        break
                    else:
                        print("You should enter a valid value.")
                else:
                    print("You should enter a valid value. ")

            if choose_non_member == 1:
                view_room_detail()

            elif choose_non_member == 2:
                registration()

            elif choose_non_member == 3:
                break

            while True:
                decision_to_continue = input("Do you wish to continue? (y/n): ").lower()
                if decision_to_continue == "y" or decision_to_continue == "n":
                    break
                else:
                    print("You should enter a valid value. ")

            if decision_to_continue == "y":
                continue

            elif decision_to_continue == "n":
                break

        print("Thanks for using the hotel reservation system.")

complete_system()