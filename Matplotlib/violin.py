import matplotlib.pyplot as plt
import numpy as np
from thesis_format import ThesisFormat

class ViolinPlot(ThesisFormat):
    def __init__(self) -> None:
        super().__init__()

    def plt_violin(self):
        np.random.seed(19680801)
        all_data = [np.random.normal(0, std, 100) for std in range(7, 10)]

        labels = ['x1', 'x2', 'x3']

        fig, ax = plt.subplots()

        vio = ax.violinplot(all_data)

        # ax.violinplot(data, pos, points=40, widths=0.5,
        #                     showmeans=True, showextrema=True, showmedians=True,
        #                     bw_method='silverman')

        # ax.violinplot(data, pos, points=60, widths=0.7, showmeans=True,
        #                     showextrema=True, showmedians=True, bw_method=0.5)

        # ax.violinplot(data, pos, points=60, widths=0.7, showmeans=True,
        #                     showextrema=True, showmedians=True, bw_method=0.5,
        #                     quantiles=[[0.1], [], [], [0.175, 0.954], [0.75], [0.25]])

        # ax.violinplot(data[-1:], pos[-1:], points=60, widths=0.7,
        #                     showmeans=True, showextrema=True, showmedians=True,
        #                     quantiles=[0.05, 0.1, 0.8, 0.9], bw_method=0.5)

        

        # ax.violinplot(data, pos, points=100, vert=False, widths=0.9,
        #                     showmeans=True, showextrema=True, showmedians=True,
        #                     bw_method='silverman')

        # ax.violinplot(data, pos, points=200, vert=False, widths=1.1,
        #                     showmeans=True, showextrema=True, showmedians=True,
        #                     bw_method=0.5)

        # ax.violinplot(data, pos, points=200, vert=False, widths=1.1,
        #                     showmeans=True, showextrema=True, showmedians=True,
        #                     quantiles=[[0.1], [], [], [0.175, 0.954], [0.75], [0.25]],
        #                     bw_method=0.5)

        # ax.violinplot(data[-1:], pos[-1:], points=200, vert=False, widths=1.1,
        #                     showmeans=True, showextrema=True, showmedians=True,
        #                     quantiles=[0.05, 0.1, 0.8, 0.9], bw_method=0.5)
        for body in vio['bodies']:
            # body.set_color('C1')
            # body.set_facecolor('C2')
            body.set_edgecolor('red')
            body.set_linewidth(3)
#

        ax.set_xticks(np.arange(1, len(labels) + 1), labels=labels)
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('edge color in violin')

        plt.show()

    def plt_hori_width(self):
        np.random.seed(19680801)
        all_data = [np.random.normal(0, std, 100) for std in range(7, 10)]

        fig, ax = plt.subplots()
        # ax.violinplot(all_data, vert=False)
        # ax.violinplot(all_data, widths=0.5)
        ax.violinplot(all_data, widths=[0.2, 0.5, 1])

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('width array in violin')
        plt.show()

    def plt_showline(self):
        np.random.seed(19680801)
        all_data = [np.random.normal(0, std, 100) for std in range(7, 10)]

        labels = ['x1', 'x2', 'x3']

        fig, ax = plt.subplots()

        # ax.violinplot(all_data, showmeans=False, showextrema=False, showmedians=False)

        # 平均値のカスタマイズ
        # showmeans = ax.violinplot(all_data, showmeans=True, showextrema=False, showmedians=False)
        # showmeans['cmeans'].set_color('C1')
        # 極限領域のカスタマイズ
        # showextrem = ax.violinplot(all_data, showmeans=False, showextrema=True, showmedians=False)
        # showextrem['cmins'].set_color('C2')
        # showextrem['cmaxes'].set_color('C3')
        # 中央値のカスタマイズ
        showmedians = ax.violinplot(all_data, showmeans=False, showextrema=False, showmedians=True)
        showmedians['cmedians'].set_color('C1')

        titles = ['All False', 'means', 'extrema', 'medians']

        ax.set_xticks(np.arange(1, len(labels) + 1), labels=labels)
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('medians in violin plot')
        
        plt.show()
    
    def plt_violin_box(self):

        np.random.seed(19680801)

        all_data = [np.random.normal(0, std, 100) for std in range(7, 10)]

        labels = ['x1', 'x2', 'x3']

        fig, ax = plt.subplots()

        vio = ax.violinplot(all_data, showmeans=True, showmedians=False)
        vio['cmeans'].set_color('C1')
        ax.set_title('Violin plot')

        ax.boxplot(all_data)
        ax.set_title('Box plot')

        ax.set_xticks(np.arange(1, len(labels) + 1), labels=labels)
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')

        plt.show()


if __name__ == '__main__':
    violin_plot = ViolinPlot()
    violin_plot.plt_violin()
    # violin_plot.plt_hori_width()
    # violin_plot.plt_showline()
    # violin_plot.plt_violin_box()