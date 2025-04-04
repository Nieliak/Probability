from random import random


failure = "Sorry, you are not fortunate enough to execute your command successfully!"
def roll(p,execution,*args):
    basic_chance = random()
    if basic_chance < p:
        execution(*args)
    else:
        return failure
def main():
    while True:
        try:
            roll(float(input("Enter the probability: ")), print, "Execution succeeded!")
        except:
            break

if __name__ == "__main__":
    main()