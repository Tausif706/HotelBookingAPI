
import nltk
from nltk.corpus import stopwords
from collections import Counter

def generate_word_frequency(content):
    # Tokenize the content into words
    words = nltk.word_tokenize(content)

    # Remove stopwords (common words that don't carry much meaning)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

    # Generate word frequency
    word_freq = Counter(filtered_words)
    
    # Sort the words by frequency in descending order
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
    
    elements = []
    for word, freq in sorted_word_freq.items():
        elements.append(word)
    return elements

def append_to_output_file(sorted_word_freq ):
    # Append words and frequencies to the output file
    with open('./main/file.txt', 'a', encoding='utf-8') as output_file:
        for word in sorted_word_freq:
            output_file.write(f'{word}\n')

