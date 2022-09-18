import matplotlib.pyplot as plt
import numpy as np


class ViolinPlot:
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
        self.markers = ['o', ',', '.', 'v', '^', '<', '>', '1', '2', '3']

    def plt_violin(self):
        np.random.seed(19680801)
        all_data = [np.random.normal(0, std, 100) for std in range(7, 10)]

        labels = ['x1', 'x2', 'x3']

        fig, ax = plt.subplots()

        ax.violinplot(all_data)

        # axs[0, 1].violinplot(data, pos, points=40, widths=0.5,
        #                     showmeans=True, showextrema=True, showmedians=True,
        #                     bw_method='silverman')

        # axs[0, 2].violinplot(data, pos, points=60, widths=0.7, showmeans=True,
        #                     showextrema=True, showmedians=True, bw_method=0.5)

        # axs[0, 3].violinplot(data, pos, points=60, widths=0.7, showmeans=True,
        #                     showextrema=True, showmedians=True, bw_method=0.5,
        #                     quantiles=[[0.1], [], [], [0.175, 0.954], [0.75], [0.25]])

        # axs[0, 4].violinplot(data[-1:], pos[-1:], points=60, widths=0.7,
        #                     showmeans=True, showextrema=True, showmedians=True,
        #                     quantiles=[0.05, 0.1, 0.8, 0.9], bw_method=0.5)

        

        # axs[1, 1].violinplot(data, pos, points=100, vert=False, widths=0.9,
        #                     showmeans=True, showextrema=True, showmedians=True,
        #                     bw_method='silverman')

        # axs[1, 2].violinplot(data, pos, points=200, vert=False, widths=1.1,
        #                     showmeans=True, showextrema=True, showmedians=True,
        #                     bw_method=0.5)

        # axs[1, 3].violinplot(data, pos, points=200, vert=False, widths=1.1,
        #                     showmeans=True, showextrema=True, showmedians=True,
        #                     quantiles=[[0.1], [], [], [0.175, 0.954], [0.75], [0.25]],
        #                     bw_method=0.5)

        # axs[1, 4].violinplot(data[-1:], pos[-1:], points=200, vert=False, widths=1.1,
        #                     showmeans=True, showextrema=True, showmedians=True,
        #                     quantiles=[0.05, 0.1, 0.8, 0.9], bw_method=0.5)


        ax.set_xticks(np.arange(1, len(labels) + 1), labels=labels)
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('Basic Violin')

        plt.show()

    def plt_vert_width(self):
        np.random.seed(19680801)
        all_data = [np.random.normal(0, std, 100) for std in range(7, 10)]

        fig, axs = plt.subplots(2, 2, constrained_layout=True)

        axs[0, 0].violinplot(all_data)
        axs[0, 1].violinplot(all_data, vert=False)
        axs[1, 0].violinplot(all_data, widths=0.5)
        axs[1, 1].violinplot(all_data, widths=[0.2, 0.5, 1])

        titles = ['Basic', 'vert=False', 'widths=0.5', 'widths=[0.2, 0.5, 1]']

        for ax, title in zip(axs.flat, titles):
            ax.set_xlabel('X label')
            ax.set_ylabel('Y label')
            ax.set_title(title)
        
        fig.suptitle('vert & widths in violin plot')
        plt.show()

    def plt_showline(self):
        np.random.seed(19680801)
        all_data = [np.random.normal(0, std, 100) for std in range(7, 10)]

        labels = ['x1', 'x2', 'x3']

        fig, axs = plt.subplots(2, 2, constrained_layout=True)

        axs[0, 0].violinplot(all_data, showmeans=False, showextrema=False, showmedians=False)
        showmeans = axs[0, 1].violinplot(all_data, showmeans=True, showextrema=False, showmedians=False)
        showextrem = axs[1, 0].violinplot(all_data, showmeans=False, showextrema=True, showmedians=False)
        showmedians = axs[1, 1].violinplot(all_data, showmeans=False, showextrema=False, showmedians=True)

        # 平均値のカスタマイズ
        showmeans['cmeans'].set_color('C1')
        # 極限領域のカスタマイズ
        showextrem['cmins'].set_color('C2')
        showextrem['cmaxes'].set_color('C3')
        # 中央値のカスタマイズ
        showmedians['cmedians'].set_color('C1')
        for body in showmedians['bodies']:
            body.set_facecolor('C2')
            body.set_edgecolor('C3')

        titles = ['All False', 'means=True', 'extrema=True', 'medians=True']

        for ax, title in zip(axs.flat, titles):
            ax.set_xticks(np.arange(1, len(labels) + 1), labels=labels)
            ax.set_xlabel('X label')
            ax.set_ylabel('Y label')
            ax.set_title(title)
        
        fig.suptitle('means & extrema & medians in violin plot')
        plt.show()
    
    def plt_violin_box(self):

        np.random.seed(19680801)

        all_data = [np.random.normal(0, std, 100) for std in range(7, 10)]

        labels = ['x1', 'x2', 'x3']

        fig, axs = plt.subplots(1, 2, constrained_layout=True)

        axs[0].violinplot(all_data, showmeans=True, showmedians=False)
        axs[0].set_title('Violin plot')

        axs[1].boxplot(all_data)
        axs[1].set_title('Box plot')

        for ax in axs:
            ax.set_xticks(np.arange(1, len(labels) + 1), labels=labels)
            ax.set_xlabel('Three separate samples')
            ax.set_ylabel('Observed values')

        plt.show()


if __name__ == '__main__':
    violin_plot = ViolinPlot()
    # violin_plot.plt_violin()
    # violin_plot.plt_vert_width()
    violin_plot.plt_showline()
    # violin_plot.plt_violin_box()