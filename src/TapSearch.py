import nltk.data
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class TapSearch(object):
    def __init__(self):
        self.stop_words = set(stopwords.words('english')) 
        self.documents = dict()
        self.revIndex = dict()
        self.documentCount = 1
    
    def clear_index(self):
        self.documents.clear()
        self.revIndex.clear()
    
    def search_index(self, query):
        query = query.lower()
        if query in self.revIndex.keys():
            docs = [ self.documents[doc] for doc in self.revIndex[query] ]
            return docs[:10]
        else:
            return ["No Document Found!"]

    def preprocess_document(self, document):
        stop_words = self.stop_words

        _document = document.strip().split()
        _document = [ word.strip() for word in _document ]
        
        processedDocument = []
        for word in _document:
            _word = word.strip(" !?.,'").lower()
            if not _word in stop_words:
                processedDocument.append(_word)
        return processedDocument

    def insert_index(self, text):
        
        documents = text.replace('\r','\n').split('\n\n')

        for document in documents:

            if len(document.strip()) == 0:
                continue

            key = self.documentCount

            # Preprocess document
            _document = self.preprocess_document(document)

            if len(_document)==0:
                return

            # Insert document in document collection
            self.documents[key] = document


            # Index the document
            for word in _document:
                if word in self.revIndex.keys() and key not in self.revIndex[word]:
                    self.revIndex[word].append(key)
                else:
                    self.revIndex[word] = [ key ]
            self.documentCount += 1


tapsearch = TapSearch()