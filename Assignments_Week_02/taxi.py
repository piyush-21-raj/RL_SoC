import gymnasium as gym
import numpy as np
import time
import random as rd
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import json

env=gym.make('Taxi-v3', render_mode=None)
# reward_threshold=8, max_episode_steps=200
# action space = Discrete(6)
# observation space = Discrete(500)

# variables
episodeNumber = 1000 #number of episodes run
timesteps=200 #below 200
alpha = 0.53 #learning rate ; keep in the range [0.51,0.56]
gamma = 0.79 #discount factor ; keep in the range [0.78,0.83]
max_epsilon = epsilon = 0.2 #max exploration rate
min_epsilon = 0 #min exploration rate
epsilon_decay_rate = 0.03 #rate of decay of epsilon

num_columns = env.action_space.n
num_rows = env.observation_space.n
qtable = np.zeros((num_rows,num_columns)) #initilizing a Qtable with 0
reward_per_episode=[]

indices = np.arange(episodeNumber/100)
fig,ax = plt.subplots(figsize=(15, 4))

# # Q learning Algorithm
# for epsilon_decay_rate in np.arange(0.02,0.04,0.01):
for currentEpisode in range(episodeNumber):
    state,info =env.reset() #each episode starts fresh, with the PREVIOUS QTABLE INTACT
    done = False #check when to end an episode
    reward_current_episode = 0
    for currentStep in range(timesteps):

        # choosing an action
        if np.random.uniform(0,1) < epsilon :
            # random exploration
            action = env.action_space.sample()
        elif np.max(qtable[state]) > 0 :
            # atleast one state-action pair has a non zero value
            action = np.argmax(qtable[state])
        else:
            # all state-action pairs are 0, so choose any 1
            action = env.action_space.sample()


        # taking the chosen action
        new_state, reward, terminated, truncated, info = env.step(action)
        reward_current_episode += reward
        done = terminated or truncated

        # updating the qvalue
        qtable[state,action] += alpha*(reward + gamma*np.argmax(qtable[new_state]) - qtable[state,action])
        
        # time.sleep(0.1)
        if (done):
            # time.sleep(0.5)
            break

    reward_per_episode.append(reward_current_episode)
    exploration_rate = min_epsilon + (max_epsilon - min_epsilon) * math.exp(-epsilon_decay_rate*currentEpisode)




    # # SARSA Algorithm
    # for currentEpisode in range(episodeNumber):
    #     state,info =env.reset() #each episode starts fresh, with the PREVIOUS QTABLE INTACT
    #     done = False #check when to end an episode
    #     reward_current_episode = 0
    #     for currentStep in range(timesteps):

    #         # choosing an action
    #         if np.random.uniform(0,1) < epsilon :
    #             # random exploration
    #             action = env.action_space.sample()
    #         elif np.max(qtable[state]) > 0 :
    #             # atleast one state-action pair has a non zero value
    #             action = np.argmax(qtable[state])
    #         else:
    #             # all state-action pairs are 0, so choose any 1
    #             action = env.action_space.sample()


    #         # taking the chosen action
    #         new_state, reward, terminated, truncated, info = env.step(action)
    #         reward_current_episode += reward
    #         done = terminated or truncated

    #         # choosing the new action in the new state based on current policy (epsilon greedy)
    #         if np.random.uniform(0,1) < epsilon :
    #             # random exploration
    #             new_action = env.action_space.sample()
    #         elif np.max(qtable[new_state]) > 0 :
    #             # atleast one state-action pair has a non zero value
    #             new_action = np.argmax(qtable[new_state])
    #         else:
    #             # all state-action pairs are 0, so choose any 1
    #             new_action = env.action_space.sample()
        
    #         # updating the qvalue
    #         qtable[state,action] += alpha*(reward + gamma*(qtable[new_state][new_action]) - qtable[state,action])
            
    #         # time.sleep(0.1)
    #         if (done):
    #             # time.sleep(0.5)
    #             break

        # reward_per_episode.append(reward_current_episode)
        # exploration_rate = min_epsilon + (max_epsilon - min_epsilon) * math.exp(-epsilon_decay_rate*currentEpisode)


# plotting the reward vs number_of_episodes
split_arr = np.array_split(reward_per_episode, episodeNumber/100)
averages = [np.mean(part) for part in split_arr]

ax.plot(indices,averages,label=f"aplha:{alpha}   gamma:{gamma}")

# saving the values
table_values = qtable.tolist()
with open('table_values1', 'w') as json_file:
    json.dump(table_values, json_file)

ax.set_xlabel('Episodes (*100)')
ax.set_ylabel('Rewards')
ax.legend()
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))
# plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(150))
plt.show()
plt.savefig("reward_over_episodes.png")