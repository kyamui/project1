init_name = input("user name:")
init_password = input("password:")
print("initial name:", init_name)
print("initial password", init_password)
init_name
flag0=0

flag1=0
print('>>>User Login<<<')

while True:
    usr = input("input username:")
    if usr == init_name:
        while True:
            psd = input("input user password:")
            if psd == init_password:
                print('Login in!')
                quit(1)
            else:
                flag1 = flag1 + 1
                if flag1 < 3:
                    print('The password is wrong, please input user password again!')
                else:
                    flag1 = 0
                    print('You have tried 3 times, please input username again')
                    break
    else:
        print('username is wrong,please input the new username!')


