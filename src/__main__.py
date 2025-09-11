import os
import sys
from lark import Lark
import argparse
import logging

from .transformer import ObjAsTransformer
from .grammar import grammar


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', action='store', nargs='+')
    parser.add_argument('--ast-only', action='store_true', help='Print AST and exit')
    parser.add_argument(
        '--no-transform',
        action='store_true',
        help='Do not transform AST (use only with --ast-only)',
    )
    args = parser.parse_args()

    if not args.ast_only:
        logging.critical('ObjAs only supports printing of AST right now')
        sys.exit(1)

    parser = Lark(
        grammar, parser='lalr', transformer=None if args.no_transform else ObjAsTransformer()
    )

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
