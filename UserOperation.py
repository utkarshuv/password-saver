import os
import shutil
import GlobalProperties as gp


# to make a new user
def make_new_user(user_name, password):
    """to make a new user

    :param user_name: str
        name of the user to be created
    :param password: str
        password for the new user
    """
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
    """to remove an existing user

    :param user_name: str
        name of the user to be deleted
    """
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


def set_user(user_dict):
    """to store the passed users(dict) in the file

    :param user_dict: dict
        dictionary for storing users with their passwords
    """
    with open(gp.sys_path.encode('unicode_escape'), 'w') as f:
        # store dictionary in a txt file as a string
        f.write(str(user_dict))


def get_user() -> tuple:
    """to read users(dict) from file and return them

    :return: a tuple with a boolean and a dictionary
        bool - does the user exist or not
        dict - dictionary read from the file
    """
    # check if the user exist or not
    if os.path.getsize(gp.sys_path.encode('unicode_escape')) == 0:
        dict_from_file = {}
        return False, dict_from_file
    else:
        with open(gp.sys_path.encode('unicode_escape'), 'r') as f:
            # read dictionary as the user exists.
            dict_from_file = eval(f.read())
        return True, dict_from_file
