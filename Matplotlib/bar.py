# group
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
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
    
    def plt_bar(self):
        # step1 データの作成
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        x = np.arange(len(labels))
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]

        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 棒グラフの描画
        ax.bar(x, men_means, label='Men', tick_label=labels)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('Basic Bar')
        ax.legend()

        plt.show()

    def plt_stack(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        x = np.arange(len(labels))
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]

        fig, ax = plt.subplots()
        ax.bar(x, men_means, label='Men', tick_label=labels)
        ax.bar(x, women_means, label='Women', bottom=men_means, tick_label=labels)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('Stacked Bar')
        ax.legend()

        plt.show()

    def plt_group(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        x = np.arange(len(labels))
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]

        width = 0.4

        fig, ax = plt.subplots()
        ax.bar(x - width/2, men_means, width, label='Men', tick_label=labels)
        ax.bar(x + width/2, women_means, width, label='Women', tick_label=labels)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('Grouped Bar')
        ax.legend()

        plt.show()

    def plt_align(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        x = np.arange(len(labels))
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]

        fig, ax = plt.subplots()
        ax.bar(x, men_means, align='edge', label='Men', tick_label=labels)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('align = edge')
        ax.legend()

        plt.show()
    
    def plt_label(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        x = np.arange(len(labels))
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]

        fig, ax = plt.subplots()
        # 一般的な棒グラフ
        basic = ax.bar(x, men_means, width=0.4, label='Men')
        ax.bar_label(basic, labels=men_means)
        ax.set_title(f'Basic with label')

        # グループ化された棒グラフ
        # group1 = ax.bar(x - width/2, men_means, width, label='Men')
        # group2 = ax.bar(x + width/2, women_means, width, label='Women')

        # ax.bar_label(group1, labels=men_means)
        # ax.bar_label(group2, labels=women_means, padding=10)
        # ax.set_title(f'Group (padding=10 in women)')

        #積み上げ式棒グラフ
        # stock1 = ax.bar(labels, men_means, width, label='Men')
        # stock2 = ax.bar(labels, women_means, width, bottom=men_means, label='Women')

        # ax.bar_label(stock1, fmt='%.1f')
        # ax.bar_label(stock2, fmt='%.1f')

        # ax.set_xlabel('X label')
        # ax.set_ylabel('Y label')
        # ax.set_title(f'Stack (fmt=%.1f)')

        ax.set_xticks(x, labels)
        ax.legend()

        plt.show()
    
    def plt_err(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        x = np.arange(len(labels))
        men_means = [20, 34, 30, 35, 27]
        # エラーバーのデータ
        men_std = [2, 3, 4, 1, 2]

        width = 0.4

        fig, ax = plt.subplots()

        # 一般的な棒グラフのエラーバー
        # ax.bar(x, men_means, width, yerr=men_std)
        # エラーバーのラベル付き棒グラフ
        # basic = ax.bar(x, men_means, width, yerr=men_std)
        # ax.bar_label(basic, labels=['±%.1f' % e for e in men_std])
        # エラーバーの色
        # ax.bar(x, men_means, width, yerr=men_std, ecolor='red')
        # エラーバーのサイズ
        ax.bar(x, men_means, width, yerr=men_std, capsize=10)
        
        ax.set_title('Size of error bars')
        ax.set_xticks(x, labels)
        plt.show()

    def plt_color(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        x = np.arange(len(labels))
        men_means = [20, 34, 30, 35, 27]

        fig, ax = plt.subplots()
        # ax.bar(x, men_means, color=['C'+str(i) for i in range(len(men_means))])
        ax.bar(x, men_means, color='white', edgecolor=['C'+str(i) for i in range(len(men_means))], linewidth=5)

        ax.set_title('EdgeColor of bars')
        ax.set_xticks(x, labels)
        plt.show()

    def plt_log(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        x = np.arange(len(labels))
        men_means = [20, 34, 30, 35, 27]

        fig, ax = plt.subplots()
        ax.bar(x, men_means, log=True)

        ax.set_title('log scale bar')
        ax.set_xticks(x, labels)
        plt.show()


if __name__ == '__main__':
    bar_format = BarFormat()
    # bar_format.plt_bar()
    bar_format.plt_stack()
    # bar_format.plt_group()
    # bar_format.plt_align()
    # bar_format.plt_label()
    # bar_format.plt_err()
    # bar_format.plt_color()
    # bar_format.plt_log()