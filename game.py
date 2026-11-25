# PS 41 - Text-Based Adventure Game (Simple Version)
# Concepts: Conditions, Loops, Functions, Random

import random   # random module -> used for the monster's random damage

# For testing, change this to 30 (fixed damage). Keep None for random damage.
TEST_DAMAGE = None


# ---------------------------------------------------------
# FUNCTION 1: show_menu()
# Purpose : prints the choices to the player
# ---------------------------------------------------------
def show_menu():
    print("\nYou are in the Forest. Where do you want to go?")
    print("1. Cave")
    print("2. River")
    print("3. Quit")


# ---------------------------------------------------------
# FUNCTION 2: get_choice()
# Purpose : takes input and checks it is 1, 2 or 3
# Uses    : while loop (repeats until input is valid)
#           if condition (checks the input)
# ---------------------------------------------------------
def get_choice():
    while True:
        choice = input("Choice: ")          # input() reads text from the user
        if choice == "1" or choice == "2" or choice == "3":
            return int(choice)              # valid -> convert to number and return
        print("Invalid choice. Enter 1, 2 or 3.")   # invalid -> no health lost


# ---------------------------------------------------------
# FUNCTION 3: cave(health, score)
# Purpose : monster attacks the player; key is found if player survives
# Uses    : random.randint() for damage
#           if condition to check if the player is still alive
# ---------------------------------------------------------
def cave(health, score):
    if TEST_DAMAGE is None:
        damage = random.randint(10, 40)     # random damage between 10 and 40
    else:
        damage = TEST_DAMAGE                # fixed damage (for test cases)

    health = health - damage
    if health < 0:
        health = 0                          # health never goes below 0

    print(f"Cave: Monster attacks! Damage: {damage}. Health: {health}")

    if health > 0:                          # player survived
        score = score + 20
        print("You found a key! Score:", score)

    return health, score                    # send updated values back


# ---------------------------------------------------------
# FUNCTION 4: river(health, score)
# Purpose : player finds a treasure (+50 score)
# ---------------------------------------------------------
def river(health, score):
    score = score + 50
    print("River: You found a treasure! Score:", score, "| Health:", health)
    return health, score


# ---------------------------------------------------------
# FUNCTION 5: play_game()
# Purpose : main game, controls everything
# Uses    : while loop (runs until Health is 0 or player quits)
#           if / elif / else (decides which place to visit)
#           show_menu(), get_choice(), cave(), river()
# ---------------------------------------------------------
def play_game(health=100, score=0):
    print("=== Text-Based Adventure Game ===")
    print("Health:", health, "| Score:", score)

    while health > 0:                       # loop until health becomes 0
        show_menu()                         # calls Function 1
        choice = get_choice()               # calls Function 2

        if choice == 1:
            health, score = cave(health, score)    # calls Function 3
        elif choice == 2:
            health, score = river(health, score)   # calls Function 4
        else:                                      # choice == 3
            print("You left the adventure. Final score:", score, "| Health:", health)
            return

    # reaches here only when health is 0
    print("Game Over! Final score:", score)


# Program starts here
play_game()
