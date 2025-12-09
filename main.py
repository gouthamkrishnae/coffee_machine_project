MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#coins = {"penny":0.01,"nickel":0.05,"dime":0.10,"quater":0.25}

def coin():
    q = int(input("How many quarters?:"))
    d = int(input("How many dimes?:"))
    n = int(input("How many Nickel?:"))
    p = int(input("How many pennies?:"))
    total = (q * 0.25) + (d * 0.1) + (n * 0.05) + (p * 0.01)
    return total


def espresso():
    if resources["water"] >= 50 and resources["coffee"] >= 18:
        print("Please insert the coin:\n")
        total = coin()
        resources["water"] = resources["water"] - 50
        resources["coffee"] = resources["coffee"] - 18
        if total == MENU["espresso"]["cost"]:
            print("Here is your espresso:)")
        elif total > MENU["espresso"]["cost"]:
            change = total - MENU["espresso"]["cost"]
            print("Here is your change:",change)
            print("Here is your espresso")
        else:
             print("There is no enough coin. The money is refunded")
    else:
        if resources["water"] < 50:
            print("There is no enough water")
        else:
            print("there is no enough coffee")

def latte():
    if resources["water"] >= 200 and resources["coffee"] >= 24 and resources["milk"] >= 180:
        print("Please insert the coin:\n")
        total = coin()
        resources["water"] = resources["water"] - 200
        resources["coffee"] = resources["coffee"] - 24
        resources["milk"] = resources["milk"] - 180
        if total == MENU["latte"]["cost"]:
            print("Here is your latte:)")
        elif total > MENU["latte"]["cost"]:
            change = total - MENU["latte"]["cost"]
            print("Here is your change:",change)
            print("Here is your latte")
        else:
             print("There is no enough coin. The money is refunded")
    else:
        if resources["water"] < 200 :
            print("There is no enough water")
        elif resources["coffee"] < 24:
            print("There is no enough coffee")
        else:
            print("there is no enough milk")

def cappuccino():
    if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100:
        print("Please insert the coin:\n")
        total = coin()
        resources["water"] = resources["water"] - 250
        resources["coffee"] = resources["coffee"] - 24
        resources["milk"] = resources["milk"] - 100
        if total == MENU["cappuccino"]["cost"]:
            print("Here is your cappuccino:)")
        elif total > MENU["cappuccino"]["cost"]:
            change = total - MENU["cappuccino"]["cost"]
            print("Here is your change:",change)
            print("Here is your cappuccino")
        else:
             print("There is no enough coin. The money is refunded")
    else:
        if resources["water"] < 250 :
            print("There is no enough water")
        elif resources["coffee"] < 24:
            print("There is no enough coffee")
        else:
            print("there is no enough milk")
def report():
    print(resources)

def main_function(coffee_type):

    if coffee_type == "espresso":
        espresso()
    elif coffee_type == "latte":
        latte()
    elif coffee_type == "cappuccino":
        cappuccino()
    elif coffee_type == "report":
        report()
    else:
        print("your input is invalid!Please choose another option.")

condition = True
while condition:
     choice = input("What would you like?(espresso/latte/cappuccino):")
     main_function(choice)