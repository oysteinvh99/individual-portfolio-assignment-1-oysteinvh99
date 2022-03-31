import random

from scipy import rand
from sympy import re 







#List of verbs
verb=["play", "watch", "run","sing", "sleep","jump", "visit", "jog", "eat","talk", "walk","bake", "fly", "swim", "cook","skate", "fight", "cry", "bye"]

#Lists of noun
food=["Rice","Pizza","Kebab","Hamburger","Noodles", 
"Tikka Masala", "Pasta Bolognese", "Gyros","Crispy duck"]

tv=["James Bond", "Pirates of the Carribien", "Breaking bad", "prison break", 
"Harry potter", "Inception","Lord of the rings", "Cars", "Narnia"]

play=["football", "basket", "baseball","handball", "Volleyball",
 "Icehockey", "bandy", "boardgame", "playstation"]

totalList={"eat":food ,"watch":tv, "play":play}                                                                                 #Dictanory of noun





        
#First bot
def willy(a): 
    if a in totalList:                                                          #Check if verb is in Dictanory 
        sublist = totalList[a]                                                  #Put the verbs noun in a sublist
        return ("{} is a great suggestion, can we {}"
        " {} ?".format(a+"ing",a ,random.choice(sublist)))                      #Create sentences with the activity and nouns
  

    else:                                                                       #If the verb is not in the Dictanory, a sentence from two list will be picked
        listwithIng =["I think {} sounds great!, what do you think?",
         "Not sure about {}. Don't I get a choice?", "YESS! Time for {}"]       #Sentences using verb+ing
        listnoIng=[ "I would love to {}", "I don`t like to {} ", 
        "I cant`t {} today, maybe another day."]                                #Sentences using the verb in infintive.
        listTot=[listwithIng, listnoIng]
        list=random.choice(listTot)
        if list==listwithIng:                                                   #Check which list that was picked.
            sent=random.choice(list).format(a+ "ing")                           #Add the verb to the sentence and put it in send         
        else:
            sent=random.choice(list).format(a)   
        return sent                                                             #Return sent


def tom(a): 
    if a in totalList:
        sublist = totalList[a]
        return "i would love to {} , can I suggest to {} {} ?".format(a+"ing",a ,random.choice(sublist))
  
    else:
        listwithIng =["{} ? That is a stupid suggestion", "{} is boring", "{} is fun "]
        listnoIng=[" {} did we do last weekend, can we do something else?", 
        "To {} is my favourit activity", "I cant`t today, maybe next weeknd?"]
        listTot=[listwithIng, listnoIng]
        list=random.choice(listTot)
        if list==listwithIng:
            sent=random.choice(list).format(a+ "ing")
        else:
            sent=random.choice(list).format(a)   
        return sent

def roar(a):
    if a in totalList:
        sublist = totalList[a]
        return "I {} {} yesterday".format(a+"ed",random.choice(sublist))    
    else:
        listwithIng =["{} sounds great ", "{}? Thats sounds like a great plan", 
        "I never tried {}, but i would love to try"]
        listnoIng=["I love to {}", "I hate to {}", "To {} is fun"]
        listTot=[listwithIng, listnoIng]
        list=random.choice(listTot)
        if list==listwithIng:
            sent=random.choice(list).format(a+ "ing")
        else:
            sent=random.choice(list).format(a)   
        return sent


def chad(a): 
     if a in totalList:
        sublist = totalList[a]
        return "Yes let's {} {} ".format(a ,random.choice(sublist))
    
     else:
        listwithIng =["{} sounds great, my uncle died while doing it ", 
        "i can`t go {}  today because my siter is sick", "{} was my fathers favourit"]
        listnoIng=["To {} is the funniest thing in the world", "To {} is boring", 
        "Yes please! I want to {}"]
        listTot=[listwithIng, listnoIng]
        list=random.choice(listTot)
        if list==listwithIng:
            sent=random.choice(list).format(a+ "ing")
        else:
            sent=random.choice(list).format(a)   
        return sent




def callBot(inp,activity):                                                         #The clients calls this function and sending in which bot it is and activity
    inp = str(inp).lower()                                                         #Formating to string.
    if inp=="roar":                                                                #Check which bot it is who called on callBot
        return roar(activity)                                                      #Return a sentence with the recived msg
    elif inp=="tom":
        return tom(activity)
    elif inp=="chad":
        return chad(activity)
    elif inp=="willy":
        return willy(activity)
    else:
        return "ingenting"
       