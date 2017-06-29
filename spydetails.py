
from datetime import datetime
class Spy:

    def __init__(self,name,salutation,age,rating):
        self.name=name
        self.salutation= salutation
        self.age = age
        self.rating = rating
        self.is_online= True
        self.chats= []
        self.current_status_message= None

class ChatMsg:

    def __init__(self,message,sent_by_me):
        self.message= message
        self.time= datetime.now()
        self.sent_by_me= sent_by_me
spy=Spy('amit','Mr',22,4.0)
friend_one = Spy('vivek','Mr',20,4.2)
friend_two = Spy('praveen','Mr',21,5)
friend_three = Spy('sakshi','Miss',22,4.0)
friends=[friend_one,friend_two,friend_three]
