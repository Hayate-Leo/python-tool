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
    
    def plt_donut_basic(self):
        # step1 データの作成
        width = 0.3
        vals = [40, 60]
        # step1.1 カラーマップの作成
        cmap = plt.get_cmap('Blues')
        colors = cmap(np.linspace(0.2, 0.7, len(vals)))
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 ドーナツグラフの描画
        ax.pie(vals, startangle=90,
                # ドーナツの幅
                wedgeprops={'width':width},
                # カラー
                colors=colors
        )
        ax.set_title('Donut chart')
        plt.show()

    def plt_donut_text(self):
        # step1 データの作成
        width = 0.3
        vals = [40, 60]
        # step1.1 カラーマップの作成
        cmap = plt.get_cmap('Blues')
        colors = cmap(np.linspace(0.2, 0.7, len(vals)))
        color_text = cmap(0.7)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 ドーナツグラフの描画
        ax.pie(vals, startangle=90, 
               wedgeprops={'width':width},
               colors=colors
        )
        # step4 テキストの追加
        # ax.text(0, 0, r'60%'+'\nDonut Chart', fontsize=20)
        # ax.text(0, 0, r'60%'+'\nDonut Chart', color='black', fontsize=20, 
        #         horizontalalignment='center', 
        #         verticalalignment='center'
        #         )
        ax.text(0, 0, r'60%', color=color_text, fontsize=32, fontweight='medium',
                horizontalalignment='center', verticalalignment='bottom')
        ax.text(0, 0, r'Donut Chart', color=color_text, fontsize=20, 
                horizontalalignment='center', verticalalignment='top')

        plt.show()

    def plt_donut_legend(self):
        # step1 データの作成
        labels = ['A', 'B', 'C', 'D']
        width = 0.3
        vals = np.array([[60, 32], [40, 35], [29, 10], [18, 5]])
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 ドーナツグラフの描画
        ax.pie(vals.sum(axis=1), labels=labels, 
                startangle=90, counterclock=False,
                wedgeprops={'width':width}
        )

        ax.set_title('Donut chart with a legend')
        # 凡例
        ax.legend(loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        plt.show()
    
    def plt_donut_label(self):
        # step1 データの作成
        labels = ['A', 'B', 'C', 'D']
        width = 0.3
        vals = np.array([[60, 32], [40, 35], [29, 10], [18, 5]])
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 ドーナツグラフの描画
        ax.pie(vals.sum(axis=1), labels=labels, startangle=90, counterclock=False,
                wedgeprops={'width':width},
                # 数値%ラベルの表記
                autopct='%.1f%%', 
                # 数値%ラベルの位置
                pctdistance=0.85,
        )

        ax.set_title('Donut chart with labels')
        # 凡例
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
        print(vals.shape[0])


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
    
    def plt_cmap(self):
        gradient = np.linspace(0, 1, 256)
        gradient = np.vstack((gradient, gradient))
        nrows = len(gradient)
        figh = 0.35 + 0.15 + (nrows + (nrows-1)*0.1)*0.22
        fig, ax = plt.subplots(figsize=(6.4, figh))
        cmap_name = 'tab20c'
        ax.imshow(gradient, aspect='auto', cmap=cmap_name)
        ax.text(-.01, .5, cmap_name, va='center', ha='right', fontsize=20,
                transform=ax.transAxes)
        ax.set_axis_off()
        plt.show()
 

if __name__ == '__main__':
    donut_format = DonutFormat()
    # donut_format.plt_donut_basic()
    # donut_format.plt_donut_text()
    # donut_format.plt_donut_legend()
    # donut_format.plt_donut_label()
    donut_format.plt_tab20c()
    # donut_format.plt_cmap()