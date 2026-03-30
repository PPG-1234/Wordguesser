from slow import slow
from random import choice 
from webbrowser import open as troll
def game():
    with open("words.txt", "r") as f:
        data=f.read().split()
    word=choice(data).upper()
    slow("Welcome to the Word Guesser Game!",0.1) 
    slow("You must guess the word, letter by letter.",0.1) 
    slow("You have 6 chances to guess the word.",0.1) 
    slow("Let's begin!",0.1) 
    tries=6
    tab=[]
    for i in word:
        tab.append("_")
    slow(" ".join(tab),0.3) 
    while tries>0:
        slow("guess a letter: ",0.1,end=False)
        guess=input()
        guess=guess.upper()
        if guess in guessed:
            slow("You already guessed that letter.",0.1) 
        elif not(guess.isalpha()) or len(guess)!=1:
            slow("Please enter a single letter.",0.1) 
        elif guess not in word:
            tries-=1
            slow("Wrong guess.",0.1) 
            guessed+=guess
            slow(f"You have {tries} tries left.",0.1) 
        else:
            guessed+=guess
            for i in range(len(word)):
                if word[i]==guess:
                    tab[i]=guess
            slow(" ".join(tab),0.3)
            if "_" not in tab:
                slow ("Congratulations! You guessed the word!",0.1)
                slow("\nYou've earned a special prize!",0.1)
                troll("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                slow("\nNow you can touch some grass!",0.1)
                break
    else:
        slow(f"Game over! The word was {word}.",0.1)
    slow("Do you want to play again?(Y/N): ",0.1,end=False)
    ch=input()
    if ch.upper()=="N":
        slow("Too Bad",0.1) 
        slow("Smell ya later!",0.1) 
    elif ch.upper()=="Y":
        game()
    else:
        slow("Are you Stupid?",0.1) 
game()
        
        
        