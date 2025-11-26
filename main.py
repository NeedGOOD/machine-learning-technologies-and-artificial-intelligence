import csv

# Contact directory

contact_directory = [
    {'surname': 'Іваненко', 'firstName': 'Олег', 'telephone': '', 'day': '', 'month': '', 'year': '', 'sex': ''},
    {'surname': '', 'firstName': '', 'telephone': '', 'day': '', 'month': '', 'year': '', 'sex': ''},
    {'surname': '', 'firstName': '', 'telephone': '', 'day': '', 'month': '', 'year': '', 'sex': ''},
    {'surname': '', 'firstName': '', 'telephone': '', 'day': '', 'month': '', 'year': '', 'sex': ''},
    {'surname': '', 'firstName': '', 'telephone': '', 'day': '', 'month': '', 'year': '', 'sex': ''},
]

with open('contact-directory.csv', 'wt', newline='') as frecord:
    crecord = csv.DictWriter(frecord, ['surname', 'firstName', 'telephone', 'day', 'month', 'year', 'sex'])
    crecord.writeheader()
    crecord.writerows(contact_directory)


test = [
    {'language': 'Python', 'developer': 'Guido van Rossum'},
    {'language': 'Scala', 'developer': 'Martin Odersky'},
    {'language': 'PHP', 'developer': 'Rasmus Lerdorf'},
    {'language': 'Ruby', 'developer': 'Yukihiro Matsumoto'},
    {'language': 'C', 'developer': 'Dennis Ritchie'},
]

with open('test.csv', 'wt', newline='') as frecord:
    crecord = csv.DictWriter(frecord, ['language', 'developer'])
    crecord.writeheader()
    crecord.writerows(test)






















test = [
    ['Python', 'Guido van Rossum'],
    ['Scala', 'Martin Odersky'],
    ['PHP', 'Rasmus Lerdorf'],
    ['Ruby', 'Yukihiro Matsumoto'],
    ['C', 'Dennis Ritchie'],
]

with open('test.csv', 'wt', newline='') as frecord:
    csvrecord = csv.writer(frecord)
    csvrecord.writerows(test)

with open('test.csv', 'rt') as freading:
    creading = csv.reader(freading)
    test = [row for row in creading]

print(test)

with open('test.csv', 'rt') as freading:
    creading = csv.DictReader(freading, fieldnames=['language', 'developer'])
    test = [row for row in creading]

print(test)

# test = [
#     {'language': 'Python', 'developer': 'Guido van Rossum'},
#     {'language': 'Scala', 'developer': 'Martin Odersky'},
#     {'language': 'PHP', 'developer': 'Rasmus Lerdorf'},
#     {'language': 'Ruby', 'developer': 'Yukihiro Matsumoto'},
#     {'language': 'C', 'developer': 'Dennis Ritchie'},
# ]

# with open('test.csv', 'wt', newline='') as frecord:
#     crecord = csv.DictWriter(frecord, ['language', 'developer'])
#     crecord.writeheader()
#     crecord.writerows(test)

