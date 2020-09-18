import csv
import matplotlib.pyplot as plt
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Full text in category ham
category_ham = ''
# Full text in category spam
category_spam = ''
# List of each word in category spam
words_spam = []
# List of words in category spam
word_spam_count = []
# List of each word in category ham
words_ham = []
# List of words in category ham
word_ham_count = []
# List of each sentence in category spam
sentences_spam = []
# List of each sentence in category ham
sentences_ham = []
# Count of all words in category spam
count_of_all_words_spam = 0
# Count of all words in category ham
count_of_all_words_ham = 0
# List of numbers to delete
numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
# List of special symbols to delete
special_symbols = {'\n', '\b', '\f', '\r', '\t', '\v', '\a', '$', '\0', '^', '|', '[', ']', '(', ')', '*', '.', '"',
                   '\\', '/', '&', ';', '#', '@', '!', '`', '`', '%', '_', '-', '+', '=', '{', '}', '<', '>', '?', ':',
                   '№', '	', "'", ',', '‰', '©'}
# List of stop words to delete
stop_words = {'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out',
              'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into',
              'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the',
              'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me',
              'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both',
              'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and',
              'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over',
              'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too',
              'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my',
              'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than'}


# Function deletes numbers
def delete_numbers(text):
    return ''.join([char for char in text if char not in numbers])


# Function deletes special symbols
def delete_special_symbols(text):
    return ''.join([char for char in text if char not in special_symbols])


# Function deletes stop words
def delete_stop_words(text):
    tokenized_row = word_tokenize(text)

    return ''.join(' '.join([char for char in tokenized_row if char not in stop_words]))


# Function do stemming
def porter_stammer(text):
    porter = PorterStemmer()
    tokenized_row = word_tokenize(text)
    result = ''

    for w in tokenized_row:
        result = result + ' ' + porter.stem(w)

    return result


# Function find frequency of each words
def frequency_of_words(text):
    text_split = text.split()
    frequency_text = []

    for w in text_split:
        if w not in frequency_text:
            frequency_text.append(w)

    # for word in range(0, len(frequency_text)):
        # print('Frequency of', frequency_text[word], 'is :', text.count(frequency_text[word]))

    return frequency_text, text_split


# Finding length of each word in the list
def length_of_words(t_list, count_of_all_words):
    words_lengths = []

    for w in range(0, len(t_list)):
        words_lengths.append(len(t_list[w])/count_of_all_words)

    return words_lengths


# Finding length of each sentence in the list
def length_of_sentences(t_list):
    sentences_lengths = []

    for w in range(0, len(t_list)):
        sentences_lengths.append(len(t_list[w]))

    return sentences_lengths


# Function find most frequent words
def most_frequent_word(list_of_words, top_list):
    counter = 0
    curr_most_frequent_word = list_of_words[0]

    for w in list_of_words:
        curr_frequency = list_of_words.count(w)
        if curr_frequency > counter:
            if w not in top_list:
                counter = curr_frequency
                curr_most_frequent_word = w

    return curr_most_frequent_word


# Function find average length of words in the list
def average_length_of_words(t_list):
    value = 0
    count = 0

    for w in range(0, len(t_list)):
        value = value + len(t_list[w])
        count = count + 1

    return value/count


# Function find average length of sentences in the list
def average_length_of_sentences(t_list):
    value = 0
    count = 0

    for w in range(0, len(t_list)):
        value = value + len(t_list[w])
        count = count + 1

    return value/count


# Reading CSV file
with open('sms-spam-corpus.csv', "r", newline='') as csvFileRead:
    next(csvFileRead)
    reader = csv.reader(csvFileRead)
