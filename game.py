from turtle import *
from random import randint, choice
from time import time

counter = 0
colorL = ["red", "blue", "green", "yellow", "purple"]
color_choice = None

def marque(x,y):
    '''take a postion and increase the counter'''
    global counter
    if color_choice != None:
        if color_choice == "red":
            print("Rouge")
            counter += 2
        else:
            print("Pas rouge")
            counter += 1



while counter <= 20:
    Time = time()
    
    up()
    hideturtle()
    color_choice = choice(colorL)
    color(color_choice)
    goto(randint(-200, 200), randint(-200, 200))
    while time() < Time + randint(1, 3):
        showturtle()
    onclick(marque)
    
    print(counter)