import time
import sys
import os


os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, speed=0.08, newline=True):
    """Affiche le texte lettre par lettre avec une vitesse donnée"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    if newline:
        print() 
def printIntro():
   
    lines = [
        ("So close, no matter how far.", 1.0),
        ("Couldn't be much more from the hearth.", 0.5),
        ("Forever trusting who we are.", 0.5),
        ("Never opened myself this way.", 1.0),
        ("Life is ours, we live it our way.", 1.2),
        ("All these words, I don't just say.", 1.0),
        ("And nothing else matters", 1.1),
        ("")
    ]

    
    typing_speed = 0.1
  
    for text, pause in lines:
        type_text(text, typing_speed)
        time.sleep(pause)


if __name__ == "__main__":
    printIntro()