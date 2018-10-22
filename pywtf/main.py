#! /usr/bin/env python3
# coding: utf-8
import ast
import sys
import itertools
from typing import List, Generator

def get_ast_body(filename: str) -> List[ast.stmt]:
    with open(filename) as f:
        code = f.read()
    mod = ast.parse(code)
    return mod.body

def get_top_level_funcs(ast_body: List[ast.stmt]) -> Generator:
    top_level_funcs = (node for node in ast_body if isinstance(node, ast.FunctionDef))
    return top_level_funcs

def get_cls_member_funcs(ast_body: List[ast.stmt]) -> Generator:
    for cls_ in (node_c for node_c in ast_body if isinstance(node_c, ast.ClassDef)):
        for cls_member_funcs in (node_f for node_f in cls_.body if isinstance(node_f, ast.FunctionDef)):
            yield cls_, cls_member_funcs

def get_func_names(ast_body: List[ast.stmt]) -> itertools.chain:
    top_level_funcs = get_top_level_funcs(ast_body)
    cls_member_funcs = get_cls_member_funcs(ast_body)
    all_funcs = itertools.chain(top_level_funcs, cls_member_funcs)
    return all_funcs

def print_func_names(func_names: itertools.chain) -> None:
    for func_name in func_names:
        if isinstance(func_name, tuple):
            print("{}: {}".format(func_name[0].name, func_name[1].name))
        else:
            print(func_name.name)

def main(argv):
    for filename in argv[1:]:
        print(filename)
        body = get_ast_body(filename)
        func_names = get_func_names(body)
        print_func_names(func_names)


if __name__ == "__main__":
    main(sys.argv)
