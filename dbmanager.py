from vedis import Vedis

filename = 'customers_data'
db = Vedis(filename)


def set_data(key, customer_data):
    with db.transaction():
        db.set(key, customer_data)


def get_data(key):
    return db.get(key)


def create_card_key(discount_type):
    if discount_type == '20%':
        for i in range(1, 30):
            if not db.exists(i):
                return i
        else:
            return -1
    elif discount_type == '15%':
        for i in range(31, 121):
            if not db.exists(i):
                return i
        else:
            return -1
    elif discount_type == '10%':
        for i in range(121, 301):
            if not db.exists(i):
                return i
        else:
            return -1
