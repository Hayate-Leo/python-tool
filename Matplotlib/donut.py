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

class DonutFormat(ThesisFormat):
    def __init__(self) -> None:
        super().__init__()
    
    def plt_donut(self):
        # step1 ラベルとデータの作成
        labels = ['A', 'B', 'C', 'D']
        width = 0.3
        vals = np.array([[60, 32], [40, 35], [29, 10], [18, 5]])
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 ドーナツグラフの描画
        ax.pie(vals.sum(axis=1), labels=labels, startangle=90, counterclock=False,
            autopct='%.1f%%', 
            pctdistance=0.85, 
            wedgeprops={'width':width}
        )

        ax.set_title('Basic donut chart')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        plt.show()

    def plt_tab20c(self):
        # step1 ラベルとデータの作成
        labels = ['A', 'B', 'C', 'D']
        width = 0.3
        vals = np.array([[60, 32], [40, 35], [29, 10], [18, 5]])
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 カラーマップの作成
        cmap = plt.colormaps['tab20c']
        outer_colors = cmap(np.arange(vals.shape[0])*4)
        inner_colors = cmap([i*4+j+1 for i, vs in enumerate(vals) for j in range(vs.size)])

        # step4 外側のドーナツグラフの描画
        ax.pie(vals.sum(axis=1), radius=1, startangle=90, counterclock=False,
            labels=labels,
            autopct='%.0f%%', 
            pctdistance=1.15-width, 
            wedgeprops={'width':width, 'edgecolor':'white'},
            colors=outer_colors)
        
        # step5 内側ドーナツグラフの描画
        ax.pie(vals.flatten(), radius=1-width, startangle=90, counterclock=False,
            autopct='%.0f%%', 
            pctdistance=1.1-width, 
            wedgeprops={'width':width, 'edgecolor':'white'},
            colors=inner_colors)

        ax.set_title('tab20c in double donut chart')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
        plt.show()
 

if __name__ == '__main__':
    donut_format = DonutFormat()
    # donut_format.plt_donut()
    donut_format.plt_tab20c()