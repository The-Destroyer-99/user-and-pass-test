import os

'''
print('Set Username')
inputed_username = input()
print('Set Password')
inputed_password = input()
os.environ['USER'] = inputed_username
os.environ['PASSWORD'] = inputed_password

os.clear
'''

print('Please Log In. admin Is The Defalt User And Password')
print('Username:')
inputed_username = input()

logged_username = os.getenv('USER','admin')

if  inputed_username == logged_username :
  logged_password = os.environ.get('PASSWORD','admin')
  print('Password:')
  inputed_password = input()
  if inputed_password == logged_password :
    os.clear
    print('Welcome ' + inputed_username + '!')
    while True :
      print('What Do You Want To Do?')
      print('''
    1: Change Username
    2: Change Password
    3: Log Out
      ''')
      ch1 = input()
      if ch1 == '1' :
        print('What Do You Want Your New Username To Be?')
        new_username = input()
        os.environ['USER'] = new_username
        
      if ch1 == '2' :
        print('What Do You Want Your New Password To Be?')
        new_password = input()
        os.environ['PASSWORD'] = new_password
        
      if ch1 == "3" :
        break
        
        
  else :
      print('WRONG PASSWORD')
else :
  print('WRONG USERNAME')
