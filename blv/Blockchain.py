import time
from Block import Block
from Transaction import Transaction

class Blockchain:

    def __init__(self):
        self.chain = [self.createGenesisBlock()]
        self.difficulty = 1
        self.pending_transactions =[]

    def createGenesisBlock(self):
        return Block("0",[])
    
    def createTransactions(self,transaction):
        self.pending_transactions.append(transaction)
    
    def getLatestBlock(self):
        return self.chain[-1]

    def mine_pending_transactions(self):
        new_block = Block(self.getLatestBlock(),self.pending_transactions)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = []

    def isMyChainValid(self):

        for i in range(1,len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i-1]

            if currentBlock.hash != currentBlock.calculateHash():
                return False
            
            if currentBlock.previous_hash != previousBlock.hash:
                return False
            
        return True
    
    def __repr__(self):
        return f"Blockchain(Chain:{self.chain})"
    


if __name__ == "__main__":
    blockchain = Blockchain()

    blockchain.createTransactions(Transaction("Alice","Bob",100))
    blockchain.createTransactions(Transaction("Bob","Charlie",50))
    blockchain.mine_pending_transactions()

    print(blockchain)
