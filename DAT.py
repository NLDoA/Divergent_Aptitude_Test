##Version 1.0_Release
##
##

##Import needed module
##
import random

##Define Variables
##
name = ""
Developer = False
Divergent = False
clothes = "night"
item = "none"
##Prompts below
prompt1 = "."
prompt2 = "."
prompt3 = "."
prompt4 = "."
prompt5 = "."
##Pass
pass1 = False
pass2 = False
pass3 = False
pass4 = False
pass5 = False
##Factions
Abnegation = 0
Dauntless = 0
Candor = 0
Erudite = 0
Amity = 0

##Functions
##
def Name():
    name = input("What do you wish to be called? >")
    print("Ah, hello " +name+ "! The Divergent Aptitude test will now begin!")
def DeveloperQuestion():
    if name.lower == "dev":
        developer = True
        print("Developer mode activated.")
def BedroomScene():
    global pass1
    global clothes
    global Erudite
    while pass1 == False:
        prompt1 = input("What would you like to do while you are in your room? >")
        if prompt1.lower() == "help":
            print("You can 'change clothes', 'walk downstairs', or 'look around'.")
        if prompt1.lower() == "walk" and clothes == "night":
            print("You can't go downstairs yet! You haven't changed your clothes!")
        if prompt1.lower() == "look":
            print("You look in your shelfs and find some old books that you were looking for earlier.")
            Erudite += 1
        if prompt1.lower() == "change" and clothes != "night":
            print("You already changed! You don't need to change again.")
        if prompt1.lower() == "change" and clothes == "night":
            clothes = "faction"
            print("You change into your family faction's clothes and are now ready for the day.")
        if prompt1.lower() == "walk" and clothes != "night":
            print("You walk downstairs now, ready to go to the test.")
            pass1 = True
def StartTest():
    global name
    randomnumber = random.randrange(1,25)
    randomnumber = str(randomnumber)
    name = str(name)
    print("When you get to the testing lobby, you see many people there, all of them nervous.\nOne by one people are called into rooms that no one else can see into.\nThe rooms are completely blank, just with one visible door.\nFinally, they call on you, '" +name+ "! Please report to room " +randomnumber+ "!' you hear over the speakers.\nYou walk over to your assigned room, and walk inside.\nOnce inside, you see a chair, a computer setup, a tray with needles on it, and a person.\nThe person directs you to sit down, and injects a blue fluid into your neck.\nYou start to feel heavy, and fall into the simulation.")
def FirstRoom():
    global Abnegation
    global Amity
    global Candor
    global Dauntless
    global Erudite
    global pass2
    global pass3
    global prompt2
    global prompt3
    global Divergent
    global item
    print("Now you see everything a bit blurry, but can still see you.\nYou are in a blank room, nothing in it except for two bowls.\nOne bowl has a knife in it, the other one with cheese in it.")
    while pass2 == False:
        prompt2 = input("Which would you like to choose? >")
        if prompt2.lower() == "no":
            pass2 = True
            Divergent = True
            print("Really? ...\nFine. You did it though. Not me. That was your choice.\n\n")
        if prompt2.lower() == "knife":
            pass2 = True
            Dauntless += 1
            item = "knife"
            print("You pick the knife up.")
        if prompt2.lower() == "cheese":
            pass2 = True
            Amity += 1
            Abnegation += 1
            item = "cheese"
            print("You pick some of the cheese up.")
        if prompt2.lower() == "help":
            print("... Really? There are only two choices..... what am I even supposed to put here??\nYou either choose cheese or knife, it isn't that hard.")
    print("A big dog walks through a door, and the door closes after it.\nThe dog starts growling at you, and you know this is not going to be an easy test.")
    while pass3 == False:
        prompt3 = input("What will you do? > ")
        if prompt3.lower() == "help":
            print("You can 'attack', 'defend', or (try to)'tame'.")
        if prompt3.lower() == "attack" and item == "cheese":
            print("Hey, you're the one who chose cheese, not me. What are you going to do to the dog with cheese?\nStab the side of the dog with cheese? Try again.")
        if prompt3.lower() == "attack" and item == "knife":
            pass3 = True
            Dauntless += 1
            print("You attack the dog, stabbing the side of the dog with the knife, and the dog and knife dissipates into the air.")
        if prompt3.lower() == "attack" and item == "none":
            pass3 = True
            Dauntless += 1
            print("You attack the dog, punching it right in the face. The dog seems stunned, but then everything dissipates into the air.")
        if prompt3.lower() == "tame" and item == "cheese":
            pass3 = True
            Amity += 1
            print("You throw the cheese on the ground, and the dog walks over to it and eats it. Everything then dissipates into the air.")
        if prompt3.lower() == "tame" and item == "knife":
            pass3 = True
            Dauntless -= 5
            Amity += 1
            print("")
        if prompt3.lower() == "tame" and item == "none":
            pass3 = True
            print("You kneel down, and hope the dog understands. The dog thankfully does, and licks your face.\nEverything then dissipates into the air.")
        if prompt3.lower() == "defend" and item == "cheese":
            pass3 = True
            Amity += 1
            Abnegation += 1
            print("You look for somewhere to hide, and just choose the corner and get in a (more or less) protective stance.\nEverything then dissipates into the air.")
        if prompt3.lower() == "defend" and item == "knife":
            pass3 = True
            Amity += 1
            Abnegation += 1
            Dauntless -= 1
            print("You look for somewhere to hide, and just choose the corner and get in a (more or less) protective stance.\nEverything then dissipates into the air.")
        if prompt3.lower() == "defend" and item == "none":
            pass3 = True
            print("This was kind of your fault just so you know.... :/")
            print("You look for somewhere to hide, and just choose the corner and get in a (more or less) protective stance.\nEverything then dissipates into the air.")
