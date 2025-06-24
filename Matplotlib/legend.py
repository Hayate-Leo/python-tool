import matplotlib.pyplot as plt
import numpy as np

class LegendFormat():
    def __init__(self) -> None:
        pass

    def plt_legend(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)

        # step2 グラフフレームの作成
        # fig, ax = plt.subplots(figsize=(6, 4))
        fig, axs = plt.subplots(2, 2, figsize=(8, 4))

        # step3 グラフの描画
        # ax.plot(x, y1, label='Sample 1')
        # ax.plot(x, y2, label='Sample 2')

        axs[0, 0].plot(x, y1, label='Axes 1', color='C0')
        axs[0, 1].plot(x, y2, label='Axes 2', color='C1')
        axs[1, 0].plot(x, y2, label='Axes 3', color='C2')
        axs[1, 1].plot(x, y2, label='Axes 4', color='C3')

        # step4 凡例の設定
        # ax.legend()
        # ラベルの再設定
        # ax.legend(labels=['Sample 4', 'Sample 5'])
        fig.legend()

        # step5 タイトルと軸ラベルの設定
        # ax.set_title('Default Legend')
        # ax.set_xlabel('X Label')
        # ax.set_ylabel('Y Label')
        fig.suptitle('Default Legend with pyplot.legend')
        fig.supxlabel('X Label')
        fig.supylabel('Y Label')

        # step6 Figureの呼び出し
        plt.show()

    def plt_legend_handles(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)

        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=(6, 4))

        # step3 グラフの描画
        line1, = ax.plot(x, y1, label='Axes 1')
        line2, = ax.plot(x, y2, label='Axes 2')

        # step4 凡例の設定
        ax.legend(handles=[line1])

        # step5 タイトルと軸ラベルの設定
        ax.set_title('handles')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')

        # step6 Figureの呼び出し
        plt.show()

    def plt_legend_loc(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)

        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=(6, 4))

        # step3 グラフの描画
        ax.plot(x, y1, label='Sample 1')
        ax.plot(x, y2, label='Sample 2')

        # step4 凡例の設定
        locs = ['lower right', 'center', 'upper left']
        ax.legend(loc=locs[0])

        # step5 タイトルと軸ラベルの設定
        ax.set_title('loc = ' + locs[0])
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')

        # step6 Figureの呼び出し
        plt.show()

    def plt_legend_bbox(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)

        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=(6, 4))

        # step3 グラフの描画
        ax.plot(x, y1, label='Sample 1')
        ax.plot(x, y2, label='Sample 2')

        # step4 凡例の設定
        # ax.legend(bbox_to_anchor=(0, 0))
        # ax.legend(bbox_to_anchor=(1, 1))
        ax.legend(bbox_to_anchor=(1, 1, 1, 0))

        # step5 タイトルと軸ラベルの設定
        ax.set_title('Bbox = (1, 1)')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')

        # step6 Figureの呼び出し
        plt.tight_layout()
        plt.show()

    def plt_legend_locbbox(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)

        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=(6, 4))

        # step3 グラフの描画
        ax.plot(x, y1, label='Sample 1')
        ax.plot(x, y2, label='Sample 2')

        # step4 凡例の設定
        ax.legend(loc='center', bbox_to_anchor=(1, 1))
        # ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1))
        # ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1))

        # step5 タイトルと軸ラベルの設定
        ax.set_title('loc = center & Bbox = (1, 1)')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')

        # step6 Figureの呼び出し
        plt.tight_layout()
        plt.show()

    def plt_legend_custom(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)

        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=(6, 4))

        # step3 グラフの描画
        ax.plot(x, y1, label='Sample 1')
        ax.plot(x, y2, label='Sample 2')

        # step4 凡例の設定
        # Font
        # ax.legend(prop={'weight': 'bold', 'style': 'italic', 'family': 'Times New Roman'})
        # ax.legend(fontsize='large')
        # ax.legend(fontsize=20)
        # ax.legend(labelcolor='red')
        # Color
        # ax.legend(edgecolor='#00BCD4')
        # ax.legend(facecolor='0.8')
        # title
        # ax.legend(title='Legend Title')
        # ax.legend(
        #     title='Legend Title', 
        #     title_fontproperties={'weight': '500', 'style': 'oblique', 'size': 'x-large'},
        # )
        # ax.legend(
        #     title='Legend Title', 
        #     title_fontsize='12',
        # )
        # frame
        # ax.legend(frameon=False)
        # ax.legend(fancybox=False)
        # ax.legend(shadow=True)
        # ax.legend(framealpha=1)

        # step5 タイトルと軸ラベルの設定
        ax.set_title('Legend labelspacing=1.1')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')

        # step6 Figureの呼び出し
        plt.show()

if __name__ == '__main__':
    legend_format  = LegendFormat()
    # legend_format.plt_legend()
    # legend_format.plt_legend_handles()
    # legend_format.plt_legend_loc()
    # legend_format.plt_legend_bbox()
    # legend_format.plt_legend_locbbox()
    legend_format.plt_legend_custom()
