from Transation import Transaction
from Blockchain import Blockchain

if __name__ == "__main__":

    myblockchain = Blockchain()

    myblockchain.create_transaction(Transaction("Alice","Bob",50))
    myblockchain.create_transaction(Transaction("Bob","Charlie",40))

    myblockchain.mine_pending_transactions()
    print("Blockchain after mining the first block:")

    print(myblockchain)

    myblockchain.create_transaction(Transaction("Charlie","Alice",15))
    myblockchain.mine_pending_transactions()

    print(myblockchain)

    print(f"is my chain valid? : {myblockchain.isChainValid()}")