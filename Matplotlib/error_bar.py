# https://matplotlib.org/stable/plot_types/stats/errorbar_plot.html#sphx-glr-plot-types-stats-errorbar-plot-py
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/errorbar_limits_simple.html#sphx-glr-gallery-lines-bars-and-markers-errorbar-limits-simple-py

import matplotlib.pyplot as plt
import numpy as np
from thesis_format import ThesisFormat


class ErrorBar(ThesisFormat):
    def __init__(self) -> None:
        super().__init__()
    
    def plt_simple(self):
        # step1 データの作成
        x = np.arange(5)
        y = [4.6, 3.6, 5, 4.2, 2.7]
        yerr = [0.6, 0.9, 1.2, 0.5, 0.7]

        # step2 グラフフレームの作成
        fig, ax = plt.subplots()

        # step3 エラーバー付き折れ線グラフ
        # ax.errorbar(x, y, yerr)
        ax.errorbar(x, y, xerr=0.2, yerr=0.4)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.legend()
        # ax.set_title('Simple errorbar')
        ax.set_title('xrr & yerr in errorbar')

        plt.show()
    
    def plt_fmt(self):
        # step1 データの作成
        x = np.arange(5)
        y = [4.6, 3.6, 5, 4.2, 2.7]

        # step2 グラフフレームの作成
        fig, ax = plt.subplots()

        # step3 エラーバー付き折れ線グラフ
        # 円形＋緑色＋破線
        ax.errorbar(x, y, yerr=0.4, fmt='og' ,label='fmt="og"')
        # 四角形＋赤色＋一点鎖線
        ax.errorbar(x, [i+2 for i in y], yerr=0.4, fmt='sr-.' ,label='fmt="sr-."')
        # 星形＋シアン＋点線
        ax.errorbar(x,  [i+4 for i in y], yerr=0.4, fmt='*c:' ,label='fmt="*c:"')

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.legend()
        ax.set_title('fmt in errorbar')

        plt.show()
    
    def plt_ecolor_eline(self):
        # step1 データの作成
        x = np.arange(5)
        y = [4.6, 3.6, 5, 4.2, 2.7]

        # step2 グラフフレームの作成
        fig, ax = plt.subplots()

        # step3 エラーバー付き折れ線グラフ
        # ax.errorbar(x, y, yerr=0.4, fmt='o-', ecolor='red')
        # ax.errorbar(x, y, yerr=0.4, fmt='o-', elinewidth=0.5)
        ax.errorbar(x, y, yerr=0.4, fmt='o-', ecolor='gray', barsabove=True)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('errorbar')

        plt.show()

    def plt_cap(self):
        # step1 データの作成
        x = np.arange(5)
        y = [4.6, 3.6, 5, 4.2, 2.7]

        # step2 グラフフレームの作成
        fig, ax = plt.subplots()

        # step3 エラーバー付き折れ線グラフ
        # ax.errorbar(x, y, yerr=0.4, fmt='o-', ecolor='red', capsize=0)
        # ax.errorbar(x, y, yerr=0.4, fmt='o-', ecolor='red', capthick=5)
        ax.errorbar(x, y, yerr=0.4, fmt='o-', ecolor='red', errorevery=2)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('cap in errorbar')

        plt.show()
    
    def plt_limit(self):
        # step1 データの作成
        x = np.arange(5)
        y = [4.6, 3.6, 5, 4.2, 2.7]

        # step2 グラフフレームの作成
        fig, ax = plt.subplots()

        # step3 エラーバー付き折れ線グラフ
        # 上限と下限
        ax.errorbar(x, y, yerr=0.4, fmt='o-', uplims=True, label='uplims')
        ax.errorbar(x, [i+2 for i in y], yerr=0.4, fmt='o-', lolims=True, label='lolims')
        # ax.errorbar(x, y, xerr=0.2, fmt='o-', xuplims=True, label='xuplims')
        # ax.errorbar(x, [i+2 for i in y], xerr=0.2, fmt='o-', xlolims=True, label='xlolims')

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.legend()
        ax.set_title('limit in errorbar')

        plt.show()

if __name__ == '__main__':
    error_bar = ErrorBar()
    # error_bar.plt_simple()
    # error_bar.plt_fmt()
    # error_bar.plt_ecolor_eline()
    # error_bar.plt_cap()
    error_bar.plt_limit()