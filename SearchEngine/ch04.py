from irpb import chapter04
from gensim import corpora, models

def two(path):
    book_texts = [chapter04.get_string_from_file(path+'ch04/%d.txt' % i ) for i in range(10)]

    tfidf_model, dic, book_weights = chapter04.get_tfidfmodel_and_weights(book_texts)

    keyword_lists = [[x[0] for x in w[:10]] for w in book_weights]
    #「定理の作り方」は9
    results = [(x, chapter04.jaccard(keyword_lists[9], keyword_lists[x])) for x in range(9)]
    results.sort(key=lambda x: x[1], reverse=True)

    with open(path+'ch04/book-titles.txt', encoding='utf-8') as f:
        titles = f.read().strip().split('\n')

    for x in range(9):
        print('%s %.4f' % (titles[results[x][0]], results[x][1]))


def three():
    texts = ['花より団子', 'とにかく団子', 'みたらしよりあんこ']
    words = [chapter04.get_words(text, keep_pos=['名詞']) for text in texts]
    dic = corpora.Dictionary(words)

    for i in range(len(dic)):
        print('dic[%d] = %s' % (i, dic[i]))
    
    bows = [dic.doc2bow(w) for w in words]
    tfidf = models.TfidfModel(bows)

    weights = tfidf[bows[0]]
    weights = [(i, round(j, 4)) for i, j in weights]
    print('weights =', weights)

def five(path):
    book_texts = [chapter04.get_string_from_file(path+'ch04/%d.txt' % i ) for i in range(10)]
    titles = chapter04.get_list_from_file(path+'ch04/book-titles.txt')
    # 9は「定理の作り方」，-1は以外
    result = chapter04.vsm_search(book_texts[:-1], book_texts[9])
    for x in range(9):
        print('%s %.4f' % (titles[result[x][0]], result[x][1]))

def six(path, query):
    texts = [chapter04.get_string_from_file(path+'ch04/%d.txt' % i ) for i in range(10)]
    titles = chapter04.get_list_from_file(path+'ch04/book-titles.txt')
    result = chapter04.vsm_search(texts, query)
    for x in range(len(result)):
        print('%s %.4f' % (titles[result[x][0]], result[x][1]))


if __name__ == '__main__':
    base_path = r'C:/Users/kamis/Documents/Python Scripts/irpb-files/data/'
    six(base_path, '数学')
