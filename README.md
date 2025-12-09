☕ Coffee Machine Simulator (Python)

A simple command-line based Coffee Machine Project inspired by the Python Bootcamp challenge.
This program simulates a real coffee machine where the user can:

Choose a drink: espresso, latte, or cappuccino

Insert coins

Receive drink + change

Check available machine resources using report

📌 Features

✔ Menu stored using nested dictionary
✔ Realistic resource management (water, milk, coffee decrease after every order)
✔ Coin system implemented for payments
✔ Refund system if money is insufficient
✔ Change returned if money is more than required
✔ Command loop until the user ends the program

🧠 How It Works

The machine asks:

What would you like? (espresso/latte/cappuccino):


User enters a choice.

If the drink is available and resources are sufficient, the program asks:

Please insert the coins:


After inserting coins, the machine:

Checks whether the payment is enough

Dispenses the drink

Updates available resources

Returns change (if any)

🔧 Built-in Menu
Drink	Water	Milk	Coffee	Cost
Espresso	50 ml	—	18 g	$1.5
Latte	200 ml	150 ml	24 g	$2.5
Cappuccino	250 ml	100 ml	24 g	$3.0
🪙 Accepted Coins

Quarter → 0.25

Dime → 0.10

Nickel → 0.05

Penny → 0.01

🚀 How to Run

Clone the repo:

git clone https://github.com/your-username/coffee-machine.git


Navigate to project folder:

cd coffee-machine


Run the script:

python main.py

📍 Commands Available
Command	Description
espresso	Order espresso
latte	Order latte
cappuccino	Order cappuccino
report	Print machine resources
Ctrl + C	Exit program
📦 Example Output
What would you like? (espresso/latte/cappuccino): latte
Please insert the coins:

How many quarters?: 12
How many dimes?: 0
How many nickels?: 1
How many pennies?: 0

Here is your change: 0.25
Here is your latte ☕
