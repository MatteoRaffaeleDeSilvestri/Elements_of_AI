
import math

# Data block
text = '''he really really loves coffee
          my sister dislikes coffee
          my sister loves tea'''

def main(text):

    # Split text into lists of words
    docs = [line.split() for line in text.splitlines()]

    N = len(docs)

    # Create vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.split()))

    df = {}
    tf = {}

    for word in vocabulary:
    
        tf[word] = [doc.count(word)/len(doc) for doc in docs]
        df[word] = sum([word in doc for doc in docs])/N

    # Loop through documents to calculate the tf-idf values
    for doc_index, doc in enumerate(docs):

        tfidf = []
        
        for word in vocabulary:
            
            tf_idf_val = tf[word][doc_index]*math.log(1/df[word],10)
            tfidf.append(tf_idf_val) 

        print(tfidf)

if __name__ == "__main__":
    
    main(text)
