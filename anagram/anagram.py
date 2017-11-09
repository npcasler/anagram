###############################################################################
#  AnagramMatcher
#
# Utility class to extract all anagrams from a given dictionary file
#
# Output is a comma separated list of anagrams where the word is over 4 letters
# long and as many or more anagrams were found than the number of letters in
# the origin words
#
# @param dict Path to dictionary file
# @param nLetters Number of letters needed to qualify for matching
# @param output Path to output file
#
###############################################################################
import csv
import pandas as pd


class AnagramMatcher():
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
        # Get frequency list for keys
        freq = word_list.groupby('key').agg('count')
        # Filter out only keys with greater or equal frequency to length
        key_list = freq.loc[freq['word'] >= freq.index.str.len()]
        return key_list

    def write_csv(self, key_list, word_list):
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
        return 0
