#import pytorch
import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np
#nltk.download('punkt') if you get error you have to use this line
temmer=PorterStemmer()

def tokenization(sentence):
    return nltk.word_tokenize(sentence)
def temming(word):
    return temmer.stem(word.lower())
def bag_of_word(tokenized_sentence, all_word):
    tokenized_sentence=[temming(w) for w in tokenized_sentence]
    bag=np.zeros(len(all_word), dtype=np.float32)#get lenght of all_word and create a array zero
    for inx,w in enumerate(all_word):
        if w in tokenized_sentence:
            bag[inx]=1.0
    return bag
    
'''arr=["hello","how","are","you"]
words=["hi","hello","I","you","bye","thank","cool"]
b=bag_of_word(arr,words)
print(b)'''