##Version 0.5 Alpha

name = ""
game = True
Divergent = False
books = False
Knife = False
Cheese = False
No = False
KnowTheMan = False
Clothes = "Night"
Abnegation = 0
Dauntless = 0
Candor = 0
Erudite = 0
Amity = 0
prompt1 = "what"
prompt2 = " "
prompt3 = " "
prompt4 = " "

while name == "":
    name = input("What do you wish to be called? >")
    print("Ah, hello " +name+ "! The Divergent Aptitude test will now begin!")

if(name[0:2].lower() == "dev"):
    developer = True
    print("Developer mode active. :D")
    print("Credits should not show at the end.")

print("'You are going to be late for the aptitude test if you don't wake up!!' you hear your mother yelling from downstairs.\n")

##Main loop below
while game == True:
    while prompt3[0:4].lower != "exit" or prompt2[0:4].lower == "stop" or prompt1[0:4].lower() == "what" or prompt1[0:4].lower() == "help":
        prompt1 = input("What would you like to do while you are in your room? > ")
        if(prompt1[0:6].lower() == "change"):
            Clothes = "Faction"
            print("You changed into your birth faction clothes, now you are ready to go to the test.")
        elif(prompt1[0:4].lower() == "look"):
            books = True
            print("You find some books that you were missing for a while in there.")
        elif(prompt1[0:4].lower() == "what" or prompt1[0:4].lower() == "help"):
            print("You can 'look in your drawers', 'walk downstairs', or 'change clothes'.")
        elif(prompt1[0:4].lower() == "walk" and Clothes == "Night"):
            print("You are not dressed to go downstairs yet!")
        elif(prompt1[0:4].lower() == "walk" and Clothes == "Faction"):
