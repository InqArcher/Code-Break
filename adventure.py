import random
import time
import sys


answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
#cutting down on duplications
required = ("\nUse only A, B, or C\n")


print("         ####################")
print("         #                  #")
print("         #    Code Break    #")
print("         #                  #")
print("         ####################")


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./30)


def game_over():
    slowprint("\nGame over!")
    play_again = input("Would you like to play again? [Y/N]")
    if play_again.lower() == "y":
        start()
    else:
        slowprint("Thanks for playing.")


#Code master last part
def code_battle():
    slowprint("\nUsing the magic of code, the code master "
    "creates a quiz infront of you and says break "
    "the code if you can or get destroyed by my coding "
    "wraith!")
    slowprint("Solve this quiz, otherwise "
    "you are as good as dead!")
    true = ["T", "t", "True"]
    false = ["F", "f", "False"]
    correct = 0  #Storing the correct answers
    name = input ("Adventurer, what is your name?\n")  #Storing the user's name
    print ("\nOK, " +  name +", let's get started. Remember, the following answers are only True or False.")
    time.sleep(2)
    print ("\nThe 5th character in 'Code break' is b.")
    choice = input(">>> ")
    if choice in true:
        correct += 1 #If correct, the user gets one point
    else:
        correct += 0
    print ("\nYou can create an infinite loop in python using a for loop.")
    choice = input(">>> ")
    if choice in false:
        correct += 1
    else:
        correct += 0  
    print ("\nData types consists of string, character, float and boolean ONLY ")
    choice = input(">>> ")
    if choice in false:
        correct += 1
    else:
        correct += 0 
    print ("\nYou're finished, " + name +". You got", correct, "out of 3 correct.")
    if correct >= 2:
        slowprint("As you finish off the last code, it "
        "sends out a shockwave of energy! You are unsure "
        "what you did but it starts to suck all the code "
        "into the middle of the room, as this happens, "
        "you see as the body of the Code Master start to "
        "break apart in strings of different code and be "
        "sucked into the center of the room. You see on "
        "horror as the Code Master struggles to try and "
        "create code to defend himself but its too late "
        "his entire form breaks apart and gets sucked "
        "into the center of the room and disappear in a "
        "shower of luminous code runes.")
        slowprint("\nWell Done Adventurer! You have "
        "survived the Code Break Dungeon and defeated "
        "the Code Master and broken his code!")
    else:
        print("You died!")
        game_over()


def serious_master():
    slowprint("\nWell that gives you an understanding, "
    "I will allow you one more question")
    slowprint("\na. What has this magical code got to do with me?")
    slowprint("b. Oh wise Code Master could you teach me how to code like you?")
    answer= input(">>> ")
    if answer.lower().strip() == "a":
        slowprint("Well! I am glad you asked, you see, "
        "I have identified that you also hold the power "
        "to manipulate code magic and that is how I am "
        "going to crush you! - Prepare to Battle!")
        code_battle()
    elif answer.lower().strip() == "b":
        slowprint("Oh! you wish for me to teach you "
        "how to use my awesome and amazing code magic? "
        "I'll teach you alright! - The Code Master wants "
        "to fight you!")
        code_battle()
    else:
        slowprint("\nyou only have option A and B")
        serious_master()


