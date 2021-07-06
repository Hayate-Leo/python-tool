import pandas as pd

class Document:
    def __init__(self):
        self.read_excel()

    def read_excel(self):
        self.df = pd.read_excel('SearchEngine/murataisao.xlsx', sheet_name='contents')
    
    def __str__(self):
        return self.df['研究代表者'][0]
    
    @property
    def doc(self):
        return self.df['研究実績の概要'][0]
        
    
    

if __name__ == '__main__':
    print(Document())