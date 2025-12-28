def validate_amount(amount):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
        return amount
    except ValueError:
        print("Invalid amount. Please enter a positive number.")
        return None
