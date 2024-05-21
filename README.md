# Unscramble Words

## Overview

The "Unscramble Words" project is designed to make it easier to unscramble words using Python. This project was created to address the difficulty I faced in unscrambling words manually. The project consists of two main files: `unscramble_words_function.py` and `unscramble_words_api.py`. The former contains the core functions used for unscrambling words, while the latter provides an API interface to facilitate easier usage.

## Features

- **Unscramble Words**: The program can unscramble words with a minimum length of 3 letters up to any length.
- **Multilingual Support**: The dataset includes words in both English and Indonesian.
- **Comprehensive Datasets**: The English dataset is sourced from multiple dictionaries, including Longman, MIT, and Oxford. The Indonesian dataset is sourced from Kamus Besar Bahasa Indonesia (KBBI).

## Project Structure

```plaintext
Unscramble_Words/
├── README.md
├── unscramble_words_function.py
├── unscramble_words_api.py
├── .gitignore
├── requirements.txt
└── datasets/
    ├── eng_corpus.txt
    └── id_corpus.txt
```
## Installation
To get started with the project, clone the repository and install the required dependencies.

```
git clone https://github.com/irasalsabila/unscramble_words.git
cd unscramble-words
pip install -r requirements.txt
```

## Usage
### Using the Functions Directly

You can use the functions provided in `unscramble_words_function.py` to unscramble words directly.

```
import unscramble_words_function as uw

# load dictionary
dictionary_loaded = uw.load_dictionary(dictionary)

# get into the scramble
scrambled_word = "taurdesta"
possible_words = uw.unscramble(text, dictionary_loaded)
print(possible_words)
```

### Using the API
The `unscramble_words_api.py` file provides an API interface for easier usage.

1. Access `127.0.0.1:5001/update_dictionary` to update the dictionary
```
{
    "dictionary": "dictionary/id_corpus.txt"
}
```

2. Time to predict using `127.0.0.1:5001/predict`
```
{
    "text": "DAKIT"
}
```

## Datasets
The project uses datasets in both English and Indonesian languages. The English dataset is compiled from Longman, MIT, and Oxford dictionaries, while the Indonesian dataset is sourced from Kamus Cesar Bahasa Indonesia (KBBI).

## Contact
For any questions or suggestions, feel free to contact me at [irasalsabila@gmail.com].