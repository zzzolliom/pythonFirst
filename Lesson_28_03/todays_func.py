def login(login, lst):
    for u in lst:
        if login in lst:
            password = input("вводите пароль")
            for p in lst:
                if password in lst.password:
                    print("ок")
                else:
                    print("passport incorrect")
        else:
            print("invalid username")


def register(login, lst):
    for u in lst:
        if login in lst.login:
            print("invalid username")
        else:
            return True
