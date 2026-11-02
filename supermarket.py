print("==================================")
print("WELCOME TO PYTHON MART")
print("===================================")
print("SUPERMARKET PRODUCT LIST")
products = {
  "101": {"name": "sugar", "price": 250},
  "102": {"name": "rice", "price": 300},
  "103": {"name": "cooking rice", "price": 450}
  "104": {"name": "bread", "price": 70},
  "105": {"name": "milk", "price": 65},
  "106": {"name": "flour", "price": 180},
  "107": {"name": "tea leaves", "price": 120},
  "108": {"name": "soap", "price": 100}
}
for code, item in products.items():
print(f"{code} - {item['name']:<12} Ksh {item['price']}")
print("===================================")
cart = []
total = 0
while true:
  code = input("\nEnter product code (or 'done' to finish): ")
  if code.lower() == 'done':
    break
  if code in products:
    qty = int(input(f"How many {products[code]['name']}? "))
    price = products[code]['price'] * qty
    cart.append(f"{products[code]['name']} *{qty} = Ksh {price}")
    total += price
    print(f"Added. Current total: Ksh {total}")
  else:
    print("Invalid code! Try again.")
print("\n========== RECEIPT ==========")
for item in cart:
  print(item)
print(f"----------------------------")
print(f"TOTAL = Ksh {total}")
print("Thank you for shopping!")
print("============================")
