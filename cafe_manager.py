"""Cafe Management System
Joshua Corten
CSCI 1250-201
Ai was used to help reseach errors and debug code i.e a broken show cart function"""
cafe_menu = [("Coffee", 3.00), ("Tea", 2.50), ("Sandwich", 5.00), ("Salad", 4.50), ("Cookie", 2.00)]
item_quantities = []
shopping_cart = []
#Display menu
def display_menu():
    print("----------------------------------------")
    print("Menu:")
    print("1. Coffee - $3.00")
    print("2. Tea - $2.50") 
    print("3. Sandwich - $5.00")
    print("4. Salad - $4.50")
    print("5. Cookie - $2.00")
    print("----------------------------------------")
# Add item to cart
def add_item():
    while True:
        display_menu()
        choice = input("enter 'q' to quit or press 1-5 to add an item:")
        if choice.lower() in ('q','b','0'):
            print("Exiting add item menu.")
            break
        elif choice in ['1','2','3','4','5']:
            try:
                item = int(choice)
                quantity = int(input("Enter the quantity: "))
                if 1 <= item <= len(cafe_menu):
                    name, price = cafe_menu[item - 1]
                    shopping_cart.append((name, price, quantity))
                    print(f"Added {quantity} x {name} at ${price:.2f} each.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a valid number.")
# Show cart contents
def show_cart():
    if not shopping_cart:
        print("Your cart is empty.")
        return
    print("----------------------------------------")
    print("Cart:")
    subtotal = 0.0
    for name, price,quantity in shopping_cart:
        item_total = price * quantity
        subtotal += item_total
        print(f"{quantity} x {name} at ${price:.2f} each: ${item_total:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax rate: 9.5%")
    total = subtotal * 1.095
    print(f"Total: ${total:.2f}")
    print("----------------------------------------")
# Remove item from cart
def remove_item():
    while True:
        if not shopping_cart:
            print("Your cart is empty.")
            return
        display_menu()
        show_cart()
        try:
            item = int(input("Enter the item number to remove: (1-5)"))
            if 1 <= item <= len(cafe_menu):
                name, price = cafe_menu[item - 1]
                for i, (cart_name, cart_price, quantity) in enumerate(shopping_cart):
                    if cart_name == name:
                        remove_qty = int(input(f"Enter quantity to remove (in cart: {quantity}): "))
                        if remove_qty < 1:
                            print("Please enter a valid quantity.")
                            return
                        if remove_qty >= quantity:
                            shopping_cart.pop(i)
                            print(f"Removed all {name} from cart.")
                        else:
                            shopping_cart[i] = (cart_name, cart_price, quantity - remove_qty)
                            print(f"Removed {remove_qty} x {name} from cart.")
                        return
                print(f"{name} not found in cart.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")
# make main menu function
def main_menu():
    #defined variables
    cafe="Blue Ridge Cafe"
    tax_rate=0.095
    user_Choice = 0
    #Choice menu
    while user_Choice !=5:
        print("Welcome to the Blue Ridge Cafe!")
        print("Our tax rate is 9.5%")
        print("-----------------------------------------")
        print("Would you like to:")
        print("1. View Menu")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Show Cart")
        print("5. Exit")
        print("-----------------------------------------")
        try:
            user_Choice = int(input("Please select an option (1-5): "))
            if user_Choice == 1:
                display_menu()
           # Call display menu function
            elif user_Choice == 2:
                add_item()
            # Call add item function
            elif user_Choice == 3:
                remove_item()
                # Call remove item function
            elif user_Choice == 4:
                show_cart()
            # call show cart function
            elif user_Choice == 5:
                print("Exiting the system. Goodbye!")
                quit()
            # Exit statement
            else:
                print("Invalid choice. Please try again.")
        except ValueError: 
            print("Please enter a valid number.")
            #If statment that handels choice menu
    
main_menu()
# Calls main menu function
