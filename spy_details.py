

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
    def __init__(self, hidden_text , sent_by_me, time):
        self.hidden_text = hidden_text
        self.sent_by_me = sent_by_me
        self.time = time



# By Default be will'be countinue with Mr. Bond
spy = Spy('Mr.', 'Bond' , 24, 4.7)


# Total friends will be loaded automatically from database file : friends_database.csv []
friend_list = []
