#!/usr/bin/env python3

import sys

def main(args):
    subsDict(args[0])


def subsDict(reportfile):
    reportDict = {}
    with open(reportfile) as subs:
        while True:
            line = subs.readline()
            if not line:
                break

            info = line.split(',')[2:4]
            key = info[0][6:]
            values = info[1][8:].split('.')
            values = (values[0], values[2])
            reportDict[key] = values



if __name__ == '__main__':
    main(sys.argv[1:])
