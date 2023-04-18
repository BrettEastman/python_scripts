class Account:

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance
        print("Account owner: {}".format(self.owner))
        print("Account balance: {}".format(self.balance))

    def deposit(self, amountd):

        self.balance = self.balance + amountd
        print("Deposit accepted.")
        print("You have added {} to your balance".format(amountd))

    def withdraw(self, amountw):

        if self.balance - amountw <= 0:
            self.balance = self.balance - amountw
            print("Withdrawal accepted.")
            print("You have withdrawn {} from your balance".format(amountw))
        else:
            print("Sorry, you do not have enough funds.")
