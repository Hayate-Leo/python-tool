from irpb import chapter09
from gensim.models import LsiModel
from pprint import pprint

def one(path):
    book_texts = [chapter09.get_string_from_file(path+'ch05/%d.txt' % i) for i in range(10)]
    tfidf_model, dic, tfidf_weights = chapter09.get_tfidfmodel_and_weights(book_texts)
    
    num_topics = 5
    lsi_model = LsiModel(corpus=tfidf_weights, id2word=dic, num_topics=num_topics)
    print(lsi_model.print_topics())

def six(path):
    book_texts = [chapter09.get_string_from_file(path+'ch05/%d.txt' % i) for i in range(10)]
    query = '人工知能'
    tfidf_result = chapter09.vsm_search(book_texts, query)
    num_topics = 5
    lsi_result = chapter09.lsi_search(book_texts, query, num_topics)
    pprint(lsi_result)

    right_answer = [0, 1, 0, 1, 0, 1, 0, 0, 1, 1]

    tfidf_ranking = [x[0] for x in tfidf_result]
    lsi_ranking = [x[0] for x in lsi_result]

    print('TFIDF: %.4f' % chapter09.get_average_precision(tfidf_ranking, right_answer))
    print('LSI: %.4f' % chapter09.get_average_precision(lsi_ranking, right_answer))



if __name__ == '__main__':
    base_path = r'C:/Users/kamis/Documents/Python Scripts/irpb-files/data/'
    six(base_path)