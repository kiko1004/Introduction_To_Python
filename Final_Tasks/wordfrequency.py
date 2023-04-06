# Write a program that reads a text file and counts the frequency of each word in the file.
def word_frequency(file_name):
    with open(file_name) as file:
        words = file.read().split()
        freq_dict = {}
        for word in words:
            freq_dict[word] = freq_dict.get(word, 0) + 1
        return freq_dict
