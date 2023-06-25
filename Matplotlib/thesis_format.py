# https://matplotlib.org/stable/api/matplotlib_configuration_api.html?highlight=rcparams#matplotlib.rcParams
# https://qiita.com/qsnsr123/items/325d21621cfe9e553c17


import matplotlib.pyplot as plt
import numpy as np

class ThesisFormat:
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

    def plt_line_marker(self):
        x = np.linspace(0, 10, 30)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)

        fig, ax = plt.subplots()

        ax.plot(x, y1, self.markers[0]+'--', label='Sample 1')
        ax.plot(x, y2, self.markers[1]+'--', label='Sample 2')

        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        ax.set_ylabel('Y label')
        ax.set_xlabel('X label')
        ax.legend()

        ax.set_title('Markered line')
        fig.suptitle('Fig Title')

        plt.show()

    def plt_scatter(self):
        np.random.seed(19680801)

        x = np.random.randn(100)
        y1 = np.random.randn(100)
        y2 = np.random.randn(100)

        fig, ax = plt.subplots()

        ax.scatter(x, y1, alpha=0.5, label='Sample1')
        ax.scatter(x, y2, alpha=0.5, label='Sample2', marker=self.markers[1])

        ax.set_ylabel('Y label')
        ax.set_xlabel('X label')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.set_title('Simple scatter')

        plt.show()
    
    def plt_scatter_edge(self):
        np.random.seed(19680801)

        x = np.random.randn(100)
        num = 5
        ys = [np.random.randn(100) for _ in range(num)]

        fig, ax = plt.subplots()

        for i, y in enumerate(ys):
            ax.scatter(x, y, label='Sample '+str(i+1), c='white', edgecolor='C'+str(i), marker=self.markers[i])

        ax.set_ylabel('Y label')
        ax.set_xlabel('X label')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.set_title('Edgecolor scatter')

        plt.show()
    
    def plt_bar(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        men_means = [20, 34, 30, 35, 27]
        men_std = [2, 3, 4, 1, 2]

        x = np.arange(len(labels))

        fig, ax = plt.subplots()
        bar = ax.bar(x, men_means, label='Men', tick_label=labels, yerr=men_std)

        labels = [str(m) + ' ± ' + str(s) for m, s in zip(men_means, men_std)]
        ax.bar_label(bar, labels=labels)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title('Basic bar')
        ax.legend()

        plt.show()

    def plt_bar_group_stack(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]

        x = np.arange(len(labels))
        width = 0.4

        fig, axs = plt.subplots(1, 2, sharey=True)
        # Grouped bar chart
        group1 = axs[0].bar(x - width/2, men_means, width, label='Men')
        group2 = axs[0].bar(x + width/2, women_means, width, label='Women')

        # Stacked bar chart
        stack1 = axs[1].bar(labels, men_means, width, label='Men')
        stack2 = axs[1].bar(labels, women_means, width, bottom=men_means, label='Women')

        # Grouped bar chart labels
        axs[0].bar_label(group1, labels=men_means)
        axs[0].bar_label(group2, labels=women_means)

        # Stacked bar chart labels
        axs[1].bar_label(stack1, fmt='%.1f')
        axs[1].bar_label(stack2, fmt='%.1f')

        axs[0].set_ylabel('Y label')
        axs[0].set_title(f'Grouped Bar')
        axs[1].set_title(f'Stacked Bar')

        for ax in axs.flat:
            ax.set_xticks(x, labels)
            ax.set_xlabel('X label')
            ax.legend()

        fig.suptitle('Bar for a Thesis')
        plt.show()
    
    def plt_step(self):
        np.random.seed(3)
        x = 0.5 + np.arange(8)
        y = np.random.uniform(2, 7, len(x))

        fig, ax = plt.subplots()

        ax.step(x, y, label='Sample 1')

        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        ax.set_xlabel('Time [$sec$]')
        ax.set_ylabel('Frequency [$Hz$]')  
        ax.legend()

        plt.show()

    def plt_circle(self):
        labels = ['A', 'B', 'C', 'D']
        sizes = [15, 30, 45, 10]

        fig, ax = plt.subplots()
        # カラーマップの指定
        cmap = plt.colormaps['viridis']
        colors = cmap((np.linspace(0.4, 0.9, len(sizes))))
        # 円グラフの描画
        ax.pie(sizes, labels=labels, autopct='%.0f%%', startangle=90, counterclock=False, normalize=True,
            colors=colors,
            wedgeprops = {'edgecolor': 'white', 'linewidth': 1.2}, 
            textprops={'fontsize': 17, 'fontweight': 'bold', 'family': 'Times new roman'}
        )

        ax.set_title('circle plot for a thesis')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        plt.show()

    def plt_contour(self):
        delta = 0.025
        x = np.arange(-3.0, 3.0, delta)
        y = np.arange(-2.0, 2.0, delta)
        X, Y = np.meshgrid(x, y)
        Z1 = np.exp(-X**2 - Y**2)
        Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
        Z = Z1 - Z2

        fig, ax = plt.subplots()
        # 等高線のラベル
        CS = ax.contour(X, Y, Z, colors='black')
        ax.clabel(CS, inline=True)

        # 等高線の塗りつぶし
        CSf = ax.contourf(X, Y, Z)

        # カラーバーの設定
        cbar = fig.colorbar(CSf)
        cbar.ax.set_ylabel('Z Label')
        cbar.add_lines(CS)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_title('Simple Contour')
        plt.show()

if __name__ == '__main__':
    thesis_format = ThesisFormat()
    # thesis_format.plt_line()
    # thesis_format.plt_line_marker()
    # thesis_format.plt_scatter()
    # thesis_format.plt_scatter_edge()
    # thesis_format.plt_bar()
    thesis_format.plt_bar_group_stack()
    # thesis_format.plt_step()
    thesis_format.plt_circle()
    # thesis_format.plt_contour()