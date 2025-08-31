#!/usr/bin/env python3

import argparse

def input_to_lists(infile):
    print("Not yet implemented")

    # open file
    # for each line of file:
        # split on ',' to get name and payment
        # if payment < 0:
            # add (name, payment) entry to payers list
        # elif payment > 0:
            # add (name, payment) entry to receivers list
        # else:
            # how to handle 0 payments? come back to this when other parts are designed
    # close file
    # return (payers, receivers)

def main():
    # File paths from args
    infile = args.data
    outfile = args.destination

    # bring in and sort lists
    # lists = input_to_lists(infile)
    # payers = lists[0].sort(key = lambda payer: payer[1], reverse=True)
    # receivers = lists[1].sort(key = lambda receiver: receiver[1])

    # check that len(payers) == len(receivers), exit if False

    # open outfile for writing

    # 



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