import os
import sys
from lark import Lark
import argparse
import logging
from .grammar import grammar


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', action='store', nargs='+')
    parser.add_argument('--ast-only', action='store_true')
    args = parser.parse_args()

    if not args.ast_only:
        logging.critical('ObjAs only supports printing of AST right now')
        sys.exit(1)

    parser = Lark(grammar, parser='lalr')

    for file_name in args.file:
        if file_name == '-':
            content = sys.stdin.read()
            file_name = '/dev/stdin'
            print()
        else:
            with open(file_name, 'r') as file:
                content = file.read()

        ast = parser.parse(content)
        print(file_name)
        print('=' * len(file_name))
        print(ast.pretty())
        print()
        print()


if __name__ == '__main__':
    main()
