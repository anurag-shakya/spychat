'''
Project Name : SPYCHAT
Created By   : ANURAG SHAKYA       [IMS ENGINEERING COLLEGE]
Submitted to : Mr. SHUBHAM JAIN    [AcadView]
             : Ms. TANVI RANGA     [AcadView]
             : Mr. RISHABH ARORA   [AcadView]
Date         : 22/01/2018
'''



from spy_details import spy, Spy, friend_list, ChatMessage           # importing specific auxilliary details from file named as: spy_details
from steganography.steganography import Steganography                # To encode text into some other files like music, image files
from colorama import Fore                                            # To provide information using some colored text
from datetime import datetime                                        # To use different date and time formats
import csv                                                           # importing csv modules to operate on csv files
import os                                                            # importing os modules for reading, writing files
import ctypes                                                        # usued to provied message boxes of different styles eg, 0,1,2 etc.,
import sys                                                           # to use system specific parameters and functions




#-------------------------  function start_chat()  starts here  --------------------------------------------------------

# function name: start_chat ,used to provide a spy chat menu to spy so that he/she could select different options

def start_chat(spy):

    current_status_message = None

    # loading friend list from the database file friends_databse.csv
    try:
        print Fore.CYAN + "Loading friends..."
        load_friends()

    # if met some error while loading friends
    except Exception as e:
        print Fore.RED + "Please Check you friends_databse.csv file \n Some friends might not loaded :(\n Error : %s" %(e)


    # loading chat data from the database file chats_database.csv
    try :
        print Fore.CYAN + "Loading chats...\n"
        load_chats()

    # if met some error while loading chat data
    except Exception as e :
        print Fore.RED + "Please Check you chats_databse.csv file \n Some chats might not loaded :( \n Error : %s" %(e)

    print Fore.BLUE + "successfully structured SPY CHAT MENU"

    # To validate the spy age, whether he/she belongs to age to be a spy.
    if spy.age > 12 and spy.age < 50:

        print Fore.GREEN +" \n Authentication complete.... \n" + Fore.BLUE + " Welcome " + Fore.RED + spy.salutation +" "+ spy.name +\
              Fore.BLUE + ", age: %d with a rating of: %.1f Proud to have you onboard \n\n" % (spy.age, spy.rating) + Fore.BLACK

        # loop will not end until spy want to exit the SPY CHAT MENU
        show_menu = True
        while show_menu :

            print """\n                     SPY CHAT MENU \n=========================================================\n                 

            select an option      
                   1. Show/Update Status  
                   2. Check Friend List
                   3. Add a Friend 
                   4. Send a Secret Message
                   5. Read a Personal Message
                   6. Show Chat History with Specific Spy 
                   7. Switch User (to change spy)
                   8. Want Some Miscellaneous Options?              -->[ADVANCE OPTIONS]
                   9. Exit from Spy chat menu
            
                  """
            choice = raw_input()

            # to show current status or to update new status of spy
            if choice == '1' :
                current_status_message = add_status(current_status_message)
                print "success! status updated \n Entering Main menu... \n"

            # to print all the friends with details who are in the friend list of spy
            elif choice == '2' :
                check_friend_list()

            # to add a spy friend
            elif choice == '3' :
                number_of_friends = add_friend()
                print "Now You\'ve %d Friend detective(s) \n" % (number_of_friends)

            # to send a secret message to a specific spy friend
            elif choice == '4' :
                send_message()

            # to read the message from a specific spy friend
            elif choice == '5' :
                read_message()

            # to show chat history with some specific spy friend
            elif choice == '6' :
                show_chat_history()

            # to switch user on to the spy chat menu [by default it's Mr. Bond is set at initiataion of pragram]
            elif choice == '7' :
                print " Logging in new spy to the chat... \n"
                switch_user()


            # Advance features like : 1) to delete a spy friend from friend list from RAM and database file friend_database.csv
            #                         2) to clear chats with some specific spy friend from RAM and database file chats_databse.csv
            #                         3) to perform MASTER RESET [CLEAR whole friend list from RAM and database]

            elif choice == '8' :

                ans = raw_input("Your rating must be greater than or eqaul 4.5 for this Option \n Press y to continue else any key to enter Main Menu... \n")

                #  this option is available only for spy with rating greater than or equal to 4.5
                if ans.upper() == 'Y':
                    if spy.rating >= 4.5 :
                        miscellaneous_options(spy)

                    else:
                        print "Sorry %s %s. You aren't authorised for these options.\n Entering Main Menu... \n" % (spy.salutation, spy.name)

                else:
                    print "Alright %s %s. \n Entering Main Menu... \n" % (spy.salutation, spy.name)

            # code to exit from the spy chat menu
            elif choice == '9' :
                print "Thank you for using SPY CHAT.\n  exiting ... \nYou are offline now"
                spy.is_online = False
                show_menu = False

            # if spy selected an in valid option
            else :
                message_box("whoa! You've selected an invalid option\n Please try again ", "Oops", 0)

    else :
        message_box("Sorry!! you are too younger to be a spy", "Oops", 0)


