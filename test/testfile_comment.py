## skr skr skr skr skr
def test_one(param1, param2=100):
    # loose comment
    pass

def test_one_half(pa: str) -> str:
    # test_one_half comment
    pass

def test_two_bevor():

    # above is intended to leave blank
    pass
# very close to previous comment
def test_two(arg: str):
    pass

def test_three(arg):
    """One line docstring."""
    pass

def test_four(param):
    '''Single quote docstring'''
    pass

def test_five(par):
    '''Two line single quote
    '''
    pass

def test_six():  # test_six right comment
    pass

# outside comment for test_seven
def test_seven():
    pass

class Foo():
    def __init__(self):
        pass
    
    def foo(self, word):
        # foo comment
        print(word)

    # bar comment
    def bar(self):
        pass

    def foobar(self): # foobar right comment
        pass
