# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_zoom_effect.html#sphx-glr-gallery-subplots-axes-and-figures-axes-zoom-effect-py
# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/zoom_inset_axes.html#sphx-glr-gallery-subplots-axes-and-figures-zoom-inset-axes-py

import matplotlib.pyplot as plt
import numpy as np

# from matplotlib.transforms import (
#     Bbox, TransformedBbox, blended_transform_factory)
# from mpl_toolkits.axes_grid1.inset_locator import (
#     BboxPatch, BboxConnector, BboxConnectorPatch)


class PlotZoom:
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

    def plt_in_zoom(self):
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)

        fig, ax = plt.subplots()

        ax.plot(x, y1, linestyle=self.line_styles[0], label='Sample 1')
        ax.plot(x, y2, linestyle=self.line_styles[1], label='Sample 2')
        
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_xlabel('Time [sec]')
        ax.set_ylabel('Frequency [Hz]')
        ax.legend(loc='upper left')

        # zoomしたグラフの描画
        axins = ax.inset_axes([0.6, 0.6, 0.37, 0.37])
        axins.plot(x, y1, linestyle=self.line_styles[0], label='Sample 1')
        axins.plot(x, y2, linestyle=self.line_styles[1], label='Sample 2')

        # zoomしたグラフの設定
        x1, x2, y1, y2 = 2, 4, 4, 6
        axins.set_xlim(x1, x2)
        axins.set_ylim(y1, y2)
        axins.set_xticklabels([])
        axins.set_yticklabels([])

        ax.indicate_inset_zoom(axins)


        plt.show()
    


if __name__ == '__main__':
    plot_zoom = PlotZoom()
    plot_zoom.plt_in_zoom()