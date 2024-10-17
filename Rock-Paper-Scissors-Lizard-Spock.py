#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Modules
import time
import random


# Set of choices
actions = ['rock', 'paper', 'scissors', 'lizard', 'spock']


# Function receives choice
def consist(x):
    if x == "help": 
        return("help") 
    elif x in actions:
        return("game on")
    else: 
        raise ValueError("Idiot, your input is invalid")
        
        
# Opponent function spits out randomly selected weapon 
def opponent():
     return random.choice(actions)

    
# Create function for each weapon that returns True if the weapon beats the play and False if it ties or loses
def rock(play):
    if play == "lizard" or play == "scissors": 
        return True 
    if play == "paper" or play == "spock" or play == "rock": 
        return False 
    
def scissors(play):
    if play == "lizard" or play == "paper": 
        return True 
    if play == "scissors" or play == "spock" or play == "rock": 
        return False 
    
def paper(play):
    if play == "lizard" or play == "paper": 
        return True 
    if play == "scissors" or play == "spock" or play == "rock": 
        return False 
    
def lizard(play):
    if play == "spock" or play == "paper": 
        return True 
    if play == "rock" or play == "scissors" or play == "lizard": 
        return False
    
def spock(play):
    if play == "rock" or play == "paper": 
        return True 
    if play == "spock" or play == "scissors" or play == "lizard": 
        return False

    
# Save functions in dictionary
myplays = dict(zip(['rock', 'scissors', 'paper', 'lizard', 'spock'], [rock, scissors, paper, lizard, spock]))


# Gameon function receives dictionary and the two plays
def gameon(myplays, you, comp):
    if you == comp:
        return ('tie', you, comp)
    elif myplays[you](comp):
        return ('you', you, comp)
    else:
        return ('computer', you, comp)


# Hooray dunction takes winner and celebrates them. Receives results from gameon function 
def hooray(result):
    outcome, you, computer = result
    if outcome == "you":
        inspiration = "Hooray, you won!"
    elif outcome == 'computer':
        inspiration = "Oh no, you lost... Better luck next time!"
    elif outcome == 'tie':
        inspiration = "It was a tie. Keep up, you got this!"

    hooraytext = f"""
You choose: {you}
The computer chose: {computer}

{inspiration}
"""
    return hooraytext


# A prompt function takes user input, processes their choice, and repeats until the user types 'stop' to exit
def myprompt():
    x = input("Choose a weapon or stop: >> ")
    x = x.lower()
    if x == 'stop':
        print('\n\nThanks for playing. See you next time!', end = '\n\n')
        return None
    try:
        if consist(x) == 'help':
            myhelp()
            hooray(result)
        else:
            # And this is why using FP is cool:
            print(hooray(gameon(myplays, mythrill(x), opponent())))
    except:
        print("\nThis selection is invalid. Type 'help' to check your options or 'stop' to stop the game.\n")
    myprompt()


# A thriller function
def mythrill(mychoice):
    print('\n\nAlright. ', end = '')
    time.sleep(1)
    print('Now shout with me: ', end = '')
    time.sleep(1)
    print('...Rock...', end = '')
    time.sleep(0.5)
    print('...Paper...', end = '')
    time.sleep(0.5)
    print('...Scissors...', end = '')
    time.sleep(0.5)
    print('...Lizard...', end = '')
    time.sleep(0.5)
    print('...Spock!', end = '\n\n')
    time.sleep(1)
    return mychoice


# A help function
def myhelp():
    myhelpstr = """
This is my Rock-Paper-Scissors-Lizard-Spock game.

You can select among the following weapons:

1. Rock: It wins against Lizard or Scissors (crushes the Lizard and breaks the Scissor)

2. Paper: Wins against Spock or Rock (disproves Spock and wraps the Rock)

3. Scissors: Wins against Lizard and Paper (kills the Lizard or cuts the Paper)

4. Lizard: Wins against Spock and Paper (poisons Spock or eats the Paper)

5. Spock: Wins against Rock and Paper (vaporizes the Rock and smashes the Scissors)

To choose a weapon, just type its name. No need to type in lower or upper case. The prompt is smart 
enough to choose the right action here.

When you are done, you can leave the game by typing 'stop'.

Game on!
"""
    print('\n\n')
    print(myhelpstr, end = '\n\n')
    

myprompt()

