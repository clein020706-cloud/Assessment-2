items = {
    'A1': {'name': 'Soda', 'price': 1.50, 'category': 'Drinks', 'stock': 5},
    'A2': {'name': 'Chips', 'price': 1.00, 'category': 'Snacks', 'stock': 3},
    'A3': {'name': 'Candy', 'price': 0.75, 'category': 'Snacks', 'stock': 10},
    'B1': {'name': 'Coffee', 'price': 2.00, 'category': 'Drinks', 'stock': 4},
    'B2': {'name': 'Biscuits', 'price': 1.25, 'category': 'Snacks', 'stock': 6}
}

complementary_suggestions = {
    'Drinks': 'Snacks',
    'Snacks': 'Drinks'
}

balance = 0.0

def display_welcome():
    print("Welcome to the Vending Machine!")
    print("Please select an item from the menu.\n")

def display_menu():
    print("Available Items:")
    categories = {}
    for code, item in items.items():
        cat = item['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(f"{code}: {item['name']} - ${item['price']:.2f} (Stock: {item['stock']})")
    
    for cat, item_list in categories.items():
        print(f"\n{cat}:")
        for item in item_list:
            print(f"  {item}")
    print()

def validate_item_code(code):
    return code in items

def check_stock(code):
    return items[code]['stock'] > 0

def handle_payment(price):
    global balance
    while balance < price:
        try:
            amount = float(input(f"Insert money (current balance: ${balance:.2f}, needed: ${price - balance:.2f}): "))
            if amount <= 0:
                print("Please insert a positive amount.")
                continue
            balance += amount
            print(f"New balance: ${balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    return balance - price

def dispense_item(code):
    item = items[code]
    item['stock'] -= 1
    print(f"Dispensed: {item['name']}")
    print(f"Thank you for your purchase!")

def suggest_complementary(category):
    if category in complementary_suggestions:
        sug_cat = complementary_suggestions[category]
        print(f"We suggest trying a {sug_cat.lower()} item next time!")
        for code, item in items.items():
            if item['category'] == sug_cat and item['stock'] > 0:
                print(f"Example: {code} - {item['name']}")
                break

def main():
    global balance
    display_welcome()
    
    while True:
        display_menu()
        code = input("Enter item code: ").upper()
        
        if not validate_item_code(code):
            print("Invalid item code. Please try again.\n")
            continue
        
        if not check_stock(code):
            print("Item out of stock. Please select another item.\n")
            continue
        
        item = items[code]
        print(f"Selected: {item['name']} - Price: ${item['price']:.2f}")
        
        remaining = handle_payment(item['price'])
        
        dispense_item(code)
        
        if remaining > 0:
            print(f"Change returned: ${remaining:.2f}")
            balance = 0.0
        
        suggest_complementary(item['category'])
        
        while True:
            choice = input("\nWould you like to purchase another item? (y/n): ").lower()
            if choice == 'y':
                break
            elif choice == 'n':
                print("Thank you for using the Vending Machine! Goodbye.")
                return
            else:
                print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()