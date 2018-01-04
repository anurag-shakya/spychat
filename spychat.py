
print "Hello Spy!"
print 'Let\'s get started'

spy_name = raw_input("Welcome to spy chat, could you please tell me your name : ")

if len(spy_name) > 0:
    # If spy do not provide his/her name empty

    print ('\n Welcome %s . Glad to have you back with us.') % (spy_name)

    spy_salutation = raw_input("What should I call you (Mr. or Ms.): ")

    spy_name = spy_salutation + ". " + spy_name

    print ("Alright %s I'd like to know a little bit more about you before we proceed...\n") % (spy_name)

    # python is a loosely typed (Duck Typing) programming language
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_age = input("What is your age? ")

    spy_age = int(spy_age)

    # To validate the spy age, whether he/she belongs to age to be a spy.
    if spy_age > 12 and spy_age < 50:

        spy_rating = input("What is your spy rating? ")

        if spy_rating > 4.5 and spy_rating <=5 :
            print 'Great ace!'
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'

        spy_is_online = True

        print ("Authentication complete... \n Welcome %s, age: %d and rating of: %.1f Proud to have you onboard") % (
        spy_name, spy_age, spy_rating)



    else:
        # spy doesn't belongs to the authentic age to be a spy.
        print 'Sorry! your age doesn\'t lie under the age to be a spy'


else:
    # If spy provides his/her name empty
    print "whoa! You don\'t have a name?\n Try again please."