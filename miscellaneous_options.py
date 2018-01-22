show_inner_menu = True

while show_inner_menu :

    print """                     SPY CHAT MENU \n========================================================\n                 

    select an option      
           1. Want to delete a friend 
           2. Want to clear chat of particular friend ?
           3. Remove all Friends and Clear chats [for spy's whose rating is more than 4.5] 
           4. Read a Personal Message
           5. Show Chat History with Specific Spy 
           6. Switch User (to change spy)
           7. Exit from Spy chat menu

    ----------------------- press m anytime for the Main Menu -------------------------
          """
    option = raw_input()
    if option == '1':

        print "success! status updated \n Entering Main menu... \n"


    elif option == '2':
        # code to add a spy friend

        print "Now You\'ve a Friend detective(s) \n"

    elif option == '3':
        pass


    elif option.upper() == 'M':
        print "\n Entering Main menu... \n"
        break




    else:
        # if spy selected an in valid option
        print "whoa! You've selected an invalid option.\n Please try again "
