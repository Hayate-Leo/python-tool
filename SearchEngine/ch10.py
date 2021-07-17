from irpb import chapter10
from gensim.models import Word2Vec, KeyedVectors, Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from pprint import pprint
import pickle

def one():
    training_documents = ['年越しには天ぷら蕎麦をいただきます',
                        '関東では雑煮に鶏肉と小松菜を入れます']
    training_data = [chapter10.get_words(d) for d in training_documents]
    print('training_data = ', training_data)

    w2v_model = Word2Vec(training_data, vector_size=3, window=2, sg=1, min_count=1)

    word = '蕎麦'
    print(word, '=', w2v_model.wv[word])

def two(path):
    word_vectors = KeyedVectors.load(path+'ch10/w2v.kv')
    pprint(word_vectors.most_similar(positive=['酸素'], topn=5))
    print(word_vectors.most_similar(positive=['饂飩', 'イタリア'],
                            negative=['日本'], topn=1))
    
    data = [
        [['饂飩', 'イタリア'], ['日本']],
        [['信長', '美濃'], ['尾張']],
        [['丸の内', '大阪'], ['東京']]
    ]

    for p_words, n_words in data:
        top = word_vectors.most_similar(positive=p_words, negative=n_words, topn=1)
        answer = top[0][0]

        print(f'{p_words[0]} - {n_words[0]} + {p_words[1]} = {answer}')

def six():
    training_documents = ['年越しには天ぷら蕎麦をいただきます',
                        '関東では雑煮に鶏肉と小松菜を入れます']
    training_data = [chapter10.get_words(d) for d in training_documents]
    tagged_data = [TaggedDocument(words=d, tags=[i]) for i, d in enumerate(training_data)]
    pprint(tagged_data)

    d2v_model = Doc2Vec(tagged_data, dm=1, vector_size=3, window=2, min_count=1)
    print(d2v_model.docvecs[0])

def nine(path):
    model_file = path+'jawiki.doc2vec.dmpv300d.model'
    d2v_wikipedia_model = Doc2Vec.load(model_file)

    doc1 = chapter10.get_words('Pythonを使うと自然言語処理が簡単にできる')
    doc2 = chapter10.get_words('実データを用いた情報検索プ ログラミングは楽しい')
    print(f'doc1 = {doc1}')
    print(f'doc2 = {doc2}')

    print('類似度： %.4f ' % d2v_wikipedia_model.docvecs.similarity_unseen_docs(d2v_wikipedia_model, doc1, doc2, steps=50))

def twelve(path):
    model_file = path+'jawiki.doc2vec.dmpv300d.model'
    d2v_wikipedia_model = Doc2Vec.load(model_file)
    book_texts = [chapter10.get_string_from_file(path+'ch05/%d.txt' % i) for i in range(10)]
    query = '人工知能'
    right_answer = [0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
    result = chapter10.d2v_search(d2v_wikipedia_model, book_texts, query)

    ranking = tuple([x[0] for x in result])
    print(ranking)

    print('%.4f' % chapter10.get_average_precision(ranking, right_answer))

def thirteen(path):
    model_file = path+'jawiki.doc2vec.dmpv300d.model'
    d2v_wikipedia_model = Doc2Vec.load(model_file)
    with open(path+'ch10/tokenized.dat', 'rb') as f:
        tokenized_texts, tokenized_query = pickle.load(f)
    
    right_answer = [0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
    
    result = chapter10.d2v_search(d2v_wikipedia_model, tokenized_texts, tokenized_query)

    ranking = tuple([x[0] for x in result])
    print(ranking)

    print('%.4f' % chapter10.get_average_precision(ranking, right_answer))


if __name__ == '__main__':
    base_path = r'C:/Users/kamis/Documents/Python Scripts/irpb-files/data/'
    thirteen(base_path)