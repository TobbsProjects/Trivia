import os
import sys
from time import sleep
import random

def clear_sleep():
    if(os.name == 'posix'):
        sleep(2)
        os.system('clear')
    else:
        sleep(2)
        os.system('cls')

def clear():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

# Klass för att lägga till spelare. Upp till 4.
# Namn, poäng/tårtbitar, plats på brädet?, rulla tärning och spara senaste värdet för att placera utt på kartan.

class Player:
    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.points = 0
        self.first_position = 0
        self.second_position = 0
    
    def roll_dice(self):
        dice = random.randrange(1, 7)
        print(f"{self.name} rolls a {dice}")
        upcoming_position = dice + self.first_position

        if upcoming_position > 20:
            self.first_position = upcoming_position - 20
        else:
            self.first_position = upcoming_position

def CreatePlayer(id):
    name = input(f"Enter name for player {id}: ")
    Player(name, id)


# Karta bestående av 2D-array för varje plats samt inåt. Uppdatera karta med en for loop som kollar hur många tårtbitar, 
# vilken spelare det är som flyttar sig och till vilken array den hör hemma.

playing_field = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

# Om spelaren står på specifik plats så ska den transport.

# Huvudfunktion för att spela spelet.

def main():
    print('Welcome to my Wikipedia trivia game.')
    player_amount = input('How many players are there? (1 - 4) : ')

    if int(player_amount) >= 1:
        player_1 = CreatePlayer(1)
        if int(player_amount) >= 2:
            player_2 = CreatePlayer(2)
            if int(player_amount) >= 3:
                player_3 = CreatePlayer(3)
                if int(player_amount) >= 4:
                    player_4 = CreatePlayer(4)

    else:
        print("That's not a valid choice of players!")
        print("I don't wan't to play anymore.")
        sleep(3)
        quit()

    clear()

    while(player_1.points >= 4 or player_2.points >= 4 or player_3.points >= 4 or player_4.points >= 4):
        for(i = 0; i < playing_field.len(); i)

main()
# Antal spelare och initiera dessa klasser på ett snyggt sätt presentera dessa i kommandoprompten. Möjligtvis olika färger för varje spelare?
# Skapa spelbrädet med 2D array till en kvadrat i kommandoprompten.
# Placera ut spelarna på brädet via arrayen där klassen hela tiden tar bort och lägger till position i arrayen. Om positionen är tom så skapa en kvadrat av kategorifärg.
