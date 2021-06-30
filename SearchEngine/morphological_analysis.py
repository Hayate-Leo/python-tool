from janome.tokenizer import Tokenizer
from document import Document

class MorphoAna:
    def __init__(self, doc):
        self.doc = doc
        self.execute()
    
    def execute(self):
        print(self.doc)
        

if __name__ == '__main__':
    doc = Document()
    MorphoAna(doc)