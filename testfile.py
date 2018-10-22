"""Hello I'm testfile.py.
"""

def hello(who, when):
    print(who)
    print(when)

def world():
    """This is world.
    """
    print('World')

class HelloWorld():
    """This is HelloWorld class.
    """
    def __init__(self, name):
        self.name = name
    
    def test_no_args(self):
        print("This is test_no_args.")
    
    def test_with_args(self, what):
        print(what)
    
    def test_with_comment(self):
        """This is a comment of function: test_with_comment
        """
        pass

class JustDance(HelloWorld):
    def __init__(self, name):
        super().__init__(name)
    
    def just(self):
        print("This is just.")
    
    def dance(self, dc):
        print(dc)
    
    def test_with_comment(self, cm):
        """Just dance when you are not happy!
        """
        print(cm)