#-------------------------  function start_chat() ends here  -----------------------------------------------------------



#-------------------------  function message_box() starts here  -----------------------------------------------------------

def message_box(text, title, style) :

    return ctypes.windll.user32.MessageBoxA(0, text, title, style)

#-------------------------  function message_box() ends here  -----------------------------------------------------------



#-------------------------  function add_status() starts here  ---------------------------------------------------------

# function name: add_status, used to choose the status of spy from older status or to add new status by appending to older status list

def add_status(current_status_message) :

    if current_status_message != None :
        print "Your current status message is %s " % (current_status_message)
    else :
        print "You don\'t have any status message currently \n"


    while True :                                                         # Until spy doesn't pressed a correct key

        default = raw_input("Do you want to select from the older status (y/n)? ")


        # if spy want to write new status
        if default.upper() == "N" :
            new_status_message = raw_input("Okay! Write a new status ")

            # if spy provided an empty input
            if len(new_status_message) > 0 :
                updated_status_message = new_status_message
                STATUS_MESSAGES.append(updated_status_message)
                break

            else :
                print "You didn\'t write anything. \n Please try again"

        # if spy want to choose a status from existing status

        elif default.upper() == 'Y' :
            item_position = 1

            # if there is no message in Existing list of status

            if STATUS_MESSAGES == [] :
                print "Sorry! you do not have any Status messages \n Please select option N (To add new status)"
                continue

            # showing list of older status

            for message in STATUS_MESSAGES :
                print "%d. %s" % (item_position, message)
                item_position = item_position + 1

            while True :                                            # Until spy doesn't pressed a correct key

                message_selection = raw_input("\nChoose from the above messages ")

                # handling wrong entries made by spy
                try :
                    message_selection = int(message_selection)

                except ValueError :
                    message_box("You need to press a numeric key only   \n Please try again","Oops",  0)

                if len(STATUS_MESSAGES) >= message_selection :
                    updated_status_message = STATUS_MESSAGES[message_selection - 1]
                    break

                # if the selected number is exceeding the list
                else :
                    message_box("You've selected an invalid option  \n Please try again","Oops",  0)

            break

        else :
            message_box("You've entered an invalid key \n Please try again","Oops",  0)

    return updated_status_message


#-------------------------  function add_status() ends here  -----------------------------------------------------------



#-------------------------  function add_friend() starts here  ---------------------------------------------------------

# function name: add_friend, used to add SPY friends to the CHAT