def codemaster():
    slowprint("\nWe have much to discuss you and I, "
    "the fact that you also hold the power of a coder, "
    "but more about that later, what would you like "
    "to know?...")
    slowprint("a. What are those windows you were looking at?")
    slowprint("b. What is Code? ")
    slowprint("c. What were you looking at in one of the those windows, what are caps?")
    slowprint("d. Oh, I was asked to give you these - You take out the cookies from your pack")
    slowprint("e. What is all this stuff around the room and falling down the walls?")
    slowprint("f. Is your name Willie?")
    answer = input(">>> ")
    if answer.lower().strip() == "a":
        slowprint("These magical screens allow me to "
        "create and manipulate the code, I can break it "
        "down and build it up!, from here I can build "
        "anything I want, those skeletons and zombies you "
        "fought, I created them from using a code language "
        "I like to call the C++, isn't it amazing!")
        codemaster()
    elif answer.lower().strip() == "b":
        slowprint("Of course! you are an uneducated "
        "noob! Code is essentially a magical concept "
        "that I created, it can be used to build things "
        "and be broken down and then used in different "
        "ways. There are several types or languages of "
        "code which are used to make different things, "
        "like those zombies or even the question the "
        "stone gargoyle asked you before you entered my "
        "chambers!")
        serious_master()
    elif answer.lower().strip() == "c":
        slowprint("None of your business! The Code "
        "Master points a finger at you and before "
        "your eyes your body starts to break apart in "
        "the pieces of code and float away")
        slowprint("You Died!")
        game_over()
    elif answer.lower().strip() == "d":
        slowprint("Oh thank you very much! - The Code "
        "Master takes the wrapped up cookies off you and "
        "places them on a table next to him - Where were "
        "we?...Oh yes you were asking me...")
        codemaster()
    elif answer.lower().strip() == "e":
        slowprint("What do you think it is? It is all "
        "the code I have ever written! there are thousands, "
        "if not millions of strings of code running "
        "through this chamber! and I, I created it all!")
        codemaster()
    elif answer.lower().strip() == "f":
        slowprint("How do you... No! No its not! It's "
        "The Code Master! You insolent code noob!")
        serious_master()
    else:
        print("\nChoose from option a, b, c, d, e, f")
        codemaster()


def cm_intro():
    slowprint("\nThe doors are heavy, but you "
    "manage to push them open without much trouble. "
    "As you enter the room you have to stop for a "
    "moment in amazement to take in the sight you see.")
    slowprint("\nIt is a large circler room with a "
    "stone platform in the middle, it shows clear "
    "signs of someone living here, with piles of "
    "books and other nick-knacks strewn around.")
    slowprint("\nBut the most impressive sight is "
    "the magical runes that float down every wall, "
    "in different, luminous colors")
    slowprint("\nYou have never seen the likes of "
    "this before and are almost mesmerized by the "
    "strange, weird yet chillness to the room.")
    slowprint("\nYour attention is then drawn to the "
    "opposite side of the room were you see countless "
    "magical windows with the same runes falling down "
    "them as on the walls")
    slowprint("\nYou notice someone sitting in front "
    "of these magical windows, using their hands to "
    "write the runes on the windows, however on one "
    "of the windows you notice that it has imagines "
    "of some sort of head gear, displayed on peoples "
    "heads called caps? You don't know what these "
    "things are, but as you are staring your attention "
    "is immediately drawn to the person as they say")
    slowprint("\nWelcome Adventurer to my abode! I have been "
    "expecting you! - The figure  then turns around "
    "to reveal a man in wizard robes. He looks rather "
    "frail and pale as if they hadn't been outside "
    "for sometime.")
    slowprint("\nWhat do you think of my magical "
    "code! It is my own creation, it is perfect in "
    "every way, no faults or flaws!")
    codemaster()


def gar_answer():
# Riddle 2 - The Stone Gargoyle
    slowprint("\nAs you make your way further through the dungeon, you think about what Sandra had said to you - if you get past that horrible stone monster..."
    "\nAs you are lost in your thoughts you wander into the next room. You understand right away what Sandra meant by a stone monster, as you see a huge, stone gargoyle standing guard in front of some large double doors. The monster notices you straight away and reaches out with one massive stone, claw and grabs you!"
    "\nThe huge gargoyle brings you close to its face and closely examines you, then says in a loud voice"
    "\n I am the guardian of the Code Master's abode, you may pass if you can answer my riddle, if you can't, I will crush you to dust")
    # The Gargoyles Riddle -
    slowprint("\nA thief wishes to break into a wizards tower, however it only has one entrance and it was guarded by magical stone gargoyle."
    "\nThe Thief watches the entrance to see if they can figure out how to get past the gargoyle."
    "\nA wizard approaches and the gargoyle guardian say to the wizard - 12 and the wizard answers 6 and is let inside the tower."
    "\nThen a second wizard approaches the tower and the gargoyle guarding the entrance asks the wizard - 6 in which the wizard answers 3 and the wizard is allowed to enter the tower."
    "\nConfident the thief has cracked the code, they then approaches the tower when the gargoyle asks them - 10 the thief answers 5 and the gargoyle crushes them."
    "\nMy question to you, adventurer, is; what should the thief have answered?")
    choice = input("\nWhat do you answer the stone gargoyle?\n")
    if choice == "3":
        slowprint("\nThe gargoyle puts you down and you quickly make your way to the double doors and out of that room!")
        cm_intro()
    else:
        slowprint("\nThe gargoyle pauses for a moment as if contemplating your answer - Wrong - he says, Then crushes you to death in his huge claw."
        "\nYou Died")
        game_over()


