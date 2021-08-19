class phone:
    def __init__(self):
       print("i am phone class")

class samsung(phone):
    #pass
    def __init__(self):
        super().__init__()
        print("hello i am in samsung class")



s=samsung()