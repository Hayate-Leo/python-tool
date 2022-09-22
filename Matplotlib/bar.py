# group
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
# label demo
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html#sphx-glr-gallery-lines-bars-and-markers-bar-label-demo-py


from gzip import _PaddedFile
import matplotlib.pyplot as plt
import numpy as np

class BarFormat:
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
        self.markers = ['o', ',', '.', 'v', '^', '<', '>', '1', '2', '3']
    
    def plt_bar(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]

        x = np.arange(len(labels))

        fig, ax = plt.subplots()
        ax.bar(x, men_means, label='Men', tick_label=labels)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('Basic Bar')
        ax.legend()

        plt.show()

    def plt_stock(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]

        x = np.arange(len(labels))

        fig, ax = plt.subplots()
        ax.bar(x, men_means, label='Men')
        ax.bar(x, women_means, label='Women', bottom=men_means)

        ax.set_xticks(x, labels)
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('Stocked Bar')
        ax.legend()

        plt.show()
    
    def plt_group(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]

        x = np.arange(len(labels))
        width = 0.4

        fig, axs = plt.subplots(1, 2, sharey=True)
        axs[0].bar(x - width/2, men_means, width, label='Men')
        axs[0].bar(x + width/2, women_means, width, label='Women')

        axs[1].bar(x - width, men_means, width, align='edge', label='Men')
        axs[1].bar(x, women_means, width, align='edge', label='Women')

        axs[0].set_ylabel('Y label')
        axs[0].set_title('align=center')
        axs[1].set_title('align=edge')

        for ax in axs.flat:
            ax.set_xticks(x, labels)
            ax.set_xlabel('X label')
            ax.legend()

        fig.suptitle('Grouped Bar')

        plt.show()
    
    def plt_label(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]

        x = np.arange(len(labels))
        width = 0.4

        fig, axs = plt.subplots(1, 2, sharey=True)
        # グループ化された棒グラフ
        group1 = axs[0].bar(x - width/2, men_means, width, label='Men')
        group2 = axs[0].bar(x + width/2, women_means, width, label='Women')

        #積み上げ式棒グラフ
        stock1 = axs[1].bar(labels, men_means, width, label='Men')
        stock2 = axs[1].bar(labels, women_means, width, bottom=men_means, label='Women')

        # グループ化された棒グラフのラベル
        axs[0].bar_label(group1, labels=men_means)
        axs[0].bar_label(group2, labels=women_means, padding=10)

        # 積み上げ式棒グラフのラベル
        axs[1].bar_label(stock1, fmt='%.1f')
        axs[1].bar_label(stock2, fmt='%.1f')

        axs[0].set_ylabel('Y label')
        axs[0].set_title(f'Group (padding=10 in women)')
        axs[1].set_title(f'Stock (fmt=%.1f)')

        for ax in axs.flat:
            ax.set_xticks(x, labels)
            ax.set_xlabel('X label')
            ax.legend()

        fig.suptitle('Bar label')
        plt.show()
    
    def plt_err(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]
        # エラーバーのデータ
        men_std = [2, 3, 4, 1, 2]
        women_std = [3, 5, 2, 3, 3]

        x = np.arange(len(labels))
        width = 0.4

        fig, axs = plt.subplots(1, 2, sharey=True)
        # グループ化された棒グラフ
        group1 = axs[0].bar(x - width/2, men_means, width, label='Men', yerr=men_std)
        group2 = axs[0].bar(x + width/2, women_means, width, label='Women', yerr=women_std)

        #積み上げ式棒グラフ
        stock1 = axs[1].bar(labels, men_means, width, label='Men', yerr=men_std)
        stock2 = axs[1].bar(labels, women_means, width, bottom=men_means, label='Women', yerr=women_std)

        # グループ化された棒グラフのラベル
        axs[0].bar_label(group1, labels=['±%.1f' % e for e in men_std])
        axs[0].bar_label(group2, labels=['±%.1f' % e for e in women_std])

        # 積み上げ式棒グラフのラベル
        axs[1].bar_label(stock1, labels=['±%.1f' % e for e in men_std])
        axs[1].bar_label(stock2, labels=['±%.1f' % e for e in women_std])

        axs[0].set_ylabel('Y label')
        axs[0].set_title('Group')
        axs[1].set_title('Stock')

        for ax in axs.flat:
            ax.set_xticks(x, labels)
            ax.set_xlabel('X label')
            ax.legend()

        fig.suptitle('Bar error')
        plt.show()

    def plt_color(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]
        men_std = [2, 3, 4, 1, 2]
        women_std = [3, 5, 2, 3, 3]

        x = np.arange(len(labels))

        fig, axs = plt.subplots(2, 2, sharey=True, sharex=True)
        axs[0, 0].bar(x, men_means, color=['C'+str(i) for i in range(len(men_means))], log=True)
        axs[0, 1].bar(x, women_means, edgecolor=['C'+str(i) for i in range(len(women_means))],linewidth=x, log=True)

        axs[1, 0].bar(x, men_means, tick_label=labels, yerr=men_std, ecolor='red', log=True)
        axs[1, 1].bar(x, women_means , tick_label=labels, yerr=women_std, capsize=10, log=True)     

        axs[0, 0].set_title('Color')
        axs[0, 1].set_title('Edgecolor')
        axs[1, 0].set_title('Ecolor=red')
        axs[1, 1].set_title('capsize=10')

        axs[1, 0].set_xlabel('[1, 0] label')
        axs[1, 1].set_xlabel('[1, 1] label')
        axs[0, 0].set_ylabel('[0, 0] label')
        axs[1, 0].set_ylabel('[1, 0] label')

        fig.suptitle('color & edgecolor & linewidth & ecolor & capsize in logbar')

        plt.show()

if __name__ == '__main__':
    bar_format = BarFormat()
    # bar_format.plt_bar()
    # bar_format.plt_stock()
    # bar_format.plt_group()
    bar_format.plt_label()
    # bar_format.plt_err()
    # bar_format.plt_color()