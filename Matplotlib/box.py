# https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html
# https://matplotlib.org/stable/gallery/statistics/boxplot_color.html
# https://matplotlib.org/stable/gallery/statistics/boxplot.html


import matplotlib.pyplot as plt
import numpy as np


class BoxFormat:
    def __init__(self) -> None:
        self.plt_style()
    
    def plt_style(self):
        # グラフのフォーマット整形
        plt.rcParams['figure.autolayout'] = True
        plt.rcParams['figure.figsize'] = [6.4, 4.8]
        plt.rcParams['font.family'] ='Times New Roman'
        plt.rcParams['font.size'] = 12
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        plt.rcParams['axes.linewidth'] = 1.0
        plt.rcParams['errorbar.capsize'] = 6
        plt.rcParams['lines.markersize'] = 6
        plt.rcParams['lines.markerfacecolor'] = 'white'
        plt.rcParams['mathtext.fontset'] = 'cm'
        self.line_styles = ['-', '--', '-.', ':']
        self.markers = ['o', 's', '^', 'D', 'v', '<', '>', '1', '2', '3']

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

        # ノッチ付き
        # ax.boxplot(all_data, 1, labels=labels)
        # ax.set_title('notched plot')

        # 外れ値の記号
        # ax.boxplot(all_data, 0, 'gD', labels=labels)
        # ax.set_title('change outlier\npoint symbols')

        # 外れ値の表示有無
        ax.boxplot(all_data, 0, '', labels=labels)
        ax.set_title("don't show\noutlier points")

        # 水平箱ひげ図
        # ax.boxplot(all_data, 0, 'rs', 0, labels=labels)
        # ax.set_title('horizontal boxes')

        # 髭の長さ
        # ax.boxplot(all_data, 0, 'rs', 0, 0.75, labels=labels)
        # ax.set_title('change whisker length')

        # 箱の色
        # bplot = ax.boxplot(all_data, labels=labels, patch_artist=True)
        # colors = ['pink', 'lightblue', 'lightgreen']
        # for patch, color in zip(bplot['boxes'], colors):
        #     patch.set_facecolor(color)
        # ax.set_title('change the color of boxes')

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')

        plt.show()


if __name__ == '__main__':
    box_format = BoxFormat()
    box_format.plt_box()