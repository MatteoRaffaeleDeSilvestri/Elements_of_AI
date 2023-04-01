
import math 
import numpy as np

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def distance(data):
    difference = [[sum([abs(i-j) for i, j in zip(row1, row2)]) for row1 in data] for row2 in data]
    return difference

def main(text):

    docs = [line.split() for line in text.splitlines()] # split text into lines and lists of words
    vocabulary = list(set(text.split())) # create the vocabulary: the list of words that appear at least once

    df = {}
    tf = {}
    
    for word in vocabulary:
        tf[word] = [doc.count(word)/len(doc) for doc in docs]
        df[word] = sum([word in doc for doc in docs])/len(docs)
    
    full_tfidf = []
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            tf_idf_val = tf[word][doc_index]*math.log(1/df[word],10)
            tfidf.append(tf_idf_val) 
        full_tfidf.append(tfidf)
    dist = distance(full_tfidf)
    all_of_them = np.asarray(dist).astype('float')
    all_of_them[all_of_them==0] = np.nan
    print(np.unravel_index(np.nanargmin(all_of_them), all_of_them.shape))

if __name__ == "__main__":

    main(text)
