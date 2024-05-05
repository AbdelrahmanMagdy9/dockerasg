import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist
import os

# Ensure the necessary NLTK resources are available
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

def analyze_text(file):
    """
    Reads the text file, filters out stopwords, and returns how many times each words was repeated
    """
    with open(file, 'r') as file:
        text = file.read().lower()

    stop_words = stopwords.words('english')
    tokens = word_tokenize(text)

    # Remove stopwords tokenized text
    words = [word for word in tokens if word not in stop_words and word.isalnum()]
    return FreqDist(words)

def save_repeated_words(fd, output_file):
    """
    Takes a frequency distribution and writes it to a specified output file.
    """
    with open(output_file, 'w') as output_file:
        for word, count in sorted(fd.items(), key=lambda x: x[1], reverse=True):
            line = f"{word}: {count}\n"
            output_file.write(line)
            print(line, end="")

def main():
    input_file = 'text_to_filter.txt'
    output_file = 'repeated_words.txt'

    if not os.path.exists(input_file):
        print(f"'{input_file}' doesn't exist. Make sure the file is in the correct directory")
        return

    # Process the text and get the frequency distribution
    repeated_words = analyze_text(input_file)

    # Save the frequency distribution to a file
    save_repeated_words(repeated_words, output_file)

    print(f"Repeated words saved to '{output_file}'.")

if __name__ == "__main__":
    main()
