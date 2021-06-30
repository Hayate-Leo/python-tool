import pandas as pd

class Document:
    def __init__(self):
        self.execute()

    def read_excel(self):
        return pd.read_excel('SearchEngine/murataisao.xlsx', sheet_name='contents')
    
    def execute(self):
        df = self.read_excel()
        self.doc = df['研究実績の概要'][0]
    
    def __str__(self):
        return self.doc
        
    
    

if __name__ == '__main__':
    print(Document())