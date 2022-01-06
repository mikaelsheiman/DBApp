
from windows import *
from customer import *
from dbmanager import *


def show_window_open(customer_data):
    print(customer_data)
    window = show_window(customer_data)

    while True:

        event, values = window.read()
        window['-ERROR_MESSAGE-'].update(visible=False)

        if event is lang[Keys.CHANGE_CARD_NUMBER]:
            window.disable()

            customer_data = change_card_number_window_open(customer_data)

            window.enable()

            window['-CARD_NUMBER-'].update(customer_data['card_number'])
            window['-DISCOUNT-'].update(calculate_discount(customer_data['card_number']))

        elif event == '+1':
            try:
                number_of_visits = int(values['-NUMBER_OF_VISITS-'])

            except ValueError:
                window['-ERROR_MESSAGE-'].update(lang[Keys.VALUE_ERROR_MESSAGE], visible=True)

            else:
                number_of_visits += 1

                window['-NUMBER_OF_VISITS-'].update(number_of_visits)

        elif event is lang[Keys.ADD]:
            try:
                money_spent = float(values['-MONEY_SPENT-'])

                to_add = float(values['-ADD-'])

            except ValueError:
                window['-ERROR_MESSAGE-'].update(lang[Keys.VALUE_ERROR_MESSAGE], visible=True)

            else:
                money_spent += to_add

                window['-MONEY_SPENT-'].update(money_spent)

        elif event is lang[Keys.SAVE]:
            try:
                key = customer_data['card_number']

                params = list(values.values())[:-1]

                new_data = get_customer_data(key, *params)

                set_data(key, new_data)

            except ValueError:
                window['-ERROR_MESSAGE-'].update(lang[Keys.VALUE_ERROR_MESSAGE], visible=True)

            except KeyError:
                window['-ERROR_MESSAGE-'].update(lang[Keys.KEY_ALREADY_EXISTS_ERROR_MESSAGE], visible=True)

        if event in (lang[Keys.CANCEL], sg.WINDOW_CLOSED):

            window.close()
            break


def change_card_number_window_open(customer_data):
    old_key = customer_data['card_number']

    new_data = customer_data.copy()

    window = change_card_number_window(old_key)

    while True:
        event, values = window.read()
        window['-ERROR_MESSAGE-'].update(visible=False)

        if event is lang[Keys.CHANGE_CARD_NUMBER]:
            try:
                new_key = int(values['-CARD_NUMBER-'])

                new_data['card_number'] = new_key

                add_data(new_key, new_data)

            except ValueError:
                window['-ERROR_MESSAGE-'].update(lang[Keys.VALUE_ERROR_MESSAGE], visible=True)

            except KeyAlreadyExistsError:
                window['-ERROR_MESSAGE-'].update(lang[Keys.KEY_ALREADY_EXISTS_ERROR_MESSAGE], visible=True)

            else:
                del_data(old_key)
                window.close()
                return new_data

        if event in (lang[Keys.CANCEL], sg.WINDOW_CLOSED):
            window.close()
            return customer_data


def add_window_open():

    window = add_window()

    while True:

        event, values = window.read()
        window['-ERROR_MESSAGE-'].update(visible=False)

        if event is lang[Keys.ADD]:

            try:
                key = int(values['-CARD_NUMBER-'])

                params = list(values.values())

                customer_data = get_customer_data(*params)

            except KeyAlreadyExistsError:
                window['-ERROR_MESSAGE-'].update(lang[Keys.KEY_ALREADY_EXISTS_ERROR_MESSAGE], visible=True)

            except ValueError:
                window['-ERROR_MESSAGE-'].update(lang[Keys.VALUE_ERROR_MESSAGE], visible=True)

            else:
                set_data(key, customer_data)

                window.close()

                show_window_open(customer_data)
                break

        elif event in (lang[Keys.CANCEL], sg.WINDOW_CLOSED):

            window.close()
            break


def search_window_open():
    window = search_window()

    while True:
        event, values = window.read()
        window['-ERROR_MESSAGE-'].update(visible=False)

        if event is lang[Keys.SEARCH]:
            try:
                key = int(values['-CARD_NUMBER-'])

                customer_data = get_data(key)

            except KeyError:
                window['-ERROR_MESSAGE-'].update(lang[Keys.KEY_ERROR_MESSAGE], visible=True)

            except ValueError:
                window['-ERROR_MESSAGE-'].update(lang[Keys.VALUE_ERROR_MESSAGE], visible=True)

            else:
                window.disable()
                window.hide()

                show_window_open(customer_data)

                window.un_hide()
                window.enable()

        elif event is lang[Keys.ADD_NEW]:
            window.disable()
            window.hide()

            add_window_open()

            window.un_hide()
            window.enable()

        if event in (lang[Keys.CANCEL], sg.WINDOW_CLOSED):
            break


def main():
    search_window_open()


if __name__ == '__main__':
    main()
