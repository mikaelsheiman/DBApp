import PySimpleGUI as sg
from language import *

lang = RU


def calculate_discount(key):
    discount = ''
    if key in range(1, 30):
        discount = '20%'
    elif key in range(31, 121):
        discount = '15%'
    elif key in range(121, 301):
        discount = '10%'
    return discount


class UserDefines:
    def ErrorMessege(self):
        return sg.Text(text='', text_color='red', key='-ERROR_MESSAGE-', visible=False)


ud = UserDefines()


def search_window():
    layout = [
        [sg.R(lang[Keys.CARD_NUMBER], 'RADIO1', default=True), sg.R(lang[Keys.PHONE_NUMBER], 'RADIO1')],
        [sg.InputText(key='-CARD_NUMBER-')],
        [sg.Button(lang[Keys.SEARCH], size=(15, 1))],
        [sg.Button(lang[Keys.ADD_NEW], size=(15, 1))],
        [sg.Button(lang[Keys.CANCEL], size=(15, 1))],
        [ud.ErrorMessege()],
    ]
    return sg.Window(title=lang[Keys.SEARCH], layout=layout)


def add_window():
    layout = [
        [sg.Text(lang[Keys.CARD_NUMBER], size=(15, 1)), sg.InputText(key='-CARD_NUMBER-')],
        [sg.Text(lang[Keys.NAME], size=(15, 1)), sg.InputText(key='-NAME-')],
        [sg.Text(lang[Keys.PHONE_NUMBER], size=(15, 1)), sg.InputText(key='-PHONE_NUMBER-')],
        [sg.Text(lang[Keys.ADDRESS], size=(15, 1)), sg.InputText(key='-ADDRESS-')],
        [sg.Text(lang[Keys.BIRTH_DATE], size=(15, 1)), sg.InputText(key='-BIRTH_DATE-')],
        [ud.ErrorMessege()],
        [sg.Button(lang[Keys.ADD], size=(15, 1))],
        [sg.Button(lang[Keys.CANCEL], size=(15, 1))],
    ]
    return sg.Window(title=lang[Keys.ADD_NEW], layout=layout)


def show_window(data):
    discount = calculate_discount(data['card_number'])
    layout = [
        [sg.T(lang[Keys.CARD_NUMBER], size=(15, 1)), sg.T(data['card_number'], key='-CARD_NUMBER-'),
         sg.B(lang[Keys.CHANGE_CARD_NUMBER])],
        [sg.Text(lang[Keys.NAME], size=(15, 1)), sg.InputText(data['name'])],
        [sg.Text(lang[Keys.PHONE_NUMBER], size=(15, 1)), sg.InputText(data['phone_number'])],
        [sg.Text(lang[Keys.ADDRESS], size=(15, 1)), sg.InputText(data['address'])],
        [sg.Text(lang[Keys.BIRTH_DATE], size=(15, 1)), sg.InputText(data['birth_date'])],
        [sg.T(lang[Keys.DISCOUNT]), sg.T(discount, text_color='yellow', key='-DISCOUNT-')],
        [sg.Text(lang[Keys.ADDITIONAL])],
        [sg.MLine(data['description'])],
        [sg.T(lang[Keys.NUMBER_OF_VISITS], size=(15, 1)), sg.I(data['number_of_visits'], key='-NUMBER_OF_VISITS-'),
         sg.B('+1')],
        [sg.Text(lang[Keys.MONEY_SPENT], size=(15, 1)), sg.InputText(data['money_spent'], key='-MONEY_SPENT-')],
        [sg.Text(lang[Keys.ADD], size=(15, 1)), sg.InputText(0, key='-ADD-'), sg.Button(lang[Keys.ADD])],
        [sg.Button(button_text=lang[Keys.SAVE], size=(15, 1))],
        [sg.Button(button_text=lang[Keys.CANCEL], size=(15, 1))],
        [ud.ErrorMessege()],
    ]
    return sg.Window(title=data["name"], layout=layout)


def change_card_number_window(card_number):
    layout = [
        [sg.Text(lang[Keys.CARD_NUMBER])],
        [sg.InputText(card_number, key='-CARD_NUMBER-')],
        [sg.Button(lang[Keys.CHANGE_CARD_NUMBER], size=(15, 1)), sg.Button(lang[Keys.CANCEL], size=(15, 1))],
        [ud.ErrorMessege()],
    ]
    return sg.Window(title=lang[Keys.CHANGE_CARD_NUMBER], layout=layout)
