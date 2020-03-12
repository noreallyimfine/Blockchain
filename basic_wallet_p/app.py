import time
from miner import proof_of_work, valid_proof

class User:
    def __init__(self, uid):
        self.uid = uid
        self.balance = 0
        self.transactions = []

    def change_uid(self):
        new_uid = input("Enter a new name: ")
        self.uid = new_uid

    def get_balance(self):
        return f"\n{self.uid} has a balance of {self.balance} coins."

    def get_transactions(self):
        return f"\nList of transactions by {self.uid}:\n {self.transactions}"

    def mine_coin(self):
        pass

def choose_action():
    choices = [0, 1,2, 3, 4]
    while True:
        action = input(
"""Choose an option:\n
Check Balance (1)\n
View Transactions (2)\n
Change Name (3)\n
Mine a Coin (4)\n
Quit (0):\n"""
)
        if int(action) in choices:
            break
    return int(action)

if __name__ == "__main__":
    name = input("Choose a username: ")
    user = User(name)
    print(user.uid)
    print(user.get_balance())
    print(user.get_transactions())
    while True:
        action = choose_action()
        if action == 1:
            print(user.get_balance())
        elif action == 2:
            print(user.get_transactions())
        elif action == 3:
            user.change_uid()
            print(f"\nName changed to {user.uid}")
        elif action == 4:
            # get last block from server
            # search for proof
            # post proof and id to server
            # get response
            
        elif action == 0:
            break
        time.sleep(3)