def add_friend() :

    new_friend = Spy('','',0,0.0)

    addmore = True
    while addmore :                                                    # to add more than one Spy friend

         # Asking Spy Friend's Details

         new_friend.salutation = raw_input("Please add your SPY friend's salutation: ")
         new_friend.name = raw_input("Enter friend's Name: ")
         new_friend.age = input("Age: ")
         new_friend.rating = input("and Spy rating: ")
		 
         # Validating new spy eligibility

         if len(new_friend.name) > 0 :
             if new_friend.age > 12 and new_friend.age <= 50 :


                 if new_friend.name.isalpha() :

                     if new_friend.rating >= spy.rating:

                         # adding new friend to the friend list
                         friend_list.insert(len(friend_list), new_friend)

                         print "\n %s %s is added to the SPY CHAT! \n" % (new_friend.salutation, new_friend.name)

                     else :
                         message_box("Sorry! you aren't eligible to add friends \n Your Rating is not so high ", "Oops", 0)

                 else :
                     message_box("Please enter a valid name", "Oops", 0)
             else :
                 message_box("Sorry! your age is not to be a spy \n Please try again", "Oops", 0)

         else :
             # if friend is not provide your spy friend's name
             message_box("Sorry! you must provide your spy friend name.", "Oops", 0)


         while True :                                                  # asking for more friends

             more = raw_input("Do you want to add more Spy Friends? (y/n) ")

             if more.upper() == "N" :
                 addmore = False
                 break

             elif more.upper() == "Y" :
                 break

             else :
                 message_box("Please press a valid key (y/n)", "Oops", 0)

    return len(friend_list)


#-------------------------  function add_friend() ends here  -----------------------------------------------------------



#-------------------------  function check_friend_list() starts here  --------------------------------------------------

# function name : check_friend_list() : To show the friend list of the spy

def check_friend_list():

    print "Your friends are : \n"
    i=0
    for friend in friend_list :
        i = i+1

        # printing names with other details all friends
        print "%d." %(i) + Fore.RED + " %s %s " %(friend.salutation, friend.name) + Fore.BLACK + "with age: " +\
              Fore.BLUE + "%d" %(friend.age) + Fore.BLACK + " and rating: " + Fore.BLUE + "%.1f" %(friend.rating) + Fore.BLACK


#-------------------------  function check_friend_list() ends here  ----------------------------------------------------



#-------------------------  function select_a_friend() starts here  ----------------------------------------------------

# function name :select_a_friend(), used to choose a friend from a list of all Spy friends
                                  # (purpose of choosing friend : to read, delete specific friend or friend's chat)

def select_a_friend() :

    # Showing all friends
    check_friend_list()

    while True :

        index_choice = raw_input("\nChoose a friend from the above list ")

        # handling wrong entries made by spy
        try :

            # if entered choice is exceeding total number of friends or if alphabetic key is entered
            if int(index_choice) > len(friend_list) :
                message_box("Index selected does not exist \n Please try again \n", "Oops", 0)
                continue

        except ValueError :
            message_box("you should press a numeric key only \n Please try again \n", "Oops", 0)
            continue

        print Fore.RED + "%s %s" %(friend_list[int(index_choice)-1].salutation,friend_list[int(index_choice)-1].name) + Fore.BLACK +" is selected"

        return int(index_choice) -1


#-------------------------  function select_a_friend() ends here -------------------------------------------------------



#-------------------------  function send_message() starts here  -------------------------------------------------------

# function name : send_message(), To send a secret message to other spy friends by encoding it using steganography.
                          #[steganography: to encode text into some other files like music, image files]

