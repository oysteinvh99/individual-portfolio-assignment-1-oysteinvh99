import random
import socket
from ssl import SOL_SOCKET
import threading
import time

from bot3 import verb


#lister med pålogget bruker

clients = []
users= []

#Server and port
PORT = 5060                                                             
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

#Server setup      
sserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
sserver.bind(ADDR)
sserver.listen(4)


#Broadcaster which sends out msg to the clients, 
def broadcast(msg, sender=None):                                                                        #takes in a msg and a client
    for client in clients:                                                                              #Loops thru the client list
        if client != sender:                                                                       #checks if client is the sender
            time.sleep(0.1)
            client.send(msg.encode())                                                              #Every time that is the case the server sends the msg to that client. 


#Function witch check if new client has choosen a bot who is already taken.
def addUser(client):                                                                               #Add user to the user and client list.
    userOk="0"                                                                                     #Sets userOK to "0"//false
    while userOk=="0":                                                                             #As long as userOK="0" this program will run
        usercheck=client.recv(1024).decode()                                                       #Recive a username from the client.
        userOk = "1"
        if usercheck in users :                                                                    #If user in userlist the bot is taken
            userOk="0"                                                                             #UserOk==false
        if userOk == "0":                                                                          #If userOk=false
            client.send(userOk.encode())                                                           #Server will send back false to the client and client will make sure a new bot is choosen. 
            time.sleep(0.05)
        else:                                                                                      #If not the user is added to the client and user array. And a msg is broadcastet.
            client.send(userOk.encode())                                                           #Send userOk=true to the server
            clients.append(client)                                                                 #Add client to clientlist
            users.append(usercheck)                                                                #Add user to userlist
            msg=(f"{usercheck} joined the room. We har now {len(clients)} in the room.")           #create msg
            broadcast(msg,client)                                                                  #Broadcast msg to the other connected bots that a new bot is connected
            time.sleep(0.05)    
            client.send("user".encode())                                                           #Sends a msg to the client. The client will use this to welcome the new bot to the room.
    
#Function to check if the input from the host is in verblist
def pickupverb(msg):                                                                                 
    send=False                                                                                     #Sets send to false
    for word in verb:                                                                              #Run through every verb in verblist  
        if word in msg:                                                                            #Check if verb is in msg. 
            send=True                                                                              #If thats the case send=true
    return send                                                                                    #Return send



#The function which handels the bots
def theBot():
    connected=True                                                                                                      #Keep the function listening if not told otherwise.
    while connected:
    
        verbcheck=False                                                                                                 #Sets verbcheck to False
        while verbcheck==False:                                                                                         #Run as long as verbcheck is false
            activity=input("What assignment would you suggest to your bots?('Bye' to end) ").lower()                    #Ask the host which activity he wish to suggest today
            verbcheck=pickupverb(activity)                                                                              #Send the input to pickupverb, where the sentence get anlyze
            if verbcheck==False:
                print(f"That activity doesnt excist in my list, can i suggest {random.choice(verb)}")                   #If activity is not in the verblist, another activty will be suggested
      
       
        msg=(f"host said: {activity}")                                                                                  #Create msg
        if activity=="bye":                                                                                             #Check if activity is bye. 
            broadcast("Bye, thanks for the conversation")                                                               #Then the server will broadcast a goodbye msg
            users.clear                                                                                                 #Clear the list
            clients.clear
            sserver.close                                                                                               #Close server
            connected=False                                                                                             #Turn off connected
           

            
        else:
            for client in clients:
                client.send(msg.encode())                                                           #Send activity to clients to activate the bot 
            for client in clients:
                msg = client.recv(1024).decode()                                                    #Recive msg from bot 
                time.sleep(0.15)
                broadcast(msg,client)                                                               #Broadcast recived msg to the clients
                




def connect():                                      #Handles the client
    while len(clients)<4:                           #As long as clients below 4 the server is listening to new bots
        print("[LISTENING...]")
        client , address = sserver.accept()         #Recive client and adress
        addUser(client)                             #Adduser if bot is not taken
        print(f"connect to {address}")              #Print msg if accsepted
        print(len(clients))                         #print number of clients connected
    if len(clients) == 4:                           #When server reach 4 bots the function theBot is activated. 
        thread=threading.Thread(target=theBot)      #Create thread
        thread.start()                              #Start thread
        thread.join()                               
         




connect()                                           #run connect functions