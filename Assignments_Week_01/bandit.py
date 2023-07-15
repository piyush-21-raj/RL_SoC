# implementing an epsilon-greedy agent with a 5-armed bandit

from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

EPISODE = 1000
TIME_STEP = 100

def coinToss():
    """a fair toss with a +5/-6 reward"""
    toss=random.rand()
    if(toss >= 0.5):
        return(5.0)
    else:
        return(-6.0)

def poissonDist():
    """a +2 variance Poisson Distributed Reward"""
    reward_poisson=random.poisson(lam=2)
    return(reward_poisson)

def expoDist():
    """a +3 mean Exponential Distributed Reward"""
    reward_expo=random.exponential(scale=3)
    return(reward_expo)

def gaussDist():
    """a (+2,1) Gaussian Distributed Reward"""
    reward_gauss=random.normal(loc=2,scale=1)
    return (reward_gauss)

def crazy():
    """equal chance of getting one of the other 4 buttons"""
    prob=random.rand()
    if (prob < 0.25):
        return(coinToss())
    elif (prob < 0.5):
        return(poissonDist())
    elif (prob < 0.75):
        return(expoDist())
    else:
        return(gaussDist())

def epsGreedy(epsilon):

    df_arr=np.array([]) #store the max mean for every time step
    episode=0 #no of episodes
    while(episode < EPISODE):
        time_steps = 0 #no of time steps
        Bandit=dict(zip([0,1,2,3,4],[[coinToss,0],[poissonDist,0],[expoDist,0],[gaussDist,0],[crazy,0]])) #index : [arms of bandit, number of times they have been called]
        B_mean=[0,0,0,0,0] #assocaites i indexed element to ith key:value pair of Bandit

        while(time_steps < TIME_STEP):
            # stores the index of the greedy/non greedy buttons
            greedy=[]
            not_greedy=[]
            i=0

            # finding the greedy/non greedy buttons
            while (i < len(B_mean)):
                if (B_mean[i] != max(B_mean)):
                    not_greedy.append(i)
                else:
                    greedy.append(i)
                i=i+1


            if (len(greedy) != 5):
                # some estimated means are different 
                chance=random.rand()

                if (chance < epsilon):
                    # exploration into non greedy functions
                    chance1=random.rand()

                    if (chance1 < (1/len(not_greedy))):
                        Bandit[not_greedy[0]][1]=Bandit[not_greedy[0]][1]+1       #increment the number of times that button has been pushed
                        B_mean[not_greedy[0]]= B_mean[not_greedy[0]] + (Bandit[not_greedy[0]][0]() - B_mean[not_greedy[0]])/Bandit[not_greedy[0]][1]
                        #update the mean
                    elif(chance1 < (2/len(not_greedy))):
                        Bandit[not_greedy[1]][1]=Bandit[not_greedy[1]][1]+1 #increment the number of times that button has been pushed
                        B_mean[not_greedy[1]]= B_mean[not_greedy[1]] + (Bandit[not_greedy[1]][0]() - B_mean[not_greedy[1]])/Bandit[not_greedy[1]][1]
                        #update the mean
                    elif(chance1 < (3/len(not_greedy))):
                        Bandit[not_greedy[2]][1]=Bandit[not_greedy[2]][1]+1 #increment the number of times that button has been pushed
                        B_mean[not_greedy[2]]= B_mean[not_greedy[2]] + (Bandit[not_greedy[2]][0]() - B_mean[not_greedy[2]])/Bandit[not_greedy[2]][1]
                        #update the mean
                    elif(chance1 < (4/len(not_greedy))):
                        Bandit[not_greedy[3]][1]=Bandit[not_greedy[3]][1]+1 #increment the number of times that button has been pushed
                        B_mean[not_greedy[3]]= B_mean[not_greedy[3]] + (Bandit[not_greedy[3]][0]() - B_mean[not_greedy[3]])/Bandit[not_greedy[3]][1]
                        #update the mean
                    else:
                        Bandit[not_greedy[4]][1]=Bandit[not_greedy[4]][1]+1 #increment the number of times that button has been pushed
                        B_mean[not_greedy[4]]= B_mean[not_greedy[4]] + (Bandit[not_greedy[4]][0]() - B_mean[not_greedy[4]])/Bandit[not_greedy[4]][1]
                        #update the mean

                else:
                    #exploitation of greedy button
                    if (len(greedy) != 1):
                        # more than one greedy button
                        chance1=random.rand()

                        if (chance1 < (1/len(greedy))):
                            Bandit[greedy[0]][1]=Bandit[greedy[0]][1]+1       #increment the number of times that button has been pushed
                            B_mean[greedy[0]]= B_mean[greedy[0]] + (Bandit[greedy[0]][0]() - B_mean[greedy[0]])/Bandit[greedy[0]][1]
                            #update the mean
                        elif(chance1 < (2/len(greedy))):
                            Bandit[greedy[1]][1]=Bandit[greedy[1]][1]+1 #increment the number of times that button has been pushed
                            B_mean[greedy[1]]= B_mean[greedy[1]] + (Bandit[greedy[1]][0]() - B_mean[greedy[1]])/Bandit[greedy[1]][1]
                            #update the mean
                        elif(chance1 < (3/len(greedy))):
                            Bandit[greedy[2]][1]=Bandit[greedy[2]][1]+1 #increment the number of times that button has been pushed
                            B_mean[greedy[2]]= B_mean[greedy[2]] + (Bandit[greedy[2]][0]() - B_mean[greedy[2]])/Bandit[greedy[2]][1]
                            #update the mean
                        elif(chance1 < (4/len(greedy))):
                            Bandit[greedy[3]][1]=Bandit[greedy[3]][1]+1 #increment the number of times that button has been pushed
                            B_mean[greedy[3]]= B_mean[greedy[3]] + (Bandit[greedy[3]][0]() - B_mean[greedy[3]])/Bandit[greedy[3]][1]
                            #update the mean
                        else:
                            Bandit[greedy[4]][1]=Bandit[greedy[4]][1]+1 #increment the number of times that button has been pushed
                            B_mean[greedy[4]]= B_mean[greedy[4]] + (Bandit[greedy[4]][0]() - B_mean[greedy[4]])/Bandit[greedy[4]][1]
                            #update the mean
                    else:
                        # only one greedy button
                        Bandit[greedy[0]][1]=Bandit[greedy[0]][1]+1       #increment the number of times that button has been pushed
                        B_mean[greedy[0]]= B_mean[greedy[0]] + (Bandit[greedy[0]][0]() - B_mean[greedy[0]])/Bandit[greedy[0]][1]
                        #update the mean
            else:
                # all estimated means are same.
                if (len(greedy) != 1):
                    # more than one greedy button
                    chance1=random.rand()

                    if (chance1 < (1/len(greedy))):
                        Bandit[greedy[0]][1]=Bandit[greedy[0]][1]+1       #increment the number of times that button has been pushed
                        B_mean[greedy[0]]= B_mean[greedy[0]] + (Bandit[greedy[0]][0]() - B_mean[greedy[0]])/Bandit[greedy[0]][1]
                        #update the mean
                    elif(chance1 < (2/len(greedy))):
                        Bandit[greedy[1]][1]=Bandit[greedy[1]][1]+1 #increment the number of times that button has been pushed
                        B_mean[greedy[1]]= B_mean[greedy[1]] + (Bandit[greedy[1]][0]() - B_mean[greedy[1]])/Bandit[greedy[1]][1]
                        #update the mean
                    elif(chance1 < (3/len(greedy))):
                        Bandit[greedy[2]][1]=Bandit[greedy[2]][1]+1 #increment the number of times that button has been pushed
                        B_mean[greedy[2]]= B_mean[greedy[2]] + (Bandit[greedy[2]][0]() - B_mean[greedy[2]])/Bandit[greedy[2]][1]
                        #update the mean
                    elif(chance1 < (4/len(greedy))):
                        Bandit[greedy[3]][1]=Bandit[greedy[3]][1]+1 #increment the number of times that button has been pushed
                        B_mean[greedy[3]]= B_mean[greedy[3]] + (Bandit[greedy[3]][0]() - B_mean[greedy[3]])/Bandit[greedy[3]][1]
                        #update the mean
                    else:
                        Bandit[greedy[4]][1]=Bandit[greedy[4]][1]+1 #increment the number of times that button has been pushed
                        B_mean[greedy[4]]= B_mean[greedy[4]] + (Bandit[greedy[4]][0]() - B_mean[greedy[4]])/Bandit[greedy[4]][1]
                        #update the mean
                else:
                    # only one greedy button
                    Bandit[greedy[0]][1]=Bandit[greedy[0]][1]+1       #increment the number of times that button has been pushed
                    B_mean[greedy[0]]= B_mean[greedy[0]] + (Bandit[greedy[0]][0]() - B_mean[greedy[0]])/Bandit[greedy[0]][1]
                    #update the mean
            df_arr=np.append(df_arr,(max(B_mean))) #add the max mean for the time step
            time_steps=time_steps+1

        episode=episode+1

    df_arr = df_arr.reshape(EPISODE,TIME_STEP) #reshape into a Time Steps*Episode dataframe
    df = pd.DataFrame(df_arr, columns=[f"Time Step {i+1}" for i in range(TIME_STEP)], index=[f"Episode {i+1}" for i in range(EPISODE)]) 
    return (df)


if __name__ == "__main__":
    epsilon1=0
    epsilon2=0.1
    epsilon3=0.01

    time_step=[i+1 for i in range(TIME_STEP)] #x axis of the plots

    df1 = epsGreedy(epsilon1)
    for i in range(EPISODE):
        plt.plot(time_step,df1.iloc[i], "bs")
        plt.xlabel('Time Steps')
        plt.ylabel('Mean Reward')
    # plt.show()

    df2 = epsGreedy(epsilon2)
    for i in range(EPISODE):
        plt.plot(time_step,df2.iloc[i], "r--")
        plt.xlabel('Time Steps')
        plt.ylabel('Mean Reward')
    # plt.show()
    
    df3 = epsGreedy(epsilon3)
    for i in range(EPISODE):
        plt.plot(time_step,df3.iloc[i], "g^")
        plt.xlabel('Time Steps')
        plt.ylabel('Mean Reward')
    # plt.show()
    # uncomment to produce separate plots 
   
    plt.show()