def more_convo():
    slowprint("\nThe old women moves off and busies herself "
    "with the tea then turns to you - "
    "\nWould you like some tea and a cookie they are "
    "fresh! (yes/no)")
    slowprint("a. yes")
    slowprint("b. no ")
    answer = input(">>> ")
    if answer.lower().strip() == "a":
        slowprint("\nThe old women give you a cup of tea "
        "and a freshly baked cookie, you sit down "
        "with her at an old table and you chat with "
        "her for awhile - My name is Sandra, if you "
        "haven't guessed it already, I'm Willie's "
        "mother, he's a good boy he lets me stay here "
        "and bake him cookies. By the way I presume you "
        "should be on your way to him! If you make it "
        "past that horrible stone monster could you give "
        "my Willie a cookie please. The old women hands "
        "you a several cookies wrapped up. \nYou put them "
        "in your pack. Thank you - the old women says - "
        "off you go then and good luck!")
        slowprint ("You bid the old women farewell and continue on your way.")
        gar_answer()
    elif answer.lower().strip() == "b":
        slowprint("\nThe women shrugs and says - "
        "very well, suit yourself but before you go, "
        "if you manage to get past that horrible stone "
        "monster could you take my willie a cookie their "
        "his favorite! The old women gives you a several "
        "freshly baked cookies wrapped up, you put them "
        "in your pack. Thank you - the old women says - "
        "off you go then and good luck!")
        slowprint ("\nYou bid the old women farewell and continue on your way.")
        gar_answer()
    else:
        slowprint(required)
        more_convo()


# None Player Character (NPC) ENCOUNTER - Sandra
def room_5():
    slowprint("\nYou find yourself walking through " 
    "the dungeons corridor wondering what to "
    "expect next in this crazy place, when you " 
    "come to another room with a strange sight. " 
    "In this large room you see that it is well " 
    "maintained and very clean. "
    "\nAs you make your way into the room you smell "
    "something sweet baking and notice there is a pot "
    "of tea boiling away on a small stove in the far "
    "corner of the room. From these signs someone "
    "must be living here, your on your guard "
    "when you hear a crackly old voice from behind "
    "you!")
    slowprint("\nWho are you?" 
    "\nAre you here to play with my Willie?")
    slowprint("a. yes")
    slowprint("b. no ")
    slowprint("c. who is Willie?")
    answer = input(">>>")
    if answer.lower().strip() == "a":
        slowprint("\nOh right so you know my Willie then, "
        "he gets lots of people coming here to play "
        "with him and his strange magic or code as "
        "he calls it! So serious my Willie is...")
        more_convo()
    elif answer.lower().strip() == "b":
        slowprint("\nThe old women looks at you strangely - "
        "If your not here to play with my willie "
        "what are you here for?... Oh! you must be "
        "one of those adventurer types to put my Willie "
        "in his place! He is so serious of late...")
        more_convo()
    elif answer.lower().strip() == "c":
        slowprint("\nThe old women looks at you funny - "
        "I'm surprised you don't know, my Willie seems "
        "to know lots of people, he gets lots of visitors "
        "now!")
        more_convo()
    else:
        slowprint(required)
        room_5()


