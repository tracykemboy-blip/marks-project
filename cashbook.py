print("=== DAILY CASHBOOK ===")
income = float(input("Enter today's total sales (KES): "))
expenses = float(input("Enter today's expenses (KES): "))
profit = income - expenses
print("\n--- SUMMARY ---")
print(f"Sales: KES {income}")
print(f"Expenses: KES {expenses}")
print(f"Profit: KES {profit}")
if profit > 0:
  print("Result: You made profit today! Keep going!")
elif profit == 0:
  print("Result: You broke even.")
else:
  print("Result: You made a loss today. Check expenses.")
  
  
