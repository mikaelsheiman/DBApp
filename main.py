from language import *
from windows import *
from customer import *
from dbmanager import *
import json


def show_window_open(customer_data):

    window = show_window(customer_data)

    while True:

        event, values = window.read()

        print(event, *list(values.values())[:-1])

        if event is lang[Keys.SAVE]:

            key = customer_data['card_number']

            params = list(values.values())[:-1]

            new_data = get_customer_data(key, *params)

            set_data(key, json.dumps(new_data))

        if event is lang[Keys.CANCEL]:

            window.close()
            break


def add_window_open():

    window = add_window()

    while True:

        event, values = window.read()

        if event is lang[Keys.ADD]:

            key = create_card_key(values['discount'])

            params = list(values.values())

            customer_data = get_customer_data(key, *params)

            set_data(key, json.dumps(customer_data))

            window.close()

            show_window_open(customer_data)
            break

        if event is lang[Keys.CANCEL]:

            window.close()
            break


def search_window_open():
    window = search_window()

    while True:
        event, values = window.read()

        if event is lang[Keys.SEARCH]:

            key = int(values['card_number'])

            data = get_data(key)

            customer_data = json.loads(data)

            show_window_open(customer_data)

        if event is lang[Keys.ADD_NEW]:

            window.close()

            add_window_open()

        if event is None:
            break


def main():
    search_window_open()


if __name__ == '__main__':
    main()
