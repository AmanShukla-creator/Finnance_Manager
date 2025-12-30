class ExpenseData:
    def __init__(self, date, category, amount, description, time):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description
        self.time = time

    def to_list(self):
        return [self.date, self.category, self.amount, self.description]

print("ExpenseData class loaded")
