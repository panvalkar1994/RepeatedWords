# python 3.8.6 environment
# In this problem we will take string input from user via commandline.
# This program will be useful to type small input to console.

# Take input from user
raw_str = input('Enter your string: ')
words = raw_str.split()

# Build frequency map
word_freq = {}
for word in words:
    if word not in word_freq.keys():
        word_freq[word] = 1
    else:
        word_freq[word] += 1

# repeated words
num_repeat_words = 0
for word in word_freq:
    if word_freq[word]>1:
        num_repeat_words += 1
        # print(word, str(word_freq[word]))

# Result
print("Number of repeated words is "+ str(num_repeat_words))

# Enter your string: I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn’t really happy.
# Output:
# I 5
# happy 2
# because 2
# Number of repeated words is 3


