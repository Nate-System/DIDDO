#CC is Current Character.
#python "C:\Users\ndixon\Projects\DIDDO\AA Consolidated Functions.py"

import pandas as pd
CC = 1
CS = pd.read_csv(r'C:\Users\ndixon\Projects\DIDDO\CHARACTERLOAD.csv', index_col = 0)

def Startup(CC):
    print('\033[H\033[J', end='')
    print("Who is playing the game right now? Enter 'New' to set up a new character.")
    while True:
        print("To use a existing character, please enter their name or enter 'New' to set up a new character. Here are all of the players currently set up: ")
        for i in CS["NAME"]:
            print(i)
        print("")
        X = str(input())
        if X in CS["NAME"].values:
            CCC = CS[CS['NAME'] == X].index
            CC = CCC[0]
            if CS.loc[CC,"PIN"] == 9999999999:
                print('\033[H\033[J', end='')
                print("Welcome back, " + CS.loc[CC,"NAME"] + ". We're glad you're here.")
                CS.to_csv(r'C:\Users\ndixon\Projects\DIDDO\CHARACTERLOAD.csv')
                return(CC)
            else:
                print('\033[H\033[J', end='')
                if str(CS.loc[CC,"PIN"]) == str(input("What is your PIN? ")):
                    print('\033[H\033[J', end='')
                    print("Welcome back " + CS.loc[CC,"NAME"] + ", we're glad you're here.")
                    CS.to_csv(r'C:\Users\ndixon\Projects\DIDDO\CHARACTERLOAD.csv')
                    return(CC)
                else: 
                    print('\033[H\033[J', end='')
                    print("We're sorry, that is the wrong PIN for " + CS.loc[CC,"NAME"] + ".")
                    continue
        if X == "New":
            print('\033[H\033[J', end='')
            Y = str(input("What would you like to be called? "))
            if Y == "New":
                print('\033[H\033[J', end='')
                print("We're so sorry! We need to keep 'New' reserved for setting up new characters. Can you please pick something else or log in using an existing name?\n\n")
                continue
            if Y in CS["NAME"].values:
                print('\033[H\033[J', end='')
                print("That name is already set up. Please try logging in under that name or use a different name such as " + Y + "123 instead\n\n")
                continue
            else:
                NC = [Y, 9999999999, 0, "they", "them", "their", "theirs", "alters"]
                CC = len(CS)
                CS.loc[len(CS)] = NC
                print('\033[H\033[J', end='')
                print('Hello ' + str(CS.loc[CC,"NAME"]), ", we're so glad you're here!. \nTo set up more options such as a PIN(to protect your account), pronouns, age, etc, please head to Character Setup.\n\n")
#once startup instructions and game tutorial are created, add that here (possibly with the option to bypass it) as new players may not know how to play the game.
                CS.to_csv(r'C:\Users\ndixon\Projects\DIDDO\CHARACTERLOAD.csv')
                return(CC)
        else:
            print('\033[H\033[J', end='')
            print("We don't show anyone with that name right now. Here are all of the players currently set up: \n\n")
            continue

def CharacterPINentry():
    print('\033[H\033[J', end='')
    if CS.loc[CC,"PIN"] == 9999999999:
        CharacterSetup()
    else:
        if CS.loc[CC,"PIN"] == int(input("What is you PIN? ")):
            CharacterSetup()
        else:
            print("Incorrect PIN, please try again.")

