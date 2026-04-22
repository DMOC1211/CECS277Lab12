'''
Name: Jacob Miranda & Daniel Puerto
Date: 4/22/26
Group: 10
Description: Creates the game, the user input as to which spy to select, and all the challenges that the spy needs to pass through. 
'''



from sneakyspy import SneakySpy
from hackerspy import HackerSpy

from grappling_hook import GrapplingHook
from goggles import Goggles
from hackingkit import HackingKit
from lockpick import Lockpick
from jetpack import Jetpack

import random
import os


# CHALLENGES 

def cliffside_challenge(spy):
    print("\n=== Cliffside Challenge ===")
    print("A steep rocky cliff blocks your path.")

    if spy.agility() >= 6:
        print("Your agility is high enough — you climb the cliff easily.")
        return True

    print("Your agility is too low. Guess a number from 1 to 5.")
    secret = random.randint(1, 5)

    for attempt in range(1, 4):
        guess = int(input(f"Attempt {attempt}/3 — Enter your guess: "))
        if guess == secret:
            print("Correct! You scale the cliff successfully.")
            return True
        print("Incorrect.")

    print("You failed to climb the cliff.")
    return False


def laser_grid_challenge(spy):
    print("\n=== Laser Grid Challenge ===")
    print("A hallway filled with laser beams blocks your path.")

    if spy.stealth() >= 6:
        print("Your stealth is exceptional — you slip through effortlessly.")
        return True

    print("Your stealth is too low. Memorize the following sequence:")

    directions = ["Up", "Down", "Left", "Right"]
    sequence = [random.choice(directions) for _ in range(4)]

    print(" ".join(sequence))
    input("Press Enter when ready...")

    os.system('cls' if os.name == 'nt' else 'clear')

    user_input = input("Re-enter the sequence (space-separated): ").split()

    if user_input == sequence:
        print("You dodged the lasers successfully!")
        return True

    print("You were hit by the lasers. Mission failed.")
    return False


def vent_shaft_challenge(spy):
    print("\n=== Vent Shaft Challenge ===")
    print("You must crawl quickly through a narrow ventilation shaft.")

    if spy.agility() >= 6:
        print("Your agility allows you to move swiftly through the shaft!")
        return True

    print("Tap Enter 5 times to crawl through the shaft.")
    for i in range(5):
        input(f"Tap {i+1}/5")

    print("You made it through the vent!")
    return True


def security_terminal_challenge(spy):
    print("\n=== Security Terminal Challenge ===")
    print("You must hack the security terminal to open the door.")

    if spy.tech_ability() >= 6:
        print("Your tech ability is high — you hack the terminal instantly!")
        return True

    print("Your tech ability is too low. Guess a 3‑character pattern of X's and O's.")

    pattern = [random.choice(["X", "O"]) for _ in range(3)]

    for attempt in range(1, 4):
        guess = list(input(f"Attempt {attempt}/3 — Enter pattern (e.g., XOX): ").upper())

        if guess == pattern:
            print("Correct! You hacked the terminal.")
            return True

        correct = sum(1 for g, p in zip(guess, pattern) if g == p)
        print(f"Incorrect. {correct} characters are correct.")

    print("You failed to hack the terminal. Mission failed.")
    return False


# SPY SELECTION

def choose_spy():
     #Presents the spy selection menu and returns the constucted spy object

    while True:
        print("\nChoose your Spy:")
        print("1. Sneaky Spy")
        print("2. Hacker Spy")

        choice = input("Enter choice: ")

        if choice == "1":
            return SneakySpy()
        elif choice == "2":
            return HackerSpy()
        else:
            print("Invalid choice. Try again.")


# GADGET SELECTION

def choose_gadgets(spy):

    #Presents the gadget menu twice, each gadget decorates the spy and returns the spy fully decorated

    gadgets = {
        "1": ("Grappling Hook", GrapplingHook),
        "2": ("Goggles", Goggles),
        "3": ("Hacking Kit", HackingKit),
        "4": ("Lockpick", Lockpick),
        "5": ("Jetpack", Jetpack)
    }

    print("\nChoose TWO gadgets for your spy.")

    for _ in range(2):
        while True:
            print("\nAvailable Gadgets:")
            for key, (name, _) in gadgets.items():
                print(f"{key}. {name}")

            choice = input("Enter choice: ")

            if choice in gadgets:
                name, decorator = gadgets.pop(choice)
                spy = decorator(spy)
                print(f"Added {name}!")
                break
            else:
                print("Invalid choice. Try again.")

    return spy


# MAIN GAME LOOP

def main():
    print("=== Welcome to Spy Mission ===")

    spy = choose_spy()
    spy = choose_gadgets(spy)

    print("\nYour Spy Loadout:")
    print(spy)

    print("\n=== Mission Start ===")

    if not cliffside_challenge(spy):
        print("\nMission Failed.")
        return

    if not laser_grid_challenge(spy):
        print("\nMission Failed.")
        return

    if not vent_shaft_challenge(spy):
        print("\nMission Failed.")
        return

    if not security_terminal_challenge(spy):
        print("\nMission Failed.")
        return

    print("\nCongratulations! You completed the mission successfully!")


if __name__ == "__main__":
    main()

