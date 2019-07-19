import random

def main():
   
   #Rock, Paper, Scissors
    while(True):
        CPU = random.randint(1,3)
        start = input("Choose rock, paper, or scissors(r/p/s):")
        if(CPU == 1 and start == "r"):
            print("Computer chose rock. Tie")
        elif(CPU == 1 and start == "p"):
            print("Computer chose rock. You win!")
        elif(CPU == 1 and start == "s"):
            print("Computer chose rock. You lose.")
        elif(CPU == 2 and start == "r"):
            print("Computer chose paper. Your lose")
        elif(CPU == 2 and start == "p"):
            print("Computer chose paper. Tie")
        elif(CPU == 2 and start == "s"):
            print("Computer chose paper. You win!")
        elif(CPU == 3 and start == "r"):
            print("Computer chose scissors. You Win!")
        elif(CPU == 3 and start == "p"):
            print("Computer chose scissors. You lose")
        elif(CPU == 3 and start == "s"):
            print("Computer chose scissors. Tie")
        else:
            print("Invalid input")
        again = input ("Play again?y/n:")
        if again == "y":
            print (str(start))
        else:
            break
            
                
if __name__=="__main__":
    main()