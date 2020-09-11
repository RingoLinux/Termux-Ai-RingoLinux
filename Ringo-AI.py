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
            User_Player = input("username: ")
            Password_Player = input("pasword: ")
            while True:
                if User_Player == self.User_Login and Password_Player == self.Password_Login:
                    print("Bạn đã đăng nhập thành công")
                    time.sleep(1)
                    os.system("clear")
                    break
                else:
                    print("Bạn đã đăng nhập thất bại")
                    time.sleep(1)
                    os.system("clear")
                    contri

a = Ringo_System()
a.From_Login()
