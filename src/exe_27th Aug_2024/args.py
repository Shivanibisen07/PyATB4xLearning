# Pizza lover -- Yes

def make_pizza(*toppings):  #----Only one star argument is allowed
    print(toppings)

shivani = make_pizza("tomato", "onion", "cheese")
Arman = make_pizza("Mushroom", "jalepano", "sweetcorn")

def make_pizza(*toppings,base):
    print(toppings)

shivani = make_pizza("tomato", "onion", "cheese", base="thin crust")
Arman = make_pizza("Mushroom", "jalepano", base="Cheese brust")
Bhavik = make_pizza(base="Cheese brust", toppings: "Mushroom", "jalepano")