#File Indexing of a specific folder indicated by the user

import glob
import re

def main():
    word_files = dict()
    file_list = glob.glob("[abc].txt")

    for filename in file_list:
        with open(filename, 'r') as infile:
            content = infile.read()
            words = set(re.findall(r"\w+", content, re.I))  # `set` evita duplicati nel singolo file
            for word in words:
                key = word.upper()
                if key not in word_files:
                    word_files[key] = []
                if filename not in word_files[key]:
                    word_files[key].append(filename)

    for word in sorted(word_files):
        print(word, "->", word_files[word])

main()