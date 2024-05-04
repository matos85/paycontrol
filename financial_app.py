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
    # Чтение данных из файла и возврат списка словарей
    # Каждый словарь представляет собой одну запись о финансах
    with open(data_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# Функция для записи данных в файл
def write_data(data: List[Dict[str, str]]):
    # Запись данных в файл
    # Принимает: список словарей с данными о финансах
    with open(data_file, 'w', newline='') as file:
        headers = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

# Функция для отображения текущего баланса
def display_balance(data: List[Dict[str, str]]):
    # Отображение текущего баланса
    # Вычисляет общий доход, общие расходы и баланс на основе данных
    total_income = sum(float(row['amount']) for row in data if row['category'] == 'income')
    total_expense = sum(float(row['amount']) for row in data if row['category'] == 'expense')
    total_balance = total_income - total_expense
    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Balance: {total_balance}")

# Функция для добавления новой записи
def add_record(date: str, category: str, amount: str, description: str, data: List[Dict[str, str]]):
    # Добавление новой записи о финансах в список данных
    data.append({'date': date, 'category': category, 'amount': amount, 'description': description})

# Функция для редактирования записи
def edit_record(index: int, date: str, category: str, amount: str, description: str, data: List[Dict[str, str]]):
    # Редактирование существующей записи о финансах в списке данных
    data[index] = {'date': date, 'category': category, 'amount': amount, 'description': description}

# Функция для поиска записей
def search_records(data: List[Dict[str, str]], category: str = None, date: str = None, amount: str = None):
    # Поиск записей о финансах по заданным критериям
    results = data
    if category:
        results = [row for row in results if row['category'] == category]
    if date:
        results = [row for row in results if row['date'] == date]
    if amount:
        results = [row for row in results if row['amount'] == amount]
    return results
