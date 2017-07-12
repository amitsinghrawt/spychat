 from termcolor import color
#improt the spy detetalis in spydetail libary
from spydetails import spy,Spy,ChatMsg,friends
from datetime import datetime
from steganography.steganography import Steganography
STATUS_MESSAGE =['status1','i am in class','spy is enjoying list!']
#this for to check the given infomation is right or not
def vaildion(spy):
#isalpha is use for check given name in alphabetes
    if (spy.name.isalpha()):

        spy.age = int(raw_input('enter your age'))
        if spy.age > 12 and spy.age < 50:
            spy.rating = float(raw_input("enter your rating"))
            if spy.rating > 4.5:
                print'your are an ace'
            elif spy.rating <= 4.5 and spy.rating > 3.5:
                print 'you are one of the good ones'
            elif spy.rating <= 3.5 and spy.rating > 2.5:
                print 'you can do better'
            else:
                print 'we can always us to help'
            spy_status = True
            print 'authentication  ' + spy.name+ ' age : ' + str(spy.age) + 'rating: ' + str(spy.rating) + 'proudan'

        else:
            print  'sorry! not allow in spy_chat '
    else:
         print "you don't have name"

# read_chat() is use for read old message
def read_chat_history():
    read_for = selcet_friend()
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s]%s%s' % (chat.time.strftime('%d %B %Y'), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)

def send_message():
    friend_choice = selcet_friend()
    original_image = raw_input('what is the name of the image?  ')
    output_path = 'output.jpg'
    text = raw_input('what do you want to say')
    Steganography.encode(original_image, output_path, text)
    new_chat =ChatMsg(text,True)
    friends[friend_choice]['chats'].append(new_chat)
    print 'Your secret message is ready!'

#read_message() is use for read the message of spy
def read_message():
    sender = selcet_friend()#calling selcet_friend funtion
    output_path = raw_input('What is the name of the file')
    secret_text = Steganography.decode(output_path)
    new_chat=ChatMsg(secret_text,True)
    friends[sender]['chats'].append(new_chat)
    print 'Your secret message has been saved'




def selcet_friend():
    item_number = 0
    for friend in friends:
        print '%d. %s. %s. %d. %f' % (item_number + 1, friend.name,friend.salutation,friend.age,friend.rating)
        item_number = item_number + 1
    friend_choice = raw_input('Choose from your friends')
    #now we are choose friend and then we are able to acces him
    friend_choice_position = int(friend_choice) - 1
    return friend_choice_position


#add_status is use for update the status of the spy
def add_status(current_status_message):
    now_status = None
    if current_status_message != None:
        print 'your currrent status is :' + current_status_message
    else:
        print 'you don\'t have any status at this time'
    ques = raw_input('do you want to select status from old status ? y/n :')
    if ques.upper() == 'N':
        new_status = raw_input('enter your status')
        if len(new_status) > 0:
            STATUS_MESSAGE.append(new_status)
            now_status = new_status
    else:
        for i in STATUS_MESSAGE:
            print str(STATUS_MESSAGE.index(i)) + '.' + i
        ques2 = int(raw_input('which status update you want to update'))

        return now_status

        # add_friend fuction is use for add the spy friend in spy with help of dictrony
def add_friend():

    new_friend =Spy('','',0,0.0)
    new_friend.name = raw_input('Please add your friend\'s name :')
    new_friend.salu = raw_input('are they Mr or Miss ? :')
    new_friend.age =int(raw_input('age:'))
    new_friend.rating= float(raw_input('spy rating'))
    if (new_friend.name.isalpha()) and new_friend.age > 12 and new_friend.rating >= spy.rating:
        #add friend into friend list
        friends.append(new_friend)

    else:
        print'Sorry! invalid entry.We can\'t add spy with the detalis you provided '
    return len(friends)


#this funtion is use for starting chat
def start_chat():
    show_menu=True
    while (show_menu):
        menu_choice = 'What do you want to do? \n 1. Add a status update \n 2.Add frinend  \n 3.send  a secrrt message \n 4.read a secret message \n 5.read chat history from a user \n 6. close appliction'
        menu_choice = raw_input(menu_choice)
        menu_choice = int(menu_choice)
        if menu_choice == 1:
            print 'You chose to update the status'
            add_status()#calling add _status funtion
        elif menu_choice == 2:
            add_friend()#calling add _friend funtion
        elif menu_choice == 3:
            send_message()#calling send_message funtion
        elif menu_choice == 4:
            read_message()#calling read_message funtion
        elif menu_choice == 5:
            read_chat_history()#calling read_chat_history  funtion
        elif menu_choice == 6:
            show_menu = False
        else:
            print 'plz enter given choice number'

#this for you are countinue with old spy details Yes or no
question =raw_input('do you want the  countinue yes(Y) or no(N) :')
if (question.upper() =='Y'):
    print 'okey'
    start_chat()
else:
    spy = Spy('', '', 0, 0.0)
    spy.name = raw_input("Enter the name")
    vaildion(spy.name)












