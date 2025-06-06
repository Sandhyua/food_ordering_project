from menu_item import MenuItem
from order import Order

class FoodOrderingApp:
    def __init__(self):
        self.menu = []
        self.order_id_counter = 1001
        self.load_menu()

    def load_menu(self):
        with open('menu.txt', 'r') as f:
            for line in f:
                item_id, name, price = line.strip().split(',')
                self.menu.append(MenuItem(int(item_id), name, int(price)))

    def show_menu(self):
        print("\nMenu:")
        for item in self.menu:
            print(item)

    def start_order(self):
        self.show_menu()
        order = Order()

        while True:
            choice = input("\nEnter item number to add to cart (or 'done' to finish): ")
            if choice.lower() == 'done':
                break
            try:
                item_id = int(choice)
                menu_item = next((item for item in self.menu if item.item_id == item_id), None)
                if not menu_item:
                    print("Invalid item number. Try again.")
                    continue
                quantity = int(input(f"Enter quantity for {menu_item.name}: "))
                order.add_item(menu_item, quantity)
            except ValueError:
                print("Invalid input. Try again.")

        if not order.items:
            print("No items selected.")
            return

        order.display_order()
        confirm = input("\nConfirm order? (yes/no): ")
        if confirm.lower() == 'yes':
            order.save_receipt(self.order_id_counter)
            print(f"Order placed! Receipt saved as orders/order_{self.order_id_counter}.txt")
            self.order_id_counter += 1
        else:
            print("Order cancelled.")
