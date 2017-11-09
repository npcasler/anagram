#!/usr/bin/env python
#
# AnagramTest
# License: CC0 1.0 Universal

from __future__ import print_function

from anagram.anagram import AnagramMatcher
import argparse
import textwrap


DESCRIPTION = """Anagram is a command-line utility that groups available permutations
of words in a dictionary into a comma-separated value file

Usage:
    anagram [-i --input] [-n -num-letters] [-o --output] [-h]

    arguments:
        -i, --input         Path to input dictionary file

        -h, --help          Show this help message and exit

        -c, --count   Minimum number of letters for word to be included

        -o, --output        Path for output CSV file of permutations

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
                        default='./examples/american-english',
                        help="Path to input dictionary")

    parser.add_argument('-c', '--count', type=int, default=4,
                        help="Number of letters needed for word to be parsed")

    parser.add_argument('-o', '--output', type=str,
                        default='anaTest.csv', help="Path to output csv")

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

        if args.output:
            output_csv = args.output

        if args.count:
            count = args.count

        # Instantiate the AnagramMatcher class
        anagram = AnagramMatcher(input_dict, count, output_csv)
        # Create key/value store of words
        word_list = anagram.read_dict()
        # Filter keys with requirement that they perm count >= letter count
        key_list = anagram.build_list(word_list)
        # Write the new list to a headerless csv
        anagram.write_csv(key_list, word_list)
        print("Successfully wrote anagrams to {}".format(output_csv))
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
