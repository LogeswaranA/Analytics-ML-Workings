
from Block import Block

class Blockchain:

    def __init__(self):
        self.chain = [self.createGenesisBlock()]
        self.difficulty = 2
        self.pending_transactions = []

    def createGenesisBlock(self):
        return Block("0",[])
    
    def get_latest_block(self):
        return self.chain[-1]

    def create_transaction(self,transaction):
        print(f"Creating transaction: {transaction}")
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self):
        if len(self.pending_transactions) == 0:
            print("No transactions to mine.")
            return
        print("Mining new block with pending transactions...")
        new_block = Block(self.get_latest_block().hash, self.pending_transactions)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = []

    def isChainValid(self):
        for i in range(1,len(self.chain)):

            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False
            
        return True
    

    def __repr__(self) -> str:
        return f"Blockchain(chain:{self.chain})"
