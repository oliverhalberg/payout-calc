#!/usr/bin/env python3

import argparse

def input_to_dict(infile):
    print("Not yet implemented")

    # open file
    # for each line of file:
        # if payment < 0:
            # add name:payment entry to payers dict
        # elif payment > 0:
            # add name:payment entry to receivers dict
        # else:
            # how to handle 0 payments? come back to this when other parts are designed
    # close file
    # return (payers, receivers)

def main():
    # File paths from args
    infile = args.data
    outfile = args.destination

    # dicts = input_to_dict(infile)
    # payers = dicts[0]
    # receivers = dicts[1]

    print("to implement")
    if (args.verbose):
        print("vvvv tester code")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="run program in verbose mode", action="store_true")
    parser.add_argument("data", help="the .csv file to read from. there should be two columns: one with names and one with corresponding net payments")
    parser.add_argument("destination", help="the file path to write output to")
    args = parser.parse_args()
    main()