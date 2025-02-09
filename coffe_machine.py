# Menu of available coffee options with ingredients and cost
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

# Initial resources available in the machine (water, milk, coffee, and money)
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


# Function to choose the type of coffee or other options (off, report)
def check_response():
    while True:
        # Prompt user to choose a coffee or special option
        type_of_coffe = input("What would you like?(espresso/latte/cappuccino): ").lower()

        if type_of_coffe in MENU:
            return type_of_coffe  # Return the chosen coffee if valid
        elif type_of_coffe == "off":
            print("Turning off. Goodbye!")
            exit()  # Exit the program if 'off' is chosen
        elif type_of_coffe == "report":
            print(resources)  # Print the current resources if 'report' is chosen
        else:
            print("Invalid choice, Please choose a valid one")  # Inform the user of invalid input
            continue  # Continue the loop to allow a valid input


# Function to insert coins and calculate the total money
def money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    # Calculate the total value of inserted coins
    total_quarters = 0.25 * quarters
    total_dimes = 0.10 * dimes
    total_nickels = 0.05 * nickles
    total_pennies = 0.01 * pennies
    total_money = total_nickels + total_dimes + total_pennies + total_quarters
    return total_money  # Return the total money inserted


# Function to check if the inserted money is enough to buy the selected coffee
def cost_coffe(type_of_coffe, total_money):
    cost_of_coffe = MENU[type_of_coffe]["cost"]
    if total_money < cost_of_coffe:
        print("Sorry that's not enough money. Money refunded.")  # Inform if not enough money
    else:
        charge = total_money - cost_of_coffe
        resources["money"] += round(cost_of_coffe, 2)  # Add the cost of coffee to the machine's money
        if charge > 0:
            print(f"Here is ${charge:.2f} in change.")  # Provide change if there's any excess
        else:
            print("That's exactly the amount of money you need.")  # Inform if no change is needed


# Function to check if there are enough resources to prepare the selected coffee
def check_resources(type_of_coffe, total_money):
    resources_coffe = MENU[type_of_coffe]["ingredients"]

    for item in resources_coffe:
        if resources[item] < resources_coffe[item]:
            print(f"Sorry, there is not enough {item}.")  # Inform if any ingredient is missing
            return False
    for item in resources_coffe:
        resources[item] -= resources_coffe[item]  # Deduct the used resources from the machine
    return True


# Function to print a goodbye message and confirm the coffee
def goodbye_message(coffe):
    print(f"Here is your {coffe}. Enjoy!")


# Main loop to continuously run the coffee machine
while True:
    coffe = check_response()  # Get the user's choice of coffee
    total_coins = money()  # Get the total money inserted by the user
    cost_coffe(coffe, total_coins)  # Check if the money is enough for the selected coffee
    if check_resources(coffe, total_coins):  # Check if there are enough resources
        goodbye_message(coffe)  # Serve the coffee if everything is fine
