import json


def get_list_of_transactions(filename):
    """
    Получение списка всех транзакций
    """
    with open(filename) as file:
        transactions = json.loads(file.read())
    return transactions


def get_matching_transactions(transactions):
    """
    Отбор транзакций содержащих поля для вывода пользователю
    """
    matching_transaction = []
    for el in transactions:
        if 'state' in el:
            if 'date' in el:
                if 'description' in el:
                    if 'from' in el:
                        if 'to' in el:
                            if 'operationAmount' in el:
                                matching_transaction.append(el)
    return matching_transaction


def get_executed_transactions(transactions):
    """
    Получение списка успешных транзакций
    """
    successful_transactions = [el for el in transactions if el['state'] == "EXECUTED"]
    return successful_transactions


def get_latest_transactions(transactions):
    """
    Сортировка всех транзакций по дате и вывод 5 последних
    """
    result = sorted(transactions, key=lambda x:x['date'])
    return result[-5:][::-1]


def information_output(transactions):
    """
    Подготовка информации для пользователя согласно требованиям
    """
    result = ""
    for el in transactions:
        original_date = el['date'][0:10]
        date = f"{original_date[-2:]}.{original_date[-5:-3]}.{original_date[:4]}"
        a = el["from"]
        to_from = a[0:-16] + " " + a[-16:-12] + " " + a[-12:-10] + "** ****" + a[-4:]
        to_to = el['to'][0:-20] + "**" + el['to'][-4:]
        answer = f"""{date} {el['description']}
{to_from} -> {to_to}
{el['operationAmount']['amount']} {el['operationAmount']['currency']['name']}\n\n"""
        result += answer
    return result

