import os  # for folder creation

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, MenuItem, quantity):
        self.items.append((MenuItem, quantity))

    def display_order(self):
        print("\nYour Order:") 
        total = 0
        for item, quantity in self.items:
            cost = item.price * quantity
            total += cost
            print(f"{item.name} x {quantity} = ₹{cost}")
        print(f"\nTotal Bill: ₹{total}")

    def save_receipt(self, order_id):
        os.makedirs("orders", exist_ok=True)  # make folder if missing
        filename = f"orders/order_{order_id}.txt"
        total = 0
        with open(filename, 'w', encoding='utf-8') as file_object:  # utf-8 to support ₹ symbol
            file_object.write(f"Order Receipt - Order ID: {order_id}\n")
            for item, quantity in self.items:
                cost = item.price * quantity
                total += cost
                file_object.write(f"{item.name} x {quantity} = ₹{cost}\n")  # fixed quantity error
            file_object.write(f"Total Bill: ₹{total}")
