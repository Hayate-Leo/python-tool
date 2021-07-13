from irpb import chapter08
from pprint import pprint

def one(path):
    texts = [chapter08.get_string_from_file(path+'ch08/%d.txt' % i) for i in range(12)]
    titles = chapter08.get_list_from_file(path+'ch08/book-titles.txt')

    r = chapter08.vsm_search(texts, '環境')
    pprint([(i, titles[i]) for i, _ in r])

    # 適合性フィードバック
    rf = chapter08.vsm_search_with_feedback(texts, '環境', [6], [11])
    pprint([(i, titles[i]) for i, _ in rf])

if __name__ == '__main__':
    base_path = r'C:/Users/kamis/Documents/Python Scripts/irpb-files/data/'
    one(base_path)