from numpy import random


# define a "state" class
# which consists of its name, reward, and a list of possible actions from this state
class State:
    def __init__(self, name, reward, distance, actions):
        self.name = name
        self.reward = reward
        self.distance = distance
        self.actions = actions
    
    def __str__(self):
        return self.name

if __name__ == "__main__":
    Cool = State("Cool", [2,1], [2,1], ["Fast", "Slow"])
    Warm = State("Warm", [-10,1], [0,0.5], ["Fast", "Slow"])
    Overheat = State("Overheat", [],[],[])

    current_state = Cool
    total_reward = 0
    total_distance = 0
    states_visited = []

    #take the number and sequence of actions which the user the user wants to perform
    num_my_actions = int(input())
    my_actions = []

    # what actions the user wants to perform, in order of performance
    for i in range(num_my_actions):
        my_actions.append(input())

    print(my_actions)

    #iteratively go through all the actions in order
    for my_action in my_actions:

        # check for overheat
        if current_state != "Overheat": #no overheat

            # check if the action given is possible for the current state
            if my_action not in current_state.actions:
                print("Invalid action")
                break

            # assign the reward based on what action we are going take and the state we are in
            # we can assign reward before checking for final state because the reward depends only on the action we are about to take and is same for all final states
            # same argument hold for distance
            total_reward += current_state.reward[current_state.actions.index(my_action)]
            total_distance += current_state.distance[current_state.actions.index(my_action)]

            if current_state.name != "Warm" : #if current state is Cool
                if my_action != "Slow":
                    rand_select = random.rand()
                    if rand_select > 0.5:
                        current_state = Cool
                    else:
                        current_state = Warm
                else:
                    current_state = Cool
            
            else: #if current state is warm
                if my_action != "Fast":
                    rand_select = random.rand()
                    if rand_select > 0.5:
                        current_state = Cool
                    else:
                        current_state = Warm
                else:
                    current_state = Overheat

        else: #Overheat Condition
            print("Breakdown due to overheat")
            break

        states_visited.append(current_state.name) #make a list of visited states

if current_state != "Overheat":
    print(f"The reward is {total_reward}")
    print(f"The distance travelled is {total_distance}km")
    print(f"The states visited are {states_visited}")