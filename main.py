import math

def SizeOfPizza():
    PizzaSize = str(input("What size of pizza would you like? Enter Character \"L\" for large or \"X\" for Extra large\n"))
    while True:
        if (PizzaSize == "L"):
            return "Large"
        elif (PizzaSize == "X"):
            return "Extra Large"
        elif (PizzaSize != "X") or (PizzaSize != "L"):
            PizzaSize = str(input('Invalid input, choose "L" or "X"\n'))
    
print(SizeOfPizza())

def NumberOfToppings():
    Toppings = str(input("How many toppings would you like? Enter amount from 0-4.\n"))
    while True:
        if (Toppings == "0"):
            return "0 toppings"
        elif (Toppings == "1"):
            return "1 topping"
        elif (Toppings == "2"):
            return "2 toppings"
        elif (Toppings == "3"):
            return "3 toppings"
        elif (Toppings == "4"):
            return "4 toppings"
        Toppings = str(input('Invalid input, choose number between 1-4.\n'))
    
print(NumberOfToppings())
    