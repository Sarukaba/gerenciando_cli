from gui.menus import autentication_screen, login_screen, register_screen
from tasks.tasks_user import register_user, log_in_user


def main():
    while True:
        user_option = autentication_screen()

        if user_option == "1":
            log_data = login_screen()
            
            if log_in_user(log_data["username"],log_data["password"]):
                print("Logim Efetuado")
            else:
                print("Falha ao realizar o login")

        elif user_option == "2":
            user_data = register_screen()         
            print(register_user(user_data))
            

if __name__ == "__main__":
    main()