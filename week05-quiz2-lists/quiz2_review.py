'''

Quiz 2 review... a BankAccount class

These code snippets were presented in class to review for Quiz 2.
The only change is that instead of BankTransaction, it's BankAccount.

Beware... as is, the code is full of syntax errors!
'''

class BankAccount:
    def __init__(self, account_type : str, initial_balance : float) -> None:
        self.account_type : str = account_type
        self.balance : float = initial_balance


    def deposit(self, amount : float) -> None:
        '''Adds amount to the account'''

        self.balance += amount

    def __eq__(self, other : object) -> bool:
        if isinstance(other, BankAccount):
            # we can compare two BankAccount objects
            ... # Example: equal if they have the same account number (a unique value)
        else:
            return False

    def __str__(self) -> str:
        # readable/descriptive representation of the object
        return f'{self.account_type}, ${self.balance}'

    def __repr__(self) -> str:
        # unique representation of the object
        # This is the method called by containers (lists)
        return self.__str__() # if we want the same string representation for both functions

def main() -> None:
    t1 = BankAccount("Savings", 500)
    t2 = BankAccount("Checking", 150)
    s : str = "Deposit"

    if (t1 == t2):   # calls t1.__eq__(t2)
        print("oh oh! They shouldn't be equal")
    else:
        print("Good... they are different")


    t1 = t2
    t1.deposit(100)
    t2.deposit(50)

    if (t1 == t2):   # calls t1.__eq__(t2)
        print("Now they are the same due to t1 now an alias of t2")


    if t1 == s:
        print("Comparing a BankAccount to a String... kind of nonsense")

    lst : list[BankAccount] = [t1, t2]

    print(lst) # container uses __repr__() method, rather than __str()__