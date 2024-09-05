
import time
import hashlib

class Block:

    def __init__(self,previous_hash,transactions):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.timestamp = time.time()
        self.hash = self.calculateHash()

    def calculateHash(self):
        content = str(self.timestamp) + str(self.previous_hash) + str(self.nonce) + str(self.transactions)
        hash = hashlib.sha256(content.encode()).hexdigest()
        return hash
    
    def mine_block(self,difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce +=1
            self.hash = self.calculateHash()

        print(f"Block mined with the hash:{self.hash}")

    def __repr__(self):
        return f"Block(timestamp:{self.timestamp}, transactions:{self.transactions}, previous_hash:{self.previous_hash}, hash:{self.hash})"