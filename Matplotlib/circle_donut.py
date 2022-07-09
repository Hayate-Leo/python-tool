# 基本的な円グラフ
# https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
# pie demo 2
# https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_demo2.html
# Nested pie
# https://matplotlib.org/stable/gallery/pie_and_polar_charts/nested_pie.html


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
        plt.rcParams['errorbar.capsize'] = 6
        plt.rcParams['lines.markersize'] = 7
        self.line_styles = ['-', '--', '-.', ':']
        self.markers = ['o', ',', '.', 'v', '^', '<', '>', '1', '2', '3', '.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3']

    def plt_pie(self):
        labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
        sizes = [15, 30, 45, 10]
        explode = (0, 0.1, 0, 0)

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, explode=explode)

        plt.show()
    
    def plt_donut(self):
        fig, ax = plt.subplots()

        size = 0.3
        vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

        cmap = plt.colormaps['tab20c']

        outer_colors = cmap(np.arange(3)*4)
        inner_colors = cmap([1, 2, 5, 6, 9, 10])

        ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors, startangle=90,
            wedgeprops=dict(width=size, edgecolor='w'))

        ax.pie(vals.flatten(), radius=1-size, colors=inner_colors, startangle=90,
            wedgeprops=dict(width=size, edgecolor='w'))

        plt.show()
        print(vals.sum(axis=1))

if __name__ == '__main__':
    thesis_format = ThesisFormat()
    # thesis_format.plt_pie()
    thesis_format.plt_donut()
