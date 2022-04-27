#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 00:12:23 2022

@author: royalihuaenyi
"""
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images=[rock,paper,scissors]
your_selection=input("Select 0 for Rock, 1 for Paper and 2 for Scissors: ")
selection=int(your_selection[0])
if selection >=3 or selection<0:
    print("Invalid number, you lose")
else:
    print(images[selection])
    
c_selection=random.randint(0,2)
print("Computer chose: ")
print(images[c_selection])


if c_selection == selection:
    print ("Stalemate")
elif c_selection == 0 and selection ==2:
    print ("You lose")
elif c_selection == 1 and selection ==0:
    print ("You lose")
elif c_selection == 2 and selection ==1:
    print ("You lose")  
else:
    print('You win')