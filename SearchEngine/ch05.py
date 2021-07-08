from pprint import pprint
from irpb import chapter05
import matplotlib.pyplot as plt


def two(path):
    book_texts = [chapter05.get_string_from_file(path+'ch05/%d.txt' % i) for i in range(10)]
    query = '人工知能'
    result = chapter05.vsm_search(book_texts, query)
    pprint(result)
    #five
    right_answer = [0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
    my_answer = chapter05.select_by_threshold(result, threshold=0)
    print(f'right_answer = {right_answer}')
    print(f'my_answer = {my_answer}')
    #six
    chapter05.print_scores(right_answer, my_answer)

def seven(path):
    book_texts = [chapter05.get_string_from_file(path+'ch05/%d.txt' % i) for i in range(10)]
    query = '人工知能'
    result = chapter05.vsm_search(book_texts, query)
    right_answer = [0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
    my_answer = chapter05.select_by_threshold(result, threshold=0.3)
    print(f'my_answer = {my_answer}')
    chapter05.print_scores(right_answer, my_answer)
    #nine
    my_ranking = tuple(x[0] for x in result)
    print(my_ranking)
    #ten
    print(''.join([str(right_answer[i]) for i in my_ranking]))
    #eleven
    matching = [i for i, x in enumerate(right_answer) if x == 1]
    non_matching = [i for i, x in enumerate(right_answer) if x == 0]
    good_ranking = tuple(matching + non_matching)
    print(good_ranking)
    print(''.join([str(right_answer[i]) for i in good_ranking]))
    #13
    n = 2
    my_answer_n = chapter05.top_n(my_ranking, n)
    print(my_answer_n)
    print(chapter05.recall_score(right_answer, my_answer_n))
    print(chapter05.precision_score(right_answer, my_answer_n))

def sixteen(path):
    book_texts = [chapter05.get_string_from_file(path+'ch05/%d.txt' % i) for i in range(10)]
    query = '人工知能'
    result = chapter05.vsm_search(book_texts, query)
    right_answer = [0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
    my_ranking = tuple(x[0] for x in result)
    matching = [i for i, x in enumerate(right_answer) if x == 1]
    non_matching = [i for i, x in enumerate(right_answer) if x == 0]
    good_ranking = tuple(matching + non_matching)
    chapter05.draw_pr_curve(my_ranking, right_answer)
    chapter05.draw_pr_curve(good_ranking, right_answer)
    plt.show()
    #19 平均適合率
    print('my_ranking %.4f' % chapter05.get_average_precision(my_ranking, right_answer))
    print('good_ranking %.4f' % chapter05.get_average_precision(good_ranking, right_answer))


if __name__ == '__main__':
    base_path = r'C:/Users/kamis/Documents/Python Scripts/irpb-files/data/'
    sixteen(base_path)