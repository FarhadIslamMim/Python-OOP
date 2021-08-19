class phone:
    def call(self):
        print("you can call")
    def msg(self):
        print("you can msg")
class samsung(phone):
    def pictur(self):
        print("you can clcik pictur")

p=samsung()
p.call()
p.msg()
#print(issubclass(samsung,phone))