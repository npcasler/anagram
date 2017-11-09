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
python anagramTest.py -i {input_dict} -c {count} -o {output_csv}
```

Where

* *input\_dict* - Path to input dictionary file
* *count* - Minimum letter count needed for a word to be included
* *output\_csv* - Path for output CSV 

### Dependencies

* [Pandas](https://pandas.pydata.org) - Data Frame Manipulation and Querying

### Datasets

* afrikaans        : Sample dictionary file of Afrikaans words 
  [Source](https://download.openwall.net/pub/wordlists/languages/Afrikaans/lower.gz)
* american-english : Sample English dictionary
  [Source](https://packages.ubuntu.com/trusty/wordlist/wamerican)
* british-english  : Sample British English dictionary
  [Source](https://packages.ubuntu.com/trusty/wordlist/wbritish)
* czech            : Sample Czech dictionary 
  [Source](https://download.openwall.net/pub/wordlists/languages/Czech/lower.gz)
* danish           : Sample Danish dictionary
  [Source](https://download.openwall.net/pub/wordlists/languages/Danish/2-large/lower.gz)
* finnish          : Sample Finnish dictionary
  [Source](https://download.openwall.net/pub/wordlists/languages/Finnish/lower.gz)
* german           : Sample German dictionary
  [Source](https://download.openwall.net/pub/wordlists/languages/German/2-large/cap.gz)
* mixed            : Mixed case English dictionary
  [Source](https://download.openwall.net/pub/wordlists/languages/English/4-extra/mixed.gz)

## Authors

* **Nathan Casler** - *Initial Commits* [github](https://github.com/npcasler)




