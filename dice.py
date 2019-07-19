#!/usr/bin/env python3

"""
File: dice.py
Name:

Rolls a dice and outputs the result
Concepts covered: Random, printing
"""

import random

def main():
    dice = random.randint(1,6)
   

    roll = input("Type anything to roll a dice:")
    print ("You rolled a " + str(dice))
    while(True):
        dice = random.randint(1,6)
        again = input("Would you like to go again? Yes or No:")
        if ( again == "Yes"):
            print ("You rolled a " + str(dice))
            
            size = input("Would you like your die to be big, stay the same size, or small:")
            if (size == "big"):
                dice = random.randint(1,10)
                print ("You rolled a " + str(dice))
            elif (size == "small"):
                dice = random.randint(1,3)
                print ("You rolled a " + str(dice))
           
                    
        else:
            break

    
if __name__ == "__main__":
    main()
