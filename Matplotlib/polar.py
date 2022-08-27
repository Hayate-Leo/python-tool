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
        plt.rcParams['font.family'] ='Times New Roman'
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        plt.rcParams['font.size'] = 12
        plt.rcParams['axes.linewidth'] = 1.0
        plt.rcParams['errorbar.capsize'] = 6
        plt.rcParams['lines.markersize'] = 7
        plt.rcParams['mathtext.fontset'] = 'dejavuserif'
        self.line_styles = ['-', '--', '-.', ':']
        self.markers = ['o', ',', '.', 'v', '^', '<', '>', '1', '2', '3', '.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3']
    
    def plt_bar(self):
        # 再現性を高めるためのランダムな状態の固定化
        np.random.seed(19680801)

        # パイスライスの計算
        N = 20
        theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
        radii = 10 * np.random.rand(N)
        width = np.pi / 4 * np.random.rand(N)
        colors = plt.cm.viridis(radii / 10.)

        ax = plt.subplot(projection='polar')
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
    
    def plt_legend(self):
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar', 'facecolor': 'lightcyan'})

        r = np.linspace(0, 3, 301)
        theta = 2 * np.pi * r
        ax.plot(theta, r, color="C0", lw=3, label="a line")
        ax.plot(0.5 * theta, r, color="C1", ls=self.line_styles[1], lw=3, label="another line")
        ax.tick_params(grid_color="cyan")
        # スニペットでは、凡例の左下隅を極軸のすぐ外側に、極座標で67.5度の角度で配置
        angle = np.deg2rad(67.5)
        # 凡例と軸の重なりを避けるために、凡例を軸の中心から少し離す
        ax.legend(loc="lower left",
                bbox_to_anchor=(.5 + np.cos(angle)/2, .5 + np.sin(angle)/2))

        plt.show()
    
    def plt_scatter(self):
        np.random.seed(19680801)

        # 面積と色の計算
        N = 150
        r = 2 * np.random.rand(N)
        theta = 2 * np.pi * np.random.rand(N)
        area = 200 * r**2
        colors = theta

        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

        plt.show()


if __name__ == '__main__':
    polar_axis = PolarAxis()
    polar_axis.plt_bar()
    # polar_axis.plt_line()
    # polar_axis.plt_legend()
    # polar_axis.plt_scatter()