def send_message():

    # choosing friend to send a new secret message
    chosen_friend = select_a_friend()

    input_image_path  =   raw_input("What is the name [with full path] of the image? ")
    output_image_path =   "output.jpg"
    hidden_text       =   raw_input("Type your secret message here: ")

    # checking for hidden text whether spy is in some emergency or not, if so send an immediate alert to the friend
    msg_part1, msg_part2 = check_if_any_sos(hidden_text)

    # If found any sos, sent an immediate emergency alert to thier spy friend
    if msg_part1 != 0 and msg_part2 != 0:
        hidden_text = "Hey! %s " %(spy.name) + msg_part1 + " %s " %(friend_list[chosen_friend].name) + msg_part2


    # Encoding the message using steganography
    try :
        Steganography.encode(input_image_path, output_image_path, hidden_text)

    except Exception as e:
        msg = "Error : %s" %(e)
        message_box(msg, "Oops", 0)


    sent_by_me = True
    t = datetime.now()
    time = t.strftime("%d %B %Y %A at %H:%M:%S")
    new_chat = ChatMessage(hidden_text, sent_by_me,time)

    # savaing chat
    friend_list[chosen_friend].chats.append(new_chat)

    # writing chat to the database file chats_database.csv for permanent use
    try :
        with open("chats_database.csv","a") as chats_data:

            write_object = csv.writer(chats_data, delimiter = ',' )
            write_object.writerow([friend_list[chosen_friend].salutation, friend_list[chosen_friend].name,hidden_text,new_chat.time,new_chat.sent_by_me])
            print "Your secret message has been sent!"

    except csv.Error as e1:
        sys.exit('file chats_database.csv", error name: %s' % (e1))


#-------------------------  function send_message() ends here  ---------------------------------------------------------



#-------------------------  function read_message() starts here  -------------------------------------------------------

# function name :read_message(), To read a recieved secret message by decoding it from some other files [like music, image files]

def read_message():

    # choosing a friend whose message is to be read
    chosen_friend = select_a_friend()

    output_image_path = raw_input("What is the name of the file? ")

    # performing decoding to extract hidden text from some other file(like image, music file etc.,)
    hidden_text = Steganography.decode(output_image_path)

    sent_by_me = False
    t = datetime.now()
    time = t.strftime("%d %B %Y %A at %H:%M:%S")

    new_chat = ChatMessage(hidden_text, sent_by_me, time)

    # saving chat
    friend_list[chosen_friend].chats.append(new_chat)

    # writing chat to the database file chats_database.csv for permanent use
    try :
        with open("chats_database.csv", "a") as chats_data:
            write_object = csv.writer(chats_data, delimiter=',')
            write_object.writerow(
                [friend_list[chosen_friend].salutation, friend_list[chosen_friend].name, hidden_text, new_chat.time,
                 new_chat.sent_by_me])

        print hidden_text
        print "Your secret message has been saved!"

    except csv.Error as e2:
        sys.exit('file chats_database.csv, error name: %s' % (e2))


#-------------------------  function read_message() ends here  ---------------------------------------------------------



#-------------------------  function check_if_any_sos() starts here  ---------------------------------------------------

# function name :check_if_any_sos(), If finds any sos messages in the Hidden Text immediately send emergency alert

def check_if_any_sos(hidden_text):

    # default list of sos messages
    sos_messages = ["I QUIT", "SAVE ME", "CALL 100", "ALERT", "SOS", "HELP", "I AM DONE", "PLEASE HELP ME"]
    hidden_text = hidden_text.upper()

    # If finds any sos messages send emergency alert
    sos_count = 0
    for sos in sos_messages:
        if sos == hidden_text:
            sos_count += 1


    # If found some sos Immediately send emergency alert else do nothing
    if sos_count > 0:
        return  "Your friend is in big EMERGENCY \n Reach out to HELP ", "as soon as Possible"
    else:
        return 0,0


#-------------------------  function check_if_any_sos() ends here  -----------------------------------------------------



#-------------------------  function show_chat_history() starts here  --------------------------------------------------

# function name: show_chat_history(), used to show chat history with a particular friend

