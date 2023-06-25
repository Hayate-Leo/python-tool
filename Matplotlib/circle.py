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
from thesis_format import ThesisFormat

class CircleFormat(ThesisFormat):
    def __init__(self) -> None:
        super().__init__()

    def plt_pie(self):
        # step1 ラベルとデータの作成
        labels = ['A', 'B', 'C', 'D']
        sizes = [15, 30, 45, 10]
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 円グラフの描画
        ax.pie(sizes, labels=labels, autopct='%.1f%%', startangle=90)

        ax.set_title('Basic pie chart')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        plt.show()
    
    def plt_position(self):
        labels = ['A', 'B', 'C', 'D']
        sizes = [15, 30, 45, 10]
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 円グラフの描画
        # counterclock=False
        # ax.pie(sizes, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False)
        # ax.set_title('counterclock=False')
        # explode = (0, 0.1, 0, 0)
        # ax.pie(sizes, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False, explode=explode)
        # ax.set_title('explode = (0, 0.1, 0, 0)')
        # startangle=0
        ax.pie(sizes, labels=labels, autopct='%.1f%%', startangle=0, counterclock=False)
        ax.set_title('startangle=0')

        plt.show()
    
    
    def plt_pct(self):
        labels = ['A', 'B', 'C', 'D']
        sizes = [15, 30, 45, 10]

        fig, ax = plt.subplots()

        # ax.pie(sizes, labels=labels, startangle=90, autopct='%.1f')
        # ax.set_title(r'autopct=%.1f')

        # ax.pie(sizes, labels=labels, startangle=90, autopct='autopct', pctdistance=0.9)
        # ax.set_title(r'autopct=String, pctdistance=0.9')

        # ax.pie(sizes, labels=labels, startangle=90, autopct=self.add_ten)
        # ax.set_title(r'autopct=function')

        # sizes = [100, 30, 45, 10]
        # ax.pie(sizes, labels=labels, startangle=90, autopct='%.1f%%', normalize=True)
        # ax.set_title(r'normalize=True')

        # ax.pie(sizes, labels=labels, startangle=90, autopct='%.1f', labeldistance=1.3)
        # ax.set_title('labeldistance=1.3')

        ax.pie(sizes, labels=labels, startangle=90, autopct='%.1f', rotatelabels=True)
        ax.set_title('rotatelabels=True')

        plt.show()

    def add_ten(self, x):
        return round(x + 10, 1)

    def plt_colors(self):
        labels = ['A', 'B', 'C', 'D']
        sizes = [15, 30, 45, 10]

        fig, ax = plt.subplots()

        # ax.pie(sizes, labels=labels, autopct='%.1f', startangle=90, colors=['r', 'b', 'g', 'y'], counterclock=False)
        # ax.set_title("colors=['r', 'b', 'g', 'y']")

        # https://matplotlib.org/stable/gallery/color/colormap_reference.html
        cmap = plt.colormaps['viridis']
        colors = cmap((np.linspace(0.4, 0.9, len(sizes))))
        # ax.pie(sizes, labels=labels, autopct='%.1f', startangle=90, colors=colors, counterclock=False)
        # ax.set_title("colors=colormap")
        
        # ax.pie(sizes, labels=labels, startangle=90, autopct='%.1f', colors=colors, counterclock=False, 
        #         wedgeprops = {'edgecolor': 'red', 'linewidth': 3}
        # )
        # ax.set_title('wedgeprops')

        # ax.pie(sizes, labels=labels, startangle=90, autopct='%.1f', colors=colors, counterclock=False, 
        #         textprops={'color': 'white', 'fontsize':20}
        # )
        # ax.set_title('textprops')
        ax.pie(sizes, labels=labels, autopct='%.0f%%', startangle=90, counterclock=False, normalize=True,
            colors=colors,
            wedgeprops = {'edgecolor': 'white', 'linewidth': 1.2}, 
            textprops={'fontsize': 17, 'fontweight': 'bold', 'family': 'Times new roman'}
        )

        ax.set_title('circle plot for a thesis')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        plt.show()


if __name__ == '__main__':
    circle_format = CircleFormat()
    # circle_format.plt_pie()
    # circle_format.plt_position()
    # circle_format.plt_pct()
    # circle_format.plt_norm()
    circle_format.plt_colors()