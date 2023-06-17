'''
Ayush Dhananjai
CS 5001, Fall 2020
Final Project - Card Memory Game
'''

# Importing the turtle module
import time
import turtle
import random

class Game:
    '''
    The Game class creates an instance of the
    board in which the game will be played.
    '''

    def __init__(self):
        '''
        method -- __init__
            constructor method to create
            an instance of the class

        Parameters: N/A

        Returns an instance of the class
        '''

        # Creating an instance of the turtle
        # and setting the specifications
        self.boi = turtle.Turtle()
        self.boi.pensize(6.5)
        self.boi.speed(9)
        self.boi.hideturtle()
        
        # Creating an instance of the screen
        self.screen = turtle.Screen()
        self.screen.setup(width = 1000, height = 1000)

        # Storing the names of the cards
        # in a list
        self.face_names = ['2_of_clubs.gif', '2_of_diamonds.gif',
                      '3_of_hearts.gif', 'ace_of_diamonds.gif',
                      'jack_of_spades.gif', 'king_of_diamonds.gif']

        # Keeping track of the first
        # card I click
        self.first_card_idx = None
        self.idx_cleared_cards = []

        # Setting the guess counter
        self.guess_count = 0

        # counting the number of matches
        self.match_count = 0

        # Flag to show if click is being processed
        self.processing_click = False

        # Leaderboard list
        self.open_leaderboard_list = []
        
    def click_area(self, x, y):
        '''
        method -- click_area
            returns true if the area clicked is within
            the bounds of the cards are and false otherwise

        Parameters:
            self -- the current object
            x (float) -- x coordinate of the area
                         clicked in
            y (float) -- y coordinate of the area
                         clicked in

        Returns a boolean value.
        '''

        # Locking the board
        if self.processing_click:
            print('Sorry, board is locked')
            return

        # setting the click processing
        # to be true
        self.processing_click = True

        self.boi.penup()
        self.boi.goto(x, y)

        # setting the boundaries
        # for the top left card
        card_right = -330
        card_left = -425
        card_top = 425
        card_bottom = 275
        
        if self.num_cards == 8 or self.num_cards == 10 or self.num_cards == 12:
            # Looping over the number of cards
            for i in range(int(self.num_cards)):
                
                # If the x and y coordinates are in
                # the first row
                if i <= 3 and \
                   card_left + (150*i) <= x <= card_right + (150*i) \
                   and card_bottom <= y <= card_top:
                    print("Caught you clicking on card #", i+1)
                    self.play_game(idx = i)
                    
                # If the x and y coordinates are in
                # the second row
                if 4 <= i <= 7 and \
                     card_left + (150*(i-4)) <= x <= card_right + (150*(i-4)) \
                     and card_bottom - 170 <= y <= card_top - 170:
                    print("Caught you clicking on card #", i+1)
                    self.play_game(idx = i)
                    
                # If the x and y coordinates are in
                # the third row
                if 8 <= i <= int(self.num_cards) and \
                     card_left + (150*(i-8)) <= x <= card_right + (150*(i-8)) \
                     and card_bottom - (170*2) <= y <= card_top - (170 * 2):
                    print("Caught you clicking on card #", i+1)
                    self.play_game(idx = i)

            if 222 <= x <= 280 and -400 <= y <= -360:
                print(x, y)
                self.quit_game()

        self.processing_click = False

    def play_game(self, idx):
        '''
        method -- play_game
            setting the rules of the game.
            This is where the cards are
            matched and if they aren't, it
            resets them back.

        Parameters:
            self -- the current object
            idx (int) -- the index of the current
                         card that is being clicked
                         on

        Returns nothing. Simply sets the rules
        such that the game can be played.
        '''

        # if the current card I'm clicking on
        # is in the list of cards that contains
        # the cards that have already been cleared,
        # do nothing.
        if idx in self.idx_cleared_cards:
            print('This card has already been removed')
            return

        # If the card I click on is equal
        # to the first card I clicked on,
        # then quit out of this function
        if self.first_card_idx == idx:
            print('This card is alredy flipped')
            return

        # If they aren't then hide the back
        # card and show the front facing card
        self.turtle_dictionary['turtle_' + str(idx)].hideturtle()
        self.faceTurtles['faceTurt_' + str(idx)].showturtle()

        # If the first card index is None,
        # then set the current index to the
        # first card.
        if self.first_card_idx is None:
            self.first_card_idx = idx
            print('First card set to index', idx)
            return
        
        print('Second card set to index', idx)

        # increase the guess counter
        self.guess_count += 1

        # Get the names of the face card
        # files into two variables
        self.face_1 = self.faceTurtles['faceTurt_' + str(self.first_card_idx)].shape()
        self.face_2 = self.faceTurtles['faceTurt_' + str(idx)].shape()
        print(f'Card names: {self.first_card_idx} -> {self.face_1} || {idx} -> {self.face_2}')

        # if the second card i've opened up is equal
        # to the first card I opened, then remove them
        time.sleep(2)
        if self.face_1 == self.face_2:
            # hide the first card I opened up
            # and hide the second card I flipped
            self.faceTurtles['faceTurt_' + str(self.first_card_idx)].hideturtle()
            self.faceTurtles['faceTurt_' + str(idx)].hideturtle()

            # Also count this condition as a match
            # and updating status
            self.match_count += 1
            self.status_update()

            # Extending the the list of
            # cleared cards with the cards
            # that were just cleared
            self.idx_cleared_cards.extend([self.first_card_idx, idx])

            # if the number of cleared cards
            # is equal to the number of cards
            # I entered, then the game has finished
            # and then call on the finish game
            # method
            if len(self.idx_cleared_cards) == self.num_cards:
                self.won_game()
                self.write_leaderboard()
                time.sleep(2)
                self.screen.bye()
        
        else:
            # If the two cards are not equal,
            # then show the back turtle and hide
            # the face turtle of both the current
            # card and the previous card
            self.turtle_dictionary['turtle_' + str(self.first_card_idx)].showturtle()
            self.faceTurtles['faceTurt_' + str(self.first_card_idx)].hideturtle()

            # Hiding the second card as well
            self.turtle_dictionary['turtle_' + str(idx)].showturtle()
            self.faceTurtles['faceTurt_' + str(idx)].hideturtle()

            # Update the status of the game
            self.status_update()

        print('match_count:', self.match_count)
        print('Reset cards')
        
        # Resetting the current card
        self.first_card_idx = None

    def won_game(self):
        '''
        method -- won_game
            creates a new turtle to print
            the "won game" stamp

        Parameters:
            self -- the current object

        Returns nothing.
        '''

        # Creating a new turtle for the win logo
        win_turtle = self.boi.clone()
        win_turtle.penup()
        win_turtle.hideturtle()
        win_turtle.goto(0, 0)
        self.screen.addshape('winner.gif')
        win_turtle.shape('winner.gif')
        win_turtle.stamp()

    def card_boundary(self, length, width):
        '''
        method -- card_boundary
            draws the boundary around the cards

        Parameters:
            self -- the current object
            length (float) -- the length of the boundary
            width (float) -- the width of the boundary

        Returns nothing. Simply draws the boundary
        for the cards.
        '''

        # Moving the turtle to the desired location 
        self.boi.penup()
        self.boi.goto(-450, 450)
        self.boi.pendown()
        
        # Drawing the boundary
        self.boi.forward(width)
        self.boi.right(90)
        self.boi.forward(length)
        self.boi.right(90)
        self.boi.forward(width)
        self.boi.right(90)
        self.boi.forward(length)
        self.boi.right(90)
        
    def status_boundary(self, length, width):
        '''
        method -- status_boundary
            moves the turtle object to the
            new location where the boundary
            for the move and click counter
            will be drawn

        parameters:
            self -- the current object
            length (float) - the length of the boundary
            width (float) - the width of the boundary

        Returns nothing. Simply draws the boundary around
        the move and match counter
        '''
        
        # Moving the turtle to the desired location
        self.status_boi = turtle.Turtle()
        self.status_boi.hideturtle()
        self.status_boi.pensize(6.5)
        self.status_boi.speed(9)
        self.status_boi.penup()
        self.status_boi.goto(-450, -450)
        self.status_boi.pendown()

        # Drawing the boundary
        self.status_boi.forward(width)
        self.status_boi.left(90)
        self.status_boi.forward(length)
        self.status_boi.left(90)
        self.status_boi.forward(width)
        self.status_boi.left(90)
        self.status_boi.forward(length)

        # Write the "Status" text
        self.status_boi_text = turtle.Turtle()
        self.status_boi_text.penup()
        self.status_boi_text.hideturtle()
        self.status_boi_text.speed(9)
        self.status_boi_text.goto(-440, -350)
        self.status_specs = ("Arial", 38, "italic")
        self.status_boi_text.write("Status: Guesses: 0 Matches: 0", font=self.status_specs)

    def status_update(self):
        '''
        method -- status_update
            updates the number of guesses

        Parameters:
            self -- the current object

        Returns nothing. Simply shows
        the number of guesses
        '''

        # Hiding the status
        self.status_boi_text.clear()

        # updating the status
        if self.guess_count == 1:
            self.update_turtle = turtle.Turtle()
            self.update_turtle.speed(9)
            self.update_turtle.hideturtle()
            self.update_turtle.penup()
            self.update_turtle.goto(-440, -350)
            num_guesses = "Status: " + "Guesses: " + str(self.guess_count) + " Matches: " + str(self.match_count)
            self.update_turtle.write(num_guesses, font=self.status_specs)

        if self.guess_count > 1:
            self.update_turtle.clear()
            self.update_turtle = turtle.Turtle()
            self.update_turtle.speed(9)
            self.update_turtle.hideturtle()
            self.update_turtle.penup()
            self.update_turtle.goto(-440, -350)
            num_guesses = "Status: " + "Guesses: " + str(self.guess_count) + " Matches: " + str(self.match_count)
            self.update_turtle.write(num_guesses, font=self.status_specs)

    def leaderboard_boundary(self, length, width):
        '''
        method -- leaderboard_boundary
            moves the turtle object to the
            new location where the boundary
            for the leaderboard will be drawn

        Parameters:
            self -- the current object
            length (float) - the length of the boundary
            width (float) - the width of the boundary

        Returns nothing. Simply draws the boundary
        around the leaderboard
        '''
        
        # Moving the turtle to the desired location
        self.boi.penup()
        self.boi.goto(200, 450)
        self.boi.color('blue')
        self.boi.pendown()

        # Drawing the boundary
        self.boi.forward(width)
        self.boi.right(90)
        self.boi.forward(length)
        self.boi.right(90)
        self.boi.forward(width)
        self.boi.right(90)
        self.boi.forward(length)

        # Write the "leaders" text
        self.boi.penup()
        self.boi.goto(210, 400)
        self.boi.pendown()
        specifications = ("Arial", 38, "italic")
        self.boi.write("Leaders:", font=specifications)

        # loading the leader board text file
        try:
            player_specs = ("Arial", 20, "normal")
            self.boi.penup()
            self.boi.goto(210, 350)
            with open('leaderboard.txt', 'r') as leaderboard:
                for player in leaderboard:
                    self.open_leaderboard_list.append(player)

            # Sorting the leaderboard list
            if len(self.open_leaderboard_list) > 0:
                self.open_leaderboard_list.sort(key = lambda x: int(x.split(': ')[0]))

                # Removing any new line characters
                for i in range(len(self.open_leaderboard_list)):
                    if '\n' in self.open_leaderboard_list[i]:
                        self.open_leaderboard_list[i] = self.open_leaderboard_list[i].rstrip('\n')

                print(self.open_leaderboard_list)
                # Removing any new line characters

                # Writing the names in the leaderboard
                for i in range(len(self.open_leaderboard_list)):
                    self.boi.goto(210, self.boi.ycor() - (25))
                    self.boi.write(self.open_leaderboard_list[i], font=player_specs)
            else:
                self.boi.goto(210, 350)

        # If the file doesn't exist, we print
        # the error message to the turtle window
        except FileNotFoundError:
            self.file_not_foundTurtle = turtle.Turtle()
            self.file_not_foundScreen = turtle.Screen()
            self.file_not_foundTurtle.penup()
            self.file_not_foundTurtle.hideturtle()
            self.file_not_foundTurtle.goto(300, 350)
            self.file_not_foundScreen.addshape('leaderboard_error.gif')
            self.file_not_foundTurtle.shape('leaderboard_error.gif')
            self.file_not_foundTurtle.stamp()

    def write_leaderboard(self):
        '''
        method -- write_leaderboard
            opens a new file to write the current winner
            of the game to the leaderboard.txt file
        
        Parameters:
            self -- the current object
        
        Returns nothing.
        '''

        with open('leaderboard.txt', 'a') as leaders:
            leaders.write(str(self.guess_count) + ": " + self.name)
            leaders.write("\n")

    def click_registration(self):
        '''
        method -- click_registration
            gets the turtle board ready to
            start registering clicks

        Parameters:
            self -- the current object

        Returns a boolean.
        '''

        self.screen.onclick(self.click_area)
        return True

    def face_card_placement(self):
        '''
        method -- face_card_placement
            places the faces of the card
            on the board

        Parameters:
            self -- the current object

        Returns nothing. Simply places the
        face cards on the board.
        '''

        if int(self.num_cards) == 8:
            self.face_cards = self.face_names[2:]
            self.face_cards *= 2
            random.shuffle(self.face_cards)
        elif int(self.num_cards) == 10:
            self.face_cards = self.face_names[1:]
            self.face_cards *= 2
            random.shuffle(self.face_cards)
        elif int(self.num_cards) == 12:
            self.face_cards = self.face_names[0:]
            self.face_cards *= 2
            random.shuffle(self.face_cards)

        # Creating an empty dictionary
        # to put new turtles into
        self.faceTurtles = dict()

        # Looping over the empty dictionary
        # and creating new turtle instances
        for i in range(int(self.num_cards)):
            self.faceTurtles['faceTurt_' + str(i)] = turtle.Turtle()
            self.faceTurtles['faceTurt_' + str(i)].hideturtle()

        # adding the face shapes
        for face_card in self.face_cards:
            self.screen.addshape(face_card)
        
        for i, face_card in enumerate(self.face_cards):
            self.faceTurtles['faceTurt_' + str(i)].speed(9)
            self.faceTurtles['faceTurt_' + str(i)].penup()
            self.faceTurtles['faceTurt_' + str(i)].shape(face_card)

            # Placing them into the first row
            if i <= 3:
                self.faceTurtles['faceTurt_' + str(i)].hideturtle()
                self.faceTurtles['faceTurt_' + str(i)].goto(-380 + (150)*i, 350)

            # Placing them into the second row
            elif 4 <= i <= 7:
                self.faceTurtles['faceTurt_' + str(i)].hideturtle()
                self.faceTurtles['faceTurt_' + str(i)].goto(-380 + (150)*(i-4), 180)

            # Placing them into the last row
            elif 8 <= i <= int(self.num_cards):
                self.faceTurtles['faceTurt_' + str(i)].hideturtle()
                self.faceTurtles['faceTurt_' + str(i)].goto(-380 + (150)*(i-8), 10)

    def back_card_placement(self):
        '''
        method -- back_card_placement
            places the back of the
            cards on the board

        Parameters:
            self -- the current object

        Returns nothing. Simply places the
        cards onto the board.
        '''

        # Creating empty turtle dictionaries
        # and empty screen dictionaries
        self.turtle_dictionary = dict()
        
        # Looping over all the cards and creating
        # num_cards different turtle instances
        for i in range(int(self.num_cards)):
            # Updating the dictionary
            self.turtle_dictionary['turtle_' + str(i)] = turtle.Turtle()
            self.turtle_dictionary['turtle_' + str(i)].hideturtle()

        # Adding the back of the card pic
        # to the screen
        self.screen.addshape('card_back.gif')

        for i in range(int(self.num_cards)):
            self.turtle_dictionary['turtle_' + str(i)].shape('card_back.gif')
            self.turtle_dictionary['turtle_' + str(i)].speed(9)
            
            # First Row
            if i <= 3:
                self.turtle_dictionary['turtle_' + str(i)].penup()
                self.turtle_dictionary['turtle_' + str(i)].goto(-380 + (150)*i, 350)

            # Second Row
            elif 4 <= i <= 7:
                self.turtle_dictionary['turtle_' + str(i)].penup()
                self.turtle_dictionary['turtle_' + str(i)].goto(-380 + (150)*(i-4), 180)

            # Third Row
            elif 8 <= i <= int(self.num_cards):
                self.turtle_dictionary['turtle_' + str(i)].penup()
                self.turtle_dictionary['turtle_' + str(i)].goto(-380 + (150)*(i-8), 10)

            self.turtle_dictionary['turtle_' + str(i)].showturtle()
       
    def quit_button(self):
        '''
        method -- quit_game
            loads the quit button on
            to the screen

        Parameters:
            self -- the current object

        Returns nothing. Simply loads
        the quit button.
        '''

        # Creating a new turtle for the quit logo
        quit_turtle = self.boi.clone()
        quit_turtle.penup()
        quit_turtle.hideturtle()
        quit_turtle.goto(250, -380)
        self.screen.addshape('quitbutton.gif')
        quit_turtle.shape('quitbutton.gif')
        quit_turtle.stamp()

    def quit_game(self):
        '''
        method -- quit_game
            when the user clicks
            on the quit button, they
            quit the game

        Parameters:
            self -- the current object

        Returns nothing. Quits the
        game.
        '''

        # Creating a new quit popup msg
        quit_popup = self.boi.clone()
        quit_popup.penup()
        quit_popup.goto(0, 0)
        self.screen.addshape('quitmsg.gif')
        quit_popup.shape('quitmsg.gif')
        quit_popup.showturtle()

        # making the program sleep
        time.sleep(3.5)

        # ending the program
        self.screen.bye()

    def load(self):
        '''
        method -- load
            creates an instance of the turtle
            and sets up the background/board of
            the game
            
        Parameters:
            self -- the current object
        
        Returns nothing. Simply draws the bounds
        '''

        # Prompting the user to enter a name
        self.name = self.screen.textinput("Do you want to play a game?", "Enter your name:")
        while True:

            # If the user doesn't enter a valid name, ask
            # them to re-enter the name
            if len(self.name) == 0:
                error_msg = "Please enter a valid name, so we can keep track"\
                            " of the leaderboard"
                self.name = self.screen.textinput("Do you want to play a game?", error_msg)

            # If the user does enter a valid name, break
            # out of the loop and move on
            elif len(self.name) > 0:
                break

        # Prompting the user to enter a valid
        # number of cards
        self.num_cards = self.screen.numinput("Set Up", "# of Cards to Play (8, 10 or 12):", 8)

        while True:
            # If the user does enter a valid number,
            # create the game board and break out
            # of the loop
            if self.num_cards == 8 or self.num_cards == 10 or self.num_cards == 12:
               #Drawing the card boundary
               self.card_boundary(700, 600)
        
               # Drawing the status boundary
               self.status_boundary(150, 600)
               
               # Drawing the leaderboard
               # boundary
               self.leaderboard_boundary(700, 250)
               
               # Getting the program ready
               # to start registering for clicks
               self.click_registration()

               # Placing the face cards
               print('beep beep! shuffling and placing the face cards...')
               self.face_card_placement()
               print('finished placing face cards')
               
               # Placing the back cards
               self.back_card_placement()

               # Placing the quit button
               self.quit_button()
               
               turtle.mainloop()
               break
            
            # If the user doesn't enter a valid card number,
            # ask them to re-enter a number
            else:
                error_statement = "The number of cards HAS to be either 8,"\
                                  "10 or 12. Please re-enter your number:"
                self.num_cards = self.screen.numinput("Set Up", error_statement, 8)   

def main():
    
    game = Game()
    game.load()
    
if __name__ == "__main__":
    main()
