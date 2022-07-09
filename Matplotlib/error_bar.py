# https://matplotlib.org/stable/plot_types/stats/errorbar_plot.html#sphx-glr-plot-types-stats-errorbar-plot-py
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/errorbar_limits_simple.html#sphx-glr-gallery-lines-bars-and-markers-errorbar-limits-simple-py

import matplotlib.pyplot as plt
import numpy as np

class ErrorBar:
    def __init__(self) -> None:
        self.plt_style()
    
    def plt_style(self):
        plt.rcParams['font.family'] ='Times New Roman'
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        plt.rcParams['font.size'] = 12
        plt.rcParams['axes.linewidth'] = 1.0
        plt.rcParams['lines.markersize'] = 7
        plt.rcParams['errorbar.capsize'] = 6
        self.line_styles = ['-', '--', '-.', ':']
        self.markers = ['o', ',', '.', 'v', '^', '<', '>', '1', '2', '3', '.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3']
    
    def simple(self):
        np.random.seed(1)
        x = [2, 4, 6]
        y = [3.6, 5, 4.2]
        yerr = [0.9, 1.2, 0.5]

        # plot:
        fig, ax = plt.subplots()

        ax.errorbar(x, y, yerr, fmt=self.markers[0], capthick=10)

        ax.set(xlim=(0, 8), xticks=np.arange(1, 8), xlabel=(r'Sample [$No$]'),
            ylim=(0, 8), yticks=np.arange(1, 8), ylabel=(r'Weight [$g$]'))

        plt.show()

    def line(self):
        x = np.arange(0.1, 4, 0.5)
        y = np.exp(-x)

        fig, ax = plt.subplots()
        ax.errorbar(x, y, fmt=self.line_styles[1], xerr=0.2, yerr=0.4)
        plt.show()

if __name__ == '__main__':
    error_bar = ErrorBar()
    error_bar.simple()
    # error_bar.line()