from werkzeug import generate_password_hash, check_password_hash

class User:
    '''类用于创建用户账号
    '''
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = self.save_password(password)

    def check_email(self, email):
        return self.email == email
    
    def save_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

def main():
    userlist = []
    print('----------welcome----------')
    while 1:
        choose = int(input('''
please choose:
1.sign up
2.sign in
3.exit
'''))
        if choose == 1:
            print('please enter: ')
            name = input('name: ')
            email = input('email: ')
            password = input('password: ')
            newuser = User(name, email, password)
            userlist.append(newuser)

        if choose == 2:
            print('please enter: ')
            email = input('email: ')
            password = input('password: ')
            inlist = False
            for user in userlist:
                if user.check_email(email):
                    inlist = True
                    if user.check_password(password):
                        print('sign in success')
                    else:
                        print('wrong password or name')
                    break
            if inlist == False:
                print('please enter right email')
        if choose == 3:
            break

if __name__ == '__main__':
    main()
