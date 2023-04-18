from task import authorization_dict


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password


def registration(login, password):
    authorization_dict[login] = login
    authorization_dict[password] = password


def authorization(login, password):
    if User(login, password) == authorization_dict[login] and User(login, password) == authorization_dict[password]:
        print('True')
    else:
        print('Error')


registration('LoremAmoris', 'stalker1')
authorization('LoremAmoris', 'stalker1')
