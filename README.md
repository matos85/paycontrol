# paycontrol

## 1. Запуск программы Windows:
    1.1.  Запуск программы:
   - Сохраните предоставленный файл financial_app.py.
   - Откройте командную строку в Windows.
   - Перейдите в каталог, содержащий файл financial_app.py.
   - Запустите программу, введя команду python financial_app.py.
(
не забудьте импортировать файл from financial_app import *  для financial_app
и
from OOP_financial_app import * для ООП версии
)
  
     1.2 Запуск программы Linux:
   - Сохраните предоставленный вами файл financial_app.py.
   - Откройте терминал в Linux.
   - Перейдите в каталог, содержащий файл financial_app.py.
   - Запустите программу, введя команду python3 financial_app.py.

## 2. Основные возможности программы:
   - Вывод баланса:
     - Показать текущий баланс, а также отдельно доходы и расходы.
     - Эта функциональность реализована с помощью функции display_balance(data) в коде.
   - Добавление записи:
     - Возможность добавления новой записи о доходе или расходе.
     - Используйте функцию add_record(date, category, amount, description, data), передавая необходимые параметры.
   - Редактирование записи:
     - Изменение существующих записей о доходах и расходах.
     - Для этого используйте функцию edit_record(index, date, category, amount, description, data), указав индекс записи для редактирования и новые значения.
   - Поиск по записям:
     - Поиск записей по категории, дате или сумме.
     - Вызовите функцию search_records(data, category, date, amount) с необходимыми параметрами для поиска.

## 3. Запись данных:
   - После внесения изменений в данные (добавления, редактирования или удаления записей), данные должны быть записаны обратно в файл с помощью функции write_data(data).

## Пример использования функций
data = read_data()

Добавление новой записи
add_record('2022-10-01', 'income', '1000', 'Salary', data)

Редактирование записи
edit_record(0, '2022-10-01', 'income', '1200', 'Salary', data)

Вывод текущего баланса
display_balance(data)

Поиск записей по критериям
results = search_records(data, category='income', date='2022-06-01', amount='1000')
print(results)

Запись данных обратно в файл
write_data(data)

## Для ООП:
Пример использования класса FinancialApp
app = FinancialApp()
data = app.read_data()

Добавление новой записи
app.add_record('2022-10-01', 'income', '1000', 'Salary', data)

Редактирование записи
app.edit_record(0, '2022-10-01', 'income', '1200', 'Salary', data)

Вывод текущего баланса
app.display_balance(data)

Поиск записей по критериям
results = app.search_records(data, category='income', date='2022-06-01', amount='1000')
print(results)

Запись данных обратно в файл
app.write_data(data)



## Тесты для TestFinancialApp.py
