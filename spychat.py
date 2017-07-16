import os
from termcolor import colored
#improt the spy detetalis in spydetail libary
from spydetails import spy,Spy,Chat,friends
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
    read_for = select_a_friend()  # calling the select_a_friend() fucntion and getting the choosen friend
    if read_for == None:
        print colored("Try again :(", "blue")  # if wrong friend choosen then display try again
    else:  # if correct friend choosen then else part run of this function
        if len(friends[read_for].chats) > 0:  # will work if there is any message in chats
            for chat in friends[read_for].chats:  # fetcing chats from friends
                if chat.sent_by_me:  # check if send_by_me is true
                    print colored('[%s] %s %s', "red") % (chat.time.strftime("%d %B %Y"), colored('You said:', 'blue'),chat.message)
                else:
                    print colored('[%s] %s said: %s', 'blue') % (
                    chat.time.strftime("%d %B %Y"), colored(friends[read_for].name, "blue"),
                    chat.message)  # printing time and chat emssage send by spy


def send_message():
    friend_choice = select_a_friend()  # calling the select_a_friend() fucntion and getting the choosen friend
    if friend_choice == None:  # if wrong friend choosen then display try again
        print colored("Try again :(", "blue")
    else:  # if correct friend choosen then else part run of this function

        original_image = raw_input("What is the name of the image?")  # ask name of file
        if os.path.exists(original_image):  # if file exist in os then true
            output_path = "output.jpg"  # giving the path to encoded image
            text = raw_input("What do you want to say? ")  # getting msg to be send
            list = ['SOS', 'SAVE ME', 'HELP ME!']  # creating list for emergency msgs
            if text in list:  # check if text entered is in list
                text = colored("Its an emergency.Reach me as soon as possible", "red")
                Steganography.encode(original_image, output_path, text)  # encoding the image with text
            if len(text) > 0 and len(
                    text) < 100 and text.isspace() == False:  # check if len of text between 1 to 100 and it shouldnt be only spaces
                Steganography.encode(original_image, output_path, text)  # encoding the image with text
                new_chat = Chat(text, True)  # calling Chat class
                friends[friend_choice].chats.append(new_chat)  # appending in chats in friends list
                print colored("Your secret message image is ready!", "green")
            else:
                if len(text) > 100:  # check if spy is talkitive by seeing if he speak more tha 100 words
                    print colored(" You are speaking alot! We are removing you from chat list", "red")
                    del (friends[friend_choice])  # delete the garrulous friend
        else:
            print colored("No such file present!", "red")  # print when file name dont exist


#read_message() is use for read the message of spy
def read_message():
    sender = select_a_friend()  # calling the select_a_friend() fucntion and getting the choosen friend
    if sender == None:
        print colored("Try again :(", "red")  # if wrong friend choosen then display try again
    else:  # if correct friend choosen then else part run of this function

        output_path = raw_input("What is the name of the file?")  # ask name of file

        if os.path.isfile(output_path) == 1:  # if given name is file in os then true
            secret_text = Steganography.decode(output_path)  # decode the txt from image
            if len(secret_text) > 0:  # if there is secret msg in image only then this if true
                new_chat = Chat(secret_text, False)  # Chat class called and secret text stored
                words = secret_text.split() # creating list of words of secret message
                print "your message :%s"%secret_text
                friends[sender].chats.append(new_chat)  # append the message
                print colored("Your secret message has been saved!", "green")  # print when msg saved

            else:
                print colored("there is no secret message in this image", "red")  # print when len of secret msg < 0
        else:
            print colored("No such file present !", "red")  # print when no file present  by the name given by spy


def select_a_friend():
    item_number = 0
    for friend in friends:  # fetching friends from friends list created in spy_details
        print '%d. %s aged %d with rating %.2f is online' % (item_number + 1, friend.name, friend.age, friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")
    if len(
            friend_choice) > 0 and friend_choice.isdigit():  # check if the length if friend choosen is greater than zero and it should be digit
        friend_choice = int(friend_choice)  # converting string to int
        if friend_choice > 0 and friend_choice < item_number + 1:  # check if the choosen friend lie in the list
            friend_choice_position = int(friend_choice) - 1  # index of friend_choice stored in friend_choice_position
            return friend_choice_position  # returned index
        else:
            print colored("Choose friends between (1 - %d)","red") % item_number
            return None
    else:
        print colored("Choose number between (1 - %d)","red") % item_number  # tells that the friend choosen should be in between range
        return None


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
    current_status_message=None
    show_menu=True
    while (show_menu):
        menu_choice = 'What do you want to do? \n 1. Add a status update \n 2.Add frinend  \n 3.send  a secrrt message \n 4.read a secret message \n 5.read chat history from a user \n 6. close appliction'
        menu_choice = raw_input(menu_choice)
        menu_choice = int(menu_choice)
        if menu_choice == 1:
            print 'You chose to update the status'
            current_status_message = add_status(current_status_message)#calling add _status funtion
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