import os

print(os.name)

if os.name == 'posix':
    os.system("bash app_sh.py")
else :
    print("os = windows")
