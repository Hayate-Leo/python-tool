import matplotlib.pyplot as plt
import numpy as np


class SetAxis:
    def __init__(self) -> None:
        pass

    def plt_label(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=(6, 4))
        # step3 グラフの描画
        ax.plot(x, y1, 'o--')
        ax.plot(x, y2, 'D--')
        # step4 軸の設定
        # 軸ラベル設定
        # ax.set_xlabel('X Label', labelpad=-10)
        # ax.set_ylabel('Y Labelpad=20', labelpad=20)
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        # ax.set_xlabel('X Label', fontfamily='Times New Roman', fontstyle='italic')
        # ax.set_ylabel('Y Label', fontweight='bold', fontsize=16, color='red')
        fig.supxlabel('Fig X label')
        fig.supylabel('Fig Y label')

        # ax.set_xlim(0, 8)
        # ax.set_ylim(0, 8)
        ax.set_title('Axis Label Text')

        # step5 Figureの呼び出し
        plt.show()

    def plt_limit(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=(6, 4))
        # step3 グラフの描画
        ax.plot(x, y1, 'o--')
        ax.plot(x, y2, 'D--')
        # step4 軸の設定
        # 軸ラベル
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')     
        # 軸リミット
        ax.set_xlim(8, 0)
        ax.set_ylim(0, 8)
        ax.set_title('Invert Axis Limit')

        # step5 Figureの呼び出し
        plt.show()
    
    def plt_log(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = np.exp(1.2*x) + np.sin(2*x)
        y2 = np.exp(x) + 2*np.cos(x)

        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=(6, 4), constrained_layout=True)

        # step3 グラフの描画
        ax.plot(x, y1)
        ax.plot(x, y2)

        # step4 軸ラベル，タイトルの設定
        ax.set_xlabel('log')
        ax.set_ylabel('log')
        ax.set_title('Axis Scale')

        # step5 スケールの設定
        # ax.set_xscale('linear')
        # ax.set_yscale('linear')
        ax.set_xscale('log')
        ax.set_yscale('log')

        # step6 グラフの呼び出し
        plt.show()

    def plt_ticks(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=(6, 4))
        # step3 グラフの描画
        ax.plot(x, y1, 'o--')
        ax.plot(x, y2, 'D--')
        # step4 軸の設定
        # 軸ラベル
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        # 軸リミット
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        # 目盛り
        # ax.set_xticks(
        #     [0, 1, 2, 3, 4, 5, 6, 7, 8], 
        #     labels=['a', 'b', 'c', 'e', 'f', 'g','h', 'i', 'j']
        # )
        ax.set_xticks([2.5, 3.5, 4.5, 5.5, 6.5])
        ax.set_yticks([0, 4, 8])
        ax.set_title('Axis Ticks minor=False')

        # step5 Figureの呼び出し
        plt.show()

    def plt_tick_params(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=(6, 4))
        # step3 グラフの描画
        ax.plot(x, y1, 'o--')
        ax.plot(x, y2, 'D--')
        # step4 軸の設定
        # 軸ラベル
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        # 軸リミット
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        # 目盛り
        # x軸，目盛りの色と向き，幅
        ax.tick_params('x', color='red', direction='in', width=5)
        # y軸，ラベルの色とサイズ
        ax.tick_params('y', labelcolor='red', labelsize=16)
        ax.set_title('Axis Tick Params')

        # step5 Figureの呼び出し
        plt.show()

    def plt_tick_del(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=(6, 4))
        # step3 グラフの描画
        ax.plot(x, y1, 'o--')
        ax.plot(x, y2, 'D--')
        # step4 軸の設定
        # y軸目盛りの削除
        # ax.yaxis.set_visible(False)
        # 枠の削除
        ax.spines[['top', 'right', 'left']].set_visible(False)
        # 軸すべての削除
        # ax.set_axis_off()
        ax.set_title('Axis Spines Off')

        # step5 Figureの呼び出し
        plt.show()

    def plt_tick_add(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=(6, 4))
        # step3 y軸の作成
        twin1 = ax.twinx()
        # step4 グラフの描画
        ax.plot(x, y1, color='C0')
        twin1.plot(x, y2, color='C1')
        # step4 軸の設定
        # 軸ラベル
        ax.set_xlabel('X label')
        ax.set_ylabel('Y1')
        twin1.set_ylabel('Y2')
        # 軸の色
        ax.tick_params(axis='y', colors='C0')
        twin1.tick_params(axis='y', colors='C1')

        ax.set_title('Twin Axis Ticks')
        # step5 Figureの呼び出し
        plt.show()

if __name__ == '__main__':
    set_axis = SetAxis()
    # set_axis.plt_label()
    # set_axis.plt_limit()
    # set_axis.plt_log()
    # set_axis.plt_ticks()
    # set_axis.plt_tick_params()
    set_axis.plt_tick_del()
    # set_axis.plt_tick_add()
