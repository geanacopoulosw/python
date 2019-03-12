#Challange 1
#
#create a program that prints a list of word
#in random order. The program should print all the words
#and not repeat any
#imports
import random

words = ["Celtics", "Patriots", "Bruins", "Red Sox"]
print (words)
print("Welcome to the Challange 1. The words are:\n ")
random.shuffle(words)
print(*words)
   
input("\n\nPress the enter key to exit.")
