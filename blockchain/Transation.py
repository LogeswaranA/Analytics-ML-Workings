import time

class Transaction:

    def __init__(self,sender,receiver,amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()

    def __repr__(self):
        return f"Transaction(sender:{self.sender},receiver:{self.receiver},amount:{self.amount},timestamp:{self.timestamp})"