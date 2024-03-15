# step0 ライブラリのインストール
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl


class QuickStartGuide:
    def __init__(self) -> None:
        pass

    def simple_example(self):

        # Create a figure containing a single axes.
        # 1つのaxesを含むfigureを作成
        fig, ax = plt.subplots() 
        # Plot some data on the axes.
        # axesにデータを描画
        ax.plot([1, 2, 3, 4, 5], [1, 4, 2, 5, 7]) 
        plt.show()

    def oo_style(self):
        # step1 データの作成
        x = np.arange(8)
        apples = [5, 12, 8, 15, 20, 10, 18, 7]
        oranges = [3, 14, 9, 17, 22, 11, 16, 6]
        grapes = [8, 18, 12, 20, 25, 15, 23, 9]
        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=(6, 4))
        # step3 グラフの描画
        # 1 Axes.plotで呼び出したとき
        ax.plot(x, apples, label='apples', color='red', linewidth=3, linestyle='--')
        # 2 Artistの"setter"で後から追加
        o, = ax.plot(x, oranges, label='oranges', color='#F44336')
        o.set_linewidth(2)
        o.set_linestyle('-.')
        # step4 軸ラベル，タイトル，凡例の設定
        ax.set_xlabel('X label') # Xラベル
        ax.set_ylabel('Y label') # Yラベル
        # ax.set_title('Figure+Axes OO-style')  # タイトル
        ax.set_title('Figure+Axes styling')  # タイトル
        ax.legend()  # 凡例
        # step5 グラフの呼び出し
        plt.show()

    def pyplot_style(self):
        # step1 データの作成
        x = np.arange(8)
        apples = [5, 12, 8, 15, 20, 10, 18, 7]
        oranges = [3, 14, 9, 17, 22, 11, 16, 6]
        grapes = [8, 18, 12, 20, 25, 15, 23, 9]
        # step2 グラフフレームの作成
        plt.figure(figsize=(6, 4))
        # step3 グラフの描画
        plt.plot(x, apples, label='apples')
        plt.plot(x, oranges, label='oranges')
        plt.plot(x, grapes, label='grapes')
        # step4 軸ラベル，タイトル，凡例の設定
        plt.xlabel('X label') # Xラベル
        plt.ylabel('Y label') # Yラベル
        plt.title('Only Figure pyplot-style')  # タイトル
        plt.legend()  # 凡例
        # step5 グラフの呼び出し
        plt.show()

    def multi_axs(self):
        # step1 データの作成
        x = np.arange(8)
        apples = [5, 12, 8, 15, 20, 10, 18, 7]
        oranges = [3, 14, 9, 17, 22, 11, 16, 6]
        grapes = [8, 18, 12, 20, 25, 15, 23, 9]
        # step2 グラフフレームの作成
        fig, axs = plt.subplots(2, 1, figsize=(6, 4))
        # step3 グラフの描画
        axs[0].plot(x, apples, label='apples', color='r')
        axs[1].plot(x, oranges, label='oranges', color='C1')
        # step4 軸ラベル，タイトル，凡例の設定
        axs[0].set_xlabel('X label') # Xラベル
        axs[0].set_ylabel('Y label') # Yラベル
        axs[0].legend()  # 凡例
        fig.suptitle('Multiple Figures and Axes') 
        # step5 グラフの呼び出し
        plt.show()

    def set_axis(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = np.exp(x) + 2 * np.sin(2 * x)
        y2 = np.exp(x) + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, axs = plt.subplots(1, 2, sharex=True)
        # step3 グラフの描画
        for ax in axs.flat:
            ax.plot(x, y1, label='Sample 1')
            ax.plot(x, y2, label='Sample 2')
            ax.legend()

        # step4 軸ラベル，タイトルの設定
        axs[0].set_title('linear')
        axs[1].set_title('log')

        fig.suptitle('scale')
        fig.supxlabel('X label')
        fig.supylabel('Y label')

        # step5 対数スケールと目盛り，刻み幅の設定
        axs[0].set_xlim(0, 10)
        axs[0].set_ylim(0)
        axs[0].set_yticks([0, 6000, 12000, 18000, 24000])
        axs[1].set_yscale('log')

        # step6 グラフの呼び出し
        plt.show()


if __name__ == '__main__':
    start_guide = QuickStartGuide()
    # start_guide.simple_example()
    # start_guide.oo_style()
    # start_guide.pyplot_style()
    # start_guide.multi_axs()
    start_guide.set_axis()