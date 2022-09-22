# 基本的な円グラフ
# https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
# pie demo 2
# https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_demo2.html
# Nested pie
# https://matplotlib.org/stable/gallery/pie_and_polar_charts/nested_pie.html
# Axes.pie
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie

import matplotlib.pyplot as plt
import numpy as np

class CircleFormat:
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
        self.line_styles = ['-', '--', '-.', ':']
        self.markers = ['o', ',', '.', 'v', '^', '<', '>', '1', '2', '3']

    def plt_pie(self):
        labels = ['A', 'B', 'C', 'D']
        sizes = [15, 30, 45, 10]

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%.1f%%', startangle=90)

        ax.set_title('Basic pie chart')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        plt.show()
    
    def plt_donut(self):
        size = 0.3
        labels = ['A', 'B', 'C']
        vals = np.array([60, 37, 29])

        fig, ax = plt.subplots()

        ax.pie(vals, labels=labels, startangle=90, 
            autopct='%.1f%%', 
            pctdistance=0.5, 
            wedgeprops={'width':size}
        )
        
        ax.set_title('Basic donut chart')

        plt.show()
    
    def plt_donuts(self):
        labels = ['A', 'B', 'C']
        size = 0.3
        vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

        cmap = plt.colormaps['tab20c']
        fig, ax = plt.subplots()

        outer_colors = cmap(np.arange(3)*4)
        inner_colors = cmap([1, 2, 5, 6, 9, 10])

        ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors, startangle=90,
            labels=labels,
            autopct='%.1f%%', 
            pctdistance=1.15-size, 
            wedgeprops=dict(width=size, edgecolor='w'))

        ax.pie(vals.flatten(), radius=1-size, colors=inner_colors, startangle=90,
            autopct='%.1f%%', 
            pctdistance=1.1-size, 
            wedgeprops=dict(width=size, edgecolor='w'))
        
        ax.set_title('Double donut chart')

        plt.show()
    
    def plt_explode_angle(self):
        labels = ['A', 'B', 'C', 'D']
        sizes = [15, 30, 45, 10]
        explode = (0, 0.1, 0, 0)

        fig, axs = plt.subplots(2, 2, constrained_layout=True)

        axs[0, 0].pie(sizes, labels=labels, autopct='%.1f', startangle=0, explode=explode)
        axs[0, 1].pie(sizes, labels=labels, autopct='%.1f', startangle=90, explode=explode)
        axs[1, 0].pie(sizes, labels=labels, autopct='%.1f', startangle=180, explode=explode)
        axs[1, 1].pie(sizes, labels=labels, autopct='%.1f', startangle=270, explode=explode)

        axs[0, 0].set_title('startangle=0')
        axs[0, 1].set_title('startangle=90')
        axs[1, 0].set_title('startangle=180')
        axs[1, 1].set_title('startangle=270')

        fig.suptitle('explode & startangle in pie')

        plt.show()
    
    def plt_colors(self):
        labels = ['A', 'B', 'C', 'D']
        sizes = [15, 30, 45, 10]

        # https://matplotlib.org/stable/gallery/color/colormap_reference.html
        cmaps = ['Pastel1', 'Accent', 'Set1', 'tab10']
        colors = []
        for i, name in enumerate(cmaps):
            cmap = plt.colormaps[name]
            colors.append(cmap(np.arange(len(sizes))))

        fig, axs = plt.subplots(2, 2, constrained_layout=True)

        for i, ax in enumerate(axs.flat):
            ax.pie(sizes, labels=labels, autopct='%.1f', startangle=90, colors=colors[i], counterclock=False)
            ax.set_title(cmaps[i])

        fig.suptitle('colors & counterclock in pie')

        plt.show()
    
    def plt_pct(self):
        labels = ['A', 'B', 'C', 'D']
        sizes = [15, 30, 45, 10]

        fig, axs = plt.subplots(2, 2, constrained_layout=True)

        axs[0, 0].pie(sizes, labels=labels, startangle=90)
        axs[0, 1].pie(sizes, labels=labels, startangle=90, autopct='%.1f')
        axs[1, 0].pie(sizes, labels=labels, startangle=90, autopct='autopct', pctdistance=0.1)
        axs[1, 1].pie(sizes, labels=labels, startangle=90, autopct=self.add_ten, pctdistance=0.9)

        axs[0, 0].set_title('autopct=None')
        axs[0, 1].set_title('autopct=fmt')
        axs[1, 0].set_title('autopct=String, pctdistance=0.1')
        axs[1, 1].set_title('autopct=function, pctdistance=0.9')

        fig.suptitle('autopct & pctdistance in pie')

        plt.show()

    def add_ten(self, x):
        return round(x + 10, 1)
    
    def plt_norm(self):
        labels = ['A', 'B', 'C', 'D']
        sizes = [15, 30, 45, 10]

        fig, axs = plt.subplots(2, 2, constrained_layout=True)

        axs[0, 0].pie(sizes, labels=labels, startangle=90, autopct='%.1f')
        axs[0, 1].pie(sizes, labels=labels, startangle=90, autopct='%.1f', normalize=True)
        axs[1, 0].pie(sizes, labels=labels, startangle=90, autopct='%.1f', shadow=True)
        axs[1, 1].pie(sizes, labels=labels, startangle=90, autopct='%.1f', frame=True)

        axs[0, 0].set_title('default')
        axs[0, 1].set_title('normalize')
        axs[1, 0].set_title('shadow')
        axs[1, 1].set_title('frame')

        fig.suptitle('normalize & shadow & frame in pie')

        plt.show()

    def plt_props(self):
        labels = ['A', 'B', 'C', 'D']
        sizes = [15, 30, 45, 10]

        fig, axs = plt.subplots(2, 2, constrained_layout=True)

        axs[0, 0].pie(sizes, labels=labels, startangle=90, autopct='%.1f')
        axs[0, 1].pie(sizes, labels=labels, startangle=90, autopct='%.1f', wedgeprops = {'edgecolor': 'red'})
        axs[1, 0].pie(sizes, labels=labels, startangle=90, autopct='%.1f', textprops={'color': 'white'})
        axs[1, 1].pie(sizes, labels=labels, startangle=90, autopct='%.1f', 
            wedgeprops = {'edgecolor': 'red'}, 
            textprops={'color': 'white', 'fontsize':20}
        )

        axs[0, 0].set_title('default')
        axs[0, 1].set_title('wedgeprops')
        axs[1, 0].set_title('textprops')
        axs[1, 1].set_title('wedge & text')

        fig.suptitle('wedgeprops & textprops in pie')

        plt.show()
    
    def plt_labels(self):
        labels = ['A', 'B', 'C', 'D']
        sizes = [15, 30, 45, 10]

        fig, axs = plt.subplots(2, 2, constrained_layout=True)

        axs[0, 0].pie(sizes, labels=labels, startangle=90, autopct='%.1f')
        axs[0, 1].pie(sizes, labels=labels, startangle=90, autopct='%.1f', labeldistance=1.3)
        axs[1, 0].pie(sizes, labels=labels, startangle=90, autopct='%.1f', rotatelabels=True)
        axs[1, 1].pie(sizes, labels=labels, startangle=90, autopct='%.1f', center=(30, 10))

        axs[0, 0].set_title('default')
        axs[0, 1].set_title('labeldistance=1.3')
        axs[1, 0].set_title('rotatelabels=True')
        axs[1, 1].set_title('center=(30, 10)')

        fig.suptitle('labeldistance & rotatelabels & center in pie')

        plt.show()

if __name__ == '__main__':
    circle_format = CircleFormat()
    # circle_format.plt_pie()
    # circle_format.plt_explode_angle()
    # circle_format.plt_colors()
    # circle_format.plt_pct()
    # circle_format.plt_norm()
    # circle_format.plt_props()
    # circle_format.plt_labels()
    #circle_format.plt_donut()
    circle_format.plt_donuts()
