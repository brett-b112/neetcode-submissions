class BankAccount:
    total_accounts = 0    # Class attribute: Shared by ALL accounts
    total_balance = 0     # Class attribute: Tracks bank's total money

    def __init__(self, name: str, balance: float):
        self.name = name        # Instance: Each account has unique owner
        self.balance = balance  # Instance: Each account has unique balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance


# TODO: Create two accounts
bobs_account = BankAccount("Bob", 2000)
alice_account = BankAccount("Alice", 1000)
# TODO: Print the information using the mentioned format
print(f"Alice's balance: ${alice_account.balance}")
print(f"Bob's balance: ${bobs_account.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")

