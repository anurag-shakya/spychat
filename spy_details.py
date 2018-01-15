from datetime import datetime

class Spy:
    def __init__(self, salutation, name, age, rating):
        self.salutation = salutation
        self.name = name
        self.age = age
        self.rating = rating
        self.chats = []
        self.is_online = True
        self.current_status_message = None

# CLASS TO STORE THE CHATS
class ChatMessage():
    def __init__(self, hidden_text , sent_by_me):
        self.hidden_text = hidden_text
        self.sent_by_me = sent_by_me
        self.time = datetime.now()



# By Default be will'be countinue with Mr. Bond
spy = Spy('Mr.', 'Bond' , 24, 4.7)

friend_one = Spy( 'Mr.', 'Raja', 27, 4.9)
friend_two = Spy('Ms.', 'Mata Hari', 21, 4.95)
friend_three = Spy('Dr.', 'No', 37, 4.39)

# Total friends
friend_list = [friend_one, friend_two, friend_three]

