#! /usr/bin/env python3
# coding: utf-8
import ast
import sys
import itertools
from typing import List, Generator

def get_ast_mod(filename: str) -> ast.Module:
    with open(filename) as f:
        code = f.read()
    mod = ast.parse(code)
    return mod

def get_ast_body(filename: str) -> List[ast.stmt]:
    mod = get_ast_mod(filename)
    return mod.body

def get_top_level_funcs(ast_body: List[ast.stmt]) -> Generator:
    top_level_funcs = (node for node in ast_body if isinstance(node, ast.FunctionDef))
    return top_level_funcs

def get_cls_nodes(ast_body: List[ast.stmt]) -> Generator:
    cls_nodes = (node for node in ast_body if isinstance(node, ast.ClassDef))
    return cls_nodes

def get_cls_member_funcs(ast_body: List[ast.stmt]) -> Generator:
    for cls_ in get_cls_nodes(ast_body):
        for cls_member_funcs in (node for node in cls_.body if isinstance(node, ast.FunctionDef)):
            yield cls_, cls_member_funcs

def get_all_funcs(ast_body: List[ast.stmt]) -> itertools.chain:
    top_level_funcs = get_top_level_funcs(ast_body)
    cls_member_funcs = get_cls_member_funcs(ast_body)
    all_funcs = itertools.chain(top_level_funcs, cls_member_funcs)
    return all_funcs

def print_func_names(func_nodes: Generator) -> None:
    """Here, we use if statements in for loop to differentiate two kind of func_nodes: class member functions
    and top-level functions. For class member functions, we organize them as tuple, (class_node, class_method_node),
    and for top-level functions, we organize them only as single values.
    """
    for func_node in func_nodes:
        if isinstance(func_node, tuple):  # if the node is a class member function node
            print("{}: {}".format(func_node[0].name, func_node[1].name))
        else:  # if the node is a top-level function node
            print(func_node.name)

def print_cls_names(cls_nodes: Generator) -> None:
    for cls_node in cls_nodes:
        print(cls_node.name)

def check_func_docs(func_nodes: Generator) -> None:
    """Here, func could either be a class member function or a top-level function, so we need to differentiate
    them using if statements in for loop.
    """
    for func_node in func_nodes:
        if isinstance(func_node, tuple):  # if the node is a class member function node
            # the output below is ("NAME_OF_CLASS: NAME_OF_CLASS_MEMBER_FUNCTION: DOC_OF_FUNCTION")
            print("{}: {}: {}".format(func_node[0].name, func_node[1].name, ast.get_docstring(func_node[1])))
        else:  # if the node is a top-level function node
            # the output below is ("NAME_OF_TOP_LEVEL_FUNCTION: DOC_OF_FUNCTION")
            print("{}: {}".format(func_node.name, ast.get_docstring(func_node)))

def check_cls_docs(cls_nodes: Generator) -> None:
    for cls_node in cls_nodes:
        # the output below is ("NAME_OF_CLASS: DOC_OF_CLASS")
        print("{}: {}".format(cls_node.name, ast.get_docstring(cls_node)))

def main(argv):
    for filename in argv[1:]:
        print(filename)
        body = get_ast_body(filename)
        func_nodes = get_all_funcs(body)
        cls_nodes = get_cls_nodes(body)
        print("=====Below are class docs=====")
        check_cls_docs(cls_nodes)
        print("=====Below are function docs=====")
        check_func_docs(func_nodes)


if __name__ == "__main__":
    main(sys.argv)
