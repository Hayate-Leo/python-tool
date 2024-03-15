# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html

import matplotlib.pyplot as plt
import numpy as np
from thesis_format import ThesisFormat


class PlotFormat(ThesisFormat):
    def __init__(self) -> None:
        # super().__init__()
        pass

    def plt_line(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 グラフの描画
        ax.plot(x, y1, label='Sample 1')
        ax.plot(x, y2, linestyle='--', label='Sample 2')
        # step4 軸，凡例，タイトルの設定
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.legend()

        ax.set_title('Simple line')
        # step5 Figureの呼び出し
        plt.show()
    
    def plt_scatter(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()

        # step3 グラフの描画
        ax.plot(x, y1, 'o',label='Sample 1')
        ax.plot(x, y2, 'or--', label='Sample 2')
        # step4 軸，凡例，タイトルの設定
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.legend()

        ax.set_title('Simple scatter')
        # step5 Figureの呼び出し
        plt.show()
    
    def plt_custom_line(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()

        # step3 グラフの描画
        # ax.plot(x, y1, label='red', color='red')
        # ax.plot(x, y2, label='#00BCD4', color='#00BCD4')
        # ax.plot(x, y1, label='dashed', linestyle='-.')
        # ax.plot(x, y2, label='dotted', linestyle=':')
        ax.plot(x, y1, label='linewidth=5', linewidth=5)
        ax.plot(x, y2, label='lw=5, alpha=0.5', linewidth=5, alpha=0.5)
        # step4 軸，凡例，タイトルの設定
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.legend()

        ax.set_title('Custom line width')
        # step5 Figureの呼び出し
        plt.show()
    
    def plt_custom_markerstyle(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()

        # step3 グラフの描画
        # markerで指定
        ax.plot(x, y1, marker='o', label='marker=o', markerfacecolor='white')
        ax.plot(x, y2, marker='s', label='marker=s', markerfacecolor='white')
        ax.plot(x, y2-2, marker='^', label='marker=^', markerfacecolor='white')
        # fmtで指定
        # ax.plot(x, y1, 'o', label='fmt=o')
        # ax.plot(x, y2, 's', label='fmt=s')
        # ax.plot(x, y2-2, '^', label='fmt=^')     
        # step4 軸，凡例，タイトルの設定
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.legend()

        # ax.set_title('custom markerstyle')
        ax.set_title('Plot graph for a thesis')
        # step5 Figureの呼び出し
        plt.show()

    def plt_custom_markercolor(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()

        # step3 グラフの描画
        # markerで指定
        # ax.plot(x, y1, marker='o', label='face=white', markerfacecolor='white')
        # ax.plot(x, y2, marker='s', label='face=black', markerfacecolor='black')
        # ax.plot(x, y1, marker='o', label='edgecolor=red', 
        #         markeredgecolor='red')
        # ax.plot(x, y2, marker='s', label='edgewidth=3', 
        #         markeredgecolor='red', markeredgewidth=3)
        ax.plot(x, y1, marker='o', label='fill=top', fillstyle='top')
        ax.plot(x, y2, marker='s', label='fill=bottom', fillstyle='bottom')
        # step4 軸，凡例，タイトルの設定
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.legend()

        ax.set_title('custom fillstyle')
        # step5 Figureの呼び出し
        plt.show()

if __name__ == '__main__':
    plot_format = PlotFormat()
    # plot_format.plt_line()
    # plot_format.plt_scatter()
    # plot_format.plt_custom_line()
    plot_format.plt_custom_markerstyle()
    # plot_format.plt_custom_markercolor()