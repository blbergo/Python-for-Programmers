# part 1
class ItemToPurchase:
    def __init__(self, item_name = "none", item_price = 0.0, item_quantity = 0, item_description = "none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, self.item_price, total))
    
    def print_item_description(self):
        print("{}: {}".format(self.item_name, self.item_description))
        
# part 2
class ShoppingCart:
    def __init__(self, customer_name = "none", current_date = "January 1, 2016", cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    
    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)
    
    def remove_item(self, itemName):
        for i in self.cart_items:
            if i.item_name == itemName:
                self.cart_items.remove(i)
                return
        print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, itemToPurchase):
        for i in self.cart_items:
            if i.item_name == itemToPurchase.item_name:
                i.item_quantity = itemToPurchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        total = 0
        for i in self.cart_items:
            total += i.item_quantity
        return total

    def get_cost_of_cart(self):
        total = 0
        for i in self.cart_items:
            total += (i.item_price * i.item_quantity)
        return total
    
    def print_total(self):
        total = self.get_cost_of_cart()
        if total == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            self.output_cart()
    
    def output_cart(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Number of Items: {}\n".format(self.get_num_items_in_cart()))
        for i in self.cart_items:
            i.print_item_cost()
        print("\nTotal: ${}".format(self.get_cost_of_cart()))
    
    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("\nItem Descriptions")
        for i in self.cart_items:
            i.print_item_description()    
    
    def print_menu(self):
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit\n")
    
    def execute_menu(self, choice):
        if choice == "a":
            print("\nADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            self.add_item(ItemToPurchase(name, price, quantity, description))
        elif choice == "r":
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            self.remove_item(name)
        elif choice == "c":
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            self.modify_item(ItemToPurchase(name, 0, quantity))
        elif choice == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            self.print_descriptions()
        elif choice == "o":
            print("\nOUTPUT SHOPPING CART")
            self.print_total()
        elif choice == "q":
            return False
        else:
            print("\nChoose an option from the menu.")
        return True

def main():
    print("PART 1 \n=======================\n")
    # prompt user for two items
    name1 = input("Item 1\nEnter the item name:\n")
    price1 = float(input("Enter the item price:\n"))
    quantity1 = int(input("Enter the item quantity:\n"))
    
    name2 = input("\nItem 2\nEnter the item name:\n")
    price2 = float(input("Enter the item price:\n"))
    quantity2 = int(input("Enter the item quantity:\n"))
    
    # create two objects of class ItemToPurchase
    item1 = ItemToPurchase(name1, price1, quantity1)
    item2 = ItemToPurchase(name2, price2, quantity2)
    
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print("\nTotal: ${}".format((item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)))
    
    print("\nPART 2 \n=======================\n")
    
    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    cart = ShoppingCart(name, date)
    
    cart.print_menu()
    choice = ""
    
    while choice != 'q':
        choice = input("Choose an option:\n")
        if not cart.execute_menu(choice):
            break
    
if __name__ == "__main__":
    main()