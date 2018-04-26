Create a FORK of this repository to store your code, data, and documentation for the final project. Detailed instructions for this assignment are in the course Moodle site.  The reason I'm asking you to fork this empty repository instead of creating a stand-alone repository is that it will be much easier for me and all students in the course to find all of our projects for code review and for grading. You can even get code review from students in the other section of IS590PR this way.

Even though your fork of this repository shall be public, you'll still need to explicitly add any students on your team as Collaborators in the Settings. That way you can grant them write privileges.

DELETE these lines from TEMPLATE up.

TEMPLATE for your report:

# Title: 
# Noughts and Crosses

## Team Member(s):
Aayushi Vora
Saloni Agrawal

# Introduction
Everyone is familiar with the game Noughts and Crosses. We have created a level one Artificial Intelligence Algorithm using Monte Carlo tree search algorithm method to determine the best possible moves which could lead to a possible victory. The main focus of our project is performing Heuristic Search using Monte Carlos tree search methodology. We’ll be giving a new variation to this game, where the grid will be of 4*4 or 5*5, depending upon the player’s choice. However, the number of players will be 3 and the first player to get 3 in a row will win the game.
The symbols which we used for this game are:
X
O
T

# Monte Carlo Simulation Scenario & Purpose:
The purpose of this project is to determine the probability of winning a multiplayer or a 2 player and an AI player game of Noughts and Crosses. We will be using basic monte carlo simulation to derive statistical analysis of this simple yet complicated game. Our main purpose of using Monte Carlo Simulation is to determine the most promising next move to increase the probability of winning the game.


## Simulation's variables of uncertainty
We are trying to simulate a Multiplayer tournament of Noughts and Crosses game. Using Monte-Carlo simulation techniques, we plan to derive the statistics of this simple game scenario.
We are using Randomness in these cases:
Order in which players will be allowed to play the game.
The move of each human player or AI can or cannot be random .
Tie of all both players and an AI
Making the order selection random, we have tried to minimise any bias with respect to the general human assumption that the player who goes first has more chances of winning. We definitely think that making this scenario random, we have made a very good representation of reality.
If a player is playing the game using some strategy then his moves won’t be random in any case but if a player is just a beginner or has not planned any strategy then his moves are also considered as random moves. 
# Strategies to consider implementing for AI:
Order in which AI will play is random
AI will first check if the position is empty and then strategize in this way:
First the algorithm checks if the AI can win. If yes then make the movement accordingly.
If there is no such position of winning, the algorithm checks for one step move if any of the player can win. If yes, then the algorithm will move the AI symbol accordingly to block winning of that player. 
If both the conditions are not satisfied, algorithm will move AI in one of the centre positions.
Else, it will move the symbol to one of the 4 corners.
Else, it will move the symbol to any of the remaining positions.
# Strategies to consider for players during this game:
1. A player with same knowledge as current AI, and using the same strategy as that of AI. 
Hypothesis:
Should reduce number of ties, but might not improve the winning advantage.
2. Player 2 is adapting with the Player 1’s strategy and his choice history. 
Hypothesis:
Player 2 might have significant advantage over non AI player(Player1). Vice versa can also be applied.


## Hypothesis or hypotheses before running the simulation:

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

## Instructions on how to use the program:

# Strategies to consider for players during this game:

