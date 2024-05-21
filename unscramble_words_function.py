from itertools import permutations

def load_dictionary(file_path):
    """Load the dictionary file and return a set of words without punctuation, all in lowercase."""
    with open(file_path, 'r') as file:
        words = set(file.read().split())

    # Remove words with punctuation and convert to lowercase
    cleaned_words = {word.lower() for word in words if word.isalpha()}
    return cleaned_words

def unscramble(scrambled_word, dictionary):
    """Generate all possible unscrambled words from the scrambled word, ignoring case."""
    # Convert the scrambled word to lowercase
    scrambled_word = scrambled_word.lower()
    length = len(scrambled_word)
    unscrambled_words = set()

    # Generate permutations and check if they are in the dictionary
    for r in range(3, length+1):
        permutation_object = permutations(scrambled_word, r)
        for permutation in permutation_object:
            word = ''.join(permutation)
            if word in dictionary:
                unscrambled_words.add(word)
    
    # Sort the words by length (fewer letters first)
    sorted_words = sorted(unscrambled_words, key=len)
    
    return sorted_words