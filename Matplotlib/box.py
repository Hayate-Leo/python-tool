# https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html
# https://matplotlib.org/stable/gallery/statistics/boxplot_color.html
# https://matplotlib.org/stable/gallery/statistics/boxplot.html


import matplotlib.pyplot as plt
import numpy as np
from thesis_format import ThesisFormat


class BoxFormat(ThesisFormat):
    def __init__(self) -> None:
        super().__init__()

    def plt_box(self):
        # step1 発生する乱数の固定化
        np.random.seed(19680801)
        # step2 データの作成
        all_data = [np.random.normal(0, std, 100) for std in range(7, 10)]
        labels = ['x1', 'x2', 'x3']
        # step3 グラフフレームの作成
        fig, ax = plt.subplots()

        # step4 箱ひげ図の描画
        # 一般的な箱ひげ図
        # ax.boxplot(all_data, labels=labels)
        # ax.set_title('basic plot')

        # 平均
        ax.boxplot(all_data, labels=labels, showmeans=True, meanline=True)
        ax.set_title('show mean lines')

        # ノッチ付き
        # ax.boxplot(all_data, 1, labels=labels)
        # ax.set_title('notched plot')

        # 外れ値の記号
        # ax.boxplot(all_data, sym='gD', labels=labels)
        # ax.set_title('change outlier\npoint symbols')

        # 外れ値の表示有無
        # ax.boxplot(all_data, sym='', labels=labels)
        # ax.set_title("don't show\noutlier points")

        # 水平箱ひげ図
        # ax.boxplot(all_data, sym='rs', vert=False, labels=labels)
        # ax.set_title('horizontal boxes')

        # 髭の長さ
        # ax.boxplot(all_data, sym='rs', whis=0.75, labels=labels)
        # ax.set_title('change whisker length')

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')

        plt.show()

    def plt_color(self):
        # step1 発生する乱数の固定化
        np.random.seed(19680801)
        # step2 データの作成
        all_data = [np.random.normal(0, std, 100) for std in range(7, 10)]
        labels = ['x1', 'x2', 'x3']
        # step3 グラフフレームの作成
        fig, ax = plt.subplots()

        # 箱の色
        bplot = ax.boxplot(all_data, labels=labels, patch_artist=True)
        colors = ['pink', 'lightblue', 'lightgreen']
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_color('white')
            # patch.set_facecolor(color)
            patch.set_edgecolor(color)
            patch.set_linewidth(3)
        ax.set_title('Set the edgecolor of boxes')

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')

        plt.show()
    
    def plt_props(self):
        # step1 発生する乱数の固定化
        np.random.seed(19680801)
        # step2 データの作成
        all_data = [np.random.normal(0, std, 100) for std in range(7, 10)]
        labels = ['x1', 'x2', 'x3']
        # step3 グラフフレームの作成
        fig, ax = plt.subplots()

        # 中央値
        # ax.boxplot(
        #     all_data, 
        #     labels=labels, 
        #     medianprops={
        #         'color': 'C0',
        #         'linewidth':3,
        #         'linestyle': '-.',
        #     }
        # )
        # 平均値
        ax.boxplot(all_data, labels=labels, showmeans=True,
                    medianprops={
                        'visible': False
                    },
                    meanprops={
                        'marker': 'v',
                        'markersize': 7,
                        'markerfacecolor': 'white',
                        'markeredgecolor': '#0097a7',
                        'markeredgewidth': 2,
                    }
        )
        ax.set_title('Set the meanprops of boxes')

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')

        plt.show() 

if __name__ == '__main__':
    box_format = BoxFormat()
    # box_format.plt_box()
    # box_format.plt_color()
    box_format.plt_props()