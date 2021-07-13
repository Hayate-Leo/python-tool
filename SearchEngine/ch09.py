from irpb import chapter09
from gensim.models import LsiModel, LdaModel
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

def nine(path):
    book_texts = [chapter09.get_string_from_file(path+'ch05/%d.txt' % i) for i in range(10)]
    query = '人工知能'
    num_topics = 5
    nmf_result = chapter09.nmf_search(book_texts, query, num_topics, random_state=7)
    pprint(nmf_result)
    right_answer = [0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
    nmf_ranking = [x[0] for x in nmf_result]
    print('%.4f' % chapter09.get_average_precision(nmf_ranking, right_answer))

def eleven(path):
    book_texts = [chapter09.get_string_from_file(path+'ch05/%d.txt' % i) for i in range(10)]
    tfidf_model, dic, tfidf_weights = chapter09.get_tfidfmodel_and_weights(book_texts)
    
    lda_model = LdaModel(
        corpus=tfidf_weights, id2word=dic, num_topics=5, passes=20, random_state=6
    )

    lda_weights = lda_model[tfidf_weights]
    print(book_texts[1])
    pprint(lda_weights[1])
    print(lda_model.print_topics(0, 4))

def fif(path):
    book_texts = [chapter09.get_string_from_file(path+'ch05/%d.txt' % i) for i in range(10)]
    query = '人工知能'
    num_topics = 5
    lda_result = chapter09.lda_search(book_texts, query, num_topics, random_state=6)
    right_answer = [0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
    lda_ranking = tuple([x[0] for x in lda_result])
    print('%.4f' % chapter09.get_average_precision(lda_ranking, right_answer))

def sixteen(path):
    book_texts = [chapter09.get_string_from_file(path+'ch05/%d.txt' % i) for i in range(10)]
    query = '人工知能'
    num_topics = 5
    num_trials = 5
    sum_of_ap = 0.0
    for i in range(num_trials):
        lda_result = chapter09.lda_search(book_texts, query, num_topics)
        right_answer = [0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
        lda_ranking = tuple([x[0] for x in lda_result])
        ap = chapter09.get_average_precision(lda_ranking, right_answer)
        print('%d: %.4f' % (i, ap))
        sum_of_ap += ap
    print('平均: %.4f' % (sum_of_ap/num_trials))

if __name__ == '__main__':
    base_path = r'C:/Users/kamis/Documents/Python Scripts/irpb-files/data/'
    sixteen(base_path)