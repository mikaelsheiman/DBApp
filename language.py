from enum import Enum


class Keys(Enum):
    CARD_NUMBER = "CARD_NUMBER"
    PHONE_NUMBER = "PHONE_NUMBER"
    ADD = "ADD"
    ADD_NEW = 'ADD_NEW'
    SEARCH = "SEARCH"
    NAME = "NAME"
    CANCEL = 'CANCEL'
    BACK = 'BACK'
    ADDRESS = 'ADDRESS'
    BIRTH_DATE = 'BIRTH_DATE'
    DISCOUNT = 'DISCOUNT'
    ADDITIONAL = 'ADDITIONAL'
    SAVE = 'SAVE'
    MONEY_SPENT = 'MONEY_SPENT'
    NUMBER_OF_VISITS = 'NUMBER_OF_VISITS'
    CHANGE_CARD_NUMBER = 'CHANGE_CARD_NUMBER'
    KEY_ERROR_MESSAGE = 'KEY_ERROR_MESSAGE'
    VALUE_ERROR_MESSAGE = 'VALUE_ERROR_MESSAGE'
    KEY_ALREADY_EXISTS_ERROR_MESSAGE = 'KEY_ALREADY_EXISTS_ERROR_MESSAGE'


PT = {
    Keys.CARD_NUMBER: "Número Cartão",
    Keys.PHONE_NUMBER: "Telemóvel",
    Keys.ADD: "Adicionar",
    Keys.SEARCH: "Procurar",
    Keys.ADD_NEW: 'Adicionar novo cliente',
    Keys.NAME: 'Nome',
    Keys.CANCEL: 'Cancelar',
    #Keys.BACK: "Voltar",
    Keys.ADDRESS: 'Endereço',
    Keys.BIRTH_DATE: 'Data nascimento',
    Keys.DISCOUNT: 'Desconto',
    Keys.ADDITIONAL: 'Adicional',
    Keys.SAVE: 'Guardar',
    Keys.MONEY_SPENT: 'Valor total',
    Keys.NUMBER_OF_VISITS: 'QTD visitas',
    Keys.CHANGE_CARD_NUMBER: 'Alterar',
    Keys.KEY_ERROR_MESSAGE: '(!) Este número é vazio',
    Keys.VALUE_ERROR_MESSAGE: '(!) Formato errado',
    Keys.KEY_ALREADY_EXISTS_ERROR_MESSAGE: '(!) Este número já existe'
}
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
    Keys.ADDITIONAL: 'Дополнительно',
    Keys.SAVE: 'Сохранить',
    Keys.MONEY_SPENT: 'Сумма покупок',
    Keys.NUMBER_OF_VISITS: 'Количество посещений',
    Keys.CHANGE_CARD_NUMBER: 'Изменить',
    Keys.KEY_ERROR_MESSAGE: '(!) Этого номера нет в базе',
    Keys.VALUE_ERROR_MESSAGE: '(!) Неверный формат ввода данных',
    Keys.KEY_ALREADY_EXISTS_ERROR_MESSAGE: '(!) Этот номер уже внесен в базу'
}
