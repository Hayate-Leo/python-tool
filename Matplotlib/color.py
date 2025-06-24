import matplotlib.pyplot as plt
import numpy as np

class ColorFormat():
    def __init__(self) -> None:
        pass

    def plot_color(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)

        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=(6, 4))

        # step3 グラフの描画
        ax.plot(x, y1, label='Sample1')
        ax.plot(x, y2, label='Sample2')
        # tuple
        # ax.plot(x, y1, label='color=(0.2, 0.7, 0.7)', color=(0.2, 0.7, 0.7))
        # ax.plot(x, y2, label='color=(0.1, 0.2, 0.5, 0.3)', color=(0.1, 0.2, 0.5, 0.3))
        # 16進数
        # ax.plot(x, y1, label='#00BCD4', color='#00BCD4')
        # ax.plot(x, y2, label='#4CAF5070', color='#4CAF5070')
        # 省略した16進数
        # ax.plot(x, y1, label='#1BB', color='#1BB')
        # ax.plot(x, y2, label='#D2C6', color='#D2C6')
        # グレースケール
        # ax.plot(x, y1, label='Black=0', color='0')
        # ax.plot(x, y2, label='Gray=0.6', color='0.6')
        # ベースカラー
        # ax.plot(x, y1, label='b', color='b')
        # ax.plot(x, y2, label='r', color='r')
        # Tableau カラーパレット
        # ax.plot(x, y1, label='tab:blue', color='tab:blue')
        # ax.plot(x, y2, label='tab:orange', color='tab:orange')
        # CSSカラー
        # ax.plot(x, y1, label='olive', color='olive')
        # ax.plot(x, y2, label='mediumseagreen', color='mediumseagreen')
        # xkcdカラー
        # ax.plot(x, y1, label='xkcd:pink', color='xkcd:pink')
        # ax.plot(x, y2, label='xkcd:teal', color='xkcd:teal')
        # CNカラー
        # ax.plot(x, y1, label='C0', color='C0')
        # ax.plot(x, y2, label='C1', color='C1')

        # step4 タイトルと軸ラベルの設定
        ax.set_title('Default color')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.legend()

        # step5 Figureの呼び出し
        plt.show()

if __name__ == '__main__':
    color_style = ColorFormat()
    color_style.plot_color()