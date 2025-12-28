from collections import defaultdict


def category_report(expenses):
    summary = defaultdict(float)

    for expense in expenses:
        category = expense[1]
        amount = float(expense[2])
        summary[category] += amount

    print("\n--- Category-wise Report ---")
    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")
