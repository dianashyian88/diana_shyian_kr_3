import json

from datetime import datetime


def get_data():
    """Получение данных о транзакциях из файла json"""
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data):
    """Отбор выполненных транзакций"""
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data


def get_last_values(data, count_last_values):
    """Получение 5 последний транзакций"""
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    data = data[:count_last_values]
    return data


def get_formatted_data(data):
    """Форматирование данных о транзакциях в соответствии с ТЗ"""
    formatted_data = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = row['description']
        recipient = row['to'].split()
        to_bill = recipient.pop(-1)
        if recipient[0] != 'Счет':
            to_bill = f"{to_bill[:4]} {to_bill[4:6]}** **** {to_bill[-4:]}"
            to_info = ' '.join(recipient)
        else:
            to_bill = f"**{to_bill[-4:]}"
            to_info = ' '.join(recipient)
        operations_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"
        if 'from' in row:
            sender = row['from'].split()
            from_bill = sender.pop(-1)
            if sender[0] != 'Счет':
                from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
                from_info = ' '.join(sender)
            else:
                from_bill = f"**{from_bill[-4:]}"
                from_info = ' '.join(sender)
        else:
            from_info, from_bill = '', ''
        formatted_data.append(f"""\
{date} {description}
{from_info} {from_bill} -> {to_info} {to_bill}
{operations_amount}""")
    return formatted_data
