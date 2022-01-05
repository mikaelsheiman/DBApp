from vedis import Vedis
from customer import Customer

filename = 'customers_data'
db = Vedis(filename)


def set_data(key: int, custumer_data: Customer):
    db.set(key, custumer_data)


def get_data(key: int):
    return db.get(key)


def create_card_key():
    for i in range(1, 300):
        if not db.exists(i):
            return i
    else:
        return -1
