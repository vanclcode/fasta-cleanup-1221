#!/usr/bin/env python3

import sys

def main(args):
    if len(args) != 3:
        print("Script expects 3 arguments:\n1: reportfile, 2: input fasta file, 3: output fasta file")
        exit(1)

    subs = subsDict(args[0])
    # cleanFile(args[1], args[2], subs)

def subsDict(reportfile):
    reportDict = {}
    with open(reportfile) as subs:
        for line in subs.readlines():

            info = line.split()
            key = info[0]
            values = info[1].split('.')
            values = (values[0], values[2])
            reportDict[key] = values
    print(reportDict)
    return reportDict

def cleanFile(inputfile, outputfile, subs):
    with open(inputfile) as inp, open(outputfile) as out:
        for line in inp.readlines():
            if line[0] == '>':
                # idecko
                pass
            else:
                # sekvence
                pass


if __name__ == '__main__':
    main(sys.argv[1:])
