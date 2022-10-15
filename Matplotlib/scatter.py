# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html

import matplotlib.pyplot as plt
import numpy as np


class ScatterFormat:
    def __init__(self) -> None:
        self.plt_style()
    
    def plt_style(self):
        plt.rcParams['font.family'] ='Times New Roman'
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        plt.rcParams['font.size'] = 12
        plt.rcParams['axes.linewidth'] = 1.0
        plt.rcParams['errorbar.capsize'] = 6
        plt.rcParams['lines.markersize'] = 6
        plt.rcParams['lines.markerfacecolor'] = 'white'
        plt.rcParams['mathtext.fontset'] = 'cm'
        self.line_styles = ['-', '--', '-.', ':']
        self.markers = ['o', ',', '.', 'v', '^', '<', '>', '1', '2', '3']
    
    def plt_simple(self):
        np.random.seed(19680801)

        x = np.random.randn(100)
        y1 = np.random.randn(100)
        y2 = np.random.randn(100)

        fig, ax = plt.subplots()

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

        fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)

        axs[0, 0].scatter(x, y)
        axs[0, 1].scatter(x, y, marker='*')
        axs[1, 0].scatter(x, y, s=100)
        axs[1, 1].scatter(x, y, s=y*100)

        titles = ['default', 'marker="*"', 'markersize=100', 'markersize=100×y']

        for ax, title in zip(axs.flat, titles):
            ax.set_title(title)
        
        axs[0, 0].set_ylabel('Y label')
        axs[1, 0].set_ylabel('Y label')
        axs[1, 0].set_xlabel('X label')
        axs[1, 1].set_xlabel('X label')

        fig.suptitle('marker & markersize in scatter')

        plt.show()
    
    def plt_color(self):
        np.random.seed(19680801)

        x = np.random.randn(100)
        y = np.random.randn(100)

        fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)

        axs[0, 0].scatter(x, y, c='C1')
        axs[0, 1].scatter(x, y, alpha=0.5)
        axs[1, 0].scatter(x, y, edgecolor='red')
        axs[1, 1].scatter(x, y, edgecolor='red', linewidth=3)

        titles = ['color=C1', 'alpha=0.5', 'edgecolor=red', 'linewidth=3']

        for ax, title in zip(axs.flat, titles):
            ax.set_title(title)
        
        fig.supxlabel('X label')
        fig.supylabel('Y label')
        fig.suptitle('color in scatter')

        plt.show()
    
    def plt_cmap(self):
        np.random.seed(19680801)

        x = np.random.randn(100)
        y = np.random.randn(100)
        z = np.random.randn(100)

        fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)

        cmaps = ['viridis', 'Greys', 'winter', 'bwr']

        count = 0
        for col in range(2):
            for row in range(2):
                cmap = cmaps[count]
                ax = axs[row, col]
                if col == 1:
                    CS = ax.scatter(x, y, s=z*100, c=z, cmap=cmap)
                    ax.set_title(cmap)
                else:
                    CS = ax.scatter(x, y, s=z*100, c=z, cmap=cmap, vmax=1, vmin=0)
                    ax.set_title(cmap+' & vmax=1 vmin=0')
                fig.colorbar(CS, ax=ax)
                count += 1

        fig.supxlabel('X label')
        fig.supylabel('Y label')
        fig.suptitle('cmap in scatter')

        plt.show()

    def plt_3d(self):
        np.random.seed(19680801)

        x = np.random.randn(100)
        y = np.random.randn(100)
        z = np.random.randn(100)

        fig, ax = plt.subplots(subplot_kw={'projection':'3d'})

        CS = ax.scatter(x, y, z, s=z*100, c=z)
        fig.colorbar(CS, ax=ax)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('3dimension in scatter')

        plt.show()

if __name__ == '__main__':
    scatter_format = ScatterFormat()
    scatter_format.plt_simple()
    # scatter_format.plt_marker_s()
    # scatter_format.plt_color()
    # scatter_format.plt_cmap()
    # scatter_format.plt_3d()