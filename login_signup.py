user = {}
error_message = "\nInvalid Input\nTry Again\n"

def task():
    while True:
        print("Tasks:\n1. Login\n2. Sign Up\n3. Change Password\n4. Exit")
        task_inp = input("\nEnter your Choice : ").lower().strip()

        if task_inp and task_inp.isdigit():
            task_inp = int(task_inp)
            if 0 < task_inp <= 4:
                return task_inp
            else:
                print(error_message)
        else:
            print(error_message)
def sign_up(main_dict):
    while True:
        user_name_inp = input("User Name : ")

        if user_name_inp:
            if user_name_inp not in main_dict:
                if not user_name_inp[0].isdigit() and not user_name_inp.isdigit() and not " " in user_name_inp:
                    while True:
                        password_inp = input("\nPassword : ")
                        if password_inp:
                            main_dict[user_name_inp] = password_inp
                            print(f"\n{"User name and Password Saved Successfully".center(20, "-")}\n")
                            break
                        else:
                            print(error_message)
                else:
                    print("\n- Username should not contains only digits\n-It should not contains only numeric value\n-Should not contain white spaces\n")
            else:
                if user_name_inp in main_dict:
                    print(f"\nUser name : '{user_name_inp}' already exists")

                    while True:
                        exist_user_inp = input("\nWant to Login with Password ?\n[y/n] : ").lower().strip()

                        if exist_user_inp:

                            if exist_user_inp == "y":
                                while True:
                                    password_inp = input("\nPassword : ")
                                    if password_inp:
                                        if main_dict[user_name_inp] == password_inp:
                                            print("\nLogged in Successfully\n")
                                            break
                                        else:
                                            print("\nOops!!\nWrong Password\nTry Again")
                                    else:
                                        print(error_message)
                                break
                            elif exist_user_inp == "n":
                                break

                            else:
                                print(error_message)

                        else:
                            print(error_message)
            break
                

        else:
            print(error_message)

def login(main_dict):
    while True:
        user_name_inp = input("\nUser Name : ")

        if user_name_inp:
            if user_name_inp in main_dict:
                while True:
                    password_inp = input("\nPassword : ")
                    if password_inp:
                        if password_inp == main_dict[user_name_inp]:
                            print("\nYou have been Logged in successfully\n")
                            break
                        else:
                            print("\nYou need to eat almonds\nIt's a Wrong password\nTry Again\n")
                    else:
                        print(error_message)
                break
            else:
                print(f"\nOops!!\nUser Name : '{user_name_inp}' didn't exist\nPlease Try 'Sign Up' option from the menu bar\n")
                break
        else:
            print(error_message)

def change_password(main_dict):
   while True:
        user_name_inp = input("\nUser Name : ")

        if user_name_inp:
            if user_name_inp in main_dict:
                while True:
                    password_inp = input("\nPassword : ")
                    if password_inp:
                        if password_inp == main_dict[user_name_inp]:
                            while True:
                                new_password_inp = input("New password : ")
                                main_dict[user_name_inp] = new_password_inp
                                print(f"\n{"Password Changed successfully".center(20, "-")}\n")
                                break
                            break
                        else:
                            print("\nYou need to eat almonds\nIt's a Wrong password\nTry Again\n")
                    else:
                        print(error_message)
                break
            else:
                print(f"\nOops!!\nUser Name : '{user_name_inp}' didn't exist\nPlease Try 'Sign Up' option from the menu bar and check the credentials carefully next time\n")
                break
        else:
            print(error_message)

def log_sign(main_dict):

    print("\nWelcome To Our Website\n")

    while True:
        choice = task()

        if choice == 1:
            login(main_dict)
            continue
        elif choice == 2:
            sign_up(main_dict)
            continue
        elif choice == 3:
            change_password(main_dict)
            continue
        else:
            print("\nSee you soon\n")
            break

log_sign(user)
