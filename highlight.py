#!/usr/bin/env python

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='highlight the specified string.')
    parser.add_argument('string', type=str,
                        help='an string for highlight')
    parser.add_argument('-c', '--color', type=str, default='blue',
                        help='an color for highlighting (red,green,orange,[blue])')
    parser.add_argument('-f', '--file', type=str, default=None,
                        help='an file you want to highlight')
    args = parser.parse_args()


    COLOR_CODE = {
        'red'    : "\033[37;41;1;4;5m",
        'green'  : "\033[37;42;1;4;5m",
        'orange' : "\033[37;43;1;4;5m",
        'blue'   : "\033[37;44;1;4;5m",
        'end'    : "\033[0m",
    }


    if args.file:
        with open(args.file, 'r') as f:
            docs = f.readlines()
    else:
        docs = sys.stdin.readlines()

    _docs = ''
    string = COLOR_CODE[args.color]+args.string+COLOR_CODE['end']

    for doc in docs:
        doc = doc.split(args.string)
        _docs += string.join(doc)

    print(_docs, end='')


if __name__ == '__main__':
    main()
