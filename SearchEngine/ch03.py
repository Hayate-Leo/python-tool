from janome.analyzer import Analyzer
from janome.tokenfilter import ExtractAttributeFilter, POSStopFilter, POSKeepFilter
from irpb import chapter03
from collections import Counter
from pprint import pprint
from gensim import corpora, models


def one():
    string = '京都とは違う奈良の魅力'
    stop_pos = ['助詞', '助動詞', '記号']
    analyzer = Analyzer(token_filters=[POSStopFilter(stop_pos), 
                        ExtractAttributeFilter('surface')])
    print(list(analyzer.analyze(string)))

def two():
    string = '京都とは違う奈良の魅力'
    keep_pos = ['名詞']
    analyzer = Analyzer(token_filters=[POSKeepFilter(keep_pos), 
                        ExtractAttributeFilter('surface')])
    print(list(analyzer.analyze(string)))

def three(path):
    string = chapter03.get_string_from_file(path+'ch01/melos.txt')
    words = chapter03.get_words(string, keep_pos=['名詞'])
    count = Counter(words)
    font = chapter03.get_japanese_fonts()[0]
    chapter03.create_wordcloud(count, font)

def four(path):
    D = ['ch03/1.txt', 'ch03/2.txt']
    texts = [chapter03.get_string_from_file(path+x) for x in D]
    pprint(texts, width=40)
    #five
    docs = [chapter03.get_words(x, keep_pos=['名詞']) for x in texts]
    pprint(docs, width=40)
    #six
    dictionary = corpora.Dictionary(docs)
    for k, v in dictionary.items():
        print(k, v)
    #eight idと出現頻度
    bows = [dictionary.doc2bow(d) for d in docs]
    pprint(bows)

def eleven(path):
    D = [path+'ch03/1.txt', path+'ch03/2.txt']
    dic, bows = chapter03.build_corpus(D)
    tfidf_model = models.TfidfModel(bows, normalize=False)
    weights = tfidf_model[bows[1]]
    print(weights)

def fourteen(path):
    dic, bows = chapter03.load_aozora_corpus()
    melos_text = chapter03.get_string_from_file(path+'ch01/melos.txt')
    dic, bows, melos_bows = chapter03.add_to_corpus([melos_text], dic, bows)
    tfidf_model = models.TfidfModel(bows, normalize=True)
    weights = chapter03.get_weights(melos_bows, dic, tfidf_model, surface=True)
    count = dict(weights[0])
    font = chapter03.get_japanese_fonts()[0]
    chapter03.create_wordcloud(count, font)

if __name__ == '__main__':
    base_path = r'C:/Users/kamis/Documents/Python Scripts/irpb-files/data/'
    fourteen(base_path)