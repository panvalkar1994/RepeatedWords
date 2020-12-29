# python 3.8.6 environment
# In this program we will deal with text files. User will provide a text file to be read.
# Output will be number of words which are repeated in the text.

# Input file 
file = open('test.txt',"r")

# create a map of word frequncy
word_freq = {}

# Frequncy map builder function 
def word_freq_builder(raw_string, word_freq):
    words = raw_string.split()
    for word in words:
        # ignoring sentence endings like '.', '!', '?' are not words
        if word == '.' or word == '!' or word =='?':
            continue
        # assuming words 'round.' and 'round .' to be same
        if word[-1] == '.':
            word = word[:len(word)-1]
        if word not in word_freq.keys():
            word_freq[word] = 1
        else:
            word_freq[word] += 1


# Reading though the input file and building frequncy map
for line in file.readlines():
    # rememove white space in front and back of the line
    raw_string = line.rstrip()
    word_freq_builder(raw_string, word_freq)

# Close file
file.close()

# repeated words
num_repeat_words = 0
for word in word_freq:
    if word_freq[word]>1:
        num_repeat_words += 1
        print(word, str(word_freq[word]))

# Result
print("Number of repeated words is "+ str(num_repeat_words))
