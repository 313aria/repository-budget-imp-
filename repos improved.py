income = float(input("Enter your monthly income: "))
expenses = {}  # dictionary to store categories and amounts

while True:
    expense = input("Enter an expense (or type 'done' to finish): ")
    if expense.lower() == "done":
        break

    amount = float(expense)
    category = input("Category: ")

    # add to the correct category
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

# calculate total
total_expenses = sum(expenses.values())
balance = income - total_expenses

# print results
print("\n----- Budget Summary -----")
print(f"Total Income: ${income}")
for category, amount in expenses.items():
    print(f"{category}: ${amount}")
print(f"Total Expenses: ${total_expenses}")
print(f"Remaining Balance: ${balance}")