def CharacterSetup(): #only call Character Setup via the CharacterPINentry function to make sure that a PIN is entered before editing the character setup.
    print('\033[H\033[J', end='')
    while True:
        print("Select (type into the command field) from the following character options:")
        print("\n'Name' to update your name.")
        print("'PIN' to change your character code.")
        print("'Age' to update your age.")  
        print("'Pronouns' to update your pronouns.")
        print("'Others' to change how we refer to other parts/alters/etc.")
        print("'Quest' to update your preferences on being included in challenges/quests.")
        print("'Triggers' to update what triggers you so it can avoided in quests.")
        print("'Stop' to finish character edits.")
        print("\n(Note: don't worry, you will be able to update any of these options in the future if anything changes.)\n")
        X = str(input()).upper()
        if X == 'STOP':
            print("All of who you are is valid and amazing.")
            print('\033[H\033[J', end='')
            CS.to_csv(r'C:\Users\ndixon\Projects\DIDDO\CHARACTERLOAD.csv')
            break
        elif X == ('NAME'):
            print('\033[H\033[J', end='')
            Y = str(input("What would you like to be called? "))
            if Y == "New":
                print('\033[H\033[J', end='')
                print("We're so sorry! We need to keep 'New' reserved for setting up new characters. Can you please pick something else?\n\n")
            else:
                CS.loc[CC,"NAME"] = Y
                print('\033[H\033[J', end='')
                print('Hello ' + str(CS.loc[CC,"NAME"]), ", we're so glad you're here!.\n\n")
            continue
        elif X == ('PIN'):
            #how to resolve if someone enters anything other than numbers
            if CS.loc[CC,"PIN"] == 9999999999:
                print('\033[H\033[J', end='')
                Y = int(input("What would you like to change your PIN to? "))
                if Y == int(input("Please re-enter PIN ")):
                    CS.loc[CC,"PIN"] = Y
                    print('\033[H\033[J', end='')
                    print("PIN successfully changed to " + str(CS.loc[CC,"PIN"]) + "\n\n")
                    continue
                else:
                    print('\033[H\033[J', end='')
                    print("PIN does not match, please try again.\n\n")
                    continue
            else:
                print('\033[H\033[J', end='')
                if CS.loc[CC,"PIN"] == int(input("What is your current PIN?")):
                    Y = int(input("What would you like to change your PIN to?"))
                    if Y == int(input("Please re-enter PIN")):
                        CS.loc[CC,"PIN"] = Y
                        print('\033[H\033[J', end='')
                        print("PIN successfully changed to " + str(CS.loc[CC,"PIN"]) + "\n\n")
                        continue
                    else:
                        print('\033[H\033[J', end='')
                        print("PIN does not match, please try again.\n\n")
                        continue
                else:
                    print('\033[H\033[J', end='')
                    print("Incorrect PIN, please try again.\n\n")
                    continue
        elif X == ('AGE'):
            #how to resolve if someone enters anything other than numbers
            print('\033[H\033[J', end='')
            CS.loc[CC,"AGE"] = int(input("What is you age? If your age sometimes changes, we generally recommend picking the age you are most likely to be when using this game. You can always change this if you need to.\n"))
            print('\033[H\033[J', end='')
            print("What a great age!\n\n")
            continue
        elif X == ('PRONOUNS'):
            print('\033[H\033[J', end='')
            print("What are your pronouns?")
            print("Select (type into the command field) a number from the following character options to select. For example, if you want neutral (they/them/theirs) pronouns, you would enter 'neutral' (without the quotation marks) and hit enter.")
            print("'Neutral' for they/them/theirs")
            print("'Feminine' for she/her/hers")
            print("'Masculine' for he/him/his")
            print("'Custom' for custom pronouns\n")
            X = str(input()).upper()
            if X == "NEUTRAL":
                CS.loc[CC,"P1"] = 'they'
                CS.loc[CC,"P2"] = 'them'
                CS.loc[CC,"P3"] = 'their'
                CS.loc[CC,"P4"] = 'theirs'
            elif X == "FEMININE":
                CS.loc[CC,"P1"] = 'she'
                CS.loc[CC,"P2"] = 'her'
                CS.loc[CC,"P3"] = 'her'
                CS.loc[CC,"P4"] = 'hers'
            elif X == "MASCULINE":
                CS.loc[CC,"P1"] = 'he'
                CS.loc[CC,"P2"] = 'him'
                CS.loc[CC,"P3"] = 'his'
                CS.loc[CC,"P4"] = 'his'
            elif X == "CUSTOM":
                print("No problem, we'd love to learn your pronouns. We'll go through three scenarios to make sure we will use them correctly.")
                CS.loc[CC,"P1"] = str(input("\nUsing your pronouns, how would you complete the sentence '_____ ate some pizza.'? For example, if your pronouns were feminine, you might enter 'she' for 'She ate some pizza'"))
                CS.loc[CC,"P2"] = str(input("\nUsing your pronouns, how would you complete the sentence 'I got _____ some pizza.'?  For example, if your pronouns were feminine, you might enter 'her' for 'I got her some pizza.'"))
                CS.loc[CC,"P3"] = str(input("\nUsing your pronouns, how would you complete the sentence 'Pepperoni is _____ favorite pizza.'?  For example, if your pronouns were feminine, you might enter 'her' for 'Pepperoni is her favorite pizza."))
                CS.loc[CC,"P4"] = str(input("\nUsing your pronouns, how would you complete the sentence 'That pizza is _____.'?  For example, if your pronouns were feminine, you might enter 'hers' for 'That pizza is hers."))
            else:
                print('\033[H\033[J', end='')
                print("Invalid entry. Please try again.\n\n")
                continue
            print('\033[H\033[J', end='')
            print("Great choice! Your pronouns, '" + str(CS.loc[CC,"P1"]) + "/" + str(CS.loc[CC,"P2"]) + "/" + str(CS.loc[CC,"P3"]) + "/" + str(CS.loc[CC,"P4"]) + "' are awesome. We'll be sure to always use those when referring to you.\n\n")
            continue
        elif X == ('OTHERS'):
            print('\033[H\033[J', end='')
            print("How would you like to refer to other parts/alters/etc in your system? You can use whatever feels comfortable with you, even if it is something a little silly like 'discombobulated spaghetti pillows.'")
            CS.loc[CC,"ALTERS"] = str(input("How do you refer to your parts/alters/etc? "))
            print('\033[H\033[J', end='')
            print("We're excited that you and all of your fellow " + str(CS.loc[CC,"ALTERS"]) + " are here.\n\n")
            continue
        elif X == ('QUEST'):
            print('\033[H\033[J', end='')
            print("Would you like to be included in quests/challenges? Enter 'Yes' or 'No'")
            print("These quests are designed to help you increase you communication and cooperation between yourself and your "  + str(CS.loc[CC,"ALTERS"])+ ".")
            print("Please note that if you say yes to taking part in quests, we recommend that you update your triggers list to ensure that none of the quests that you partcipate in will include any of your triggers.\n")
            X = input().upper()
            if X == "YES":
                CS.loc[CC,"QUEST"] = 1
                print('\033[H\033[J', end='')
                print("You are now set to be included in quests.\n\n")
                continue
            elif X == "NO":
                CS.loc[CC,"QUEST"] = 0
                print('\033[H\033[J', end='')
                print("You are now set to NOT be included in quests.\n\n")
                continue
            else:
                print('\033[H\033[J', end='')
                print("Invalid entry. Please try again.\n\n")
                continue
        elif X == ('TRIGGERS'):
            Triggers()
            continue
        else:
            print('\033[H\033[J', end='')
            print("Invalid entry. Please try again.\n\n")
            continue

