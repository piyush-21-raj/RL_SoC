## The Problem Statement tackled

The file **taxi.py** contains both a *Monte Carlo Q-Learning* and a *TD SARSA* solution. The *Monte Carlo Q-Learning* is a much *better* approach for solving this problem as the environment is *episodic*, *terminal*, and *small sample space*. SARSA is better in opposite cases, where the quicker back-propagation and bootstrapping (which comes at the cost of high variance) is not that benificial. *Exploration* of an unknown space will benefit from *less variance*, which is provied by Monte Carlo (as there is no bootstraping).

## Variable Value selection

**alpha = 0.53 [0.51 - 0.56]**   *learning rate*
This value was selected by looking at the *reward-episode growth graphs* over values ranging from 0.10 to 0.90 insteps of 0.1.
This can be interpreted as *how much weight a particular new information holds over the mean*
The value can be considered ideal because :
    *higher learning rates* leads to more weightage random movements that occurs at the start, leading to an *initially slower learning curve* [as shown by an intially flatter reward-episode graph]
    *lower learning rates* leads to lesser weightage to information, leading to a faster propagation of un-neccesary data (as the negative rewards are more abundant), leading to *slower stabalization of rewards* for future states


**gamma = 0.79 [0.78 - 0.83]**   *discount factor*
This value was selected by looking at the *reward-episode growth graphs* over values ranging from 0.70 to 0.99 insteps of 0.01.
This can be interpreted as *how far the information of one state-action propagates*
The value can be considered ideal because :
    *higher discount factors* leads to higher level propagation of relevant information
    *lower discount factors* leads to lower level propagation of relevant information


**epsilon = 0.2**    *max exploration rate*
This value was selected by looking at the *reward-episode growth graphs* over values ranging from 0.10 to 0.30 insteps of 0.01.
This can be interpreted as *the rate at which agent explores the environment*
The value can be considered ideal because :
    *higher exploration rate* leads to un-neccesary exploration, as the map is relatively small, leading to slower convergence to optimal values (high variance)
    *lower exploration rate* leads to slower exploration


**epsilon_decay_rate = 0.03**   *rate of decay of epsilon*
This value was selected by looking at the *reward-episode growth graphs* over values ranging from 0.01 to 0.05 insteps of 0.01.
This can be interpreted as *how soon should the agent stop exploring*
The value can be considered ideal because :
    *higher decay rate* leads to slower exploration
    *lower decay rate* leads to un-neccesary exploration, as the map is relatively small, leading to slower convergence to optimal values (high variance)