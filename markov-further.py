"""Generate Markov text from text files. FURTHER STUDY"""

from random import choice
import sys
import string


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path) as file:
        whole_text = file.read()

    return whole_text


def make_chains(text_string,ngram_size):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()
    for i in range(len(words)-ngram_size):
        key = (words[i],)
        for n in range(1, ngram_size):
            key += (words[i+n],)

        value = words[i+ngram_size]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

    return chains


def make_text(chains,ngram_size):
    """Return text from chains."""

    words = []

    # your code goes here
    while True:
        first_words = choice(list(chains.keys())) #(tuple of ngram size)
        if first_words[0][0].isupper():
            break

    next_word = choice(chains[first_words])
    words.extend(list(first_words) + [next_word])
    

    #print(words)

    while True:
        #we grab the last n words in the words list
        key = tuple(words[-ngram_size:])

        if key in chains:
            next_word = choice(chains[key])
            words.append(next_word)
            if words[-1][-1] in string.punctuation:
                break
        else:
            break

    return " ".join(words)


input_path = sys.argv[1]

ngram_size = 2

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, ngram_size)

# for key in chains:
#     print(key, chains[key])


# Produce random text
random_text = make_text(chains, ngram_size)

print(random_text)