def show_chat_history():

    # choosing friend whose chat history is to be shown
    chosen_friend = select_a_friend()

    # initializing local temporary variables
    count_sent_chats = 0
    count_recieved_chats = 0
    temp_sent_list = []
    temp_recieved_list = []

    for chat in friend_list[chosen_friend].chats:

        # Messages that was sent by chosen friend
        if chat.sent_by_me == "True":

            temp_sent_list.append(Fore.BLUE + chat.time + " \t" + Fore.BLACK + chat.hidden_text)

            count_sent_chats += 1

        # Messages that was recieved by chosen friend
        else :

            temp_recieved_list.append(Fore.BLUE + chat.time + " \t" + Fore.BLACK + chat.hidden_text)

            count_recieved_chats += 1

    # showing name and Total sent messages of chosen friend
    print "\n Messages sent by " + Fore.RED + friend_list[chosen_friend].salutation +" "+ friend_list[chosen_friend].name \
          + Fore.BLACK + " : Total(" + Fore.RED + str(count_sent_chats) + Fore.BLACK + ")"

    # showing sent chats
    if count_sent_chats is not 0 :
        print " Time                                    Secret Message "
        print "=========                               ================="
        for line in temp_sent_list :
            print line


    # showing name and Total sent messages of chosen friend
    print "\n Messages recieved by " + Fore.RED + friend_list[chosen_friend].salutation +" "+ friend_list[chosen_friend].name \
          + Fore.BLACK + " : Total(" + Fore.RED + str(count_recieved_chats) + Fore.BLACK + ")"

    #showing recieved chats
    if count_recieved_chats is not 0 :
        print " Time                                    Secret Message "
        print "=========                               ================="
        for line in temp_recieved_list :
            print line


#-------------------------  function show_chat_history() ends here  ----------------------------------------------------



#-------------------------  function switch_user() starts here  --------------------------------------------------------

# function name : switch_user(), Used to replace/switch Spy [by Default Mr. Bond is selected at the program initiation].

def switch_user() :

    name = raw_input("Could you please tell me your name : ")

    # If spy do not provide his/her name or have invalid characters in name
    if len(name) > 0 and name.isalpha():

        print ("\n Welcome %s. Glad to have you back with us.") % (name)

        salutation = raw_input("What should I call you (Mr. or Ms.): ")

        print "Alright %s %s I'd like to know a little bit more about you before we proceed...\n" % (salutation, name)

        age = input("What is your age? ")
        rating = input("What is your spy rating? ")

        if  5 >= rating >= 4.5:
            print "Proud to have you onboard..."
        elif 4.5 > rating >= 3.5:
            print "Great!! go chat..."
        elif 3.5 > rating >= 2.5:
            print "Good! go learn with your friends... "
        elif 2.5 > rating >= 0:
            print "Sorry! you are not eligible to be a spy"
        else:
            print "Sorry! Please Enter your valid rating"

        spy = Spy(salutation, name, age, rating)

        # redirecting spy to the SPYCHAT
        start_chat(spy)


    else:

        # If spy do not provide his/her name or have invalid characters in name
        message_box("whoa! You don\'t provided your name or may pressed invalid character in name\n Please try again. \n","Oops",  0)


#-------------------------  function switch_user() ends here  ----------------------------------------------------------


#-------------------------  function load_friends() starts here  -------------------------------------------------------

# function name: load_friends(), used to load all the friends data from the friends_database.csv file

def load_friends():

    # opening file friends_database.csv in read mode
    with open('friends_database.csv', "r") as friends_data:
        read_object = csv.reader(friends_data)
        next(read_object)

        for line in read_object:
            spy = Spy(salutation = line[0], name = line[1], age = int(line[2]), rating = float(line[3]))
            friend_list.append(spy)


#-------------------------  function load_friends() ends here  ---------------------------------------------------------



#-------------------------  function load_chats() starts here  ---------------------------------------------------------

# function name: load_friends(), used to load all the friends data to RAM from the friends_database.csv file

