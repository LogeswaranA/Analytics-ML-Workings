import hashlib
import time

class Block:

    def __init__(self,previous_hash,transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content =  str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(block_content.encode()).hexdigest()
    
    def mine_block(self,difficulty):
        print(f"Starting to mine block. Difficulty: {difficulty}")
        target = '0' * difficulty
        print("self.target:::",target)
        max_iterations = 100000
        while self.hash[:difficulty] != target:
            self.nonce +=1
            self.hash = self.calculate_hash()

            print(f"Trying hash with nonce: {self.nonce} and hash : {self.hash}")
            if self.nonce >= max_iterations:
                print(f"Exceed the maximum iterations, stopping the mining operations!!")
                break

            if self.nonce % 10000 == 0:
                print(f"Current Nonce: {self.nonce}, hash:{self.hash}")

        print(f"Block minted with hash value {self.hash}")
    
    def __repr__(self):
        return f"Block(timestamp:{self.timestamp}, transactions:{self.transactions}, previous_hash:{self.previous_hash}, hash:{self.hash})"