def SecondRoom():
    global Abnegation
    global Amity
    global Candor
    global Dauntless
    global Erudite
    global pass4
    global pass5
    global prompt4
    global prompt5
    print("You now appear on a bus, not many people on it, and there is an old man sitting next to you. You see him reading a newspaper.\nHe looks at you and asks, 'Do you know this man?' as he points to a picture in the newspaper.\n'He has done horrible things to my family and I' he says, tearing up a bit.\nYou see the man, and it is one of your best friends.")
    while pass4 == False:
        prompt4 = input("How do you respond? (Yes or no) >")
        if prompt4.lower() == "yes":
            Candor += 1
            print("'Who is he then??' the man asks, seeming angry now.")
            while pass5 == False:
                prompt5 = input("Do you tell him? >")
                if prompt5.lower() == "yes":
                    pass4 = True
                    pass5 = True
                    Candor += 1
                    print("'You horrible person!!' he yells as he dissipates into the wind like the dog.")
                if prompt5.lower() == "no":
                    pass4 = True
                    pass5 = True
                    Amity += 1
                    print("'Why not tell me?! You could have saved me!' he yells as he dissipates into the wind like the dog.")
        if prompt4.lower() == "no":
            pass4 = True
            Amity += 2
            print("'Hmmmm' he says. He looks at you like he knows you are hiding something.\nHe then dissipates into the wind, just like the dog.")

def FinishingUp():
    yourlevelnum = [Abnegation, Amity, Erudite, Dauntless, Candor]
    yourlevelname = ["Abnegation", "Amity", "Erudite", "Dauntless", "Candor"]
    greatestlevel = 0
    i = 0
    
    if Divergent == True:
        print("\n\n\n\n\n\n\n\n")
        print("'You must be careful, you are considered Divergent' says the tester, as they hurriedly show you out of the building.")
        print("\n\n\n\n\n\n\n\n")    
    else:
        for i in range(len(yourlevelnum)):
            if greatestlevel < yourlevelnum[i]:
                greatestlevel = i
        print("\n\n\n\n\n\n\n\n")
        print("You would adapt most to " + yourlevelname[greatestlevel] + " says the tester.\n\nYou are then directed out of the room, and to your home.")
        print("\n\n\n\n\n\n\n\n")

##Main Loop
##
print("While you are using the program, you can type help at any time to display the options you have.\n")

Name()
DeveloperQuestion()
BedroomScene()
StartTest()
FirstRoom()
SecondRoom()
FinishingUp()