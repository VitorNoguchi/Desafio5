# Masteming_GAME

This is the repository to play the Mastermind game. The game consists in a pattern of 4 random digitis and the player (codebreaker) needs to guess the pattern, in both digits and order, within 10 moves. Each move the codebreaker inputs his guess and gets the feedback, returning '1' for each correct digit in the correct location and '0' for each correct digit in the wrong location.

In its current form, the code is meant to be executed in Python 3, it's necessary to have the python libraries within the code and the MongoDB installed. 

*Don't have MongoDB?* check https://docs.mongodb.com/manual/installation/ .

	List of libraries in use:
		- flask
		- pymongo
		- logging
		- random
		- threading

# Ready to play?

In order to start the game, clone all the files within this repo or downloand the current master and unzip it in the directory of your choice.

Next, you need to start your mongo.

	sudo systemctl start mongod

In my case, I'm using Ubuntu 18.04. For other OS, check the mongodb manual above.

Run the API.py file, it will return a url for the localhost where the game will be running.
