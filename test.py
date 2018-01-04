from spy_details import spy_name, spy_salutation, spy_rating, spy_age, spy_is_online

print "Hello! Let\'s get started"

question = "Do you want to continue as %s %s (y/n)? " % (spy_salutation, spy_name)
existing = raw_input(question)


def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None

    spy_name = spy_salutation + " " + spy_name

    if spy_age > 12 and spy_age < 50:

        print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(
            spy_rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            print """ \t\t\t SPY CHAT MENU \n========================================================\n  

            select an option      
                   1. Status Update 
                   2. Add a Friend 
                   3. Send a Secret Message
                   4. Read a Personal Message
                   5. Read Chats from a User 
                   6. Exit from Spy chat menu"""
            choice = input()
            if choice == 1:
                # code to update status
                print "status updated [code will be in next class]"

                ''' mutiline comment
            elif choice == 2:
                # code to add a spy friend


            elif choice == 3:
                # code to send a secret message

            elif choice == 4:
                # code to read personal message

            elif choice == 5:
                # code to read a chat from user
                '''
            elif choice == 6:
                # code to exit from the spy chat menu

                show_menu = False

            else:
                # if selected an in valid option
                print "whoa! You've selected an invalid option.\n Please try again "

    else:
        print 'Sorry you are not of the correct age to be a spy'

if existing == "Y" or existing == "y" :
    start_chat(spy_name, spy_age, spy_rating)
else:
    spy_name = ''
    spy_salutation = ''
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy_name) > 0:
        spy_salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy_age = input("What is your age?")

        spy_rating = input("What is your spy rating?")

        spy_is_online = True

        start_chat(spy_name, spy_age, spy_rating)
    else:
        print 'Please add a valid spy name'