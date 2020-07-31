import os

sys_path = 'C:\\uv_pw\\uv\\.sys_uv.txt'
user_path = 'C:\\uv_pw\\users'

user_signed_in = False

#to make a new user
def make_new_user(user_name):
    if not os.path.isdir((user_path+'\\'+user_name).encode('unicode_escape')):
        os.mkdir((user_path+'\\'+user_name).encode('unicode_escape'))        
        print('New User --'+user_name+'-- Initialised')
    else:        
        print('ALERT: User --' + user_name + '-- already exists')
        
#to remove a user        
def remove_user(user_name):
    if not os.path.isdir((user_path+'\\'+user_name).encode('unicode_escape')):
        print('ALER: User --'+user_name+'-- does not exist')
    else:        
            os.rmdir((user_path+'\\'+user_name).encode('unicode_escape'))
            print('REMOVED User --'+user_name+'--')
        
def main():
    
    if not os.path.isfile(sys_path):
        os.mkdir(r'C:\uv_pw')
        os.mkdir(r'C:\uv_pw\uv')
        os.mkdir(r'C:\uv_pw\users')
        with open(sys_path.encode('unicode_escape'),'w') as f:
            user = {'uv':'heheheeh', 'pv':'hahahah'}
            f.write(str(user))
        


    with open(sys_path.encode('unicode_escape'),'r') as f:
        dict_from_file = eval(f.read())
    print(dict_from_file['uv'])
    

if __name__ == "__main__":
    main()