def Triggers(): #only call Character Setup via the CharacterSetup function (via CharacterPINentry) to make sure that a PIN is entered before editing the character setup.
    print('\033[H\033[J', end='')
    while True:
        print("Select (type into the command field) from the following trigger options to update their setting:\n")
        print("Stop: to finish trigger edits.")
#how to quickly and easily convert the 0/1 for the triggers in the DataFram to "this is/not a trigger" in the print statements
        print("T1: Dogs are set to " + str(CS.loc[CC,"T1"])) 
        print("T1: Cats are set to " + str(CS.loc[CC,"T2"]))
        print("Stop: to finish trigger edits.")
        print("\n(Note: don't worry, you will be able to update any of these options in the future if anything changes.)\n")
        X = str(input()).upper()
        if X == 'STOP':
            print('\033[H\033[J', end='')
            print("Thank you for taking care of yourself!\n\n")
            CS.to_csv(r'C:\Users\ndixon\Projects\DIDDO\CHARACTERLOAD.csv')
            break
        elif X in CS.columns:
            print('\033[H\033[J', end='')
            print("Would you like this to be marked as a trigger for you? Enter 'Yes' or 'No'")
            print("Marking this as 'Yes' will mean that you will not be included in quests that include this trigger.")
            print("Marking this as 'No' will mean that you can be included in quests that include this trigger.")
            X = input().upper()
            if X == "YES":
                CS.loc[CC,"QUEST"] = 1
                print('\033[H\033[J', end='')
                print("This has been marked as a trigger for you.\n\n")
                continue
            elif X == "NO":
                CS.loc[CC,"QUEST"] = 0
                print('\033[H\033[J', end='')
                print("This has been marked that this is not a trigger for you.\n\n")
                continue
            else:
                print('\033[H\033[J', end='')
                print("Invalid entry. Please try again.\n\n")
                continue
        else: 
            print('\033[H\033[J', end='')
            print("Invalid entry. Please try again.\n\n")
            continue

CC = Startup(CC) #this is how to run the Startup function so that the CC in the function is played back to the global CC variable.
#CharacterPINentry()

print(CS)
print(CC)
