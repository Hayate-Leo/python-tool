# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_zoom_effect.html#sphx-glr-gallery-subplots-axes-and-figures-axes-zoom-effect-py
# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/zoom_inset_axes.html#sphx-glr-gallery-subplots-axes-and-figures-zoom-inset-axes-py

import matplotlib.pyplot as plt
import numpy as np


class PlotZoom:
    def __init__(self) -> None:
        self.plt_style()
    
    def plt_style(self):      
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

    def plt_in_zoom(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=[6.4, 4.8])
        # step3 折れ線グラフの描画
        ax.plot(x, y1, linestyle='-', label='Sample 1')
        ax.plot(x, y2, linestyle='--', label='Sample 2')

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.legend(loc='upper left')

        # step4 zoomしたグラフの描画
        axins = ax.inset_axes([0.6, 0.6, 0.37, 0.37])
        axins.plot(x, y1, linestyle='-', label='Sample 1')
        axins.plot(x, y2, linestyle='--', label='Sample 2')

        # step4 zoomしたグラフの設定
        x1, x2, y1, y2 = 2, 4, 4, 6
        axins.set_xlim(x1, x2)
        axins.set_ylim(y1, y2)
        ax.indicate_inset_zoom(axins)

        plt.show()

    def plt_upper(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=[6.4, 6.4])
        # step3 折れ線グラフの描画
        ax.plot(x, y1, linestyle='-', label='Sample 1')
        ax.plot(x, y2, linestyle='--', label='Sample 2')

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.legend(loc='upper left')

        # step4 zoomしたグラフの描画
        axins = ax.inset_axes([0.58, 1.08, 0.42, 0.37])
        axins.plot(x, y1, linestyle='-', label='Sample 1')
        axins.plot(x, y2, linestyle='--', label='Sample 2')

        # step4 zoomしたグラフの設定
        x1, x2, y1, y2 = 2, 4, 4, 6
        axins.set_xlim(x1, x2)
        axins.set_ylim(y1, y2)
        ax.indicate_inset_zoom(axins)
        # アスペクト比の調整
        ax.set_box_aspect(0.75)
        # subplotの位置調整
        fig.subplots_adjust(bottom=0.11, top=0.7)

        plt.show()
    
    def plt_right(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots(figsize=[7, 4.8])
        # step3 折れ線グラフの描画
        ax.plot(x, y1, linestyle='-', label='Sample 1')
        ax.plot(x, y2, linestyle='--', label='Sample 2')

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.legend(loc='upper left')

        # step4 zoomしたグラフの描画
        axins = ax.inset_axes([1.05, 0.63, 0.42, 0.37])
        axins.plot(x, y1, linestyle='-', label='Sample 1')
        axins.plot(x, y2, linestyle='--', label='Sample 2')

        # step4 zoomしたグラフの設定
        x1, x2, y1, y2 = 2, 4, 4, 6
        axins.set_xlim(x1, x2)
        axins.set_ylim(y1, y2)
        ax.indicate_inset_zoom(axins)
        # アスペクト比の調整
        ax.set_box_aspect(0.75)
        # subplotの位置調整
        fig.subplots_adjust(left=0.11, right=0.7)

        plt.show()
    

if __name__ == '__main__':
    plot_zoom = PlotZoom()
    # plot_zoom.plt_in_zoom()
    # plot_zoom.plt_upper()
    plot_zoom.plt_right()