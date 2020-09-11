
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
        self.User_Login = User_Login
        self.Pasword_Login = Password_Login
        self.Login_Switch = Login_Switch
    def From_Login(self):
        if self.Login_Switch == "Off":
            print("Login không được bật,bạn có muốn mở nó lên hay không?") 
            self.Login_Switch_YN = input("Lựa chọn y/n")
            if self.Login_Switch_YN == "y" or self.Login_Switch_YN == "Y":
                self.Login_Switch = "On"
                print(self.Login_Switch)
            else:
                print("Bạn đã lựa chọn từ chối!!")

a = Ringo_System()
a.From_Login()
