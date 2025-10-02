class BankAccount():
  def __init__(self, initial_balance=0):
    self.account_balance = initial_balance

  def deposit (self,amount):
    if amount > 0:
      self.account_balance += amount
      print(f"You have successfully deposited: ${amount}")
    else:
      print(f"Deposit amount must be positive")

  def withdraw(self, amount):
    if amount > self.account_balance:
      print(f"The amount exceeds the account balance")
    elif amount <= self.account_balance:
      self.account_balance -= amount
      print(f"You have successfully withdrawn: ${amount}")
    else:
      print(f"Withdrawal amount must be positive")

  def display_balance(self):
    """Show current account balance"""
    print(f"Current Balance: ${self.account_balance}")    
