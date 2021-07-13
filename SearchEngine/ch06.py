from scipy import linalg
from irpb import chapter06
from gensim import matutils
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster, cophenet


def one(path):
    book_texts = [chapter06.get_string_from_file(path+'ch06/%d.txt' % i) for i in range(12)]

    tfid_model, dic, vectors = chapter06.get_tfidfmodel_and_weights(book_texts)
    titles = chapter06.get_list_from_file(path+'ch06/book-titles.txt')
    # two
    dense_vectors = matutils.corpus2dense(vectors, len(dic)).T
    K = 4
    result = KMeans(n_clusters=K).fit(dense_vectors)

    for label in range(K):
        print([titles[i] for i in np.where(result.labels_ == label)[0]])
    
def three():
    data = [[1, 3], [2, 2], [2.5, 5], [5.5, 8.5], [6, 8]]

    xlist = [x[0] for x in data]
    ylist = [x[1] for x in data]

    plt.xlim(0.5, 6.5)
    plt.ylim(1.5, 9.5)
    plt.scatter(xlist, ylist)

    delta = 0.1
    for i, (x, y) in enumerate(zip(xlist, ylist)):
        plt.annotate(str(i), (x + delta, y + delta))
    plt.show()

def four():
    data = [[1, 3], [2, 2], [2.5, 5], [5.5, 8.5], [6, 8]]
    d = pdist(data)
    L = linkage(d, method='average')

    threshold = 4
    dendrogram(L, orientation='left', color_threshold=threshold)
    f = fcluster(L, threshold, criterion='distance')

    for i, j in enumerate(f):
        print('data[%d]: cluster %d' % (i, j))

    plt.show()

def six(path):
    book_texts = [chapter06.get_string_from_file(path+'ch06/%d.txt' % i) for i in range(12)]

    tfid_model, dic, vectors = chapter06.get_tfidfmodel_and_weights(book_texts)
    titles = chapter06.get_list_from_file(path+'ch06/book-titles.txt')
    # two
    dense_vectors = matutils.corpus2dense(vectors, len(dic)).T
    chapter06.configure_fonts_for_japanese()
    d = pdist(dense_vectors)

    L = linkage(d, method='ward')
    dendrogram(L, labels=titles, color_threshold=1.54, orientation='left')
    plt.show()

    # 8
    methods = ['average', 'centroid', 'complete', 'median', 'single', 'ward', 'weighted']

    for m in methods:
        L = linkage(d, method=m)
        c = cophenet(L, d)
        print('%s \t%7.4f' % (m, c[0]))


if __name__ == '__main__':
    base_path = r'C:/Users/kamis/Documents/Python Scripts/irpb-files/data/'
    six(base_path)
