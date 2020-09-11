import os
import time

class Install_Systen:
    pass
class Setting_System:
    pass
class Text_Conversation:
    "Class khai báo những thành phần về chào hỏi."
    def __init__(self,Name_Object="Người nào đó",Age_Object=0):
        self.Name_Object = Name_Object
        self.Age_Object = Age_Object
    def Hello(self): 
        print("Xin chào {}! ".format(self.Name_Object))
    def What_Your_Name(self):
        print("Tên của bạn là gì?")
    def How_Old_Are_You(self):
        print("Bạn bao nhiêu tuổi?")

class Ringo_System:
    "Class khai báo những thành phần về hệ thống trong termux "
    def __init__(self,User_Login="admin",Password_Login="admin",Login_Switch="Off"):

        #From_Login_Object
        self.User_Login = User_Login
        self.Password_Login = Password_Login
        self.Login_Switch = Login_Switch
    

    def From_Login(self):
        if self.Login_Switch == "Off":
            print("Login không được bật,bạn có muốn mở nó lên hay không?") 
            self.Login_Switch_YN = input("Lựa chọn y/n: ")
            time.sleep(1)
            os.system("clear")
            if self.Login_Switch_YN == "y" or self.Login_Switch_YN == "Y":
                self.Login_Switch = "On"
                print("Công tắc đã được " + self.Login_Switch)
                time.sleep(1)
                os.system("clear")
            else:
                print("Bạn đã lựa chọn từ chối!!")
                time.sleep(1)
                os.system("clear")
        
        if self.Login_Switch == "On":
            try:
                self.User_Player = str(input('\033[1;92mUsername \033[1;93m: '))
                print("")
                self.Password_Player = getpass('\033[1;92mPassword \033[1;93m: ')
                print ("")
                if self.User_Player == self.User_Login and self.Password_Player == Password_Login:
                   print('wait...')
                   time.sleep(1)
                   os.system('clear')
                   print('')
                   print('\033[1;92m ────────────────────────────────────── ')
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)
                      print("")
           except Exception:
                      
                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)

a = Ringo_System()
a.From_Login()
