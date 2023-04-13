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
    
def main():
  price = 0
  size = SizeOfPizza()
  if size == "Large":
    price = 6
  if size == "Extra Large":
    price = 10
  num = NumberOfToppings()
  if num == "1 topping":
    price = price + 1
  elif num == "2 toppings":
    price = price + 1.75
  elif num == "3 toppings":
    price = price + 2.5
  elif num == "4 toppings":
    price = price + 3.35
    
  print(str(round(price*1.13,2))+"$")

main()
