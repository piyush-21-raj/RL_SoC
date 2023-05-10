# The game starts with the player having Capital of $10. There are two games A and B. 

# In game A, Probabilities --> outcomes : 0.505 --> loses $1    0.495 --> wins $1
# In game B, 
# If Capital%3 = 0 , Probabilities --> outcomes : 0.9 --> loses $1    0.1 --> wins $1
# If Capital%3 != 0, Probabilities --> outcomes : 0.25 --> loses $1    0.75 --> wins $1

# Choice betweeen playing Game A or Game B after each round. 
# After 10 rounds, the program terminates.

from numpy import random


def gameA():
    """structure of game A"""
    rand_select = random.rand() #generating a random float between 0 and 1
    if rand_select > 0.505:
        return 1
    else:
        return -1

def gameB():
    """structure of game B"""
    rand_select = random.rand() #generating a random float between 0 and 1
    if Capital%3 != 0:
        if rand_select > 0.25:
            return 1
        else:
            return -1
       
    else:
        if rand_select > 0.9:
            return 1
        else:
            return -1
    
if __name__ == "__main__":
    Capital = 10
    for i in range(10):
        cont=1          #tracks if user wants to play more or not
        print(" Current Capital: ", Capital)
        # ensuring a valid input
        while(True):

            choice = input("\nEnter A for Game A and B for Game B and Q to exit: ")
            
            if choice == 'A' or choice == 'a':
                Capital += gameA()
                break
            elif choice == 'B' or choice == 'b':
                Capital += gameB()
                break
            elif choice == 'Q' or choice == 'q':
                cont=0
                break
            else:
                print("Invalid choice. Enter a valid option")
        
        if cont == 0 :
            break
    print("Final Capital: ", Capital)