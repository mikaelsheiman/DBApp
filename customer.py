from enum import Enum


class Discount(Enum):
    TEN = 0.1
    FIFTEEN = 0.15
    TWENTY = 0.20


class Customer:
    def __init__(self,
                 card_number: int,
                 name: str,
                 phone_number: str,
                 address: str,
                 birth_date: str,
                 discount: float = Discount.TEN.value):
        self.card_number = card_number
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.birth_date = birth_date
        self.discount = discount
        self.number_of_visits = 0
        self.money_spent = 0
        self.description = ''

    def add_description(self, description: str):
        self.description = description

    def increase_visits(self):
        self.number_of_visits += 1

    def increase_spent(self, spent):
        self.money_spent += spent
