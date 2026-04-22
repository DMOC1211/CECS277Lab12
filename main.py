'''
'''

import random




# Challenge 1: Cliffside

def cliffside_challenge(spy):
    """
    Spy must climb a rocky cliff.
    If agility >= 6 → automatic success.
    Otherwise → 1–5 guessing game with 3 attempts.
    """
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

# Challenge 2: Laser Grid

def laser_grid_challenge(spy):
    """
    Spy must dodge a laser grid.
    If stealth >= 6 → automatic success.
    Otherwise → memorize a 4‑direction sequence.
    """
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


# Challenge 3: Vent Shaft

def vent_shaft_challenge(spy):
    """
    Spy must crawl through a ventilation shaft.
    If agility >= 6 → automatic success.
    Otherwise → tap Enter 5 times.
    """
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


# Challenge 4: Security

def security_terminal_challenge(spy):
    """
    Spy must hack a security terminal.
    If tech ability >= 6 → automatic success.
    Otherwise → guess a 3‑character pattern of X/O with hints.
    """
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
