"""A collection of function for doing my project."""

import time 
import random

#Background Introduction
def Intro():
    
    print("Hello, how are you doing after the long journey? ")
    time.sleep(2)
    print("You are now at Pallet Town，Kanto.")
    time.sleep(2)
    print("A place where is abounded with amazing creatures we call -Pokemon ")
    time.sleep(2)
    print("Here pokemon and people work and live together peacefully")
    time.sleep(2)
    print("I am Professor Oak, a Pokemon researcher. ")
    time.sleep(2.5)
    print("Now it is your time to start your new own adventure.")
    time.sleep(2)
    print("Before you go, I have some gifts for you ")
    time.sleep(2)
    print("I have three adorable Pokemon for you. You can pick one of them as your friend!  ")
    time.sleep(3)
    print()
    


def choosePokemon():#a function that allow user choose a pokemon and store its value
    """   """
    
    Pokemon=""
    while Pokemon != "charmander" and Pokemon != "squirtle" and Pokemon != "bulbasaur":#allow user choose again if the input is not one of the three
        
        Pokemon = input("Which Pokemon would you like to choose (Charmander or Squirtle or Bulbasaur): ")
        Pokemon = Pokemon.lower()#allow user to put lower capital input
       
    return Pokemon 
      
    
def chooseSkill1():#choose a Skill and store the value
    
    Skill1= ""
    while Skill1 !="bubble"and Skill1!= "aqua tail":#choose again if input is not one of two skill
        
        Skill1 = input("Which Skill will you use against? (Bubble or Aqua Tail): ")
        Skill1 = Skill1.lower()  #allow lower case 
    return Skill1

def checkPath1(chosenSkill1):#show the result of choice of skill
    print("OK....")
    time.sleep(2)
    print("if this is your final decision")
    time.sleep(2)
    print("Let's see what will happen")
    print()
    time.sleep(2) 
    
    List_1=["bubble","aqua tail"]
    correctchoice=random.choice(List_1)#allow random choice so that every time the result will be random
    

    if  chosenSkill1 == correctchoice :
        print("Oh, that skill seems super effective.")
        print("The enemy is down, you win your first fight!")
        print("Exp+100, Gold+50")
    else:
        print("What a pity")
        print("You missed!")
        print("The enemy fight back and you lose=_=")  
    

def chooseSkill2():
    """WHAT DOES THIS DO."""
    
    Skill2= ""
    while Skill2!="Ember"and Skill2!="Flame Charge":
        
        Skill2 = input("Which Skill will you use against? (Ember or Flame Charge): ")

    return Skill2    
    
    
def checkPath2(chosenSkill2):
    print("OK....")
    time.sleep(2)
    print("if this is your final decision")
    time.sleep(2)
    print("Let's see what will happen")
    print()
    time.sleep(2) 
    
    List_1=["Ember","Flame Charge"]
    correctchoice=random.choice(List_1)
    

    if  chosenSkill2 == correctchoice :
        print("Oh, that skill seems super effective.")
        print("The enemy is down, you win your first fight!")
        print("Exp+100, Gold+50")
    else:
        print("What a pity")
        print("You missed!")
        print("The enemy fight back and you lose=_=")  
        
        
        
def chooseSkill3():
    Skill3= ""
    while Skill3!="Seed Bomb"and Skill3!="Wine Whip":
        Skill3 = input("Which Skill will you use against? (Seed Bomb or Wine Whip): ")
        
    

    return Skill3    
    
    
def checkPath3(chosenSkill3):
    print("OK....")
    time.sleep(2)
    print("if this is your final decision")
    time.sleep(2)
    print("Let's see what will happen")
    print()
    time.sleep(2) 
    
    List_1=["Wine Whip","Seed Bomb"]
    correctchoice=random.choice(List_1)
    

    if  chosenSkill3 == correctchoice :
        print("Oh, that skill seems super effective.")
        print("The enemy is down, you win your first fight!")
        print("Exp+100, Gold+50")
    else:
        print("What a pity")
        print("You missed!")
        print("The enemy fight back and you lose=_=")  
    