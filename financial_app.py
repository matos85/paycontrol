import csv
import os
from typing import List, Dict

# Определение имени файла для хранения данных
data_file = 'financial_data.csv'

# Проверка наличия файла данных. Если файл отсутствует, создаем его с заголовками
if not os.path.exists(data_file):
    with open(data_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['date', 'category', 'amount', 'description'])

# Функция для чтения данных из файла
def read_data() -> List[Dict[str, str]]:
    with open(data_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# Функция для записи данных в файл
def write_data(data: List[Dict[str, str]]):
    with open(data_file, 'w', newline='') as file:
        headers = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

# Функция для отображения текущего баланса
def display_balance(data: List[Dict[str, str]]):
    total_income = sum(float(row['amount']) for row in data if row['category'] == 'income')
    total_expense = sum(float(row['amount']) for row in data if row['category'] == 'expense')
    total_balance = total_income - total_expense
    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Balance: {total_balance}")

# Функция для добавления новой записи
def add_record(date: str, category: str, amount: str, description: str, data: List[Dict[str, str]]):
    data.append({'date': date, 'category': category, 'amount': amount, 'description': description})

# Функция для редактирования записи
def edit_record(index: int, date: str, category: str, amount: str, description: str, data: List[Dict[str, str]]):
    data[index] = {'date': date, 'category': category, 'amount': amount, 'description': description}

# Функция для поиска записей
def search_records(data: List[Dict[str, str]], category: str = None, date: str = None, amount: str = None):
    results = data
    if category:
        results = [row for row in results if row['category'] == category]
    if date:
        results = [row for row in results if row['date'] == date]
    if amount:
        results = [row for row in results if row['amount'] == amount]
    return results
#
# # Пример использования функций
# data = read_data()
#
# # Добавление новой записи
# add_record('2022-10-01', 'income', '1000', 'Salary', data)
#
# # Редактирование записи
# edit_record(0, '2022-10-01', 'income', '1200', 'Salary', data)
#
# # Вывод текущего баланса
# display_balance(data)
#
# # Поиск записей по критериям
# results = search_records(data, category='income', date='2022-06-01', amount='1000')
# print(results)
#
# # Запись данных обратно в файл
# write_data(data)
