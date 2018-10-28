# coding: utf-8
import re
import tokenize as tk
from io import StringIO
from collections import deque


def get_content(filename: str) -> str:
    """Get raw content of a file."""
    with open(filename) as f:
        content = f.read()
        return content

def get_func_name(str_):
    prog = re.compile(r'\s*def\s+(.*)\(')
    result = prog.match(str_)
    return result.group(1) if result else result

def _check_cache(cache):
    """Check if cache contains def statement, if so, return name of the function, otherwise return None"""
    for line in cache:
        if 'def ' in line:
            return get_func_name(line)
    return None

source = get_content('testfile_comment.py')
def detect_infunc_and_same_line_comment(source):
    """Detect #-style comment in the first or second line inside a function.
    It can also detect #-style comment in the same line as def statement.

    e.g. functions like below can be detected:
    def foo():
        # comment
        pass
    
    def bar():

        # comment
        pass
    
    def foobar():  # comment
        pass
    """
    cache = deque(maxlen=2)
    for type_, token, _, _, line in tk.generate_tokens(StringIO(source).readline):
        if type_ != tk.COMMENT:
            cache.append(line)
        else:
            # check "def statement" in this line
            if 'def ' in line:
                print("{}: {}".format(get_func_name(line), token))
            else:
                # check "def statement" in preceding two lines (in cache)
                func_name = _check_cache(cache)
                if func_name:
                    print("{}: {}".format(func_name, token))

def detect_outfunc_comment(source):
    """Detect #-style comment outside a function.
    Note: the comment should be next to the function so that it can be detected.

    e.g. functions like below can be detected:
    # comment
    def foo():
        pass
    """
    cache = deque(maxlen=1)
    for type_, token, _, _, line in tk.generate_tokens(StringIO(source).readline):
        if type_ not in [tk.NAME, tk.NL, tk.DEDENT]:
            cache.append((type_, token))
        else:
            if type_ == tk.NAME and token == 'def':
                prev_line_list = list(cache)
                if prev_line_list:
                    prev_line = prev_line_list[0]
                    if prev_line[0] == tk.COMMENT:
                        cmt = prev_line[1]
                        func_name = get_func_name(line)
                        print("{}: {}".format(func_name, cmt))


# for i in tk.generate_tokens(StringIO(source).readline):
#     print(i)

detect_outfunc_comment(source)
