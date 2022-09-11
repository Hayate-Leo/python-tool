# https://matplotlib.org/stable/gallery/lines_bars_and_markers/stem_plot.html#sphx-glr-gallery-lines-bars-and-markers-stem-plot-py
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html
# https://matplotlib.org/stable/gallery/mplot3d/stem3d_demo.html#sphx-glr-gallery-mplot3d-stem3d-demo-py


import matplotlib.pyplot as plt
import numpy as np

class StemFormat:
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
        plt.rcParams['mathtext.fontset'] = 'cm'
        self.line_styles = ['-', '--', '-.', ':']
        self.markers = ['o', ',', '.', 'v', '^', '<', '>', '1', '2', '3', '.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3']
    
    def plt_stem(self):
        x = np.linspace(0.1, 2 * np.pi, 41)
        y = np.exp(np.sin(x))

        fig, ax = plt.subplots()

        ax.stem(x, y)
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')

        ax.set_xlim(0, 6)

        ax.set_title('Stem demo')
        plt.show()
    
    def plt_stem_fmt(self):
        x = np.linspace(0.1, 2 * np.pi, 21)
        y = np.exp(np.sin(x))

        fig, axs = plt.subplots(2, 2, constrained_layout=True)

        axs[0, 0].stem(x, y, linefmt=None, markerfmt=None, basefmt=None)
        axs[0, 1].stem(x, y, linefmt='--')
        axs[1, 0].stem(x, y, markerfmt='^')
        axs[1, 1].stem(x, y, basefmt='C2')

        titles = ['Stem Default', 'LineFmt', 'MarkerFmt', 'BaseFmt']

        for ax, title in zip(axs.flat, titles):
            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_title(title)

        fig.suptitle('Stem Fmt')
        plt.show()
    
    def plt_orient(self):
        x = np.linspace(0.1, 2 * np.pi, 21)
        y = np.exp(np.sin(x))

        fig, axs = plt.subplots(1, 2, constrained_layout=True)
        axs[0].stem(x, y, orientation='vertical')
        axs[1].stem(x, y, orientation='horizontal')

        titles = ['Vertical', 'Horizontal']

        for ax, title in zip(axs.flat, titles):
            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_title(title)

        fig.suptitle('Stem Orientation')
        plt.show()
    
    def plt_bottom_label(self):
        x = np.linspace(0.1, 2 * np.pi, 21)
        y = np.exp(np.sin(x))

        fig, axs = plt.subplots(1, 2, constrained_layout=True)
        axs[0].stem(x, y, bottom=0, label='bottom=0')
        axs[1].stem(x, y, bottom=1, label='bottom=1')

        titles = ['Bottom=0', 'Bottom=1']

        for ax, title in zip(axs.flat, titles):
            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_title(title)
            ax.legend()

        fig.suptitle('Stem Bottom Label')
        plt.show()


if __name__ == '__main__':
    stem_format = StemFormat()
    stem_format.plt_stem()
    # stem_format.plt_stem_fmt()
    # stem_format.plt_orient()
    # stem_format.plt_bottom_label()
