# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html

import matplotlib.pyplot as plt
import numpy as np
from thesis_format import ThesisFormat

class ScatterFormat(ThesisFormat):
    def __init__(self) -> None:
        super().__init__()
    
    def plt_simple(self):
        # step1 発生する乱数の固定化
        np.random.seed(19680801)
        # step2 データの作成
        x = np.random.randn(100)
        y1 = np.random.randn(100)
        y2 = np.random.randn(100)
        # step3 グラフフレームの作成
        fig, ax = plt.subplots()
        # step4 散布図の描画
        ax.scatter(x, y1, alpha=0.5, label='Sample1')
        ax.scatter(x, y2, alpha=0.5, label='Sample2', marker=self.markers[1])

        ax.set_ylabel('Y label')
        ax.set_xlabel('X label')
        ax.legend()
        ax.set_title('Simple scatter')

        plt.show()
    
    def plt_marker_s(self):
        np.random.seed(19680801)

        x = np.random.randn(100)
        y = np.random.randn(100)

        fig, ax = plt.subplots()
        # step4 散布図の描画
        ax.scatter(x, y, marker='*')
        # ax.scatter(x, y, s=100)
        ax.scatter(x, y, s=y*100)

        titles = ['marker="*"', 'markersize=100', 'markersize=100×y']

        ax.set_title(titles[2])
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        plt.show()

    def plt_color(self):
        np.random.seed(19680801)

        x = np.random.randn(100)
        y = np.random.randn(100)

        fig, ax = plt.subplots()
        # step4 散布図の描画
        # ax.scatter(x, y, c='C1')
        # ax.scatter(x, y, alpha=0.5)
        # ax.scatter(x, y, edgecolor='red')
        ax.scatter(x, y, edgecolor='red', linewidth=3)

        titles = ['color=C1', 'alpha=0.5', 'edgecolor=red', 'linewidth=3']

        ax.set_title(titles[3])
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        plt.show()
    
    def plt_cmap(self):
        np.random.seed(19680801)

        x = np.random.randn(100)
        y = np.random.randn(100)
        z = np.random.randn(100)

        fig, ax = plt.subplots()

        cmaps = ['viridis', 'Greys', 'winter', 'bwr']
        # step4 散布図の描画
        CS = ax.scatter(x, y, s=z*100, c=z, cmap='viridis', vmax=1, vmin=0)
        fig.colorbar(CS, ax=ax)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('viridis & vmax=1 vmin=0 with colorbar')

        plt.show()

    def plt_3d(self):
        # step1 発生する乱数の固定化
        np.random.seed(19680801)
        # step2 データの作成
        x = np.random.randn(100)
        y = np.random.randn(100)
        z = np.random.randn(100)
        # step3 グラフフレームの作成
        fig, ax = plt.subplots(subplot_kw={'projection':'3d'})
        # step4 散布図の描画
        CS = ax.scatter(x, y, z, s=z*100, c=z)
        # カラーバーの作成
        fig.colorbar(CS, ax=ax)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('3dimension in scatter')

        plt.show()

if __name__ == '__main__':
    scatter_format = ScatterFormat()
    # scatter_format.plt_simple()
    # scatter_format.plt_marker_s()
    # scatter_format.plt_color()
    scatter_format.plt_cmap()
    # scatter_format.plt_3d()