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

money = 0

def is_sufficient(coffee_ingredients):
    """It checks whether there are enough ingredients to make the desired coffee."""
    for i in coffee_ingredients:
        if coffee_ingredients[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

def process_coins():
    """Calculates the amount of money inserted into the machine."""
    print("Please insert coins.")
    total_money = 0
    quarter = int(input("How many quarters?: "))*0.25
    dime = int(input("How many dimes?: ")) * 0.1
    nickle = int(input("How many nickles?: ")) * 0.05
    penny = int(input("How many pennies?: ")) * 0.01
    total_money = quarter + dime + nickle + penny
    return total_money

def is_money_enough(received_money, cost):
    """It checks whether the amount of money inserted into the machine is enough to buy coffee.
    If too much money is inserted, it calculates the change and keeps the machine's profit in the money variable."""
    if received_money >= cost:
        change = round(received_money - cost, 2)
        print(f"Here is ${change} dollars in change.")
        global money
        money += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.   ")
        return False
def make_coffee(coffee_name, coffee_ingredients):
    """Deduct the required ingredients from the resources"""
    for i in coffee_ingredients:
        resources[i] -= coffee_ingredients[i]
    print(f"Here is your {coffee_name}. Enjoy.")
print(f"Espresso cost: ${MENU['espresso']['cost']}/Latte cost: ${MENU['latte']['cost']}/Cappuccino cost: ${MENU['cappuccino']['cost']}")

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        coffee_ingredients = MENU[choice]["ingredients"]
        if is_sufficient(coffee_ingredients):
            payment = process_coins()
            if is_money_enough(payment, MENU[choice]["cost"]):
                make_coffee(choice, coffee_ingredients)

