from language import *
from windows import *
from customer import *
from dbmanager import *


def show_window_open(customer_data):
    while True:
        event, value =


def add_window_open():
    event, values = add_window.read()
    add_window.close()
    if event is lang[Keys.CANCEL]:
        search_window_open()
    if event is lang[Keys.ADD]:
        customer_data = Customer(*values)
        key = create_card_key()
        set_data(key, customer_data)
        add_window.close()


def search_window_open():
    while True:
        event, values = search_window.read()
        if event is lang[Keys.SEARCH]:
            customer_data = get_data(values[0])




def main():
    while True:  # The Event Loop
        event, values = search_window.read()
        if event is lang[Keys.ADD_NEW]:
            add_window_open()


if __name__ == '__main__':
    main()
