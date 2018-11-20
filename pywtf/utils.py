# coding: utf-8
import os
import re
import tokenize as tk
from io import StringIO
from collections import deque
from typing import List


def get_content(filename: str) -> str:
    """Get raw content of a file."""
    with open(filename) as f:
        content = f.read()
        return content

def get_func_name(str_: str):
    prog = re.compile(r'\s*def\s+(.*)\(')
    result = prog.match(str_)
    return result.group(1) if result else result

def _check_cache(cache):
    """Check if cache contains def statement, if so, return name of the function, otherwise return None"""
    for line in cache:
        if 'def ' in line:
            return get_func_name(line)
    return None

def detect_infunc_and_same_line_comment(source: str) -> List:
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
    func_name_and_cmt = []
    cache = deque(maxlen=2)
    for type_, token, _, _, line in tk.generate_tokens(StringIO(source).readline):
        if type_ != tk.COMMENT:
            cache.append(line)
        else:
            # check "def statement" in this line
            if 'def ' in line:
                func_name_and_cmt.append((get_func_name(line), token))
            else:
                # check "def statement" in preceding two lines (in cache)
                func_name = _check_cache(cache)
                if func_name:
                    func_name_and_cmt.append((func_name, token))
    return func_name_and_cmt

def detect_outfunc_comment(source: str) -> List:
    """Detect #-style comment outside a function.
    Note: the comment should be next to the function so that it can be detected.

    e.g. functions like below can be detected:
    # comment
    def foo():
        pass
    """
    func_name_and_cmt = []
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
                        func_name_and_cmt.append((func_name, cmt))
    return func_name_and_cmt

def get_all_names_of_funcs_with_comment(source: str) -> List:
    func_names = []
    infunc_and_same_cmt_list = detect_infunc_and_same_line_comment(source)
    outfunc_cmt_list = detect_outfunc_comment(source)
    cmt_list = infunc_and_same_cmt_list + outfunc_cmt_list
    for func_name, _ in cmt_list:
        func_names.append(func_name)
    return func_names

def get_py_files_inside_dir(path: str) -> List:
    """Return all python files' paths inside the given folder, recursively.
    Note:
    if you have subfolders inside the given folder, it also return python files' paths 
    inside the subfolders.
    """
    paths = []
    for root, _, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".py"):
                paths.append(os.path.join(root, filename))
    return paths
