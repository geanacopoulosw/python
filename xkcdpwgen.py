#!/usr/bin/env python
import string
import random
import argparse

def main(numberOfWords = 4, numberOfCaps = 0, numberOfNumbers = 0, numberOfSymbols = 0):

   password = ""
   listOfPasswords = (open("password.txt").read().split())  
   symbolsArray = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "?", "/", "|", ":", ";"]
      
   while(numberOfWords > 0 or numberOfCaps > 0 or numberOfNumbers > 0 or numberOfSymbols > 0):
      num = random.randint(0,2)
      if num == 0:
         if numberOfWords > 0 and numberOfCaps > 0:
            AddString = listOfPasswords[random.randint(0, len(listOfPasswords)-1)]
            beginningOfPassword = AddString[:1]
            endOfPassword = AddString[1:]
            password += (beginningOfPassword.upper() + endOfPassword)
            numberOfWords -= 1
            numberOfCaps -= 1
         else:
            password += listOfPasswords[random.randint(0, len(listOfPasswords)-1)]
            numberOfWords -= 1
      elif num == 1:
         if numberOfNumbers > 0:
            password += str(random.randint(0,9))
            numberOfNumbers -= 1
      else:
         if numberOfSymbols > 0:
            password += symbolsArray[random.randint(0, len(symbolsArray)-1)]
            numberOfSymbols -= 1
   return password

parser = argparse.ArgumentParser(description = "Generate a secure, memorable password using the XKCD method")
parser.add_argument("-w", "--words", type=int, default=4, help="include WORDS words in the password (default=4)")
parser.add_argument("-c", "--caps", type=int, default=0, help="capitalize the first letter of CAPS random words (default=0)")
parser.add_argument("-n", "--numbers", type=int, default=0, help="insert NUMBERS random numbers in the password (default=0)")
parser.add_argument("-s", "--symbols", type=int, default=0, help="insert SYMBOLS random symbols in the password (default=0)")
      
args = parser.parse_args()
print(main(args.words, args.caps, args.numbers, args.symbols))

if __name__ == "__main__":
   main()
