class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = (
            "*" * ((30 - len(self.name)) // 2)
            + self.name
            + "*" * ((30 - len(self.name)) // 2)
        )
        lines = []
        total = 0
        for element in self.ledger:
            description = element["description"][:23]
            amount = element["amount"]
            lines.append(f"{description[0:23]:23} {amount:7>.2f}")
            total += amount

        return f"{title}\n" + "\n".join(lines) + f"\nTotal: {total:.2f}"

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def check_funds(self, amount):
        return self.get_balance() - amount >= 0

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        w = self.withdraw(amount, f"Transfer to {category.name}")
        if not w:
            return False
        category.deposit(amount, f"Transfer from {self.name}")
        return True


def create_spend_chart(categories):
    pass


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)
