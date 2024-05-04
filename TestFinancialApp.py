import unittest
from financial_app import FinancialApp, read_data, write_data, display_balance, add_record, edit_record, search_records

class TestFinancialApp(unittest.TestCase):
    def setUp(self):
        # Создание экземпляра приложения для тестирования
        self.app = FinancialApp('test_financial_data.csv')

    def test_read_data(self):
        # Тестирование функции чтения данных из файла
        data = read_data('test_financial_data.csv')
        self.assertIsInstance(data, list)

    def test_write_data(self):
        # Тестирование функции записи данных в файл
        test_data = [{'date': '2022-10-01', 'category': 'income', 'amount': '1000', 'description': 'Test'}]
        write_data('test_financial_data.csv', test_data)
        data = read_data('test_financial_data.csv')
        self.assertEqual(data, test_data)

    def test_display_balance(self):
        # Тестирование функции отображения баланса
        test_data = [{'date': '2022-10-01', 'category': 'income', 'amount': '1000', 'description': 'Test'},
                     {'date': '2022-10-02', 'category': 'expense', 'amount': '500', 'description': 'Test'}]
        balance = display_balance(test_data)
        self.assertEqual(balance, 500)

    def test_add_record(self):
        # Тестирование функции добавления новой записи
        test_data = []
        add_record('2022-10-01', 'income', '1000', 'Test', test_data)
        self.assertEqual(len(test_data), 1)

    def test_edit_record(self):
        # Тестирование функции редактирования записи
        test_data = [{'date': '2022-10-01', 'category': 'income', 'amount': '1000', 'description': 'Test'}]
        edit_record(0, '2022-10-01', 'income', '1200', 'Test', test_data)
        self.assertEqual(test_data[0]['amount'], '1200')

    def test_search_records(self):
        # Тестирование функции поиска записей
        test_data = [{'date': '2022-10-01', 'category': 'income', 'amount': '1000', 'description': 'Test'},
                     {'date': '2022-10-02', 'category': 'expense', 'amount': '500', 'description': 'Test'}]
        results = search_records(test_data, category='income')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['amount'], '1000')

if __name__ == '__main__':
    unittest.main()

