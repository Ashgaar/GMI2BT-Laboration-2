from modules import read_original_file, show_json_data, save_json_file, remove_from_data, check_if_number, create_person


def menu_graphic():
    print("[ 1 ] Läs in originalfil")
    print("[ 2 ] Visa json-data")
    print("[ 3 ] Lägg till person")
    print("[ 4 ] Ta bort person")
    print("[ 5 ] Spara fil")
    print("[ 0 ] Avsluta")


def menu():
    menu_graphic()
    choice_menu = check_if_number()

    while choice_menu != 0:
        if choice_menu == 1:
            print()
            read_original_file()  # klar
        elif choice_menu == 2:
            print()
            show_json_data()  # klar
        elif choice_menu == 3:
            print()
            create_person()
        elif choice_menu == 4:
            print()
            remove_from_data() # klar
        elif choice_menu == 5:
            print()
            save_json_file() #  klar
        else:
            print()
            print("Skriv endast in giltiga nummer.")

        print()
        menu_graphic()
        choice_menu = check_if_number()


menu()
