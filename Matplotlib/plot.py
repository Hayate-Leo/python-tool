# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html

import matplotlib.pyplot as plt
import numpy as np


class PlotFormat:
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

    def plt_line(self):
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)

        fig, ax = plt.subplots()

        ax.plot(x, y1, linestyle=self.line_styles[0], label='Sample 1')
        ax.plot(x, y2, linestyle=self.line_styles[1], label='Sample 2')
        
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.legend()

        ax.set_title('Simple line')

        plt.show()
    
    def plt_scatter(self):
        x = np.linspace(0, 10, 30)
        y = 4 + 2 * np.sin(2 * x)

        fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)

        axs[0, 0].plot(x, y)
        axs[0, 1].plot(x, y, 'o')
        axs[1, 0].plot(x, y, 'o--', markersize=10)
        axs[1, 1].plot(x, y, 'or', ms=10)

        titles = ['default', 'fmt="o"', 'fmt="o" & markersize=10', 'fmt="or", ms=10']

        for ax, title in zip(axs.flat, titles):
            ax.set_xlim(0, 8)
            ax.set_ylim(0, 8)
            ax.set_title(title)
        
        axs[0, 0].set_ylabel('Y label')
        axs[1, 0].set_ylabel('Y label')
        axs[1, 0].set_xlabel('X label')
        axs[1, 1].set_xlabel('X label')

        fig.suptitle('Simple scatter')

        plt.show()
    
    def plt_custom_line(self):
        x = np.linspace(0, 10, 100)
        y = 4 + 2 * np.sin(2 * x)

        fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)

        axs[0, 0].plot(x, y)
        axs[0, 1].plot(x, y, color='C1', linestyle='--')
        axs[1, 0].plot(x, y, linestyle='-.', linewidth=5)
        axs[1, 1].plot(x, y, linestyle=':', linewidth=5, alpha=0.5)

        titles = ['default (solid)', 'color=C1 (dashed)', 'linewidth=5 (dashdot)', 'alpha=0.5 (dotted)']

        for ax, title in zip(axs.flat, titles):
            ax.set_xlim(0, 8)
            ax.set_ylim(0, 8)
            ax.set_title(title)
        
        fig.supxlabel('X label')
        fig.supylabel('Y label')
        fig.suptitle('custom line plot')

        plt.show()
    
    def plt_custom_markerstyle(self):
        x = np.linspace(0, 10, 50)
        y = 4 + 2 * np.sin(2 * x)

        fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)

        axs[0, 0].plot(x, y, self.markers[0]) # o
        axs[0, 0].plot(x, y-2, self.markers[1]) # ,
        axs[0, 1].plot(x, y, self.markers[2]) # .
        axs[0, 1].plot(x, y-2, self.markers[3]) # v
        axs[1, 0].plot(x, y, marker=self.markers[4]) # ^
        axs[1, 0].plot(x, y-2, marker=self.markers[5]) # <
        axs[1, 1].plot(x, y, marker=self.markers[6]) # >
        axs[1, 1].plot(x, y-2, marker=self.markers[7]) # 1

        titles = ['o & ,', '. & v', '^ & <', '> & 1']

        for ax, title in zip(axs.flat, titles):
            ax.set_xlim(0, 8)
            ax.set_ylim(0, 8)
            ax.set_title(title)
        
        fig.supxlabel('X label')
        fig.supylabel('Y label')
        fig.suptitle('custom markerstyle')

        plt.show()

    def plt_custom_markercolor(self):
        x = np.linspace(0, 10, 50)
        y = 4 + 2 * np.sin(2 * x)

        fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)

        axs[0, 0].plot(x, y, 'o--', markerfacecolor='white')
        axs[0, 1].plot(x, y, 'o--', markeredgecolor='red')
        axs[1, 0].plot(x, y, 'o--', markeredgecolor='red', markeredgewidth=5)
        axs[1, 1].plot(x, y, 'o', fillstyle='bottom')

        titles = ['markerfacecolor', 'markeredgecolor', 'markeredgewidth', 'fillstyle']

        for ax, title in zip(axs.flat, titles):
            ax.set_xlim(0, 8)
            ax.set_ylim(0, 8)
            ax.set_title(title)
        
        fig.supxlabel('X label')
        fig.supylabel('Y label')
        fig.suptitle('custom markercolor')

        plt.show()

if __name__ == '__main__':
    plot_format = PlotFormat()
    # plot_format.plt_line()
    plot_format.plt_scatter()
    # plot_format.plt_custom_line()
    # plot_format.plt_custom_markerstyle()
    plot_format.plt_custom_markercolor()