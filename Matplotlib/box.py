# https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html
# https://matplotlib.org/stable/gallery/statistics/boxplot_color.html
# https://matplotlib.org/stable/gallery/statistics/boxplot.html


import matplotlib.pyplot as plt
import numpy as np


class ThesisFormat:
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
        self.line_styles = ['-', '--', '-.', ':']
        self.markers = ['o', ',', '.', 'v', '^', '<', '>', '1', '2', '3', '.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3']

    def plt_box(self):

        # Fixing random state for reproducibility
        np.random.seed(19680801)

        # fake up some data
        spread = np.random.rand(50) * 100
        center = np.ones(25) * 50
        flier_high = np.random.rand(10) * 100 + 100
        flier_low = np.random.rand(10) * -100

        data = np.concatenate((spread, center, flier_high, flier_low))

        labels = ['x1', 'x2', 'x3']
        datas = [data, data[::2], data[::4]]

        fig, ax = plt.subplots()

        # basic plot
        bplot = ax.boxplot(datas, labels=labels, patch_artist=True)
        ax.set_title('basic plot')

        # notched plot
        # ax.boxplot(datas, 1)
        # ax.set_title('notched plot')

        # change outlier point symbols
        # ax.boxplot(datas, 0, 'gD')
        # ax.set_title('change outlier\npoint symbols')

        # don't show outlier points
        # ax.boxplot(datas, 0, '')
        # ax.set_title("don't show\noutlier points")

        # horizontal boxes
        # ax.boxplot(datas, 0, 'rs', 0)
        # ax.set_title('horizontal boxes')

        # change whisker length
        # ax.boxplot(datas, 0, 'rs', 0, 0.75)
        # ax.set_title('change whisker length')

        colors = ['pink', 'lightblue', 'lightgreen']
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)

        ax.set_xlabel('Three separate samples')
        ax.set_ylabel('Observed values')

        plt.show()


if __name__ == '__main__':
    thesis_format = ThesisFormat()
    thesis_format.plt_box()