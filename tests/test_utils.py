from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    assert get_filtered_data(test_data[:2]) == [
        {'id': 114832369,
         'state': 'EXECUTED',
         'date': '2019-11-07T06:17:14.634890',
         'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации',
         'from': 'Visa Classic 2842878893689012',
         'to': 'Счет 35158586384610753655'}
    ]


def test_get_last_values(test_data):
    data = get_last_values(test_data, 3)
    assert [x['date'] for x in data] == ['2019-12-08T22:46:21.935582',
                                         '2019-12-07T22:46:21.935582',
                                         '2019-11-19T09:22:25.899614']


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data[:4])
    assert data == ['08.12.2019 Открытие вклада\n  -> Счет **5907\n41096.24 USD',
                    '07.11.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD',
                    '19.11.2019 Перевод с карты на карту\nMaestro 7810 84** **** 5568 -> MasterCard 3152 47** **** 5065\n30153.72 руб.',
                    '13.11.2019 Перевод со счета на счет\nСчет **9794 -> Счет **8125\n62814.53 руб.']
