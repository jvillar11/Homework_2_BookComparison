import requests
import string

def get_unique_word_count(url):
    """Download a book from a URL, clean the text, and return the count of unique words."""
    response = requests.get(url)

    punctuation_remove = ",.!?;"
    punctuation_space = "'\"()[]=-_"

    unique_words = {}

    lines = response.text.split('\n')
    for line in lines:
        for c in punctuation_remove:
            line = line.replace(c, "")
        for c in punctuation_space:
            line = line.replace(c, " ")

        words = line.split()

        for word in words:
            word = word.lower().strip(string.punctuation)  # Ensure clean words
            if word:  # Ignore empty strings
                unique_words[word] = unique_words.get(word, 0) + 1

    return len(unique_words)

dorian_gray_url = "https://www.gutenberg.org/cache/epub/4078/pg4078.txt"
wizard_oz_url = "https://www.gutenberg.org/cache/epub/55/pg55.txt"
dorian_gray_unique_words = get_unique_word_count(dorian_gray_url)
wizard_oz_unique_words = get_unique_word_count(wizard_oz_url)

print(f"The Picture of Dorian Gray (Oscar Wilde) unique words: {dorian_gray_unique_words}")
print(f"The Wonderful Wizard of Oz (L. Frank Baum) unique words: {wizard_oz_unique_words}")

if dorian_gray_unique_words > wizard_oz_unique_words:
    print("Oscar Wilde use more unique words than Frank Baum.")
else:
    print("Frank Baum used more unique words than Oscar Wilde.")

