#!/usr/bin/env python3

import argparse

def main():
    print("to implement")
    if (args.verbose):
        print("vvvv tester code")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Run program in verbose mode", action="store_true")
    parser.add_argument("data", help="The .csv file to read from")
    parser.add_argument("destination", help="The file path to write output to")
    args = parser.parse_args()
    main()