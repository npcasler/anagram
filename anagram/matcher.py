#!/usr/bin/env python
#
# Matcher
# License: MIT
import csv
import pandas as pd


class AnagramMatcher():
    """ Container class to hold dictionary values in memory.

    :param dictionary: The file path to dictionary file
    :type dictionary:
        str
    :param count:      The character threshold for words to be permuted
    :type count:
        int
    :param str output: The file path for output csv
    :type output:
        str

    :return: AnagramMatcher instance
    """
    dictionary = ''
    count = 0
    output = ''

    # Initialize basic dataset values
    def __init__(self, dictionary, count, output):
        self.dictionary = dictionary
        self.count = count
        self.output = output

    # Read the dictionary file into memory for faster access
    def read_dict(self):
        """
        Read and pre-process the dictionary file. Processing includes
        stripping white space and forcing lowercase for all letters.
        Words are also assigned a hash key which is computed by sorting
        the letters alphabetically.

        :return word_list: DataFrame of [key,word] entries
        :type word_list: pandas.DataFrame
        """

        # Create a list to hold the dictionaries
        words = []
        with open(self.dictionary) as f:
            # Pre-process the dictioanry file
            for line in f:
                # If the words has enough letters, clean and generate key
                if len(line.strip()) >= self.count:
                    # Remove white space and force lower-case
                    word = line.strip().lower()
                    # Sort letters alphabetically for key
                    key = "".join(sorted(word))
                    # Basic key/value format for Pandas processing
                    words.append({'key': key, 'word': word})
        # Create pandas data frame for fase aggregation
        word_list = pd.DataFrame(words)
        return word_list

    def build_list(self, word_list):
        """
        Create a frequency list of permutations by aggregating matching keys.
        Keys with frequencies that match or exceed their character count are
        extracted.

        :param pandas.DataFrame word_list: DataFrame holding all {key,word}
        entries from dictionary file.

        :return pandas.DataFrame key_list: List of keys which meet count
        threshold
        """
        # Get frequency list for keys
        freq = word_list.groupby('key').agg('count')
        # Filter out only keys with greater or equal frequency to length
        key_list = freq.loc[freq['word'] >= freq.index.str.len()]
        return key_list

    def write_csv(self, key_list, word_list):
        """
        Generate csv of available permutations of which meet the count
        threshold condition.

        :param pandas.DataFrame key_list:
            DataFrame of keys which meet threshold
        :param pandas.DataFrame word_list:
            DataFrame of {key,word} entries from original dictionary file.

        :return int line_count:
            Number of permutation groups written
        """
        # Write out data
        out_data = []
        # Match filtered indexes to words
        for i in key_list.index:
            subset = word_list[word_list['key'] == i]
            # Add to aggregate list
            out_data.append(subset['word'].tolist())
        # Dump list to headerless CSV
        with open(self.output, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(out_data)
        return len(out_data)
