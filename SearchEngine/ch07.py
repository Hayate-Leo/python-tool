from irpb import chapter06
from gensim import matutils
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score, StratifiedKFold, cross_val_predict, GridSearchCV
from sklearn import svm
from sklearn.metrics import confusion_matrix


def one(path):
    book_texts = [chapter06.get_string_from_file(path+'ch07/%d.txt' % i) for i in range(15)]
    tfidf_model, dic, vectors = chapter06.get_tfidfmodel_and_weights(book_texts)

    vectors = matutils.corpus2dense(vectors, len(dic)).T

    titles = chapter06.get_list_from_file(path+'ch07/book-titles.txt')
    classes = chapter06.get_list_from_file(path+'ch07/class.txt')
    #ナイーブベイズによる学習
    mnb = MultinomialNB()
    mnb.fit(vectors, classes)
    # ナイーブベイズによる推定
    test_texts = ['Pythonで実装', '微分方程式を解く', '規格に準拠', 'アナログからデジタルへ', '人工知能']
    #フレーズの文書ベクトルを作成
    test_bows = chapter06.get_bows(test_texts, dic)
    test_vectors = chapter06.get_weights(test_bows, dic, tfidf_model)
    test_vectors = matutils.corpus2dense(test_vectors, len(dic)).T

    predicted_classes = mnb.predict(test_vectors)
    for i, j in zip(test_texts, predicted_classes):
        print(f'{i}: {j}')

def four(path):
    # read data
    cv_texts = [chapter06.get_string_from_file(path+'ch07/cv/%d.txt' % i) for i in range(90)]
    tfidf_model, dic, vectors = chapter06.get_tfidfmodel_and_weights(cv_texts)
    vectors = matutils.corpus2dense(vectors, len(dic)).T
    classes = chapter06.get_list_from_file(path+'ch07/cv/class.txt')
    # evaluate naive bayes
    K = 3
    skf = StratifiedKFold(n_splits=K)
    classifier = MultinomialNB()
    scores = cross_val_score(classifier, vectors, classes, cv=skf)

    for i in range(K):
        print('Test %d/%d:\t%.4f' % (i+1, K, scores [i]))
    print('Average:\t%.4f' % (sum(scores)/K))

def five(path):
    # read data
    cv_texts = [chapter06.get_string_from_file(path+'ch07/cv/%d.txt' % i) for i in range(90)]
    tfidf_model, dic, vectors = chapter06.get_tfidfmodel_and_weights(cv_texts)
    vectors = matutils.corpus2dense(vectors, len(dic)).T
    classes = chapter06.get_list_from_file(path+'ch07/cv/class.txt')
    K = 3
    skf = StratifiedKFold(n_splits=K)
    # サポートベクトルマシン
    classifier = svm.SVC(kernel='rbf', C=1, gamma=1)
    scores = cross_val_score(classifier, vectors, classes, cv=skf)
    for i in range(K):
        print('Test %d/%d:\t%.4f' % (i+1, K, scores [i]))
    print('Average:\t%.4f' % (sum(scores)/K))
    #混同行列
    prediction = cross_val_predict(classifier, vectors, classes, cv=skf)
    #　分類結果から混同行列作成
    cm = confusion_matrix(classes, prediction)
    class_names = [j for i, j in enumerate(classes) if not j in classes[:i]]

    fmt = '%2d\t'*6

    for i, j in enumerate(cm):
        print(fmt % tuple(j), class_names[i])
    
def eight(path):
    # read data
    cv_texts = [chapter06.get_string_from_file(path+'ch07/cv/%d.txt' % i) for i in range(90)]
    tfidf_model, dic, vectors = chapter06.get_tfidfmodel_and_weights(cv_texts)
    vectors = matutils.corpus2dense(vectors, len(dic)).T
    classes = chapter06.get_list_from_file(path+'ch07/cv/class.txt')
    # サポートベクトルマシン
    classifier = svm.SVC(kernel='rbf', C=1, gamma=1)
    parames = {
        'kernel': ['rbf'],
        'C':  [0.1, 1, 10, 100],
        'gamma': [0.1, 1, 10, 100]
    }

    classifier = svm.SVC()
    gs = GridSearchCV(classifier, parames, cv=3)
    gs.fit(vectors, classes)
    print(gs.best_params_)

if __name__ == '__main__':
    base_path = r'C:/Users/kamis/Documents/Python Scripts/irpb-files/data/'
    eight(base_path)