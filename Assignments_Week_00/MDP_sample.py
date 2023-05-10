# This program simulates a simple MDP

import numpy as np
import random


# define a "state" class
# which consists of its name, reward, and a list of possible actions from this state
class State:
    def __init__(self, name, reward, actions):
        self.name = name
        self.reward = reward
        self.actions = actions
    
    def __str__(self):
        return self.name
    
    

if __name__ == "__main__":
    # Define 5 states Wake Up, Drink Milk, Drink Wine, Study RL, and Play Video Games
    # with their respective rewards as 0, +2, -2, +4 and -2
    # and possible actions from each state

    # Wake Up
    Wake_Up = State("Wake Up", 0, ["Drink Milk", "Drink Wine"])

    # Drink Milk
    Drink_Milk = State("Drink Milk", 2, ["Study RL", "Play Video Games"])

    # Drink Wine
    Drink_Wine = State("Drink Wine", -2, ["Study RL", "Play Video Games"])

    # Study RL
    Study_RL = State("Study RL", 4, ["Wake Up"])

    # Play Video Games
    Play_Video_Games = State("Play Video Games", -2, ["Wake Up"])

    # Take Input as strings of actions each on a new line
    # We start from Wake Up state.

    # Initialize the current state to Wake Up
    current_state = Wake_Up

    # Initialize the total reward to 0
    total_reward = 0

    # Initialize the list of states visited to empty
    states_visited = []

    # Read the input
    # First line is the number of actions
    num_actions = int(input())
    actions = []

    # Read the actions
    for i in range(num_actions):
        actions.append(input())

    print(actions)

    # Iterate over the actions
    for action in actions:
        # Check if the action is valid
        if action not in current_state.actions:
            print("Invalid action")
            break

        # Add the current state to the list of states visited
        states_visited.append(current_state)


        # Update the current state
        if current_state.name == "Wake Up":
            if action == "Drink Milk":
                current_state = Drink_Milk
            elif action == "Drink Wine":
                current_state = Drink_Wine
            else:
                print("Invalid action")
                break
        elif current_state.name == "Drink Milk":
            if action == "Study RL":
                current_state = Study_RL
            elif action == "Play Video Games" :
                current_state = Play_Video_Games
            else:
                print("Invalid action")
                break
        elif current_state.name == "Drink Wine":
            if action == "Study RL":
                current_state = Study_RL
            elif action == "Play Video Games":
                current_state = Play_Video_Games
            else:
                print("Invalid action")
                break
        elif current_state.name == "Study RL":
            if action == "Wake Up":
                current_state = Wake_Up
            else:
                print("Invalid action")
                break
        elif current_state.name == "Play Video Games":
            if action == "Wake Up":
                current_state = Wake_Up
            else:
                print("Invalid action")
                break
        else :
            print("Something went wrong")
            break

        # Update the total reward
        total_reward += current_state.reward


    # Print the total reward
    print("Total Reward:", total_reward)