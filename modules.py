import json
from csv import DictReader
import csv


csv_file = "labb2-personer.csv"
json_file = "personer.json"
data_list = []


def read_original_file():
    try:
        with open(csv_file, "r", encoding="utf-8-sig") as f:
            csv_source = csv.reader(f, delimiter=";")
            for entry in csv_source:
                data_list.append(create_dict(entry))
            data_list.pop(0)
            print("Filen skannades in korrekt.")
    except FileNotFoundError:
        print("Filen skannades inte in korrekt. Kolla så att filen csv filen finns.")


def create_dict(entry):
    return {'anamn': entry[0], 'fnamn': entry[1], 'enamn': entry[2], 'email': entry[3]}


def show_json_data():
    try:
        with open(json_file, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
            i = 1
            for entry in data:
                print("[", i, "]", "Användernamn:", entry['anamn'], "Förnamn:",
                      entry['fnamn'], "Efternamn:", entry['enamn'], "Email:", entry['email'])
                i += 1
    except FileNotFoundError:
        print(
            "Filen finns inte. Läs in originalfilen och spara filen för att kunna läsa den.")


def remove_from_data():
    show_json_data()

    print("[ 0 ] Gå till huvudmenyn")
    print("Skriv in ett nummer för att ta bort en person.")

    while True:
        try:
            delete_entry_input = check_if_number()
            if delete_entry_input == 0:
                break
            delete_entry_input -= 1
            data_list.pop(delete_entry_input)
            break
        except IndexError:
            print("Skriv endast in giltiga nummer.")


def check_if_number():
    while True:
        try:
            value = int(input())
            break
        except ValueError:
            print("Skriv endast in nummer")
    return value


def save_json_file():
    print("Fil sparad.")
    with open(json_file, "w", encoding="utf-8-sig") as f:
        json.dump(data_list, f)


def create_person():
    uname = input("Användarnamn: ")
    fname = input("Namn: ")
    lname = input("Efternamn: ")
    email = input("Email: ")
    add_student = {'anamn': uname, 'fnamn': fname,
                   'enamn': lname, 'email': email}
    data_list.append(add_student)
