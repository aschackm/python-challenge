# Alex Schackmuth
# hw3 python
#PyParagraph

### import dependencies
import os
### text file path
txtpath = os.path.join("raw_data", "paragraph_1.txt")

### define variables
word_count = 0
sentence_count = 0
ave_letter_count = 0
ave_sentence_length = 0

### open txt and get counts
with open(txtpath, 'r') as paragraph:
    for line in paragraph:
        word_list = line.split(" ")
        word_count += len(word_list)
        sentence_list = line.split("." or "?" or "!")
        sentence_count += len(sentence_list)

### averages
ave_letter_count = sum(len(word) for word in word_list) / len(word_list)
ave_sentence_length = sum(len(sentence) for sentence in sentence_list) / len(sentence_list)

print("-"*40)
print("Paragraph Analysis")
print("-"*40)
print("Approximate Word Count:" + str(word_count))
print("Approximate Sentence Count:" + str(sentence_count))
print("Average Letter Count:" + str(ave_letter_count))
print("Average Sentence Length:" + str(ave_sentence_length))
print("-"*40)
    

