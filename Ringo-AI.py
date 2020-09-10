
class Text_Conversation:
    "Class khai báo những thành phần về chào hỏi."
    def __init__(self,Name_Object):
        self.Name_Object = Name_Object
    def Hello(self): 
        print("Xin chào {}! ".format(self.Name_Object))


names = input("Tên người trước mặt: ")
Name = Text_Conversation(names)
Name.Hello()