def riddle_1():
    global answer
    slowprint("\nAs you continue to follow the dimly lit tunnel, you arrive infront of a doorway.")
    slowprint("You enter a room which seems like it hasn't been used for quite some time.")
    slowprint("The air is heavy and smells musky. Thick layers of dust and cobwebs cover and cling to every surface.")
    slowprint("As you cautiously sneak further into the room, a spectral figure appears infront of you.")
    slowprint("The figure appears to be well dressed, covered with a hooded robe, from head to toe.")
    slowprint("As you approach the figure, it greets you with a bow.")
    slowprint("'Hello there... Human. I am the Ghost Riddler. If you can answer this riddle correctly, you shall be deemed worthy to continue on this journey.'")
    slowprint("\nA foolish man wastes me, the average man spends me, a wise man invests me, yet everyone succumbs to me.")
    answer = input("What am I?\n")
    if answer.lower().strip() == "time":
        slowprint("The Ghost Riddler takes a bow and exclaims - Bravo!!! You may pass, adventurer.")
        room_5()
    else:
        slowprint("The Ghost Riddler looks at you with an amusing look, the says - 'Sorry adventurer, wrong answer. Better luck next time!'")
        slowprint("The ghost reaches out and touches you with a chilling finger, you begin to shiver as your body temperature rapidly drops.")
        slowprint("You collapse, then drift off and the Code Break dungeon claims another adventurer.")
        slowprint("\nYou died.")
        riddle_1()


def zombie_defeated():
    slowprint("Nice, you have taken out two zombies, "
    "only one to go")
    slowprint("\nThe third and last zombies makes " 
    "its way over to you with blood and " 
    "guts dangling from its mouth, "
    "do you attack it or defend yourself?")
    slowprint("a. attack the zombie")
    slowprint("b. defend yourself from the zombie")
    slowprint("c. run away")
    answer = input(">>> ")
    if answer.lower().strip() == "a":
        slowprint("You manage to move quicker than " 
        "the zombie and finish it off before it "
        "manages to react to you!")
        slowprint ("You have defeated the zombies " 
        "and without becoming too much of their snack!")
        riddle_1()
# the next room function
    elif answer.lower().strip() == "b":
        slowprint("you ready yourself for the zombie, " 
        "but as it makes it way over to you, " 
        "it slips on some of the corpses guts and tumbles " 
        "to the floor, you walk over and finish it off "
        "with a clean stroke of your sword.")
        slowprint ("You have defeated the zombies " 
        "and without becoming too much of their snack!")
        riddle_1()
#   the next room function
    elif answer.lower().strip() == "c":
        slowprint("you try to run as quickly as possible, "
        "but the zombie has got you trapped and " 
        "any attack will be too slow")
        slowprint("Welp, it's got you. "
        "\nyou died!")
        game_over()
    else:
        slowprint(required)
        zombie_defeated()


def room_3():
    slowprint ("You make your way forward and notice the " 
    "corridor opens into a room, the sight " 
    "before you makes you slightly wretch.")
    slowprint("You see a corpse in the middle of the room, " 
    "with three zombies kneeing over it and "
    "feasting on the remains, what do you do?")
    slowprint("\nyou attack quickly, and you manage to "
    "take down one of the zombies down before " 
    "another attacks you!")
    slowprint("\nDo you attack the next zombie " 
    "or defend yourself?")
    slowprint("a. attack the zombies")
    slowprint("b. defend yourself against the zombies .")
    slowprint("c. sing a song to the zombies. "
    "maybe they will forgive you")
    answer = input(">>>")
    if answer.lower().strip() == "a":
        slowprint("The zombie is already upon you before "
        "you can react and manages to bite you! " 
        "Looks like your its next meal! ")
        slowprint("\n Welp, they got you. "
        "\n you died!")
        game_over()
    elif answer.lower().strip() == "b":
        slowprint("You manage to defend the attacking zombie "
        "off you, and give yourself space to " 
        "attack back and take out the second zombie!")
        slowprint("two zombies down one more to go")
        zombie_defeated()
    elif answer.lower().strip() == "c":
        slowprint("you sing some justin beiber and the " 
        "zombies go berserk and gain stronger powers "
        "and take you out ")
        slowprint("\nWelp, you have become dinner "
        "\n lol you died!")
        game_over()
    else:
        slowprint(required)
        room_3()


