from enum import Enum


class Keys(Enum):
    CARD_NUMBER = "CARD_NUMBER"
    PHONE_NUMBER = "PHONE_NUMBER"
    ADD = "ADD"
    ADD_NEW = 'ADD_NEW'
    SEARCH = "SEARCH"
    NAME = "NAME"
    CANCEL = 'CANCEL'
    ADDRESS = 'ADDRESS'
    BIRTH_DATE = 'BIRTH_DATE'
    DISCOUNT = 'DISCOUNT'
    SAVE = 'SAVE'
    MONEY_SPENT = 'MONEY_SPENT'
    NUMBER_OF_VISITS = 'NUMBER_OF_VISITS'

EN = {
    Keys.CARD_NUMBER: "Card number",
    Keys.PHONE_NUMBER: "Phone number",
    Keys.ADD: "Add",
    Keys.SEARCH: "Search",
    Keys.ADD_NEW: 'Add new',
    Keys.NAME: 'Name',
    Keys.CANCEL: 'Cancel',
}

RU = {
    Keys.CARD_NUMBER: "Номер карты",
    Keys.PHONE_NUMBER: "Номер телефона",
    Keys.ADD: "Добавить",
    Keys.SEARCH: "Найти",
    Keys.ADD_NEW: 'Добавить новый',
    Keys.NAME: 'ФИО',
    Keys.CANCEL: 'Отмена',
    Keys.ADDRESS: 'Адрес',
    Keys.BIRTH_DATE: 'Дата рождения',
    Keys.DISCOUNT: 'Скидка',
    Keys.SAVE: 'Сохранить',
    Keys.MONEY_SPENT: 'Сумма покупок',
    Keys.NUMBER_OF_VISITS: 'Количество посещений',

}
