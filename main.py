import math

def SizeOfPizza():
    PizzaSize = str(input("What size of pizza would you like? Enter Character \"L\" for large or \"X\" for Extra large"))
    while True:
        if (PizzaSize == "L"):
            return "Large"
        if (PizzaSize == "X"):
            return "Extra Large"
        if (PizzaSize != "X") or (PizzaSize != "L"):
            PizzaSize = str(('Invalid input, choose "L" or "X"'))
    
print(SizeOfPizza())

