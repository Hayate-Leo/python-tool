# stock bar
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py
# label demo
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html#sphx-glr-gallery-lines-bars-and-markers-bar-label-demo-py


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
        plt.rcParams['lines.markersize'] = 7
        plt.rcParams['errorbar.capsize'] = 3
        self.line_styles = ['-', '--', '-.', ':']
        self.markers = ['o', ',', '.', 'v', '^', '<', '>', '1', '2', '3', '.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3']

    
    def plt_men(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        men_means = [20, 35, 30, 35, 27]
        men_std = [2, 3, 4, 1, 2]
        width = 0.35       # the width of the bars: can also be len(x) sequence

        fig, ax = plt.subplots()

        ax.bar(labels, men_means, width, yerr=men_std, label='Men')

        ax.set_ylabel('Scores')
        ax.set_title('Scores by men')
        ax.legend()

        plt.show()
    
    def plt_women(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        women_means = [25, 32, 34, 20, 25]
        women_std = [3, 5, 2, 3, 3]
        width = 0.35       # the width of the bars: can also be len(x) sequence

        fig, ax = plt.subplots()

        ax.bar(labels, women_means, width, yerr=women_std, label='Women', color='C1')

        ax.set_ylabel('Scores')
        ax.set_title('Scores by women')
        ax.legend()

        plt.show()
    
    def plt_stock(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        men_means = [20, 35, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]
        men_std = [2, 3, 4, 1, 2]
        women_std = [3, 5, 2, 3, 3]
        width = 0.35       # the width of the bars: can also be len(x) sequence

        fig, ax = plt.subplots()

        ax.bar(labels, men_means, width, yerr=men_std, label='Men')
        ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
            label='Women')

        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.legend()

        plt.show()

    def plt_stock_three(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        men_means = [20, 35, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]
        alien_means = [23, 27, 24, 10, 15]
        
        men_std = [2, 3, 4, 1, 2]
        women_std = [3, 5, 2, 3, 3]
        alien_std = [1, 3, 1, 2, 3]
        width = 0.35

        fig, ax = plt.subplots()

        ax.bar(labels, men_means, width, yerr=men_std, label='Men')
        ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
            label='Women')
        bottom_stock = [a+b for a, b in zip(men_means, women_means)]
        ax.bar(labels, alien_means, width, yerr=alien_std, bottom=bottom_stock, label='Alien')


        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.legend()

        plt.show()

if __name__ == '__main__':
    thesis_format = ThesisFormat()
    # thesis_format.plt_men()
    # thesis_format.plt_women()
    # thesis_format.plt_stock()
    thesis_format.plt_stock_three()