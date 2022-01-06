import json

from vedis import Vedis


class KeyAlreadyExistsError(Exception):
    pass


filename = 'customers_data'
db = Vedis(filename)


def key_exists(key):
    if db.exists(key):
        return True
    return False


def add_data(key, customer_data):
    with db.transaction():
        if db.exists(key):
            raise KeyAlreadyExistsError
        db.set(key, json.dumps(customer_data))


def set_data(key, customer_data):
    with db.transaction():
        db.set(key, json.dumps(customer_data))


def del_data(key):
    if key_exists(key):
        print('YES')
    with db.transaction():
        del db[key]


def get_data(key):
    return json.loads(db.get(key))


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
