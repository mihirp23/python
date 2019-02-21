#!/usr/bin/env python

## Mihir Patel
## 2/21/19
## A program that calculates the frequence of the words
## from the sentence provided by user. 
## File : word_frequency.py

############################################################
def main():
############################################################

    print("Welcome!")
    print("I will output frequence of each word in your input.")

    inp_str = input("input: ")
    list_of_words = inp_str.split()
    freq_dict = {}

    # loop thorough each word and add to dictionary
    # the frequency of the word. One entry per word
    for word in list_of_words:
        if word not in freq_dict:
            print("adding to dictionary")
            freq_dict[word] = list_of_words.count(word)

    # output by sorting key alphanumerically
    for word,frequency in sorted(freq_dict.items()):
        print(str(word) + " : "+ str(frequency))

# main()

if __name__ == "__main__":
    main()
