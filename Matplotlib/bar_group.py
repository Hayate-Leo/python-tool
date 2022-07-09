# group
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
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
    
    def plt_group(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]
        # エラーバー
        men_std = [2, 3, 4, 1, 2]
        women_std = [3, 5, 2, 3, 3]

        x = np.arange(len(labels))
        width = 0.35

        fig, ax = plt.subplots()
        # ax.bar(x - width/2, men_means, width, label='Men')
        # ax.bar(x + width/2, women_means, width, label='Women')
        rects1 = ax.bar(x - width/2, men_means, width, label='Men', yerr=men_std)
        rects2 = ax.bar(x + width/2, women_means, width, label='Women', yerr=women_std)

        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.set_xticks(x, labels)
        ax.legend()

        ax.bar_label(rects1, labels=men_std)
        ax.bar_label(rects2, labels=women_std)

        plt.show()

if __name__ == '__main__':
    thesis_format = ThesisFormat()
    thesis_format.plt_group()