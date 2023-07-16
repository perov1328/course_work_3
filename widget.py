
#Загрузка функций из директории utils
from utils.utils import *

#Переменная с обозначением файла где хранится список всех операций
transactions = "operations.json"

#Запуск программы
transactions_list = get_list_of_transactions(transactions)
transactions_matching = get_matching_transactions(transactions_list)
transactions_executed = get_executed_transactions(transactions_matching)
transactions_latest = get_latest_transactions(transactions_executed)

#Вывод 5 последних подтвержденных транзакций
print(information_output(transactions_latest))
