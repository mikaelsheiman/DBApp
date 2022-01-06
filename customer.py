def get_customer_data(card_number: int,
                      name: str,
                      phone_number: str,
                      address: str,
                      birth_date: str,
                      description: str = '',
                      number_of_visits: int = 0,
                      money_spent: float = 0):
    return {
        'card_number': int(card_number),
        'name': str(name),
        'phone_number': str(phone_number),
        'address': str(address),
        'birth_date': str(birth_date),
        'description': str(description),
        'number_of_visits': str(number_of_visits),
        'money_spent': float(money_spent),
    }
