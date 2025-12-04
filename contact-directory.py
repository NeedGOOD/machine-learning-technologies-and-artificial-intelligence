import csv
import pandas as pd

line = '----------------------------------------------------------------------------------------------'

# Contact directory

contact_directory = [
    {'surname': 'Іваненко', 'firstName': 'Олег', 'telephone': '+380501234567', 'day': '12', 'month': '03', 'year': '1990', 'sex': 'M'},
    {'surname': 'Притула', 'firstName': 'Олена', 'telephone': '+380671112233', 'day': '25', 'month': '07', 'year': '1988', 'sex': 'F'},
    {'surname': 'Коваль', 'firstName': 'Андрій', 'telephone': '+380931234321', 'day': '02', 'month': '11', 'year': '1992', 'sex': 'M'},
    {'surname': 'Шевчук', 'firstName': 'Марина', 'telephone': '+380661234455', 'day': '14', 'month': '04', 'year': '1995', 'sex': 'F'},
    {'surname': 'Бондар', 'firstName': 'Ірина', 'telephone': '+380731122334', 'day': '30', 'month': '09', 'year': '1986', 'sex': 'F'},
    {'surname': 'Мельник', 'firstName': 'Дмитро', 'telephone': '+380501118899', 'day': '05', 'month': '01', 'year': '1991', 'sex': 'M'},
    {'surname': 'Ткачук', 'firstName': 'Світлана', 'telephone': '+380673003311', 'day': '19', 'month': '06', 'year': '1984', 'sex': 'F'},
    {'surname': 'Герасимчук', 'firstName': 'Віктор', 'telephone': '+380931212121', 'day': '08', 'month': '12', 'year': '1993', 'sex': 'M'},
    {'surname': 'Лисенко', 'firstName': 'Наталія', 'telephone': '+380661010101', 'day': '23', 'month': '08', 'year': '1989', 'sex': 'F'},
    {'surname': 'Романюк', 'firstName': 'Ігор', 'telephone': '+380731919191', 'day': '11', 'month': '02', 'year': '1996', 'sex': 'M'},
]

with open('contact-directory.csv', 'wt', newline='') as frecord:
    crecord = csv.DictWriter(frecord, ['surname', 'firstName', 'telephone', 'day', 'month', 'year', 'sex'])
    crecord.writeheader()
    crecord.writerows(contact_directory)

with open('contact-directory.csv', 'rt') as freading:
    creading = csv.DictReader(freading, fieldnames=[''])
    contact_directory = [row for row in creading]

print(contact_directory)

df = pd.read_csv('contact-directory.csv')

print(df.info())

print(line)

print(df.head())

print(line)

print(df.tail())

print(line)

cols = ["day", "month", "year"]
df_num = df[cols].apply(pd.to_numeric, errors="coerce")

mean = df_num.mean()
median = df_num.median()
mode = df_num.mode().iloc[0]
min_ = df_num.min()
max_ = df_num.max()

print("Середнє:\n", mean)
print("\nМедіана:\n", median)
print("\nМода:\n", mode)
print("\nМінімум:\n", min_)
print("\nМаксимум:\n", max_)

