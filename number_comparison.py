# Creation of player vs. computer, number comparison game
import random

class compgame():
    def __init__(self, numbers):
        self.numbers = numbers

    def computer(self):
        compinput = random.randint(0,1000)
        return compinput

# Testing computer randomizer
# select = compgame(0)
# print(select.computer())

    def player(self):
        number = int(input("Please enter a number: "))
        print(f'The number you have chosen is: {number}')
        return number
    
# Testing player number
# select = compgame()
# select.player()

    def compare(self, compinput, number):
        if compinput > number:
            print(f'You lose! Computer selected: ({compinput}) while you chose: ({number})')
        elif compinput < number:
            print(f'You win! Computer selected: ({compinput}) while you chose: ({number})')
        else:
            print(f"It's a tie! Computer selected: ({compinput}) while you chose: ({number})")

def run():
    start = compgame(0)
    while True:
        response = input("Please enter 's' to start or 'q' to quit: ")
        if response.lower() == "s":
            x = start.computer()
            y = start.player()
            start.compare(x, y)
        elif response.lower() == "q":
            print("Thank you for trying!")
            break
        else:
            print("Sorry, this is not valid, please try again.")
run()