def option():
    slowprint("\nYou travel through the seemingly, never ending twisting and winding tunnels of the dungeon, you turn a corner and you find yourself facing a door."
    "\nAs you cautiously approach, you also notice that there is a large hole in the floor, you take a second to look down the hole and notice there is water at the bottom and a ladder leading up out of the hole?\n")
    choice = input("\nWhat do you do, Inspect the hole or try to open the door?")
    if choice.lower().strip() == "hole":
        slowprint("You look down the hole and see water at the bottom and a ladder on one side coming out of the hole?")
        option2()
    elif choice.lower().strip() == "door":
        slowprint("You try the door, it opens towards you and as soon as you start to walk through, a gust of wind so powerful it knocks you of your feet and you feel yourself falling, then Splash! you are now in the hole, you climb up the ladder soaked to the bone and reassess what to do")
        option2()
    else:
        slowprint("\nWhat are you going to do?")
        option()
def option2():
    choice = input("\nWhat do you do, Inspect the hole or try to open the door?")
    if choice.lower().strip() == "hole":
        slowprint("You look down the hole and see the cold, watery pit, you don't really want to climb out of there again you think")
        option3()
    elif choice.lower().strip() == "door":
        slowprint("You try the door again, but try and hide to one side, it opens towards you, and as soon as you start to move through the door, again, a gust of wind so powerful it knocks you of your feet and you feel yourself falling... Again! Splash! you are in the hole again, you climb up the ladder soaked to the bone and reassess what to do, However, as you drag yourself out of the hole, you notice the door is still open, you then hear a booming voice coming from the open door, it says - How Rude! Didn't anybody teach you to 'knock'? Then the door slams shut.")
        option3()
    else:
        slowprint("\nWhat are you going to do?")
        option2()
#In here make three choices
def option3():
    choice = input("\nWhat do you do, Inspect the hole or try to open the door?")
    if choice.lower().strip() == "hole":
        slowprint("You look down the hole and see the cold, watery pit, you don't really want to climb out of there again you think")
        option3()
    elif choice.lower().strip() == "door":
        slowprint("You try the door again, but try and hide to one side, it opens towards you, and as soon as you start to move into the door, a gust of wind so powerful it knocks you of your feet and you feel yourself falling... Again! Splash! you are now in the hole, you climb up the ladder soaked to the bone and reassess what to do, However, as you drag yourself out of the water pit, you notice the door is still open, you then hear a booming voice come from the open door - How rude! Didn't anybody teach you to 'knock'? Then the door slams shut.")
        option3()
    elif choice.lower().strip() == "knock":
        slowprint("You knock on the door, there is a slight click and the door opens away from you and you pass through the door")
        room_3()
    else:
        slowprint("\nWhat are you going to do?")
        option3()


def guard_1():
    global answer
    slowprint("\nYou leave the cell, following the path into complete darkness.")
    slowprint("You sneak forward, down the twisting, dark and rocky tunnel.")
    slowprint("As you make your way around a corner, you see what seems to be a guard, but something seems off.")
    slowprint("As you look intently at the guard, you notice that its made up only of bones.")
    slowprint("A skeleton guard? Can this be real?")
    slowprint("The skeleton guard hasn't noticed you.")
    slowprint("\nWhat will you do?")
    slowprint("1. Pick up a rock and sneak attack the guard from behind.")
    slowprint("2. Charge at the guard to take it out as fast as possible.")
    answer = input("Make your decision: ")
    if answer.lower().strip() == "1":
        slowprint("You pick up a big rock from the floor and sneak up behind the skeleton guard, you then use the rock to bash it's skull in!")
        slowprint("The skeleton guard crumbles into dust. You can continue safely on your escape from this place.")
        option()
    elif answer.lower().strip() == "2":
        slowprint("You rush forward, trying to take the skeleton guard by surprise, however, it hears you coming and turns to face you.")
        slowprint("The skeleton guard stares into your soul, even with no eyeballs. You prepare to fight.")
        slowprint("\nWhat will you do?")
        slowprint("1. Punch the skeleton guard.")
        slowprint("2. Kick the skeleton guard.")
        answer = input("Make your decision: ")
        if answer.lower().strip() == "1":
            slowprint("You go to punch the skeleton guard. As you punch it in the face, it's head rolls onto the rocky floor.")
            slowprint("To your surprise, the skeleton guard is still standing.")
            slowprint("But not just standing, its now charging towards you.")
            slowprint("\nWhat will you do?")
            slowprint("1. Kick the skeleton guard.")
            slowprint("2. Punch the skeleton guard.")
            answer = input("Make your decision: ")
            if answer.lower().strip() == "1":
                slowprint("You kick the headless skeleton guards leg and it drops to the floor.")
                slowprint("As you stomp on it's chest cavity, the skeleton crumbles to dust. You can continue safely on your escape from this place.")
                option()
            elif answer.lower().strip() == "2":
                slowprint("You punch the headless skeleton guard again, this time in the ribs.")
                slowprint("As you break the ribs of the guard, it crumbles to dust. You can continue safely on your escape from this place.")
                option()
            else:
                ("Choose from option 1 or 2.")
        elif answer.lower().strip() == "2":
            slowprint("You kick the skeleton guards leg and it comes off. The guard falls to the floor.")
            slowprint("As you stomp on the guards back, breaking it, it crumbles to dust. You can continue safely on your escape from this place.")
            option()
    else:
        slowprint("Choose from option 1 or 2.")
        guard_1()


