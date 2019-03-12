#Critter Caretaker
#A Virtual pet to care for
from random import randrange

class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        self.name = name
        self.hunger = randrange(7)
        self.boredom = randrange(7)

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()
        
    def eat(self, food):
        print("Brrupp. Thank you!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Wheeeee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
           
def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)
    
    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)

        choice = input("Choice: ")
        print()

        #exit
        if choice == "0":
            print("Good-Bye")

        #listen to your critter
        elif choice == "1":
          crit.talk()

        #feed your critter
        elif choice == "2":
          food = int(input("How much food?: "))
          crit.eat(food)

        #play with your critter
        elif choice == "3":
          fun = int(input("How much fun?: "))  
          crit.play(fun)

        #some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter to exit")

