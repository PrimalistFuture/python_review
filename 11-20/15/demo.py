# Coffee Machine
# Three Hot Flavors
# Accepts coins for cost of the drink
# Checks for sufficient resources (water, milk, coffee)

import data


def get_money():
    """Asks the customer for money."""
    q = int(input("How many quarters? "))
    d = int(input("How many dimes? "))
    n = int(input("How many nickles? "))
    p = int(input("How many pennies? "))
    return [q, d, n, p]


def count_coins_and_provide_change(q, d, n, p, price):
    """Processes input coinage and provides change and
    updates machines money resource"""
    q = 0.25 * q
    d = 0.10 * d
    n = 0.05 * n
    p = 0.01 * p
    total = q + d + n + p
    if total > price:
        data.profit += price
        change = total - price
        return round(change, 2)
    if total == price:
        data.profit += price
        return "No change"
    return f"""You have not provided enough coins.
    The price of the drink is {price}.
    Returning your coins totaling {total}."""


def recieves_and_updates_money(drink):
    """Recieves customers money, calls get_money and 
    count_coins_and_provide_change and updates machine money"""
    drink_price = data.MENU[drink]["cost"]
    money = get_money()
    possible_change = count_coins_and_provide_change(
        money[0], money[1], money[2], money[3], drink_price)
    return possible_change


def handle_resources(drink):
    """Helper function for check_and_update_resources"""
    drink_resources = data.MENU[drink]["ingredients"]
    for resource in data.resources:
        if resource not in drink_resources:
            continue
        if data.resources[resource] - drink_resources[resource] < 0:
            return f"Sorry insuffiecient resources for {drink} due to lack of {resource}."
        else:
            data.resources[resource] -= drink_resources[resource]
    return


def check_and_update_resources(drink):
    """Accepts a drink, and deducts resources equal
  to that drinks requirements."""
    if drink == 'espresso':
        return handle_resources('espresso')
    if drink == 'latte':
        return handle_resources('latte')
    if drink == 'cappuccino':
        return handle_resources('cappuccino')


def machine():
    """Conducts the machine"""
    status = "on"
    while status == "on":
        order = input("What would you like (espresso / latte / cappuccino): ")
        if order == "off":
            status = "off"
        elif order == "report":
            print(data.resources)
            print(data.profit)
        else:
            money = recieves_and_updates_money(order)
            print(money)
            if isinstance(money, float) or money == "No change":
                print("Hello from if")
                resources = check_and_update_resources(order)
                print(f"Here is your {order}. Enjoy!")


machine()
