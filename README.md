# 🍔 Console Based Food Ordering System

1. This is a simple **console-based food ordering system** built using Python. The user can view a menu, select food items with quantity, see the total bill, and save a receipt as a text file.  
It is a beginner-friendly project for learning object-oriented programming, file handling, and basic terminal interaction.

---

## 📌 Features

- 📜 Display menu from `menu.txt`
- 🛒 Add food items to order with quantity
- 💰 Show total bill of all selected items
- 🧾 Save receipt in the `orders/` folder with order ID
- 🔁 Allows placing multiple orders

---

## ▶️ How to Run

Follow these steps to run the project on your local machine:

### 1. Clone this repository

```bash
git clone https://github.com/sandhyua/food_ordering_project.git
```

2. Go to the project folder
   ```cd food_ordering_project ```
3.Run the application
   python main.py
   
🗂️ Project Structure
    food_ordering_project/
│
├── main.py                  # Entry point of the application
├── food_ordering_app.py     # Main app logic
├── menu_item.py             # MenuItem class (item id, name, price)
├── order.py                 # Order class (cart, bill, receipt)
├── menu.txt                 # Menu data file (id,name,price)
└── orders/                  # Folder to save generated receipts

📋 Sample menu.txt
    1,Burger,100
    2,Pizza,250
    3,Fries,80
    4,Cold Drink,50
    5,Pasta,200
   Each line format: item_id,name,price
   You can edit this file to change menu items.

🧾 Sample Output
   Welcome to Food Ordering System
1. Start Order
2. Exit
Enter your choice (1 or 2): 1

Menu:
1. Burger - ₹100
2. Pizza - ₹250
3. Fries - ₹80
...

Enter item number to add to cart (or 'done' to finish): 2
Enter quantity for Pizza: 1

Enter item number to add to cart (or 'done' to finish): 3
Enter quantity for Fries: 2

Your Order:
Pizza x 1 = ₹250
Fries x 2 = ₹160

Total Bill: ₹410

Confirm order? (yes/no): yes
Order placed! Receipt saved as orders/order_1001.txt

✅ Requirements
.Python 3.x
.No external libraries required

🧠 Topics Covered
1.Object-Oriented Programming (OOP)

2.File handling (read, write, os.makedirs)

3.User input validation with try-except

4.Looping and conditionals

5.Code organization using classes and modules

💡 Future Improvements
.Add login/signup feature for users

.Store order history for users

.Add ability to remove/edit cart items

.GUI version using Tkinter or PyQt

.Save menu and orders in a real database (SQLite/MySQL)

## 👩‍💻 Author

**Sandhya Raj**  
GitHub: [sandhyua](https://github.com/sandhyua)



