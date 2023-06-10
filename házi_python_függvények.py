# 1. feladat
def number_finder(start: int, finish: int, oszthato: int, nem_oszthato: int):
    result = []
    for number in range(start, finish + 1):
        if number % oszthato == 0 and number % nem_oszthato != 0:
            result.append(number)
    return result

print(number_finder(start=1, finish=30, oszthato=7, nem_oszthato=5))

# 2. feladat
def counter(names: list):
    results = 0
    for arg_name in names:
        if arg_name == 'Pista':
            results += 1
    return results

first_names = ['Pista', 'Gabor', 'Pista', 'Gábor', 'István', 'István', 'László', 'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista']

print(counter(first_names))

# 3. feladat
def convert_to_number(text):
    number = int(text)
    return number

def print_hello(count):
    for i in range(1, count + 1):
        print(f"{i}. Helló!")

input_text = input("Kérem adjon meg egy számot: ")
number = convert_to_number(input_text)
print_hello(number)

# 4. feladat
def calculate_circle_area(radius):
    area = 3.14 * radius ** 2
    return area

def calculate_circle_circumference(radius):
    circumference = 2 * 3.14 * radius
    return circumference

input_text2 = input("Kérem adja meg a sugarat: ")
radius = convert_to_number(input_text2)

area = calculate_circle_area(radius)
circumference = calculate_circle_circumference(radius)
print("Kör területe:", area)
print("Kör kerülete:", circumference)

# 5. feladat
def name_grouper(arg_name):
    names = sorted(arg_name)  
    lenght = len(names)
    middle_index = lenght // 2

    if lenght % 2 == 0:  
        group1 = names[:middle_index]
        group2 = names[middle_index:]
    else:  
        group1 = names[:middle_index + 1]
        group2 = names[middle_index + 1:]

    print("Csoport 1:")
    for name in group1:
        print(name)

    print("\nCsoport 2:")
    for name in group2:
        print(name)

names = ['Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter', 'Gaál András', 'Németh Diána', 'Telek Éva', 'Ledán-Munteán Szabolcs', 'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás']
name_grouper(names)







