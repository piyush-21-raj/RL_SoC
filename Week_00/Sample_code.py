# The game starts with the player having Capital of $10. There are two games A and B. 
# In game A, a fair coin is tossed. For a Heads, the player gets $1 and the player loses $2 on a Tails
# In game B, if player's Capital is a multiple of 4, they get $2 otherwise they lose $1 

# Simulate the game such that the player gets to choose whether they want to play Game A or Game B at each turn. 
# There are 10 such turns and then the program terminates. 

import numpy as np


Capital = 10

# Function to simulate the game
def gameA():
    toss = np.random.randint(0,2)
    if toss == 0:
        return 1
    else:
        return -2

def gameB():
    if Capital%4 == 0:
        return 2
    else:
        return -1
    
if __name__ == "__main__":
    for i in range(10):
        print(" Current Capital: ", Capital)
        choice = input("Enter A for Game A and B for Game B: ")
        if choice == 'A' or choice == 'a':
            Capital += gameA()
        elif choice == 'B' or choice == 'b':
            Capital += gameB()
        else:
            print("Invalid choice")
            break
    print("Final Capital: ", Capital)
    
