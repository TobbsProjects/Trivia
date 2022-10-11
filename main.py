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
    def __init__(self, name, id, starting_position):
        self.id = id
        self.name = name
        self.points = 0
        self.first_position = 0
        self.second_position = starting_position
    
    def roll_dice(self):
        dice = random.randrange(1, 7)
        print(f"{self.name} rolls a {dice}")
        upcoming_position = dice + self.first_position

        if upcoming_position > 20:
            self.first_position = upcoming_position - 20
        else:
            self.first_position = upcoming_position

def CreatePlayer(id, starting_position):
    name = input(f"Enter name for player {id}: ")
    Player(name, id, starting_position)



# Karta bestående av 2D-array för varje plats samt inåt. Uppdatera karta med en for loop som kollar hur många tårtbitar, 
# vilken spelare det är som flyttar sig och till vilken array den hör hemma.

playing_field = [
    ["|_ _|", "|_ _|", "|_ _|", "|_ _|", "|_ _|", "|_ _|", "|_ _|", "|_ _|", "|_ _|", "|_ _|", "|_ _|", "|_ _|", "|_ _|", "|_ _|", "|_ _|", "|_ _|", "|_ _|", "|_ _|", "|_ _|", "|_ _|"], 
    ["|_ _|", "|_ _|", "|_ _|"],
    ]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKCYAN = '\033[96m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def ShowMap():
    print(bcolors.OKBLUE, playing_field[0][0], bcolors.OKGREEN, playing_field[0][1], bcolors.OKCYAN, playing_field[0][2], bcolors.WARNING, playing_field[0][3], bcolors.FAIL, playing_field[0][4])
    print(bcolors.FAIL, playing_field[0][19] + "        " + bcolors.FAIL, playing_field[1][0] + "        " + bcolors.OKBLUE, playing_field[0][5])
    print(bcolors.WARNING, playing_field[0][18] + "        " + bcolors.FAIL, playing_field[1][1] + "        " + bcolors.OKGREEN, playing_field[0][6])
    print(bcolors.OKCYAN, playing_field[0][17] + "        " + bcolors.FAIL, playing_field[1][2] + "        " + bcolors.OKCYAN, playing_field[0][7])
    print(bcolors.OKGREEN, playing_field[0][16] + "                      " + bcolors.WARNING, playing_field[0][8])
    print(bcolors.OKBLUE, playing_field[0][15] + "                      " + bcolors.FAIL, playing_field[0][9])
    print(bcolors.FAIL, playing_field[0][14], bcolors.WARNING, playing_field[0][13], bcolors.OKCYAN, playing_field[0][12], bcolors.OKGREEN, playing_field[0][11], bcolors.OKBLUE,playing_field[0][10], bcolors.ENDC)

def MapUpdate(player, first, second):
    playing_field[first][second].replace("|_ _|")
    playing_field[player.first_position][player.second_position].replace(f"|_{player.id}_|")


# Om spelaren står på specifik plats så ska den transport.

# Huvudfunktion för att spela spelet.

def main():
    no_winner = False
    print('Welcome to my Wikipedia trivia game.')
    player_amount = input('How many players are there? (1 - 4) : ')

    if int(player_amount) >= 1:
        player_1 = CreatePlayer(1, 0)
        if int(player_amount) >= 2:
            player_2 = CreatePlayer(2, 4)
            if int(player_amount) >= 3:
                player_3 = CreatePlayer(3, 10)
                if int(player_amount) >= 4:
                    player_4 = CreatePlayer(4, 14)

    else:
        print("That's not a valid choice of players!")
        print("I don't wan't to play anymore.")
        sleep(3)
        quit()

    while no_winner:
        last_seen_11 = player_1.first_position
        last_seen_12 =  player_1.second_position
        MapUpdate(player_1, last_seen_11, last_seen_12)
        ShowMap()
        no_winner = True

main()
# Antal spelare och initiera dessa klasser på ett snyggt sätt presentera dessa i kommandoprompten. Möjligtvis olika färger för varje spelare?
# Skapa spelbrädet med 2D array till en kvadrat i kommandoprompten.
# Placera ut spelarna på brädet via arrayen där klassen hela tiden tar bort och lägger till position i arrayen. Om positionen är tom så skapa en kvadrat av kategorifärg.
