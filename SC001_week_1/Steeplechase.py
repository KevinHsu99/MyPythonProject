"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()

def jump():
    up()
    cross()
    down()

def up():
    turn_left()
    #Karel is facing north
    while not right_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

def cross():
    turn_right()
    move()
    turn_right()

def down():
    while front_is_clear():
        move()
    turn_left()

















####### DO NOT EDIT CODE BELOW THIS LINE #######
if __name__ == '__main__':
    execute_karel_task(main)