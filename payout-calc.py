#!/usr/bin/env python3

import argparse

def input_to_lists(infile):

    payers = []
    receivers = []

    # open file
    with open(infile, 'r') as file:
        for line in file:
            # split on ',' to get name and earnings
            split_line = line.split(',')
            try:
                earnings = float(split_line[1])
                name = split_line[0]
                
                if earnings < 0:
                    payers.append((name, earnings))
                elif earnings > 0:
                    receivers.append((name, earnings))
                else:
                    # skip - net 0 not included in payout calculation since no action is needed
                    if args.verbose:
                        print(name + " has net earnings of 0 - skipped")
            except ValueError:
                # if payment can't parse to a float, skip to next line (allows header lines to be bypassed)
                continue
    return (payers, receivers)

    # for each line of file:
        # if payment < 0:
            # add (name, float(payment)) entry to payers list
        # elif payment > 0:
            # add (name, float(payment)) entry to receivers list
        # else:
            # if args.verbose:
                # print(name +  " has net earnings of 0 - skipped")
    # close file
    # return (payers, receivers)

def main():
    # File paths from args
    infile = args.data
    outfile = args.destination

    # Currency formatting
    currency = ''
    if args.currency == 'd':
        currency = '$'
    elif args.currency == 'e':
        currency = '€'
    elif args.currency == 'p':
        currency = '£'
    elif args.currency == 'y':
        currency = '¥'

    if args.verbose:
        print("Processing data...")

    # bring in and sort lists
    # lists = input_to_lists(infile)
    # payers = lists[0].sort(key = lambda payer: payer[1])
    # receivers = lists[1].sort(key = lambda receiver: receiver[1], reverse=True) # reverse is bigger values first

    # check that sum(payers[1]) == sum(receivers[1]), exit if False

    #output = ""

    # while len(payers) != 0:
        # current_payer = payers[0]
        # current_receiver = receivers[0]

        # amount = 0 # placeholder
        # if (abs(current_payer[1]) > current_receiver[1]):
            # amount = current_receiver[1]
            
        # elif (abs(current_payer[1]) < current_receiver[1]):
            # 

        # current_payer[1] = current_payer[1] + amount
        # current_receiver[1] = current_receiver[1] - amount
        # if (current_payer[1] == 0):
            # payers.remove(0)
        # else:
            # payers[0] = current_payer
        # if (curent_receiver[1] == 0):
            # receivers.remove(0)
        # else:
            # receivers[0] = current_receiver
        
        #output:
        # out = current_payer[0] + " pays " + current_receiver[0] + " " + currency + amount
        # if args.verbose:
            # print(out)
        # output += out

    # open outfile for writing
    # write output to file
    # close file
    # print("Done")

    print("to implement")
    if args.verbose:
        print("vvvv tester code")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="run program in verbose mode", action="store_true")
    parser.add_argument("-c", "--currency", help="optional currency sign for output - d for USD/CAD, e for euros, p for GBP, y for yen", choices=['d', 'e', 'p', 'y'], default='')
    parser.add_argument("data", help="the .csv file to read from. there should be two columns: one with names and one with corresponding net earnings. see README.md for an example")
    parser.add_argument("destination", help="the file path to write output to")
    args = parser.parse_args()
    main()