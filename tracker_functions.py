import os

def initialize_file():
    if not os.path.exists('expenses.txt'):
        with open('expenses.txt', 'w') as file:
            file.write('Date, Amount, Category, Description\n')

def add_expense(date,amount,category,description):
    with open('expenses.txt', 'a') as file:
        file.write(f'{date},{amount},{category},{description}\n')
    print('Expense added')

def view_expense():
    with open('expenses.txt','r') as file:
        lines=file.readlines()
        print(lines[0])
        for line in lines[1:]:
            print(line)

def filter_exenses(filter_by,filter_value):
    with open('expenses.txt', 'r') as  file:
        lines=file.readlines()
        print(lines[0])
        for line in lines[1:]:
            data=line.split(',')
            if filter_by=='date' and filter_value==data[0]:
                print(line)
            elif filter_by=='category' and filter_value==data[2]:
                print(line)

def delete_expense(date,amount,category,description):
    lines=[]
    with open('expenses.txt', 'r') as file:
        lines=file.readlines()
    with open('expenses.txt', 'w') as file:
        for line in lines:
            if line.strip() != f'{date},{amount},{category},{description}':   ## strip() is used to remove any trailing newline characters
                file.write(line)
    print('Expense deleted')

import datetime

def monthly_summary():
    current_month=datetime.datetime.now().strftime('%Y-%m')
    total_expense=0.0
    category_expense={}

    with open('expenses.txt', 'r') as file:
        lines=file.readlines()
        for line in lines:
            data=line.strip().split(',')
            if data[0].startswith(current_month):
                amount=float(data[1])
                category=data[2]
                total_expense+=amount
                if category in category_expense:
                    category_expense[category] += amount
                else:
                    category_expense[category]=amount

    print(f'Total expense for {current_month}: {total_expense}')
    for category,amount in category_expense.items():
        print(f'{category}:{amount}\n')






















