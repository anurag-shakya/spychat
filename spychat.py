# importing specific spy details from file name: spy_details
from spy_details import spy_name, spy_salutation, spy_rating, spy_age, spy_is_online



#======================  function start_chat()  starts here  ===========================================================

# function name: start_chat ,used to provide a spy chat menu to spy so that he/she could select different options

def start_chat(spy_name, spy_age, spy_rating):

    global spy_is_online

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
            choice = raw_input()
            if choice == '1':
                current_status_message = add_status(current_status_message)
                print "success! status updated \n Entering Main menu... \n"


            elif choice == '2':
                # code to add a spy friend
                number_of_friends = add_friend()
                print "Now You\'ve %d Friend detective(s) \n" % (number_of_friends)

                ''' mutiline comment  [remaining 3 modules: to be completed]
            elif choice == '3':
                # code to send a secret message

            elif choice == '4':
                # code to read personal message

            elif choice == '5':
                # code to read a chat from user
                '''
            elif choice == '6':
                # code to exit from the spy chat menu
                print "Thank you for using SPY CHAT.\n exiting ... \nYou are offline now"
                spy_is_online = False
                show_menu = False

            else:
                # if spy selected an in valid option
                print "whoa! You've selected an invalid option.\n Please try again "

    else:
        print 'Sorry you are not of the correct age to be a spy'

#======================  function start_chat() ends here  ==============================================================



# =====================  function add_status() starts here  ============================================================

# function name: add_status, used to choose the status of spy from older status or to add new status by appending to older status list

def add_status(current_status_message):

    global STATUS_MESSAGES

    if current_status_message != None:
        print "Your current status message is %s " % (current_status_message)
    else:
        print "You don\'t have any status message currently \n"


    while True:                                                 # Until spy doesn't pressed a correct key

        default = raw_input("Do you want to select from the older status (y/n)? ")

        # if spy want to write new status

        if default.upper() == "N":
            new_status_message = raw_input("Okay! Write a new status ")

            if len(new_status_message) > 0:
                updated_status_message = new_status_message
                STATUS_MESSAGES.append(updated_status_message)
                break
            else:
                print "You didn\'t write anything. \n Please try again"

        # if spy want to choose a status from existing status

        elif default.upper() == 'Y':
            item_position = 1

            # if there is no message in Existing list of status

            if STATUS_MESSAGES == []:
                print "Sorry! you do not have any Status messages \n Please select option N (To add new status)"
                continue

            # showing list of older status

            for message in STATUS_MESSAGES:
                print "%d. %s" % (item_position, message)
                item_position = item_position + 1

            while True:                                            # Until spy doesn't pressed a correct key

                message_selection = input("\nChoose from the above messages ")
                if len(STATUS_MESSAGES) >= message_selection:
                    updated_status_message = STATUS_MESSAGES[message_selection - 1]
                    break

                # if the selected number is exceeding the list
                else:
                    print "You've selected an invalid option \n Please try again"

            break

        else:
            print "You've entered an invalid key \n Please try again"

    return updated_status_message


#======================  function add_status() ends here  ==============================================================



#======================  function add_friend() starts here  ============================================================

# function name: add_friend, used to add SPY friends to the CHAT

def add_friend():

    global friends_name, friends_age, friends_rating, friends_is_online, spy_rating

    addmore = True
    while addmore :                                                    # to add more than one Spy friend

         # Asking Spy Friend's Details

         print "Please enter your SPY FRIEND\'s salutation"
         new_salutation = raw_input()

         print "Now Enter Spy's Name, Age and Spy rating respectively [press Return Key for every Input]"
         new_name, new_age, new_rating = raw_input(), input(), input()

         # Validating new spy eligibility

         if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating and new_name.isalpha():

             new_name = new_salutation + ". " + new_name
             friends_name.append(new_name)
             friends_age.append(new_age)
             friends_rating.append(new_rating)
             friends_is_online.append(True)
             print "\n %s is added to the SPY CHAT! \n" % (new_name)

         else:
             # Fried is not eligible to be a spy
             print 'Sorry! Invalid entry. We can\'t add spy with the details you provided \n'



         while True :                                                  # asking for more friends

             more = raw_input("Do you want to add more Spy Friends? (y/n) ")

             if more.upper() == "N":
                 addmore = False
                 break

             elif more.upper() == "Y":
                 break

             else :
                 print "Please press a valid key (y/n)"


    return len(friends_name)


#======================  function add_friend() ends here  ==============================================================



# program started

# lists initialization
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']
friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []


print "Hello Spy!"
print 'Let\'s get started'

question = "Do you want to continue as %s %s (y/n)? " % (spy_salutation, spy_name)
existing = raw_input(question)		

if existing == "Y" or existing == "y" :

    # Showing SPY CHAT MENU if default spy comes to chat
    start_chat(spy_name, spy_age, spy_rating)

elif existing == "N" or existing == "n" :

    # if some other spy comes to chat, then save his/her details and redirect to the SPY CHAT MENU
    # python is a loosely typed (Duck Typing) programming language
    spy_name = ''
    spy_salutation = ''
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_name = raw_input("Welcome to spy chat, could you please tell me your name : ")

    if len(spy_name) > 0 and spy_name.isalpha():
        # If spy do not provide his/her name empty

        print ("\n Welcome %s. Glad to have you back with us.") % (spy_name)

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
        print "whoa! You don\'t provided your name or may pressed invalid character in name\n Please try again. \n"

else :
    print "You provided an invalid input. \n Please try again \n"