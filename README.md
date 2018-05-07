**Title**: 

Noughts and Crosses

**Team Member(s):**

Aayushi Vora
Saloni Agrawal

**About the code files**

We have added 2 files named
1. Noughts and Crosses.py which contains 4 by 4 tic tac toe code.
2. five_by_five.py which contains 5 by 5 tic tac toe code.

**Introduction:**

Everyone is familiar with the game Noughts and Crosses. We have created a level one Artificial Intelligence Algorithm to determine the best possible moves which could lead to a possible victory. The main focus of our project is to create 3 Aritficial Intelligence Player's with different alogirthms and then to determine that weather the sequence in which the AI's play the game has any impact on winning porabilities of each of them.  We'll be giving a new variation to this game, where the grid will be of 4 by 4 and 5 by 5. However, the number of players will be 3 and the first player to get 3 in a row will win the game.
The symbols which we used for this game are:
X
O
T

****Monte Carlo Simulation Scenario & Purpose:****

The purpose of this project is to determine the probability of winning of each AI in this game of Noughts and Crosses. We will be using basic monte carlo simulation to derive statistical analysis of this simple yet complicated game. Our main purpose of using Monte Carlo Simulation is to determine the most promising next move to increase the probability of winning the game.

****Simulation's variables of uncertainty****

We are trying to simulate a Multiplayer tournament of Noughts and Crosses game. Using Monte-Carlo simulation techniques, we plan to derive the statistics of this simple game scenario.
We are using Randomness in these cases:
1. Order in which AI players will be allowed to play the game.
2. The symbols assigned to each AI player.

By making the order selection random, we have tried to minimise any bias with respect to the general human assumption that the player who goes first has more chances of winning. We definitely think that making this scenario random, we have made a very good representation of reality.

****Strategies to consider for implementing the smartest AI:****

1. Order in which AI will play is random
2. AI will first check if the position is empty and then strategize in this way:
- First the algorithm checks if the smartest AI can win. If yes then make the movement accordingly.
- If there is no such position of winning, the algorithm checks for one step move if any of the other AI player can win. If yes, then the algorithm will move the smartest AI's symbol accordingly to block winning of that player. 
- If both the conditions are not satisfied, algorithm will move AI in one of the centre positions.
- Else, it will move the symbol to one of the 4 corners.
- Else, it will move the symbol to any of the remaining positions.

****Strategies to consider for implementing the smart AI:****

1. Order in which AI will play is random
2. Smart AI will first check if the position is empty and then strategize in this way:
- First the algorithm checks if the smart AI(i.e.,  itself) can win. If yes then make the movement accordingly.
- If there is no such position of winning then the algorithm checks for one step move, i.e., if the smartest AI player can win. If yes, then the algorithm will move the smart AI's symbol accordingly to block winning of the smartest AI player. (Smart AI won't block the winning position of dumb AI, if it is winning the game) .
- If there is no such position mentioned above then the smart AI will look at the position where he can win and If such position exists then it'll make the movement accordingly.
- If both the conditions are not satisfied, algorithm will move AI in one of the centre positions.
- Else, it will move the symbol to one of the 4 corners.
- Else, it will move the symbol to any of the remaining positions.

****Strategies to consider for implementing the dumb AI:****

1. Order in which AI will play is random
2. Dumb AI is not working on any smart alogirthm. It is just playing as follows:
- First the algorithm checks for one step move, i.e., if any of the other AI player can win. If yes, then the algorithm will move the dumb AI's symbol accordingly to block winning of that player. 
- If there is no such position, where other AI's are winning then the dumb AI will look at the position where he can win and If such position exists then it'll make the movement accordingly.
- If both the conditions are not satisfied, algorithm will move AI symbol to one of the 4 corners.
- Else, it will move the symbol to  one of the centre positions.
- Else, it will move the symbol to any of the remaining positions.


****Winning sequences****

There will be in total 24 sequences in which a player can win the game. The sequences are described as follows-

Horizontal sequences

- 1,2,3
- 2,3,4
- 5,6,7
- 6,7,8
- 9,10,11
- 10,11,12
- 13,14,15
- 14,15,16

Vertical sequences

- 1,5,9
- 5,9,13
- 2,6,10
- 6,10,14
- 3,7,11
- 7,11,15
- 4,8,12
- 8,12,16

Diagonal sequences

- 2,7,12
- 1,6,11
- 6,11,16
- 5,10,15
- 4,7,10
- 3,6,9
- 8,11,14
- 7,10,13

****Hypothesis or hypotheses before running the simulation:****

- The winning probability is independent of the order in which the players go. 

**Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes? What are the management decisions one could make from your simulation's output, etc.)**

Based on the above mentioned features, we have calculated the winning probabilities for each player and the probabilities of tie when the game is played n number of times. We have displayed the statistics of these winning probabilities.
However,after simulating the game n number of times, where n depends on the user, we reached to the conclusion that, no matter the order in which players are playing the game,  the probability of winning is only dependent on the alogirthm a player is using, irrespective of it's turn in the game. This proves that our hypothesis was correct which we made during the start of the game.

****Instructions on how to use the program:****

1. Run the Noughts and Crosses.py file. 
2. We have created 2 different files for 4 by 4 and 5 by 5, so choose which file to run,
3. Enter the number of times you want to simulate the game.
4. The output file will show the order in which each player is going in the game, the symbols assigned to each of them, who won the game or was it a tie.
5. The end output holds the statistical analysis of the game which prints the winning percentage of each AI player , percentage of the games which resulted in tie, number of times a particular player went 1 in the game. 

**Conclusions**
After the peer reviews,  we  refined our hypothesis as "The winning probability is independent of the order in which the players go". To test our hypothesis we applied Monte Carlo Simulation in this game. We ran our simulation n number of times(n=1000 in our case. However, once can input this value of n), and obsererved the winning possibilities of each player under each play-order combination of players is different. Hence, we came to a conclusion that winning the game is independent of the order in which you play. 
We have also added doctests for both the python files.

****Note***: 'play-order combination of players' means the combinations of order in which players will play. For instance, 
- Combination 1: smartAI, smartestAI, dumbAI
- Combination2: dumbAI, smartestAI, smartAI 
and so on.*



****All Sources Used:****

https://play.google.com/store/apps/details?id=net.gameswithgravitas.tictactoe
https://int8.io/monte-carlo-tree-search-beginners-guide/