##If you are still in night clothes, you cannot walk downstairs yet.
            if(Clothes != "Night"):
                print("Downstairs there is a mirror and a kitchen. You fix your hair and decide that you should eat something. You quickly eat a granola bar, and run to the tests.")
                print("When you get to the aptitude testing lobby, you look around and see everyone is nervous.")
                print("You see some rooms in front of you, but you can't see inside because there are no windows to see into the room.")
                print("One by one, people are called into rooms")
                print("You hear your name called, " + name + "!")
                print("You walk in to the testing room nervously.")
                print("'The test will now begin. You will be hooked into the computer, and you must complete the challenges to the best of your abilities.' says the tester.")
                print("As the tester gives you the shot to hook you up to the computer, you feel a surge of energy and you enter a room that looks like your cafeteria.\nYou remind yourself that this is just in your head, and nothing can hurt you.")
            while prompt3[0:4].lower != "exit" or prompt2[0:4].lower != "stop" or prompt2 != "Knife" or prompt2 != "Cheese" or prompt2 != "No":
                prompt2 = input("You walk forward and see two baskets sitting on one of the tables. One has some cheese on it, the other has a knife.\nWill you take the knife or the cheese? > ")
                if prompt2[0:2].lower == "no":
                    Divergent == True
                    print("You probably shouldn't have done that...")
                    print("Both the knife and the cheese disappear, and you are left with nothing.\n\a")
                elif prompt2[0:5].lower == "knife":
                    Knife = True
                    Dauntless += 2
                    print("You pick up the knife, and both baskets disappear, along with the cheese.\n\a")
                elif prompt2[0:6].lower == "cheese":
                    Cheese = True
                    Amity += 2
                    Erudite += 1
                    print("You pick up the cheese, and both baskets disappear, along with the knife.\n\a")
                elif prompt2[0:4].lower == "exit" or prompt2[0:4].lower == "stop":
                    game = False

                print("A big dog walks through a door, and the door closes after it.")
                print("The dog starts growling at you, and you know this is not going to be an easy test.")
            
                while prompt3[0:3].lower != "exit" or prompt3[0:3].lower != "stop" or prompt3[0:2].lower != "run" or prompt3[0:5].lower != "attack" or prompt3[0:6].lower != "defend" or prompt3[0:4].lower != "tame":
                    prompt3 = input("What will you do? > ")
                    if prompt3[0:3].lower == "run":
                        Amity += 1
                        print("You lunge at one of the doors, expecting it to open, although it is locked. You must come up with another idea, and quickly too, the dog is advancing on you every second you waste.")
                    elif prompt3[0:3].lower == "help":
                        print("You can type 'run', 'tame', 'defend', or 'attack'.")
                    elif prompt3[0:4].lower == "tame":
                        if Cheese == True:
                            Amity += 2
                            print("The dog is going crazy for the wedge of cheese in your hand. You throw the cheese to the dog, and the dog immediately calms down. A little girls runs up to you, thanks you for finding her dog, and runs away with her dog. You then appear in a bus.")
                        else:
                            Amity += 1
                            print("You lay on the ground and face the dog.\nThe dog backs off because you are showing submission to it.")
                            print("A little girl walks over and pets the dog. 'Thanks for finding my dog for me! I have to go now, but I hope to see you soon!' she says, then runs away with her dog.")
                            print("You then appear in a bus.")
                    elif prompt3[0:6].lower == "defend":
                        Erudite += 1
                        Amity += 1
                        print("You kick over one of the tables, and use it as a shield from the dog.")
                        print("The dog easily jumps over it and you are face to face with the dog.")
                        print("You think you are really in trouble now, but then the dog licks your ear. A little girl walks over and pets the dog. 'Thanks for finding my dog for me! I have to go now, but I hope to see you soon!' she says, then runs away with her dog.")
                        print("You then appear in a bus.")
                    elif prompt3[0:6].lower == "attack":
                        if Knife == True:
                            Dauntless += 2
                            print("You manage to stab the dog right between the eyes. You see a little girl run over to you.\n'Did you do this to my dog?' She says sobbing.\nYou don't respond, but you are very sad that you did that.\nYou remind yourself that you are still in the test. You then appear in a bus.")
                        else:
                            print("You don't have anything to attack with! You better think of something quickly!")
                    elif prompt3[0:4].lower == "exit" or prompt2[0:4].lower == "stop":
                        game = False
            
            print("You are now on a bus, no one is on it except for you and one other person. The other person is reading a newspaper, the cover of the newspaper has a person on it that you seem to remember, but you don't exactly know their name.")
            print("The man on the bus asks 'Do you know this person?' he sounds desperate.")
            
            while prompt4[0:3].lower != "yes" or prompt4[0:2].lower != "no":
                prompt4 = input("How do you respond? Yes or No? > ")
                
                if prompt4[0:3].lower == "yes":
                    Candor += 3
                    print("'Are you sure you know him? This friend of yours has committed some terrible acts of crime against our world!' the man says.")
                elif prompt4[0:2].lower == "no":
                    Amity += 3
                    print("He looks at you as if he knows you are lying, then looks away, sadly.'You could have helped me...' he says.")
                elif prompt4[0:4].lower == "exit" or prompt2[0:4].lower == "stop":
                    game = False
                    
            print("'The test is now over. Your results will be given to you once the effects of the test serum wear off.' says the tester.")
            
            
            if Divergent == True:
                print("'We have some grave news for you... You are divergent' the tester says,\n'You must be careful, because there are many people who want to kill the divergent.'\n'I should not tell you any more, now go.'\nThat is the end of the Divergent Aptitude Test!")
            else:
##This stuff decides what faction you should be in. The faction with the highest points is your suggested faction
                yourlevelnum = [abnegation, amity, erudite, dauntless, candor]
                yourlevelname = ["Abnegation", "Amity", "Erudite", "Dauntless", "Candor"]
                greatestlevel = 0
                i = 0
        
                for i in range(len(yourlevelnum)):
                    if greatestlevel < yourlevelnum[i]:
                        greatestlevel = i
        
                print ("You are " + yourlevelname[greatestlevel] + " says the tester.\n")
                game = False
                
while game == False:
    if developer == False:
        print("Thank you for playing!")
        print("I hope you liked the game")
        print("If you would like to see more of our projects, look us up on GitHub.")
        print("My name is TrueRedShadow, and my organization's name is PlexiShard.")
        print("Please contribute if you can!")
    else:
        print("I hope the game worked. :D")
    exit = input("Press enter to exit")
