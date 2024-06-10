import random
import time
import os

def clear_console():
    # Clear the console based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def magic_activity_suggester():
    
    activities_low = [
        "Doodle!",
        "Read a light book!",
        "Paint your nails!",
        "Play an easy song!",
        "RomComs!",
        "Listen to music!",
        "Do some deep green!",
        "Learn a new song!",
        "Do some coloring!"
    ]

    
    activities_high = [
        "Do homework!",
        "Practice guitar!",
        "Write to your penpal!",
        "Paint your nails!",
        "Do a puzzle!",
        "Write a story!",
        "Make a sculpture!",
        "Watch a movie!",
        "Work on a moodboard!",
        "Cycle on the machine!",
        "Help cook a meal!",
        "Go for a walk!"
    ]

    clear_console()





    
    question = input("Ask her what to do: ")
    question = input("how many hours of energy do you have left? ")

    
    print("Thinking ", end="", flush=True)

    delay = 6
    # Simulate thinking with a dot added each second
    for _ in range(delay):
        time.sleep(1)
        print(".", end="", flush=True)


    
    
    
    if question == "1": 
      suggestion = random.choice(activities_low)
      print(f"\rSuggester says: {suggestion}     ", end="\n")

    if question == "2": 
       suggestion = random.choice(activities_low or activities_high)
       print(f"\rSuggester says: {suggestion}     ", end="\n")
    
    if question == "3": 
       suggestion = random.choice(activities_high)
       print(f"\rSuggester says: {suggestion}     ", end="\n")
    
    if question not in ["1", "2", "3"]:
       print("\rSuggester says: Don't be silly!     ", end="\n")


    # Simulate thinking with a delay
    time.sleep(4)
    print("\n") 

"""
    question = input("Ask the Suggester what to do: ")
    print("Thinking ...", end="", flush=True)

    # Simulate thinking with a delay
    time.sleep(4)

    suggestion = random.choice(activities)
    print(f"\r Suggester says: {suggestion}", end="\n")

    # Simulate thinking with a delay
    time.sleep(4)
    print("\n")
"""

if __name__ == "__main__":
    magic_activity_suggester()

    magic_activity_suggester()
    magic_activity_suggester()
    magic_activity_suggester()