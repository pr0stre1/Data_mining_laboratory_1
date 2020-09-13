import csv
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

category_ham = ''
category_spam = ''
words_spam = []
word_spam_count = []
words_ham = []
word_ham_count = []
most_frequent_words_spam = []
most_frequent_words_ham = []

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


# Reading SCV file
with open('sms-spam-corpus.csv', "r") as csvFileRead:
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
        # Categorize text to 'ham' and 'spam' categories
        if row[0] == 'ham':
            category_ham = category_ham + ' ' + rowText
        else:
            if row[0] == 'spam':
                category_spam = category_spam + ' ' + rowText
    # Lists of each word and list of all words
    frequency_spam, frequency_spam_text = frequency_of_words(category_spam)
    frequency_ham, frequency_ham_text = frequency_of_words(category_ham)
    # Creating lists of each word and frequencies of this words for category spam
    for word in range(0, len(frequency_spam)):
        words_spam.append(frequency_spam[word])
        word_spam_count.append(frequency_spam_text.count(frequency_spam[word]))
        # print('Frequency of', frequency_ham[word], 'is :', frequency_ham_text.count(frequency_ham[word]))
    # Creating list of top 20 most frequent words for category spam
    for i in range(20):
        most_frequent_words_spam.append(most_frequent_word(words_spam, most_frequent_words_spam))
    # Creating lists of each word and frequencies of this words for category ham
    for word in range(0, len(frequency_ham)):
        words_ham.append(frequency_ham[word])
        word_ham_count.append(frequency_ham_text.count(frequency_ham[word]))
    # Creating list of top 20 most frequent words for category ham
    for i in range(20):
        most_frequent_words_ham.append(most_frequent_word(words_ham, most_frequent_words_ham))

    print("Top 20 most frequent words in category spam:")
    print(most_frequent_words_spam)
    print("Top 20 most frequent words in category ham:")
    print(most_frequent_words_ham)
# Writing SCV file
with open('sms-spam-corpus-edited.csv', "w") as csvFileWrite:
    writer = csv.writer(csvFileWrite)
