# acilista kullanicidan 3 veri girmesini isteyecek
# Website - Kullanici adi - password
# Kullanicidan alinan veriler passwords.txt dosyasina yazdirilacak
# Her satir basinda numara 1 artarak devam edecek
# Daha sonra password generetor ile bana sifre onermesini isteyecegim
# Daha sonra istenirse arayuz yapilacak
# sifre silme ve guncelleme kismi da eklenmeli
#Bir websitesinde birden fazla kullanici hesabi olabilir bu nedenle her bir record icin ID numarasi verilecek ve degisiklikler bu ID uzerinden yapilacak

import time

class PasswordManager:
    def __init__(self):
        while True:
            # try:
                print("\n--- LOGIN PAGE ---")
                user_name = input("\nEnter user name: ")
                user_password  = input("\nEnter password: ")

                if user_name == "kerim" and user_password == "1234":
                    time.sleep(0.5)
                    print("\nLogin succesful!\n")
                    time.sleep(0.5)
                    print(50*"-")
                    print("\n----- Your all Records -----\n")
                    self.show_records()
                    print(50*"-")
                    time.sleep(0.5)
                    input("Press Enter to see menu: ")
                    self.user_menu()
                    break
                else:
                    print("Wrong user name or password, try again!")
            # except:
            #     print("User not recognized! Try again!")

    def user_menu(self):
        while True:
            options = """
            [1] Show all my passwords
            [2] Add new record
            [3] Update record
            [4] Delete record
            [Q] Exit
            """
            print(options)
            user_menu_choice = input("Enter your choice: ")  

            if user_menu_choice == "1":
                self.show_records()
            elif user_menu_choice == "2":
                self.add_record()
            elif user_menu_choice == "3":
                self.update_record()
            elif user_menu_choice == "4":
                self.delete_record()
            elif user_menu_choice == "Q" or user_menu_choice == "q":
                break
            else:
                print("Please choose one of the options!")

    def show_records(self):
        print("")
        passwords_list = self.passwords_list()
        for password in passwords_list:
            print(password, end="")
        print("")

    def add_record(self):
        while True:
            print("---Add record---\n")
            entered_website = input("Enter website: ")
            entered_user_name = input("Enter user name: ")
            entered_password = input("Enter password: ")

            passwords_list = self.passwords_list()

            if len(passwords_list) == 0:
                record_id = 1
            else:
                with open("passwords.txt", "r") as file:
                    record_id = int(passwords_list[-1].split("-")[0]) + 1
            
            line_record = "{}-{}-{}-{}\n".format(record_id,entered_website,entered_user_name,entered_password)

            with open("passwords.txt","a+")as file:
                file.write(line_record)
            
            passwords_list = self.passwords_list()

            for password in passwords_list:
                print(password, end="")
            break

    def update_record(self):
        while True:
            print("--- Update Record ---")
            passwords_list = self.passwords_list()
            self.show_records()

            entered_record_id = int(input("Enter record ID to change: "))            
            record_to_update = passwords_list[entered_record_id-1]
            print("\nWill be updated >>> " + record_to_update)

            entered_website = input("\nEnter new website name: ")
            entered_user_name = input("\nEnter new user name/email: ")
            entered_password = input("\nEnter new password: ")

            new_line_record = "{}-{}-{}-{}\n".format(entered_record_id,entered_website,entered_user_name,entered_password)
            
            passwords_list.pop(entered_record_id - 1)
            passwords_list.insert(entered_record_id - 1, new_line_record)
            
            input("\nPress Enter to update >>> " + new_line_record)
            
            self.update_list(passwords_list)
            print("\nSuccesfully Updated record! >>> " + new_line_record)
            break

    def passwords_list(self):
        with open("passwords.txt","r") as file:
            passwords_list = file.readlines()

        return(passwords_list)

    def update_list(self, last_list):
        with open("passwords.txt","w") as file:
            file.writelines(last_list)

    def delete_record(self):
        while True:
            # try:
                passwords_list = self.passwords_list()
                self.show_records()

                entered_record_id = int(input("Enter record ID to delete: "))
                record_to_del = passwords_list[entered_record_id-1]
                print("\nWill be deleted -> " + record_to_del)
                passwords_list.pop(entered_record_id - 1)

                record_id = 1
                new_passwords_list = []

                for password in passwords_list:
                    new_passwords_list.append(str(record_id) + "-" + password.split("-")[1] + "-" + "-" + password.split("-")[2] + "-" + password.split("-")[3] + "\n")
                    record_id += 1

                input("Press Enter to delete record!")

                self.update_list(new_passwords_list)
                
                print("\nSuccesfully deleted >>> " + record_to_del)
                time.sleep(0.5)


                self.show_records()
                break

            # except:
            #     print("Wrong input, try again!")

def main():
    PasswordManager()

if __name__ == "__main__":
    main()
