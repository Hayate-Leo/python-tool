# horizontal
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barh.html#sphx-glr-gallery-lines-bars-and-markers-barh-py
# label demo
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html#sphx-glr-gallery-lines-bars-and-markers-bar-label-demo-py


import matplotlib.pyplot as plt
import numpy as np


class BarFormat:
    def __init__(self) -> None:
        self.plt_style()
    
    def plt_style(self):
        plt.rcParams['figure.autolayout'] = True
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
    
    def plt_basic(self):
        # step1 データの作成
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        y = np.arange(len(labels))
        women_means = [25, 32, 34, 20, 25]

        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 水平棒グラフの描画
        ax.barh(y, women_means, label='Women', tick_label=labels)

        ax.invert_xaxis()
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('barh inverted x-axis')
        plt.show()
    
    def plt_stack(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        y = np.arange(len(labels))
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]

        fig, ax = plt.subplots()
        ax.barh(y, men_means, label='Men', tick_label=labels)
        ax.barh(y, women_means, label='Women', tick_label=labels, left=men_means)

        ax.invert_yaxis()
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('stacked barh')
        ax.legend()
        plt.show()
    
    
    def plt_group(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        y = np.arange(len(labels))
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]

        height = 0.4

        fig, ax = plt.subplots()
        ax.barh(y - height/2, men_means, height, label='Men')
        ax.barh(y + height/2, women_means, height, label='Women')

        ax.invert_yaxis()
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('grouped barh')
        ax.legend()
        plt.show()
    
    def plt_label(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        y = np.arange(len(labels))
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]

        fig, ax = plt.subplots()
        graph = ax.barh(y, women_means, height=0.6, label='Women')
        ax.bar_label(graph, labels=women_means, padding=5, fontsize=14)

        ax.invert_yaxis()
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('labeled barh')
        ax.legend()
        plt.show()
    
    def plt_err(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        y = np.arange(len(labels))
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]
        # エラーバーのデータ
        women_std = [3, 5, 2, 3, 3]

        fig, ax = plt.subplots()
        graph = ax.barh(y, women_means, height=0.6, label='Women', xerr=women_std)
        ax.bar_label(graph, labels=['±%.1f' % e for e in women_std], padding=5, fontsize=14)

        ax.invert_yaxis()
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('error barh')
        ax.legend()
        plt.show()

if __name__ == '__main__':
    bar_format = BarFormat()
    bar_format.plt_basic()
    # bar_format.plt_stack()
    # bar_format.plt_group()
    # bar_format.plt_label()
    # bar_format.plt_err()