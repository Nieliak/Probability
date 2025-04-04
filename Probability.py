from random import random

failure = "Sorry, you are not fortunate enough to execute your command successfully!"    # be used when necessary to check whether the function has been executed
def roll(p:float,execution:'the function to be executed',*args:'arguments of execution'):   # type: ignore
    '''
    Execute the function based on the given probability(p∈[0,1]).
    If success, return what the function returns.
    If not, return the failure code.
    '''
    basic_chance = random()
    if basic_chance < p:
        execution(*args)
    else:
        return failure
def main():    # a function for test
    while True:
        try:
            roll(float(input("Enter the probability: ")), print, "Execution succeeded!")
        except:
            break

if __name__ == "__main__":
    main()
