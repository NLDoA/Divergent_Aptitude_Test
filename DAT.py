##Version 0.1 Alpha

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
prompt1 = "what can I do?"
prompt2 = " "
prompt3 = " "
prompt4 = " "

while name == "" or name[0:3].lower() == "dev":
    name = input("What do you wish to be called? ")

if(name.lower() == "developer"):
    developer = True
    print("Developer mode active. :)")

print("Wake up!")
print("'You are going to be late for the aptitude test if you don't wake up!!' you hear your mother yelling from downstairs.\n")

while game == True:
    while prompt1.lower() == "what can I do?" or prompt1.lower() == "change clothes" or prompt1.lower() == "look in your drawers":
        prompt1 = input("What would you like to do while you are in your rooom> ")
        if(prompt1[0:6].lower() == "change"):
            Clothes = "Faction"
            print("You have changed into your birth faction clothes, now you are ready to go to the test.")
        elif(prompt1[0:4].lower() == "look"):
            books = True
            print("You find some books that you were missing for a while in there.")
        elif(prompt1[0:4].lower() == "what"):
            print("You can 'look in your drawers', 'walk downstairs', or 'change clothes'.")
        elif(prompt1[0:4].lower() == "walk"):
            if(Clothes == "Night"):
                print("You are not dressed to go downstairs yet!")
            if(Clothes != "Night"):
                print("Downstairs there is a mirror and a kitchen. You fix your hair and decide that you should eat something. You quickly eat a granola bar, and run to the tests.")
                print("You are not at the aptitude test waiting lobby, and everyone there is anxious for the tests.")
                print("You see some rooms in front of you, only containing a chair and a table with some needles on it.")
                print("One by one, everyone goes into the testing room.")
                print("You hear your name called," + name + "!")
                print("You walk in to the testing room nerviously.")
                print("'The test will now begin. You will be hooked into the computer, and you must complete the challenges to the best of your abitities.', says the tester.")
                print("As the tester gives you the shot to hook you up to the computer, you feel a surge of energy and you enter a room that looks like your cafeteria. You remind yourself that this is just in your head, and nothing can hurt you.")
            
while game == False:
    exit = input("Press enter to exit")