def npc_dialogue():
    global answer
    slowprint("\nIf you have any questions, you can ask me now:")
    slowprint("1. Who are you?")
    slowprint("2. What is this place?")
    slowprint("3. Is there any way out of here?")   # if this option is chosen the player recieves lock pick from the old man which is used to get out of the jail cell.
    slowprint("4. Have you got any food?")
    answer = input("Make your decision: ")
    if answer.lower().strip() == "1":
        slowprint("\nMy name is Crocus, I was the doctor on the pirate ship captained by the King of The Pirates himself, 'Gol D. Roger'. Nice to make your acquaintance.")
        npc_dialogue()
    elif answer.lower().strip() == "2":
        slowprint("\nThis dungeon is legend. Very few get to know of its existence, and those who do, NEVER, live to tell about it. Welcome, adventurer.")
        npc_dialogue()
    elif answer.lower().strip() == "3":
        slowprint("\nDon't wanna stick around? Nobody ever does. Here, take this lockpick. I'm sure you'll be able to crack the lock with it.")
        slowprint("You take the lock pick from the old man. After fiddling around with the lock you hear a click.")
        slowprint("Congratulations! You have successfully opened the cell doors.")
        guard_1()   # go to room 1: skele guard
    elif answer.lower().strip() == "4":
        slowprint("\nFood isn't something we see very often down here. Wherever 'here' is.")
        npc_dialogue()
    else:
        slowprint("Choose from option 1, 2, 3 or 4.")
        npc_dialogue()


def old_man():
    global answer
    answer = input("Make your decision: ")
    if answer.lower().strip() == "1":
        slowprint("You speak with the old man.")
        npc_dialogue()
    elif answer.lower().strip() == "2":
        slowprint("You look around and notice you're locked in a cell at the end of a dark dungeon. Maybe someone can help get us out of here.")
        old_man()
    else:
        slowprint("Choose from option 1 or 2.")
        old_man()


def start():
    answer = input("Would you like to start the game? (yes/no)")
    if answer.lower().strip() == "yes":
        slowprint("\nAs you're waking up you hear a voice.")
        slowprint("'Hello adventurer, welcome to the dungeon.'")
        slowprint("Your head is pounding, you're confused and cold, you start to notice your surroundings. 'Welcome to wh-, where am I?' you mutter to yourself.")
        slowprint("Who are you? What is this place?")
        slowprint("'Patience, adventurer. Any questions you may have, I can surely answer them for you. Just come and speak to me.'")
        slowprint("\nWhat would you like to do?")
        slowprint("1. Speak to the old man.")
        slowprint("2. Take a look around.")
        old_man()
    elif answer.lower().strip() == "no":
        slowprint("Game over.")
        game_over()
    else:
        slowprint("Choose from option 1 or 2.")

start()