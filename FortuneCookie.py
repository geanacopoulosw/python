import random

print("\tWelcome to 'My fortune cookie'!")

the_fortune = random.randint(1, 5)

if the_fortune == 1:
    print("Let's GOOOO!")
elif the_fortune == 2:
    print("That wasn't chicken")
elif the_fortune == 3:
    print("You need to shower")
elif the_fortune == 4:
    print("You will get in A")
elif the_fortune == 5:
    print("Patriots will go 16-0")


input("\n\nPress the enter key to exit.")
