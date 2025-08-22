income = float(input("Enter your monthly income: "))
expenses = 0

while True:
    expense = input("Enter an expense (or type 'done' to finish): ")
    if expense.lower() == "done":
        break
    else:
        expenses += float(expense)

balance = income - expenses

print("\n----- Budget Summary -----")
print(f"Total Income: ${income}")
print(f"Total Expenses: ${expenses}")
print(f"Remaining Balance: ${balance}")
