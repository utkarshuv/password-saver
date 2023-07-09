import os


def is_tag(tag_name, user_path, current_user) -> bool:
    """to check if the tag already exists or not

    :param tag_name: str
        name of the tag to be checked
    :param user_path: str
        path to the user directory
    :param current_user: str
        name of the currently logged-in user
    """
    user = current_user[0]
    tag_list = os.listdir((user_path + '\\' + user).encode('unicode_escape'))
    temp = list(map(bytes.decode, tag_list))
    if tag_name in temp:
        return True
    else:
        return False


def is_subtag(tag_name, subtag_name, user_path, current_user) -> bool:
    """to check if the sub tag already exists or not

    :param tag_name: str
        name of the tag for checking
    :param subtag_name: str
        name of the sub tag for checking
    :param user_path: str
        path of the user directory
    :param current_user: str
        name of the current logged-in user
    """
    user = current_user[0]
    subtag_list = os.listdir((user_path + '\\' + user + '\\' + tag_name).encode('unicode_escape'))
    temp = list(map(bytes.decode, subtag_list))

    if subtag_name + '.txt' in temp:
        return True
    else:
        return False


def make_new_subtag(tag_name, subtag_name, user_signed_in, user_path, current_user):
    """Makes a new sub-tag.

    Parameters
    ----------
    tag_name : str
        Name of the tag name inside which the sub-tag needs to be created
    subtag_name : str
        name of the tag to be created.
    user_signed_in: str
        Name of the user which is logged in currently.
    user_path : str
        Path to the 'users' directory.
    """
    if not user_signed_in:
        print('ALERT: -- User not logged in --')
    else:
        user = current_user[0]
        if is_tag(tag_name, user_path, current_user):
            if is_subtag(tag_name, subtag_name, user_path, current_user):
                print('SUBTAG already exists')
            else:
                with open((user_path + '\\' + user + '\\' + tag_name + '\\' + subtag_name + '.txt').encode(
                        'unicode_escape'), 'w') as f:
                    f.write('')
                print('SUBTAG --' + subtag_name + '-- created')
        else:
            print('ALERT: TAG --' + tag_name + '-- does not exist')


def make_new_tag(tag_name, user_path, user_signed_in, current_user):
    """To make a new tag

    Parameters
    ----------
    :param tag_name: str
        Name of the tag to be created.
    :param user_path: str
        path to the user directory
    :param user_signed_in: bool
        flag for logged-in user
    :param current_user: str
        name of the logged-in user.
    """
    if not user_signed_in:
        print('ALERT: -- User not logged in --')
    else:
        user = current_user[0]
        print(is_tag(tag_name, user_path, current_user))
        if is_tag(tag_name, user_path, current_user):
            print('Tag already exist')
        else:
            os.mkdir((user_path + '\\' + user + '\\' + tag_name).encode('unicode_escape'))
            print('Tag --' + tag_name + '-- Created')
