from cryptography.fernet import Fernet
import os


def user_function_lijst():
    file_user = open("C:\\Users\\arnau\\PycharmProjects\\password_manager\\user_data\\user_data.txt")
    lijst = []
    regels = file_user.readlines()
    for regel in regels:
        record = regel.split(";")
        lijst.append(record[0])
    file_user.close()
    return lijst


def user_maken(user_lijst):
    wachtwoord = "1"
    check_wachtwoord = "2"
    user_name = input("Username: ")
    while user_name in user_lijst:
        if user_name in user_lijst:
            print("username al in gebruik")
            user_name = input("Username: ")
    while wachtwoord != check_wachtwoord:
        wachtwoord = input("Password: ")
        check_wachtwoord = input("Password check: ")
        if check_wachtwoord == wachtwoord:
            password = wachtwoord
            return (user_name, password)
        else:
            print("Fout wachtoord ingegeven")


def inloggen(user_lijst):
    file_users_read = open("C:\\Users\\arnau\\PycharmProjects\\password_manager\\user_data\\user_data.txt", "r")
    login_username = input("Username: ")
    while login_username not in user_lijst:
        if login_username not in user_lijst:
            print("Username bestaat niet")
            stop = input("Stoppen?(y/n)").lower()
            if stop == "y":
                return 0, ""
            login_username = input("Username: ")
    while 1 != 2:
        juist = 0
        wachtwoord = input("password: ")
        regels = file_users_read.readlines()
        for regel in regels:
            record = regel.split(";")
            if record[0] == login_username and record[1].rstrip() == wachtwoord:
                juist = 1
        if juist == 1:
            print("inloggen succesvol")
            return (1, login_username)
        else:
            print("Verkeerd wachtwoord")


def wachtwoorden_invoegen(username):
    stoppen = input("Stoppen?(y/n)").lower()
    while stoppen != "y":
        user_file_path = "C:\\Users\\arnau\\PycharmProjects\\password_manager\\user_data\\" + username + ".txt"
        user_file = open(user_file_path, "a")
        website = input("Naam van de website: ")
        website_username = input("Username: ")
        website_wachtwoord = input("Password: ")
        user_file_append = website + ";" + website_username + ";" + website_wachtwoord
        user_file.write(user_file_append)
        stoppen = input("Stoppen?(y/n)").lower()
        if stoppen == "y":
            return


def wachtwoorden_uithalen(username):
    stoppen = "n"
    while stoppen != "y":
        naam_website = input("Van welke website heb je je het wachtwoord nodig? ").lower()
        user_file = open("C:\\Users\\arnau\\PycharmProjects\\password_manager\\user_data\\" + username + ".txt")
        regels = user_file.readlines()
        for regel in regels:
            record = regel.split(";")
            if record[0].lower() == naam_website:
                print("Website:", record[0])
                print("Username:", record[1])
                print("Password:", record[2])
                website_gevonden = 1
        if website_gevonden != 1:
            print("Website not found: ")
        stoppen = input("Stoppen?(y/n) ").lower()
        if stoppen == "y":
            return

antwoord = "a"
while antwoord != "S":
    print("1:user maken", end="\n")
    print("2:inloggen", end="\n")
    print("3:stoppen", end="\n")
    print("", end="\n")
    antwoord = input("Wat wil je doen :").lower()

    user_lijst = user_function_lijst()
    if antwoord == "1":
        file_users = open("C:\\Users\\arnau\\PycharmProjects\\password_manager\\user_data\\user_data.txt","a")
        (user_name, password) = user_maken(user_lijst)
        lijn = (str(user_name) + ";" + str(password) + "\n")
        file_users.write(lijn)
        file_users.close()
        path_file_user = "C:\\Users\\arnau\\PycharmProjects\\password_manager\\user_data\\" + str(user_name) + ".txt"
        file_users_passwds = open(path_file_user, "w")
        file_users_passwds.close()
        print("User goed aangemaakt")

    if antwoord == "2":
        (inloggen_succes,username) = inloggen(user_lijst)
        if inloggen_succes == 0:
            print("inloggen mislukt")
        if inloggen_succes == 1:
            print("")
            print("1: nieuwe wachtwoorden invoegen")
            print("2: wachtwoorden uithalen")
            print("")
            opdracht = input("Wat wil je doen :")
            if opdracht == "1":
                wachtwoorden_invoegen(username)
            elif opdracht == "2":
                wachtwoorden_uithalen(username)
    if antwoord == "3":
        print("data_encrypted")
        antwoord = "S"