# Action for each row in the file
    for row in reader:
        # Deleting numbers
        rowText = delete_numbers(row[1])
        # Deleting special symbols
        rowText = delete_special_symbols(rowText)
        # Deleting stop words
        rowText = delete_stop_words(rowText)
        # Changing text to lower case
        rowText = rowText.lower()
        # Stemming of the text
        rowText = porter_stammer(rowText)
        # Adding each sentence to the list
        # Categorize text to 'ham' and 'spam' categories
        if row[0] == 'ham':
            sentences_ham.append(rowText)
            category_ham = category_ham + ' ' + rowText
        else:
            if row[0] == 'spam':
                sentences_spam.append(rowText)
                category_spam = category_spam + ' ' + rowText
    # Lists of each word and list of all words
    frequency_spam, frequency_spam_text = frequency_of_words(category_spam)
    frequency_ham, frequency_ham_text = frequency_of_words(category_ham)
    # Creating lists of each word and frequencies of this words for category spam
    for word in range(0, len(frequency_spam)):
        words_spam.append(frequency_spam[word])
        word_spam_count.append(frequency_spam_text.count(frequency_spam[word]))
        # print('Frequency of', frequency_ham[word], 'is :', frequency_ham_text.count(frequency_ham[word]))
    # Sort lists of category spam
    zipped_lists = zip(word_spam_count, words_spam)
    sorted_pairs = sorted(zipped_lists)
    reversed_lists = reversed(sorted_pairs)
    tuples = zip(*reversed_lists)
    word_spam_count, words_spam = [list(tuple) for tuple in tuples]
    # Creating lists of each word and frequencies of this words for category ham
    for word in range(0, len(frequency_ham)):
        words_ham.append(frequency_ham[word])
        word_ham_count.append(frequency_ham_text.count(frequency_ham[word]))
    # Sort lists of category ham
    zipped_lists = zip(word_ham_count, words_ham)
    sorted_pairs = sorted(zipped_lists)
    reversed_lists = reversed(sorted_pairs)
    tuples = zip(*reversed_lists)
    word_ham_count, words_ham = [list(tuple) for tuple in tuples]

    """print("Top 20 most frequent words in category spam:")
    for word in range(0, 20):
        print(f'Word: {words_spam[word]}. Times: {word_spam_count[word]}')
    # print(most_frequent_words_spam)
    print("Top 20 most frequent words in category ham:")
    for word in range(0, 20):
        print(f'Word: {words_ham[word]}. Times: {word_ham_count[word]}')"""
    # print(most_frequent_words_ham)
# Writing CSV files for category spam
with open('output/category-spam-words-frequencies.csv', "w", newline='') as csvFileWrite:
    writer = csv.writer(csvFileWrite)
    for word in range(0, len(words_spam)):
        writer.writerow([words_spam[word], word_spam_count[word]])
# Writing CSV files for category ham
with open('output/category-ham-words-frequencies.csv', "w", newline='') as csvFileWrite:
    writer = csv.writer(csvFileWrite)
    for word in range(0, len(words_ham)):
        writer.writerow([words_ham[word], word_ham_count[word]])
# Count of all words in each category
for word in range (0, len(word_ham_count)):
    count_of_all_words_ham = count_of_all_words_ham + word_ham_count[word]
for word in range (0, len(word_spam_count)):
    count_of_all_words_spam = count_of_all_words_spam + word_spam_count[word]
# Find length of each word for categories
lengths_of_words_ham = length_of_words(words_ham, count_of_all_words_ham)
lengths_of_words_spam = length_of_words(words_spam, count_of_all_words_spam)
# Bins to show on the hist
# bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Hist settings
# length-of-words-histogram graphic
plt.subplots()
plt.style.use('fivethirtyeight')
plt.figure(figsize=(15, 10))
# Create hist and find average for categories (3 symbols after dot)
plt.hist(lengths_of_words_ham,
         bins=range(0, 20),
         edgecolor='black',
         label='Ham (avg: ' + str("%.3f" % average_length_of_words(words_ham)/count_of_all_words_ham) + ')')
