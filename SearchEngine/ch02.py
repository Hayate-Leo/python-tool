from janome.tokenizer import Tokenizer
from irpb import chapter02
from collections import Counter
import matplotlib.pyplot as plt


def two():
    tokenizer = Tokenizer()
    word = 'すももももももももものうち'
    for t in tokenizer.tokenize(word):
        print(f'{t.surface}\t{t.part_of_speech}')

def three():
    tokenizer = Tokenizer(wakati=True)
    word = 'すももももももももものうち'
    print(list(tokenizer.tokenize(word)))

def four():
    tokenizer = Tokenizer()
    word = 'ふなっしーはかわいい'
    for t in tokenizer.tokenize(word):
        print(f'{t.surface}\t{t.part_of_speech}')
    
def five(path):
    word = 'ふなっしーはかわいい'
    tokenizer = Tokenizer(path+'ch02/userdic.csv', udic_type='simpledic')
    for t in tokenizer.tokenize(word):
        print(f'{t.surface}\t{t.part_of_speech}')

def seven(path):
    query = '京都'
    file_list = [path+'ch01/%02d.txt' % x for x in (1, 2, 3, 4)]
    for f in file_list:
        print(f, chapter02.get_m_snippet_from_file(f, query))

def eleven(path):
    string = chapter02.get_string_from_file(path+'ch01/melos.txt')
    words = chapter02.get_words(string)
    count = Counter(words)
    font = chapter02.get_japanese_fonts()[0]
    chapter02.create_wordcloud(count, font)

def thirteen(path):
    string = chapter02.get_string_from_file(path+'ch01/melos.txt')
    words = chapter02.get_words(string)
    count = Counter(words)
    chapter02.plot_frequency(count)

    string2 = chapter02.get_string_from_file(path+'ch02/alice.txt')
    words2 = chapter02.get_words(string2)
    count2 = Counter(words2)
    chapter02.plot_frequency(count2)
    plt.show()


if __name__ == '__main__':
    base_path = r'C:/Users/kamis/Documents/Python Scripts/irpb-files/data/'
    thirteen(base_path)
