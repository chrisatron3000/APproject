# Import libraries random and time
# Welcome to virtual pet sim
# Make var name that takes user input for the pet’s name
# Make vars for the different things that the user will have to care for(happiness, hunger, fatigue, play, bathroom)
# Make happiness from 1-100, choose a starting level
# Make hunger a boolean, false to start
# Make fatigue from 1-20, choose a starting level
# Make play from 1-10, choose a starting level
# Make bathroom a boolean, false to start
# Display all these variables to the user along with instructions on how the game works so they have a jumping off point
# Make a var status and store a list in it that contains all the variables just listed
# Define a function called update_status 
# Make the function sleep for 30 sec intervals in between updates
# Make happiness decreases by 10 every interval
# Make an if statement that asks if hunger is false, if false make true, else leave as is
# Make fatigue increase by 5 each interval
# Make play increase by 1 each interval
# Make an if statement that asks if bathroom is false, if false make true, else leave as is
# Update the user on the new status of their pet
# Ex:
# print(‘Happiness is ‘, happiness, \n’Hunger is ‘, hunger, \n’Fatigue is ‘, fatigue, \n’Need   for play is ‘, play, \n’Need for using the grass is ‘, bathroom)
# Ask the user what they would like to do to improve their pet’s wellbeing, they can answer with a ‘y’ or ‘n’
# Ex:
# Response = input(‘Would you like to play with ‘, name, ‘?’, \n‘Would you like to take ‘, name, ‘ to use the grass?’)
# Make more vars to compare current hunger, bathroom and play levels with the ones before the user improved the wellbeing of their pet to affect fatigue and happiness levels
# If the user is playing with their pet too much then fatigue goes up
# If the user made hunger go down, fatigue/need to play go down and bathroom false then happiness goes up by 15


# Virtual Dog Simulator
import time
import random

print('Welcome to Virtual Dog Simulator!')

# This takes the input for the name of the dog
petname = input('\nEnter a Name for Your Dog: ')
print('Some rules for this game:', \n, 'Your dog will experience several different feelings including, happiness, fatigue, hunger, need to play and need to use the grass. It is your job to keep your dog happy, you can do this by lowering it's fatigue, keeping it fed, making sure it's going to the grass when need be and playing with it. Please inout either a y or n for each descion.')# This takes the input for the name of the dog

# happiness is 1-100, hunger is a boolean, fatigue is 1-50, does it need to play is 1-10, does it need to use the bathroom is boolean, anger is 1-10
my_dic = {hapiness : 50,
          hunger : False,
          fatigue : 5,
          play : 5,
          bathroom : False,
          anger : 2}

# def update_status(pls fix this)
#      happiness = (happiness - 10)
#      if hunger = False:
          # hunger = True
#      else:
        # hunger = False
# return(status)

# response = input('Would you like to play with your pet?)
# \n, 'Would you like to take ', name, ' to use the grass?')

