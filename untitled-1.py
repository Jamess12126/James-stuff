import random

def main():
    Randumb = random.randint(1,100)
    tries = 5
    while(tries>0):
        guess = int(input("Guess a number between 1 and 100:"))
        if (guess == Randumb):
            print ("You win!")
            break
        elif (guess > Randumb):
            print ("Your guess is too high")
        elif (guess < Randumb):
            print ("Your guess is too low")
        else:
            print ("The number was "  + str(s))

            
            tries = tries - 1
            print (" Try again. You have " + str(tries) + " tries left")
    if (tries==0):
        print("You Lose")
        
            
                 
if __name__ == "__main__":
    main()
    
