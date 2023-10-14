import os
import GlobalProperties as gp
# from UserOperation import get_user
import UserOperation as up
import TagOperation as tagop


class PasswordMain:
    user_signed_in = False
    current_user = []
    user = {}

    # user authentication
    def login(self, user_name, password):
        """ login functionality

        :param user_name: str
            user-name for login
        :param password: str
            password for login
        """
        get = up.get_user()

        if get[0]:
            users = get[1]
            if user_name not in users.keys():
                print('Either the User Name or the Password is wrong')
            else:
                if password not in users.values():
                    print('Either the User Name or the Password is wrong')
                else:
                    if users[user_name] == password:
                        self.user_signed_in = True
                        self.current_user.append(user_name)
                        print('login for User --' + user_name + '-- successfull')
                    else:
                        print('Either the User Name or the Password is wrong')
        else:
            print('ALERT -- NO Users exist')

    # logout
    def logout(self):
        """ logout functionality
        """
        print('Logging out of ' + self.current_user[0])
        self.user_signed_in = False
        self.current_user.clear()

    def main(self):
        # If default directories do not exist.
        if not os.path.isfile(gp.sys_path):
            os.mkdir(r'C:\uv_pw')
            os.mkdir(r'C:\uv_pw\uv')
            os.mkdir(r'C:\uv_pw\users')
            with open(gp.sys_path.encode('unicode_escape'), 'w') as f:
                f.write(str(self.user))
        print('---------------')
        print('Welcome to UVPW')
        print('---------------')

        while True:
            # split the entered line by " " into tokens.
            entered_keyword = input().split()
            command = entered_keyword[0]
            if command == "exit":
                print('-------------------------------------------------')
                print('Thank you for using the system.\nExiting now...')
                print('-------------------------------------------------')
                break
            elif command == "login":
                self.login(entered_keyword[1], entered_keyword[2])
            elif command == "logout":
                self.logout()
            elif command == "mkuser":
                up.make_new_user(entered_keyword[1], entered_keyword[2])
            elif command == "rmuser":
                up.remove_user(entered_keyword[1])
            elif command == "mktag":
                tagop.make_new_tag(entered_keyword[1], gp.user_path, self.user_signed_in, self.current_user)


if __name__ == "__main__":
    uvpw = PasswordMain()
    uvpw.main()
    # up.remove_user("demo3")
    # uv_pw.login("demo2", "demo2pw")
    # remove_user()
    # make_new_tag()
    # make_new_subtag()
