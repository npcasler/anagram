#!/usr/bin/env python
#
# Anagram
# License: MIT

from __future__ import print_function

from .matcher import AnagramMatcher
import argparse
import textwrap
import os

DESCRIPTION = """Anagram is a command-line utility that groups available permutations
of words in a dictionary into a comma-separated value file

Usage:
    anagram [-i --input] [-n -num-letters] [-o --output] [-h]

"""


def args_options():
    """ Generate an argument parser.

    :returns:
        Parser object
    """

    parser = argparse.ArgumentParser(prog='anagram',
                                     formatter_class=argparse
                                     .RawDescriptionHelpFormatter,
                                     description=textwrap.dedent(DESCRIPTION))

    parser.add_argument('-i', '--input', type=str,
                        default='./tests/samples/american-english',
                        help="Path to input dictionary")

    parser.add_argument('-c', '--count', type=int, default=4,
                        help="Number of letters needed for word to be parsed")

    parser.add_argument('-o', '--output', type=str,
                        default='anagrams.csv', help="Path to output csv")

    return parser


def main(args):
    """
    Main function - launches the program

    :param args:
        The parser arguments
    :type args:
        Parser object

    :returns:
        Number of lines written
    """
    input_dict = ''
    output_csv = ''
    count = 0
    if args:
        if args.input:
            input_dict = args.input
            # Check for bad paths
            if not os.path.exists(input_dict):
                raise IOError("Input dictionary doesn't exist")
            if os.stat(input_dict).st_size == 0:
                return "Input dataset is empty"

        if args.output:
            output_csv = args.output

        if args.count:
            count = args.count
            if count < 0:
                raise ValueError('Character count must be positive')

        # Instantiate the AnagramMatcher class
        anagram = AnagramMatcher(input_dict, count, output_csv)
        # Create key/value store of words
        word_list = anagram.read_dict()
        # Filter keys with requirement that they perm count >= letter count
        key_list = anagram.build_list(word_list)
        # Write the new list to a headerless csv
        rows = anagram.write_csv(key_list, word_list)
        print("Successfully wrote {} anagrams to {}".format(rows, output_csv))
    return len(key_list)


def __main__():

    global parser
    parser = args_options()
    args = parser.parse_args()
    main(args)


if __name__ == '__main__':
    try:
        __main__()
    except IOError as err:
        exit(str(err))
