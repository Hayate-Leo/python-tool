# https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_bar.html
# https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_demo.html
# https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_scatter.html
# https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_legend.html

import matplotlib.pyplot as plt
import numpy as np


class PolarAxis:
    def __init__(self) -> None:
        self.plt_style()
    
    def plt_style(self):
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
    
    def plt_bar(self):
        # step1 再現性を高めるための乱数の固定化
        np.random.seed(19680801)

        # step2 パイスライスの計算
        N = 20
        theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
        radii = 10 * np.random.rand(N)
        width = np.pi / 4 * np.random.rand(N)
        # 要素の大きさによって色を変化
        # colors = plt.cm.viridis(radii / 10.)
        # 要素の角度（位置）によって色を変化
        colors = plt.cm.hsv(theta / (2 * np.pi))

        # step3 グラフフレームの作成
        ax = plt.subplot(projection='polar')

        # step4 棒グラフの描画
        ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)

        plt.show()
    
    def plt_line(self):
        r = np.arange(0, 2, 0.01)
        theta = 2 * np.pi * r

        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        ax.plot(theta, r)
        ax.set_rmax(2)
        ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
        ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
        ax.grid(True)

        ax.set_title("A line plot on a polar axis", va='bottom')
        plt.show()
    
    def plt_line_legend(self):
        # step1 データの作成
        r = np.arange(0, 2, 0.01)
        theta = 2 * np.pi * r

        # step2 グラフフレームの作成
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

        # step3 折れ線グラフの描画
        ax.plot(theta, r, label='Sample 1')
        ax.plot(0.5 * theta, r, ls='--', label='Sample 2')

        # step4 極座標軸の凡例の設定
        # スニペットでは、凡例の左下隅を極軸のすぐ外側に、極座標で67.5度の角度で配置
        angle = np.deg2rad(67.5)
        # 凡例と軸の重なりを避けるために、凡例を軸の中心から少し離す
        ax.legend(loc="lower left",
                bbox_to_anchor=(.5 + np.cos(angle)/2, .5 + np.sin(angle)/2))

        ax.set_title("Line plots with a legend on a polar axis", va='bottom', pad=50)

        plt.tight_layout()
        plt.show()
    
    def plt_scatter(self):
        # step1 発生する乱数の固定化
        np.random.seed(19680801)

        # step2 面積と色の計算
        N = 150
        r = 2 * np.random.rand(N)
        theta = 2 * np.pi * np.random.rand(N)
        area = 200 * r**2
        colors = theta

        # step3 散布図の描画
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

        plt.show()

    def plt_scatter_colorbar(self):
        # step1 発生する乱数の固定化
        np.random.seed(19680801)

        # step2 面積と色の計算
        N = 150
        r = 2 * np.random.rand(N)
        theta = 2 * np.pi * np.random.rand(N)
        area = 200 * r**2
        colors = area

        # step3 散布図の描画
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        SC = ax.scatter(theta, r, c=colors, s=area, cmap='viridis', alpha=0.75)

        # step4 カラーバーの設定
        cbar = fig.colorbar(SC, aspect=10)
        cbar.ax.set_ylabel('Z Label')

        plt.show()


if __name__ == '__main__':
    polar_axis = PolarAxis()
    # polar_axis.plt_bar()
    # polar_axis.plt_line()
    polar_axis.plt_line_legend()
    # polar_axis.plt_scatter()
    # polar_axis.plt_scatter_colorbar()