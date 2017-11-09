# Test to check functionality of AnagramMatcher

from anagram.anagram import AnagramMatcher
import os

def main():
	# Default input parameters
	base_path = os.path.dirname(os.path.realpath(__file__))
	input_dict = "{}/{}".format(base_path,'examples/american-english')
	n_letters = 4
	output_csv = "{}/{}".format(base_path,'anaTest.csv')
	# Instantiate the AnagramMatcher class 
	anagram = AnagramMatcher(input_dict, n_letters, output_csv)
	# Create key/value store of words
	word_list = anagram.read_dict()
	# Filter keys with requirement that they permutation count >= letter count
	key_list = anagram.build_list(word_list)
	# Write the new list to a headerless csv
	anagram.write_csv(key_list, word_list)
	return 0


if __name__ == '__main__':
	main()
