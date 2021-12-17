#!/usr/bin/env python3

import sys

def main(arguments):
    print(arguments)


def subsDict(reportfile):
    with open(reportfile) as subs:
        info = subs.split(',')[3:4]
        key = info[0][10:]
        values = info[1][10:].split('.')
        values = (values[0], values[2])
        
        


if __name__ == '__main__':
    main(sys.argv[1:])