def load_chats():

    # opening file chat_database.csv in read mode
    with open('chats_database.csv', "r") as friends_data:
        read_object = csv.reader(friends_data)
        next(read_object)

        for line in read_object:
            temp_spy_name = line[1]
            for friend in friend_list :
                if friend.name == temp_spy_name :

                    hidden_text = line[2]
                    sent_by_me = line[4]
                    time = line[3]
                    new_chat = ChatMessage(hidden_text, sent_by_me,time)

                    friend.chats.append(new_chat)


#-------------------------  function load_chats() ends here  ---------------------------------------------------------



#-------------------------  function miscellaneous_options() starts here  ----------------------------------------------

# function name : Used to provided miscellaneous options to the spy's with rating higher than 4.5
                  #[like deleting friend, deleting chat history, performing MASTER RESET etc.,].

def miscellaneous_options(spy):

    while True:

        print """                MISCELLANEOUS OPTIONS \n========================================================\n                 

                select an option      
                     1. Want to Delete a Friend?
                     2. Want to Clear Chat History of a particular Friend?
                     3. Remove all Friends and Clear Chat History ie., MASTER RESET
                       [Only for spy's whose rating is more than 4.85] 
                     4. Back to Main Menu

        ----------------------- press m anytime for the Main Menu -------------------------"""

        option = raw_input()
        if option == '1':
            # To delete a specific friend
            delete_a_friend()


        elif option == '2':
            # To clear chat history with some specific friend
            clear_specific_chat_history()


        elif option == '3':

            # To perform MASTER RESET [eligibility : spy rating must be greater than 4.85]

            ans = raw_input("Your rating must be greater than or eqaul 4.85 for this Option \n Press y to continue else any key to enter Main Menu... \n")

            if ans.upper() == 'Y':

                # checking spy is eligible or not
                if spy.rating >= 4.85:
                    master_reset()

                else:
                    print "Sorry %s %s. You aren't authorised for these options.\n Entering Main Menu... \n" % (
                    spy.salutation, spy.name)
                    break

            else:
                print "Alright %s %s. \n Entering Miscellaneous Menu... \n" % (spy.salutation, spy.name)




        elif option.upper() == 'M' or option == '4':
            print "\n Entering Main menu... \n"
            break

        else:
            # if spy selected an in valid option
            message_box("whoa! You don\'t provided your name or may pressed invalid character in name\n Please try again. \n","Oops", 0)


#-------------------------  function miscellaneous_options() ends here  ------------------------------------------------



#-------------------------  function delete_a_friend() starts here  ----------------------------------------------------

# function name :delete_a_friend(), Used to remove data of a specific friend from 1)Database File   2)RAM.

def delete_a_friend() :

    # choosing friend to whose is to be deleted from the friend list
    chosen_friend = select_a_friend()

    # deleting chosen friend from database first
    with open('friends_database.csv', "rb") as friends_data, open('output_file.csv', "wb") as edited_friends_data:
        write_object = csv.writer(edited_friends_data)

        for line in csv.reader(friends_data):
            if line[1] != friend_list[chosen_friend].name:
                write_object.writerow(line)
    os.remove('friends_database.csv')
    os.rename('output_file.csv', 'friends_database.csv')

    # Now clearing data of chosen friend from RAM
    print "successfully deleted %s %s's data from the database... \n" %(friend_list[chosen_friend].salutation, friend_list[chosen_friend].name)
    friend_list.pop(chosen_friend)

#-------------------------  function delete_a_friend() ends here  ------------------------------------------------------



#-------------------------  function clear_specific_chat_history() starts here  ----------------------------------------

#function name : clear_specific_chat_history(), Used to remove Chat History of a specific friend from 1)Database File   2)RAM.

def clear_specific_chat_history() :

    # choosing friend to whose chats are to be deleted
    chosen_friend = select_a_friend()

    # deleting chosen friend from database first
    with open('chats_database.csv', "rb") as friends_data, open('output_file.csv', "wb") as edited_friends_data:
        write_object = csv.writer(edited_friends_data)

        for line in csv.reader(friends_data):
            if line[1] != friend_list[chosen_friend].name:
                write_object.writerow(line)
    os.remove('chats_database.csv')
    os.rename('output_file.csv', 'chats_database.csv')

    # Now clearing data of chosen friend from RAM
    friend_list[chosen_friend].chats = []
    print "successfully deleted chats of %s %s's data from the database... \n" % (
    friend_list[chosen_friend].salutation, friend_list[chosen_friend].name)

