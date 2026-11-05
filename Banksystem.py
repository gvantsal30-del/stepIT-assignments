from functools import wraps

SYSTEM_ACTIVE = True

GLOBAL_AUDIT_LOG = []

def audit_system(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if SYSTEM_ACTIVE:
            GLOBAL_AUDIT_LOG.append(f"გამოძახებულია ფუნქცია: {func.__name__}")

        return func(*args, **kwargs)

    return wrapper

def create_account_generator(initial_balance):

    balance = initial_balance
    transaction_id = 0

    @audit_system
    def transaction(amount):

        nonlocal balance, transaction_id

        transaction_id += 1

        balance += amount

        yield (transaction_id, balance)

    return transaction

account = create_account_generator(10000)

print(next(account(2500)))
print(next(account(-100)))
print(next(account(50)))
print(next(account(1589)))

print(GLOBAL_AUDIT_LOG)
