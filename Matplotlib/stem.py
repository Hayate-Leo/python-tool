# https://matplotlib.org/stable/gallery/lines_bars_and_markers/stem_plot.html#sphx-glr-gallery-lines-bars-and-markers-stem-plot-py
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html
# https://matplotlib.org/stable/gallery/mplot3d/stem3d_demo.html#sphx-glr-gallery-mplot3d-stem3d-demo-py


import matplotlib.pyplot as plt
import numpy as np

class StemFormat:
    def __init__(self) -> None:
        pass
    
    def plt_stem(self):
        # step1 データの作成
        x = np.linspace(0.1, 2 * np.pi, 41)
        y = np.exp(np.sin(x))
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 ステムプロットの描画
        ax.stem(x, y)
        # step4 軸ラベルとリミット，タイトルの設定
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_xlim(0, 6)
        ax.set_title('Stem demo')
        # step5 Figureの呼び出し
        plt.show()
    
    def plt_stem_fmt(self):
        # step1 データの作成
        x = np.linspace(0.1, 2 * np.pi, 41)
        y = np.exp(np.sin(x))
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 ステムプロットの描画
        # ax.stem(x, y, linefmt='g:')
        # ax.stem(x, y, markerfmt='r*')
        ax.stem(x, y, basefmt='m-.D')
        # step4 軸ラベルとタイトルの設定
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        # ax.set_title('Stem LineFmt "g:"')
        # ax.set_title('Stem MarkerFmt "r*"')
        ax.set_title('Stem BaseFmt "m-.D"')
        # step5 Figureの呼び出し
        plt.show()

    
    def plt_orient(self):
        # step1 データの作成
        x = np.linspace(0.1, 2 * np.pi, 41)
        y = np.exp(np.sin(x))
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 ステムプロットの描画
        # ax.stem(x, y, orientation='horizontal', label='hrizontal')
        ax.stem(x, y, bottom=1, label='bottom=1')
        # step4 軸ラベルとタイトルの設定
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_title('Stem bottom')
        ax.legend()
        # step5 Figureの呼び出し
        plt.show()


if __name__ == '__main__':
    stem_format = StemFormat()
    # stem_format.plt_stem()
    # stem_format.plt_stem_fmt()
    stem_format.plt_orient()
    # stem_format.plt_bottom_label()
