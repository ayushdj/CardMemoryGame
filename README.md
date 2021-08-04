# Card Memory Game
This is a project I worked on in the first semester of my MSCS-Align program.
It is a card matching/memory game. If the user selects two cards that are the same
as one another, they will be removed from the game. If not, the user has about
3 seconds to memorize the locations and kinds of each card, after which the cards
will flip back on their side such that the user has another shot. Enjoy the game!

Design:

I defined a class called "Game" that creates several instance variables for several 
purposes. The following modules are the ones I'm importing into the game:

-time
-turtle
-random

Attributes of the class:
- self.boi (turtle.Turtle()): instance of the turtle that draws boundaries
- self.screen (turtle.Screen()): instance of the turtle screen
- self.face_names (list): names of the face card files in a list
			where each element is a string of the file name
- self.guess_count (int): counts the number of guesses that the user has
			  used. This is used for the status area on the board
- self.match_count (int): the number of matches the user has had
- self.first_card_idx (int): the index of the first card
- self.idx_cleared_cards (list): the index of the cards that have already been
				   cleared from the board
- self.open_leaderboard_list (list): list of names of the leaders of the game
- self.processing_click (boolean): a boolean value that controls whether or not
				a user is allowed to click on the board while
				the two non-matching face cards are going back
				to being hidden

Methods of the class:
- __init__(self): the constructor of the class
- click_area(self, x, y): the areas on the board where the user is allowed 
			  to click
- play_game(self, idx): sets the rules for the game to be played according
			to the spec
- won_game(self): prints a message to the screen allowing the user to know
		  if the game has been won
- card_boundary(self, length, width): draws the boundary for where the cards
   				  will go
- status_boundary(self, length, width): draws the boundary around the status bar
- status_update(self): updates the game based on updating values of self.guess_count
		   and self.match_count
- leaderboard_boundary(self, length, width): draws the boundary around the leaderboard. Also loads the leaderboard
					 file in from the current directory with a try-except block
- write_leaderboard(self): writes the winner of the game to a text file called "leaderboard.txt"
- click_registration(self): calls the click_area() function such that the program can
			register for clicks on the board
- face_card_placeement(self): Calls upon the self.face_names attribute to create 8, 10 or 12
			  different turtle objects, each representing the face cards and telling
			  them to go their designated "area" on the board
- back_card_placement(self): places the back of the card by creating 8, 10 or 12 different turtle
			 objects and telling them to go to their designated "area" on the board
- quit_button(self): creates a turtle object such that the user can click on the quit button area
- quit_game(self): if the user quits the game by clicking on the quit button, the screen disappears
		indicating that the game has been quit
- load(self): loads the game by calling on all the other methods.

Data Structures Used:

list -> to store the names of the face card files and the names on the leaderboard
dictionaries (Hash Map) -> to store the 8/10/12 different turtle objects for both the back facing
					  and front facing cards. So for example, if the user selected to play a game with
					  12 cards, there will be 24 turtle objects. 12 turtles for each face card
					  and 12 objects for each back facing card
string -> to store the names of the players

Approach to Testing:

In order to see that my game works as planned, I tested the following scenarios: If the user doesn't enter a 
valid name (i.e. a name with a length greater than 0), then I force them to re-enter an actual 
name such that the leaderboard can keep track of it. I did this by simply hitting "enter" without a name
entered into the area where it asks for a name. Also, if the user doesn't enter either exactly 8,
10 or 12 cards, I force them to re-enter the number until it can go through. I entered inputs of 7, 9, 11
and numbers greater than 12. It worked as expected; it didn't start the game until the user enter either 8,
10 or 12. With regard to leaderboard testing, I created a dummy file with temporary
scores to see if it would load them in. It passed that test. To test that the code passes
the "leaderboard file not found error" test, I moved the dummy file out of the current working directory
and saw if it would load in the error message, which it did. To test whether the leaderboard is only
updated when the game is finished, I tried quitting out of the program before
matching all the cards; it worked. To test whether the leaderboard file gets updated only
when all matches have been made, I simply opened the leaderboard file after finishing and
exiting the game to see if the current person's name (who just played the game) is there; it 
passed this test.
