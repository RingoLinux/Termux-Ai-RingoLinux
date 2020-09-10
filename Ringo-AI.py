
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

#names = input("Tên người trước mặt: ")
Name = Text_Conversation()
Name.What_Your_Name()