#-------------------------  function clear_specific_chat_history() ends here  ------------------------------------------



#-------------------------  function master_reset_spy_chat() starts here  ----------------------------------------------

# function name :  master_reset(), It Clears whole friend list data and chat history data from the memory as well as the
                                 #  database files : 1)friend_list.csv, 2)chats_database.csv.
def master_reset() :

    global  friend_list

    # clearing friend list data and chat history data from database files : 1)friend_list.csv,  2)chats_database.csv

    with open('chats_database.csv', "w+"), open('friends_database.csv', "w+"):
        print "successfully performed Master Reset \n Now You don't have Friends and Chat History anymore\n Entering main Menu..."


    # clearing friend list data and chat history data from RAM

    friend_list = []


#-------------------------  function master_reset() ends here  ---------------------------------------------------------





# program started

# lists/variables initialization
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']


print "Hello Spy!"
print 'Let\'s get started'

question = "Do you want to continue as %s %s (y/n)? " % (spy.salutation, spy.name)
existing = raw_input(question)

# If default spy(ie., Mr. Bond) is requesting to be on SPY CHAT
if existing == "Y" or existing == "y" :

    # Showing SPY CHAT MENU if default spy comes to chat
    start_chat(spy)


# if some other spy comes to chat, then save his/her details and redirect to the SPY CHAT MENU
elif existing == "N" or existing == "n" :

    print "Welcome to spy chat"
    switch_user()


else :
    message_box("You provided an invalid input \n Please try again ","Oops",  0)


#========================================  Program Ended  ==============================================================
'''
                                 Function Definitions at a Glance
                                 --------------------------------
                                 

1.  spy_chat()          : It provide a spy chat menu to spy so that spy could select different options.
2.  message_box()       : To alert, or to communicate with spy for other suggetions like invalid enties etc.,  
3.  add_status()        : Used to choose the status of spy from older status or to add new status by appending to older
                          status list.
4.  add_friend()        : To add SPY friends to the CHAT after verifying the provided details.
5.  check_friend_list() : To show the friend list
6.  select_a_friend()   : Used to choose a friend from a list of all Spy friends.
                          [purpose of choosing friend : to chat, view history, removing friend, clear chat, etc.,].   
7.  send_message()      : To send a secret message to other spy friends using steganography
                          [steganography: to encode text into some other files like music, image files]
8.  read_message()      : To read a recieved secret message by decoding it from some other files [like music, image files]                       
9.  check_if_any_sos()  : This function will analyse the secret message If spy tried to send some emergency alert to 
                          thier Friend. 
10. show_chat_history() : To show whole chat history with a particular friend.     
11. switch_user()       : Used to replace/switch Spy [by Default Mr. Bond is selected at the program initiation].
12. load_friends()      : Used to load all the friends data from the database file named as friends_database.csv.
13. load_chats()        : Used to load all the chat history data from the database file named as chats_database.csv.
                          spy authentication,load_friends() and load_chats() comprises build 
14. miscellaneous_options() : Used to provided miscellaneous options to the spy's with rating higher than 4.5
                            [like deleting friend, deleting chat history, performing MASTER RESET etc.,]. 
15. delete_a_friend()   : Used to remove data of a specific friend from 1)Database File   2)RAM.   
16. clear_specific_chat_history()   : Used to remove Chat History of a specific friend from 1)Database File   2)RAM.
17  master_reset()      : It Clears whole friend list data and chat history data from the memory as well as the database
                          files : 1)friend_list.csv, 2)chats_database.csv.
                                   
'''