# importing specific spy details from file name: spy_details
from spy_details import spy_name, spy_salutation, spy_rating, spy_age, spy_is_online


# function name: start_chat ,used to provide a spy chat menu to spy so that he/she could select different options
def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None

    spy_name = spy_salutation + " " + spy_name

    # To validate the spy age, whether he/she belongs to age to be a spy.
    if spy_age > 12 and spy_age < 50:

        print "Authentication complete. Welcome %s, age: %d with a rating of: %.1f Proud to have you onboard" % (spy_name,spy_age,spy_rating )


        # loop will not end until spy want to exit the SPY CHAT MENU
        show_menu = True
        while show_menu:
            # multiline statement print
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
# function start_chat() ends here





# program started
print "Hello Spy!"
print 'Let\'s get started'


question = "Do you want to continue as %s %s (y/n)? " % (spy_salutation, spy_name)
existing = raw_input(question)		

if existing == "Y" or existing == "y" :
    start_chat(spy_name, spy_age, spy_rating)                         # Showing SPY CHAT MENU if default spy comes to chat
elif existing == "N" or existing == "n" :

    # if some other spy comes to chat, then save his/her details and redirect to the SPY CHAT MENU
    # python is a loosely typed (Duck Typing) programming language
    spy_name = ''
    spy_salutation = ''
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_name = raw_input("Welcome to spy chat, could you please tell me your name : ")

    if len(spy_name) > 0:
        # If spy do not provide his/her name empty

        print ('\n Welcome %s. Glad to have you back with us.') % (spy_name)

        spy_salutation = raw_input("What should I call you (Mr. or Ms.): ")

        spy_name = spy_salutation + ". " + spy_name

        print ("Alright %s I'd like to know a little bit more about you before we proceed...\n") % (spy_name)

        spy_age = input("What is your age? ")

        spy_age = int(spy_age)

        spy_rating = input("What is your spy rating? ")

        spy_is_online = True

        start_chat(spy_name, spy_age, spy_rating)



    else :

        # If spy provides his/her name empty
        print "whoa! You don\'t have a name?\n Please try again ."

else :
    print "You provided an invalid input. \n Please try again"