plt.hist(lengths_of_words_spam,
         bins=range(0, 20),
         edgecolor='black',
         label='Spam (avg: ' + str("%.3f" % average_length_of_words(words_spam)/count_of_all_words_spam) + ')')
plt.legend(loc='best')
plt.ylabel('Count of words')
plt.xlabel('Length of words')
plt.title('Length of words histogram')
# Saving hist to file
plt.savefig('output/length-of-words-histogram.png')
# Clear plot
plt.clf()
# length-of-sentences-histogram graphic
plt.figure(figsize=(15, 10))
# Find length of each sentence for categories
length_of_sentences_ham = length_of_sentences(sentences_ham)
length_of_sentences_spam = length_of_sentences(sentences_spam)
# Bins to show on the hist
# bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Create hist and find average for categories (3 symbols after dot)
plt.hist(length_of_sentences_ham,
         bins=range(0, 200),
         edgecolor='black',
         label='Ham (avg: ' + str("%.3f" % average_length_of_sentences(sentences_ham)) + ')')
plt.hist(length_of_sentences_spam,
         bins=range(0, 200),
         edgecolor='black',
         label='Spam (avg: ' + str("%.3f" % average_length_of_sentences(sentences_spam)) + ')')
plt.legend(loc='best')
plt.ylabel('Count of sentences')
plt.xlabel('Length of sentences')
plt.title('Length of sentences histogram')
# Saving hist to file
plt.savefig('output/length-of-sentences-histogram.png')
# 20-most frequent-words-ham graphic
plt.clf()
plt.figure(figsize=(15, 10))
bar_ham_top_20 = []
count_ham_top_20 = []
for word in range(0, 20):
    bar_ham_top_20.append(words_ham[word])
    count_ham_top_20.append(word_ham_count[word])
y_pos = np.arange(len(count_ham_top_20))
plt.title('20 most frequent words for category ham')
plt.xlabel('Words')
plt.ylabel('Count')
plt.bar(y_pos, count_ham_top_20)
plt.xticks(y_pos, bar_ham_top_20)
plt.savefig('output/20-most-frequent-words-ham.png')
# 20-most-frequent-words-spam graphic
plt.clf()
plt.figure(figsize=(15, 10))
bar_spam_top_20 = []
count_spam_top_20 = []
for word in range(0, 20):
    bar_spam_top_20.append(words_spam[word])
    count_spam_top_20.append(word_spam_count[word])
y_pos = np.arange(len(count_spam_top_20))
plt.title('20 most frequent words for category spam')
plt.xlabel('Words')
plt.ylabel('Count')
plt.bar(y_pos, count_spam_top_20)
plt.xticks(y_pos, bar_spam_top_20)
plt.savefig('output/20-most-frequent-words-spam.png')
# frequency analyze spam
plt.clf()
plt.figure(figsize=(15, 10))
bar_spam_top_20 = []
count_spam_top_20 = []
for word in range(0, 20):
    bar_spam_top_20.append(words_spam[word])
    count_spam_top_20.append(word_spam_count[word]/count_of_all_words_spam)
y_pos = np.arange(len(count_spam_top_20))
plt.title('Frequency analyze for category spam')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.bar(y_pos, count_spam_top_20)
plt.xticks(y_pos, bar_spam_top_20)
plt.savefig('output/frequency-analyze-spam.png')
# frequency analyze ham
plt.clf()
plt.figure(figsize=(15, 10))
bar_ham_top_20 = []
count_ham_top_20 = []
for word in range(0, 20):
    bar_ham_top_20.append(words_ham[word])
    count_ham_top_20.append(word_ham_count[word]/count_of_all_words_ham)
y_pos = np.arange(len(count_ham_top_20))
plt.title('Frequency analyze for category ham')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.bar(y_pos, count_ham_top_20)
plt.xticks(y_pos, bar_ham_top_20)
plt.savefig('output/frequency-analyze-ham.png')
