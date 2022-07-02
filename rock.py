from asyncore import write
from pyray import *
import pyray
import random

class Score:
    """
    displays score in the top left of the screen and sets
    the text as white

    attributes:
        self.value: sets initial score at 0
    """
    def __init__(self):
        self.value = 0

    def display_score(self):
        #displays the current score
        draw_text(f"Score: {self.value}", 20, 20, 25, WHITE)

    def update_score(self, points):
        #updates the score according to objects caught
        self.value += points

class Point:
    """
    A class to represent x/y coordinates.
    """

    def __init__(self, x, y):
        """
        The constructor for the Point class.
        """
        self.x = x
        self.y = y

class FlyingObjects:
    """
        FlyingObjects class is parent class for gem, rock, and mine class
        sets how the ojects "fall" down the screen

        attributes:
        appearance: place holder that allows child classes to set their own appearances
        
        position: randomly populates objects into random location at top of screen
        has random x position and y position set at 0 so its top of screen
        
        points: place holder that allows child classes to set their own point values for scoring  
    
        move_counter: allows for smooth movement of player and falling objects

    """
    def __init__(self):
        #constructor for FlyingObjects class
        self.appearance = "0"
        self.position = Point(random.randint(2, 890), 0)
        self.points = 1
        self.move_counter = 0

    def fall(self):
        #moves the falling object down every 30 frames
        
        if self. move_counter < 30:
            self.move_counter += 1
        else:
            self.position.y += 1
            self.move_counter = 0

class Rock(FlyingObjects):
    """
    Rock class inherits from FlyingObjects
    attributes:
        super() inherits from parent class constructor
        appearance: gives this class "o" appearance
        points: deducts 1 point when collides
    """
    def __init__(self):
        #constructor for Rock class
        super(Rock, self).__init__()
        self.appearance = "O"
        self.points = -1



class Mine(FlyingObjects):
    """
    Mine class inherits from FlyingObjects class
    attributes:
        inherits super() from parent class constructor
        appearance: gives mine "x" appearance
        points: deducts 20 points when collides
    """
    def __init__(self):
        #constructor for Mine class
        super(Mine, self).__init__()
        self.appearance = "x"
        self.points = -20


class Gem(FlyingObjects):
    """
    Gem class inherits from the FlyingObjects class
    attributes:
        inherit super() from parent class constructor
        appearance: gives the gem the "#" look
        points: adds 1 point for every "#" caught
    """
    def __init__(self):
        #constructor for gem class
        super(Gem, self).__init__()
        self.appearance = "#"
        self.points = 1

class Player:
    """
    Keeps track of the player in the game and keeps track of 
    their movement and of their current position on the screen

    attributes:
        appearance: sets the player as the "#"
        position: sets player at the center of the screen
        move_counter: allows player to move every 20 frames

    """
    def __init__(self):
        #constructor for the player class

        self.appearance = "#"
        self.position = Point(450, 300)
        self.move_counter = 0

    def move(self):
        """
        it keeps track of the player movement
        sets barrier to screen so player cannot 
        leave the confines
        
        """
        #keeps player from exiting left side of the screen
        if self.position.x == 2:
            self.position.x += 1
            return
        
        #keeps player from exiting right side of the screen
        if self.position.x == 890:
            self.position.x -= 1
            return
        
        #keeps player from exiting top side of the screen
        if self.position.y == 2:
            self.position.y += 1
            return
        
        #keeps player from exiting bottom side of the screen
        if self.position.y == 590:
            self.position.y -= 1
            return

        #if player is holding left and right it prevent movements
        if pyray.is_key_down(pyray.KEY_LEFT) and pyray.is_key_down(pyray.KEY_RIGHT):
            return

        #if player is holding left and up moves it diagonally
        if pyray.is_key_down(pyray.KEY_LEFT) and pyray.is_key_down(pyray.KEY_UP):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x -= 1
                self.position.y -= 1
                self.move_counter = 0
            return
        
        #if player is holding left and down moves it diagonally
        if pyray.is_key_down(pyray.KEY_LEFT) and pyray.is_key_down(pyray.KEY_DOWN):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x -= 1
                self.position.y += 1
                self.move_counter = 0
            return

        #if player is holding right and up moves it diagonally
        if pyray.is_key_down(pyray.KEY_RIGHT) and pyray.is_key_down(pyray.KEY_UP):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x += 1
                self.position.y -= 1
                self.move_counter = 0
            return
        
        #if player is holding right and down moves it diagonally
        if pyray.is_key_down(pyray.KEY_RIGHT) and pyray.is_key_down(pyray.KEY_DOWN):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x += 1
                self.position.y += 1
                self.move_counter = 0
            return
        
        #if player is holding up and down it prevent movements
        if pyray.is_key_down(pyray.KEY_UP) and pyray.is_key_down(pyray.KEY_DOWN):
            return

        #move left
        if pyray.is_key_down(pyray.KEY_LEFT):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x -= 1
                self.move_counter = 0
            return
        
        #move right
        if pyray.is_key_down(pyray.KEY_RIGHT):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.x += 1
                self.move_counter = 0
            return
        
        #move up
        if pyray.is_key_down(pyray.KEY_UP):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.y -= 1
                self.move_counter = 0
            return
        
        #move down
        if pyray.is_key_down(pyray.KEY_DOWN):
            if self. move_counter < 20:
                self.move_counter += 1
            else:
                self.position.y += 1
                self.move_counter = 0
            return

