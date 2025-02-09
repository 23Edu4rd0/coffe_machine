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


def money():
    print("please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?: "))
    total_quarters =  0.25 * quarters
    total_dimes =  0.10 * dimes
    total_nickles =  0.05 * nickles
    total_pennies =  0.01 * pennies
    total_money = total_nickles + total_dimes + total_pennies + total_quarters
    return total_money

def cost_coffe(coffe, total_coins):
    cost_of_coffe = MENU[coffe]["cost"]
    if total_coins < cost_of_coffe:
        print("Sorry that's not enough money. Money refunded.")
    elif total_coins > cost_of_coffe:
        charge = total_coins - cost_of_coffe
        print(f"Here is ${charge:.2f} in charge")
    elif total_coins == cost_of_coffe:
        print("That's exactly the amount of money you need")




coffe = input("What would you like?(espresso/latte/cappuccino)" ).lower()
total_coins = money()
cost_coffe(coffe,total_coins)






