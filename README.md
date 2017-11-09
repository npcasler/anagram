# Anagram Matcher

This application is a basic implementation of an anagram sort.

## Getting Started

### Prerequisites

This repository depends on the pandas library. If you do not have it already 
installed. Run the following:

```
pip install pandas
```

Or with virtualenv

```
virtualenv anagramEnv
source anagramEnv/bin/activate

pip install pandas
```

### Installing

Clone the repository from github with the following:

```
git clone https://github.com/npcasler/anagram.git
```

### Running Test

AnagramTest - This test will aggregate the example *american-english* dictionary
and generate a CSV with the anagram permutations for words with 4 or more
letters and at least as many permutations as its characters.

For the default test run:

```
python anagramTest.py
```

TO use this application on a different dictionary or to change the output file
path run the following

``` 
python anagramTest.py -i {input_dict} -n {n_letters} -o {output_csv}
```

Where

* *input\_dict* - Path to input dictionary file
* *n\_letters* - Minimum letter count needed for a word to be included
* *output\_csv* - Path for output CSV 

### Dependencies

* [Pandas](https://pandas.pydata.org) - Data Frame Manipulation and Querying

### Datasets

* american-english : Sample english dictionary file from Ubuntu OS

## Authors

* **Nathan Casler** - *Initial Commits* [github](https://github.com/npcasler)




