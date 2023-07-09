import os
import GlobalProperties as gp
# from UserOperation import get_user
import UserOperation as up


class PasswordMain:

    user_signed_in = False
    current_user = []
    user = {}

    # user authentication
    def login(self, user_name, password):
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
                        user_signed_in = True
                        gp.current_user.append(user_name)
                        print('login for User --' + user_name + '-- successfull')
                    else:
                        print('Either the User Name or the Password is wrong')
        else:
            print('ALERT -- NO Users exist')

    # logout
    def logout(self):
        gp.user_signed_in = False
        gp.current_user.clear()

    def main(self):
        if not os.path.isfile(gp.sys_path):
            os.mkdir(r'C:\uv_pw')
            os.mkdir(r'C:\uv_pw\uv')
            os.mkdir(r'C:\uv_pw\users')
            with open(gp.sys_path.encode('unicode_escape'), 'w') as f:
                f.write(str(gp.user))


if __name__ == "__main__":
    uvpw = PasswordMain()
    # uv_pw.main()
    up.remove_user("demo3")
    # uv_pw.login("demo2", "demo2pw")
    # remove_user()
    # make_new_tag()
    # make_new_subtag()
