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
        plt.rcParams['errorbar.capsize'] = 6
        plt.rcParams['lines.markersize'] = 6
        plt.rcParams['mathtext.fontset'] = 'cm'
        self.line_styles = ['-', '--', '-.', ':']
        self.markers = ['o', ',', '.', 'v', '^', '<', '>', '1', '2', '3']
    
    def plt_simple(self):
        x = np.arange(5)
        y = [4.6, 3.6, 5, 4.2, 2.7]
        yerr = [0.6, 0.9, 1.2, 0.5, 0.7]

        fig, ax = plt.subplots()

        ax.errorbar(x, y, yerr)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('Simple errorbar')

        plt.show()

    def plt_err(self):
        x = np.arange(5)
        y = np.exp(-x)

        fig, ax = plt.subplots()
        ax.errorbar(x, y, xerr=0.2, yerr=0.4)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('xrr & yerr in errorbar')

        plt.show()
    
    def plt_fmt(self):
        x = np.arange(5)
        y = np.exp(-x)

        fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)

        axs[0, 0].errorbar(x, y, yerr=0.4, fmt='--')
        axs[0, 1].errorbar(x, y, yerr=0.4, fmt='o')
        axs[1, 0].errorbar(x, y, yerr=0.4, fmt='.-')
        axs[1, 1].errorbar(x, y, yerr=0.4, fmt='.r')

        axs[0, 0].set_ylabel('Y label')
        axs[1, 0].set_ylabel('Y label')
        axs[1, 0].set_xlabel('X label')
        axs[1, 1].set_xlabel('X label')

        axs[0, 0].set_title('fmt="--"')
        axs[0, 1].set_title('fmt="o"')
        axs[1, 0].set_title('fmt=".-"')
        axs[1, 1].set_title('fmt=".r"')

        fig.suptitle('fmt in errorbar')

        plt.show()
    
    def plt_ecolor_eline(self):
        x = np.arange(5)
        y = np.exp(-x)

        fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)

        axs[0, 0].errorbar(x, y, yerr=0.4, fmt='o-')
        axs[0, 1].errorbar(x, y, yerr=0.4, fmt='o-', ecolor='red')
        axs[1, 0].errorbar(x, y, yerr=0.4, fmt='o-', elinewidth=0.5)
        axs[1, 1].errorbar(x, y, yerr=0.4, fmt='o-', ecolor='gray', barsabove=True)

        axs[0, 0].set_ylabel('Y label')
        axs[1, 0].set_ylabel('Y label')
        axs[1, 0].set_xlabel('X label')
        axs[1, 1].set_xlabel('X label')

        axs[0, 0].set_title('default')
        axs[0, 1].set_title('ecolor="red"')
        axs[1, 0].set_title('elinewidth=0.5')
        axs[1, 1].set_title('barsabove=True')

        fig.suptitle('ecolor & elinewidth in errorbar')

        plt.show()

    def plt_cap(self):
        x = np.arange(5)
        y = np.exp(-x)

        fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)

        axs[0, 0].errorbar(x, y, yerr=0.4, fmt='o-', ecolor='red')
        axs[0, 1].errorbar(x, y, yerr=0.4, fmt='o-', ecolor='red', capsize=0)
        axs[1, 0].errorbar(x, y, yerr=0.4, fmt='o-', ecolor='red', capthick=5)
        axs[1, 1].errorbar(x, y, yerr=0.4, fmt='o-', ecolor='red', errorevery=2)

        axs[0, 0].set_ylabel('Y label')
        axs[1, 0].set_ylabel('Y label')
        axs[1, 0].set_xlabel('X label')
        axs[1, 1].set_xlabel('X label')

        axs[0, 0].set_title('capsize=6')
        axs[0, 1].set_title('capsize=0')
        axs[1, 0].set_title('capthick=5')
        axs[1, 1].set_title('errorevery=2')

        fig.suptitle('capsize & capthick & errorevery in errorbar')

        plt.show()
    
    def plt_limit(self):
        x = np.arange(5)
        y = np.exp(-x)

        fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)

        axs[0, 0].errorbar(x, y, xerr=0.2, yerr=0.4, fmt='o-', ecolor='red')
        axs[0, 1].errorbar(x, y, xerr=0.2, yerr=0.4, fmt='o-', ecolor='red', lolims=True)
        axs[1, 0].errorbar(x, y, xerr=0.2, yerr=0.4, fmt='o-', ecolor='red', xlolims=True)
        axs[1, 1].errorbar(x, y, xerr=0.2, yerr=0.4, fmt='o-', ecolor='red', uplims=True, xuplims=True)

        axs[0, 0].set_ylabel('Y label')
        axs[1, 0].set_ylabel('Y label')
        axs[1, 0].set_xlabel('X label')
        axs[1, 1].set_xlabel('X label')

        axs[0, 0].set_title('default')
        axs[0, 1].set_title('lolims')
        axs[1, 0].set_title('xlolims')
        axs[1, 1].set_title('uplims & xuplims')

        fig.suptitle('lims & xlims in errorbar')

        plt.show()

if __name__ == '__main__':
    error_bar = ErrorBar()
    error_bar.plt_simple()
    # error_bar.plt_err()
    # error_bar.plt_fmt()
    # error_bar.plt_ecolor_eline()
    # error_bar.plt_cap()
    # error_bar.plt_limit()