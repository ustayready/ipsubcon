#!/usr/bin/python
# IP Subnet Converter
# v0.1
# 07/16/2014
#
# Twitter: @ustayready
# Email: mike@linux.edu

import argparse, ipcalc

ver = 0.1
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

verbose = None
output = None

parser = argparse.ArgumentParser(description='Convert multiple IP ranges to a list of usable IP addresses')
parser.add_argument('--range', help='Single range to convert', type=str)
parser.add_argument('--file', help='Filename of ranges to convert', type=str)
parser.add_argument('--output', help='output results file', type=str)
parser.add_argument('--verbose', help='print verbose output', action='store_true', default=False)
args = parser.parse_args()

def valid(args):
        global ver

        if not any([args.range, args.file]):
                parser.print_usage()
                quit()

        if args.range and args.file:
                print('ERROR: Only supply a range or file but not both.')
                quit()
        return True

def convertranges(ranges):
        global output, verbose

        for range in ranges:
                if "/" in range:
                       for x in ipcalc.Network(range):
                           if verbose:
                                 print str(x)
                           if output:
                                 with open(output, "a") as out_file:
                                      out_file.write(str(x) + "\n")

if valid(args):
        ranges = []
        if args.verbose:
                verbose = args.verbose
        if args.output:
                output = args.output
        if args.range:
                ranges.append(args.range)

        if args.file:
                f = open(args.file)
                for line in f:
                        ranges.append(line.strip())
        convertranges(ranges)

