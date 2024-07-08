class Category:
    # initialize class
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # customize returning string
    def __str__(self):
        # declare title
        title = (
            "*" * ((30 - len(self.name)) // 2)
            + self.name
            + "*" * ((30 - len(self.name)) // 2)
        )

        # amount of transactions
        total = 0
        lines = []

        for element in self.ledger:
            # get description and amount from ledger
            description = element["description"][:23]
            amount = element["amount"]
            # add the values to lines array to display them with new lines later
            lines.append(f"{description[0:23]:23} {amount:7>.2f}")
            # count the number of elements
            total += amount

        return f"{title}\n" + "\n".join(lines) + f"\nTotal: {total:.2f}"

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def check_funds(self, amount):
        return self.get_balance() - amount >= 0

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def transfer(self, amount, category):
        w = self.withdraw(amount, f"Transfer to {category.name}")
        if not w:
            return False
        category.deposit(amount, f"Transfer from {self.name}")
        return True


def create_spend_chart(categories):
    category_names = []
    withdrawals = []

    for category in categories:
        category_withdrawal = 0

        for item in category.ledger:
            if item["amount"] < 0:
                category_withdrawal += item["amount"] * -1

        category_names.append(category.name)
        withdrawals.append(category_withdrawal)

    total_withdrawal = sum(withdrawals)

    percentages = []

    for withdrawal in withdrawals:
        percentages.append((withdrawal / total_withdrawal) * 100)

    result = ""

    result += "Percentage spent by category" + "\n"

    # table
    for i in range(100, -10, -10):
        result += f"{i:3}|"
        for percentage in percentages:
            if percentage >= i:
                result += " o "
            else:
                result += "   "
        result += " \n"

    # middle line
    result += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # category names
    max_length_name = max([len(name) for name in category_names])
    for i in range(max_length_name):
        result += "     "
        for name in category_names:
            if len(name) > i:
                result += name[i] + "  "
            else:
                result += "   "
        if i != max_length_name - 1:
            result += "\n"

    return result


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)
