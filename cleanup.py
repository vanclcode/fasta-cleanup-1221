#!/usr/bin/env python3

import sys

def main(args):
    if len(args) != 3:
        print("Script expects 3 arguments:\n1: reportfile, 2: input fasta file, 3: output fasta file")
        exit(1)

    subs = subsDict(args[0])
    cleanFile(args[1], args[2], subs)

def subsDict(reportfile):
    reportDict = {}
    with open(reportfile, 'r') as subs:
        for line in subs.readlines():

            info = line.split()
            key = info[0]
            values = info[1].split('.')
            values = (int(values[0]), int(values[2]))
            reportDict[key] = values
    return reportDict

def cleanFile(inputfile, outputfile, subs):
    totalchanged = 0
    totaltested = 0
    with open(inputfile, 'r') as inp, open(outputfile, 'w') as out:
        while line := inp.readline():
            if line[0] == '>':
                # idecko
                id = line[1:].split()[0].strip()
                seq = inp.readline().strip()
                seql = len(seq)
                totaltested += 1
                if id in subs:
                    # je tam
                    if (seql - subs[id][0]) > subs[id][1]:
                        # druha pulka je vetsi
                        subseq = seq[subs[id][1]:]
                    else:
                        subseq = seq[0:subs[id][0] + 1]

                    totalchanged += 1
                    # if(totalchanged % 100 == 0):
                    #     print(f"# changed {totalchanged}/{totaltested}")
                else:
                    subseq = seq

                out.write(f">{id}\n")
                out.write(f"{subseq}\n")

    print(f"# Finished - changed total of {totalchanged}/{totaltested}")


if __name__ == '__main__':
    main(sys.argv[1:])
