def calculate_bill(order, tax, tip):
    total_cost = sum(order.values())
    tax_amount = total_cost * tax
    total_cost += tax_amount
    total_cost += tip
    return total_cost

def main():
    menu = {"pizza": 10.99, "burger": 8.99, "salad": 5.99, "fries": 3.99}
    order = {}
    total = 0
    tax = 0.08
    tip = 0

    print("Welcome to the restaurant!")
    print("Our menu for today:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

    while True:
        item = input("What would you like to order? (Enter 'done' when finished) ")
        if item == "done":
            break
        if item in menu:
            order[item] = menu[item]
            print(f"{item} has been added to your order.")
        else:
            print(f"{item} is not on the menu.")

    if order:
        tip = float(input("Enter the tip amount (in dollars): "))
        total = calculate_bill(order, tax, tip)
        print("\nYour order:")
        for item, price in order.items():
            print(f"{item}: ${price:.2f}")
        print(f"Tax ({tax * 100:.0f}%): ${tax * sum(order.values()):.2f}")
        print(f"Tip: ${tip:.2f}")
        print(f"Total: ${total:.2f}")
    else:
        print("\nNo items were ordered.")

if __name__ == "__main__":
    main()
