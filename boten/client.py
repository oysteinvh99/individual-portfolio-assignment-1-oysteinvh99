from http import client
import socket
import sys
import time
import threading

from bot3 import callBot
from bot3 import verb




#A list with available bots.
users= ["Chad","Tom","Roar","Willy"]




try:
        IP=sys.argv[1]                                                                                                           #Take out second argument from the command. 
        PORT=int(sys.argv[2])                                                                                                    #Take out third argument from command. 
        if IP!=socket.gethostbyname(socket.gethostname()) or PORT!=5060:                                                         #Check if IP and PORT is correct. Quit the program false. 
            print(f"Wrong IP and/or Port. You must include following arguments. IP: {socket.gethostbyname(socket.gethostname())}, PORT: {5060}" )
            quit()
            
except:
    
        print(f"Your syntax must be: python client.py {socket.gethostbyname(socket.gethostname())} {5060} Botname(optional)")    #If no comand propets is added
        quit()       
     
      
          




                
#Connect the client. 
clientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((IP, PORT))


#Check if user is in the list, and not already taken. 
def checkIfUserValid(user):
    userOK="0"   

    if user in users:                                               #Check if user in Users
        clientSocket.send(user.encode())                        #Send user to the server. The server will check if the bot is taken                  
        userOK=clientSocket.recv(1024).decode()                 #Recive "1" it is avalible and "0" if it is taken.
        if userOK=="0":                                         #Check if taken
            print(f"Bot {user} is taken.")                      #Print that bot is taken       
    else:                                                     
        userOK="0"                                                  #If not existing the userOk=0              
        print(f"Bot {user} does not exist.")                        #Print that bot does not exist.                    
    return userOK                                                   #Return userOK,




try:
    user=sys.argv[3].capitalize()                                                           #Take out 4 argument for command line. If it excist. 
    userEx=checkIfUserValid(user)                                                           #Check if user is one of the avelible bots and not already taken. 
except:
    userEx="0"                                                                              #Sets userEx=0 






while userEx=="0":                                                                          #Run as long as client doesent have an allowed user.
    print(f"Choose a bot: {users[0]}, {users[1]}, {users[2]}, {users[3]} ")
    user=input("User: ").capitalize()                                                       #Take bot name as input
    userEx=checkIfUserValid(user)                                                           #Send user to valid check

#function to pick out the verb from the sentence recived from the host
def pickupverb(msg):                                                                        
    for word in verb:                                                                       #Go through every verb in the verblist
        if word in msg:                                                                     #Check if the string contain the verb
            send=word                                                                       #Put the verb in to send
    
    return send                                                                             #return send


def listen():                                                                                           #Listen function wich allways listen to messegers
    while True: 
        msg = clientSocket.recv(1024).decode()
        if msg=="user":                                                                                 #If server send client "user". A welcome msg is sent.     
            print(f"Welcome to the room {user}!")

        elif msg.startswith("host said:"):                                                              #When a msg starting with host said: the bot will be activated.
            print(msg)                                                                                  #Print msg from the host
            msgsplit=pickupverb(msg)                                                                    #Send msg to pickupverb
            auto_msg=callBot(user,msgsplit)                                                             #Send user and verb to callbot in bot.py, recive a automated sentence in return
            print(f"You said: {auto_msg}")                                                              #Prints out what you said
            clientSocket.send(f"{user} said: {auto_msg}".encode())                                      #Sends the msg to the server who sends it out to the other bots
            time.sleep(0.1)
        elif msg=="Bye, thanks for the conversation":                                                   #When server send bye 
            print(msg)                                                                                  #Print msg
            clientSocket.close                                                                          #Close the server   
            quit()                                                                                      #Quit the program
        elif msg!="":                                                                                   #If msg is something else 
            print(f"{msg}")    
     



listen()                                                                                                #Run listen program. 


