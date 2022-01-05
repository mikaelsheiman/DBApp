import PySimpleGUI as sg
from language import *
lang = RU


def search_window():
    layout = [
        [sg.Radio(lang[Keys.CARD_NUMBER], 'RADIO1', default=True), sg.Radio(lang[Keys.PHONE_NUMBER], "RADIO1")],
        [sg.InputText(key='card_number')],
        [sg.Button(button_text=lang[Keys.SEARCH], size=(15, 1))],
        [sg.Button(button_text=lang[Keys.ADD_NEW], size=(15, 1))],
        [sg.Button(button_text=lang[Keys.CANCEL], size=(15, 1))]
    ]
    return sg.Window(title=lang[Keys.SEARCH], layout=layout)


def add_window():
    layout = [
        # [sg.Text(lang[Keys.CARD_NUMBER], size=(15, 1)), sg.InputText()],
        [sg.Text(lang[Keys.NAME], expand_x=True), sg.InputText()],
        [sg.Text(lang[Keys.PHONE_NUMBER], expand_x=True), sg.InputText()],
        [sg.Text(lang[Keys.ADDRESS], expand_x=True), sg.InputText()],
        [sg.Text(lang[Keys.BIRTH_DATE], expand_x=True), sg.InputText()],
        [sg.Text(lang[Keys.DISCOUNT]), sg.Combo(['10%', '15%', '20%'], default_value='10%', key='discount')],
        [sg.Button(button_text=lang[Keys.ADD], size=(15, 1))],
        [sg.Button(button_text=lang[Keys.CANCEL], size=(15, 1))]
    ]
    return sg.Window(title=lang[Keys.ADD_NEW], layout=layout)


def show_window(data):
    layout = [
        [sg.Text(lang[Keys.CARD_NUMBER], size=(15, 1)), sg.Text(data['card_number'])],
        [sg.Text(lang[Keys.NAME], expand_x=True), sg.InputText(data['name'])],
        [sg.Text(lang[Keys.PHONE_NUMBER], expand_x=True), sg.InputText(data['phone_number'])],
        [sg.Text(lang[Keys.ADDRESS], expand_x=True), sg.InputText(data['address'])],
        [sg.Text(lang[Keys.BIRTH_DATE], expand_x=True), sg.InputText(data['birth_date'])],
        [sg.Text(lang[Keys.DISCOUNT]), sg.Combo(['10%', '15%', '20%'], default_value=data['discount'])],
        [sg.MLine(data['description'])],
        [sg.Text(lang[Keys.NUMBER_OF_VISITS]), sg.InputText(data['number_of_visits']), sg.Button('+1')],
        [sg.Text(lang[Keys.MONEY_SPENT]), sg.InputText(data['money_spent'])],
        [sg.Text(lang[Keys.ADD]), sg.InputText(0), sg.Button(lang[Keys.ADD])],
        [sg.Button(button_text=lang[Keys.SAVE], size=(15, 1))],
        [sg.Button(button_text=lang[Keys.CANCEL], size=(15, 1))],
    ]
    return sg.Window(title=lang[Keys.NAME], layout=layout)
