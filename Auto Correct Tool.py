import numpy as np
from difflib import get_close_matches

def auto_correct(word, word_list, threshold=0.8):
    matches = get_close_matches(word, word_list, n=1, cutoff=threshold)
    
    if matches:
        return matches[0]
    else:
        return None

# Sample word list
word_list = ['apple', 'banana', 'cherry', 'grape', 'mango', 'orange', 'pear', 'strawberry', 'watermelon']

# Test the auto-correct tool
input_word = 'aple'
corrected_word = auto_correct(input_word, word_list)

if corrected_word:
    print(f"Did you mean '{corrected_word}'?")
else:
    print("No suggestion found.")

