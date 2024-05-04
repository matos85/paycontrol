import csv
import os
from typing import List, Dict

class FinancialApp:
    def __init__(self, data_file='financial_data.csv'):
        self.data_file = data_file
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['date', 'category', 'amount', 'description'])

    def read_data(self) -> List[Dict[str, str]]:
        with open(self.data_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data

    def write_data(self, data: List[Dict[str, str]]):
        with open(self.data_file, 'w', newline='') as file:
            headers = ['date', 'category', 'amount', 'description']
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

    def display_balance(self, data: List[Dict[str, str]]):
        total_income = sum(float(row['amount']) for row in data if row['category'] == 'income')
        total_expense = sum(float(row['amount']) for row in data if row['category'] == 'expense')
        total_balance = total_income - total_expense
        print(f"Total Income: {total_income}")
        print(f"Total Expense: {total_expense}")
        print(f"Balance: {total_balance}")

    def add_record(self, date: str, category: str, amount: str, description: str, data: List[Dict[str, str]]):
        data.append({'date': date, 'category': category, 'amount': amount, 'description': description})

    def edit_record(self, index: int, date: str, category: str, amount: str, description: str, data: List[Dict[str, str]]):
        data[index] = {'date': date, 'category': category, 'amount': amount, 'description': description}

    def search_records(self, data: List[Dict[str, str]], category: str = None, date: str = None, amount: str = None):
        results = data
        if category:
            results = [row for row in results if row['category'] == category]
        if date:
            results = [row for row in results if row['date'] == date]
        if amount:
            results = [row for row in results if row['amount'] == amount]
        return results



