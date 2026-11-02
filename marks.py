name = input("Enter name: ")
maths = float(input("Maths: "))
english = float(input("English: "))
accounting = float(input("Accountant: "))
total = maths + english + accounting
avg = total / 3
print(f"Student {name} - Total: {total}, Average: {avg:.1f}")
if avg >= 70:
  print("Grade A")
elif avg >= 60:
  print("Grade B")
elif avg >= 50:
  print("Grade C")
else:
  print("Needs improvement")
