import os

sys_path = 'C:\\uv_pw\\uv\\.sys_uv.txt'
user_path = 'C:\\uv_pw\\users'

user_signed_in = False
current_user = []
user = {}

#to make a new user
def make_new_user(user_name, password):
    if not os.path.isdir((user_path+'\\'+user_name).encode('unicode_escape')):
        os.mkdir((user_path+'\\'+user_name).encode('unicode_escape'))   
        get = get_user()
        users = get[1]
        users[user_name] = password
        set_user(users)
        print('New User --'+user_name+'-- Initialised')
    else:        
        print('ALERT: User --' + user_name + '-- already exists')
        
#to remove a user        
def remove_user(user_name):

    #if user does not exist
    if not os.path.isdir((user_path+'\\'+user_name).encode('unicode_escape')):
        print('ALERT: User --'+user_name+'-- does not exist')
    
    #if user exists        
    else:        
            os.rmdir((user_path+'\\'+user_name).encode('unicode_escape'))
            get = get_user()
            users = get[1]
            users.pop(user_name)
            set_user(users)
            print('REMOVED User --'+user_name+'--')

#to store the passed users(dict) in the file
def set_user(user):
    with open(sys_path.encode('unicode_escape'),'w') as f:            
            f.write(str(user))

#to read users(dict) from file and return them        
def get_user():
    if os.path.getsize(sys_path.encode('unicode_escape')) == 0:
        dict_from_file = {}
        return False, dict_from_file
    else:        
        with open(sys_path.encode('unicode_escape'),'r') as f:
            dict_from_file = eval(f.read())            
        return True, dict_from_file

#user authentication
def login(user_name, password):
    get = get_user()

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
                    current_user.append(user_name)
                    print(current_user)
                    print('login for User --'+user_name+'-- successfull')
                else:
                    print('Either the User Name or the Password is wrong')
    else:
        print('ALERT -- NO Users exist')



def main():
    
    if not os.path.isfile(sys_path):
        os.mkdir(r'C:\uv_pw')
        os.mkdir(r'C:\uv_pw\uv')
        os.mkdir(r'C:\uv_pw\users')
        with open(sys_path.encode('unicode_escape'),'w') as f:            
            f.write(str(user))
    
    remove_user('pv')

if __name__ == "__main__":
    main()