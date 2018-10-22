def hello(who, when):
    print(who)
    print(when)

def world():
    print('World')

class HelloWorld():
    def __init__(self, name):
        self.name = name
    
    def test_no_args(self):
        print("This is test_no_args.")
    
    def test_with_args(self, what):
        print(what)

class JustDance(HelloWorld):
    def __init__(self, name):
        super().__init__(name)
    
    def just(self):
        print("This is just.")
    
    def dance(self, dc):
        print(dc)
