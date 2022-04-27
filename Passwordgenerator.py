#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 00:56:37 2022

@author: royalihuaenyi
"""
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password=''
# easy letters and numbers are not in a random order
#letters
for i in range(1,nr_letters+1):
    random_char=random.choice(letters)
    password+=random_char

for i in range(1,nr_numbers+1):
    random_num=random.choice(numbers)
    password+=random_num

for i in range(1,nr_letters+1):
    random_symb=random.choice(symbols)
    password+=random_symb
    
l=list(password)  #stores password in a list
random.shuffle(l)  #shiffles the list


passwordrand=''

for i in l:
    passwordrand+=i

print (f'Your password is {passwordrand}')
#Hard- letters and numbers are in a random order