import os
import shutil
import GlobalProperties as gp


# to make a new user
def make_new_user(user_name, password):
    if not os.path.isdir((gp.user_path + '\\' + user_name).encode('unicode_escape')):
        os.mkdir((gp.user_path + '\\' + user_name).encode('unicode_escape'))
        get = get_user()
        users = get[1]
        users[user_name] = password
        set_user(users)
        print('New User --' + user_name + '-- Initialised')
    else:
        print('ALERT: User --' + user_name + '-- already exists')


# to remove a user
def remove_user(user_name):
    # if user does not exist
    if not os.path.isdir((gp.user_path + '\\' + user_name).encode('unicode_escape')):
        print('ALERT: User --' + user_name + '-- does not exist')
    # if user exists
    else:
        shutil.rmtree((gp.user_path + '\\' + user_name).encode('unicode_escape'))
        get = get_user()
        users = get[1]
        users.pop(user_name)
        set_user(users)
        print('REMOVED User --' + user_name + '--')


# to store the passed users(dict) in the file
def set_user(user_dict):
    with open(gp.sys_path.encode('unicode_escape'), 'w') as f:
        f.write(str(user_dict))


# to read users(dict) from file and return them
def get_user() -> tuple:
    if os.path.getsize(gp.sys_path.encode('unicode_escape')) == 0:
        dict_from_file = {}
        return False, dict_from_file
    else:
        with open(gp.sys_path.encode('unicode_escape'), 'r') as f:
            dict_from_file = eval(f.read())
        return True, dict_from_file
