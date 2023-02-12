# https://matplotlib.org/stable/gallery/spines/multiple_yaxis_with_spines.html

import matplotlib.pyplot as plt
from thesis_format import ThesisFormat


class MultiFormat(ThesisFormat):
    def __init__(self) -> None:
        super().__init__()

    def plt_line(self):
        # step1 グラフフレームの作成
        fig, ax = plt.subplots()
        fig.subplots_adjust(right=0.75)
        # step2 y軸の作成
        twin1 = ax.twinx()
        twin2 = ax.twinx()

        # twin2を右方向に動かします
        twin2.spines['right'].set_position(('axes', 1.2))
        # step3 折れ線グラフの描画
        p1, = ax.plot([0, 1, 2], [0, 1, 2], 'C0', label='Y1')
        p2, = twin1.plot([0, 1, 2], [0, 3, 2], 'C1', label='Y2')
        p3, = twin2.plot([0, 1, 2], [50, 30, 15], 'C2', label='Y3')

        ax.set_xlabel('X label')
        ax.set_ylabel('Y1')
        twin1.set_ylabel('Y2')
        twin2.set_ylabel('Y3')

        # ax.yaxis.label.set_color(p1.get_color())
        # twin1.yaxis.label.set_color(p2.get_color())
        # twin2.yaxis.label.set_color(p3.get_color())

        ax.tick_params(axis='y', colors=p1.get_color())
        twin1.tick_params(axis='y', colors=p2.get_color())
        twin2.tick_params(axis='y', colors=p3.get_color())

        ax.set_title('line graph with 3 y-axes')
        # step4 凡例の追加
        ax.legend(handles=[p1, p2, p3], loc='center left')

        plt.show()
    
    def plt_scatter(self):
        # step1 グラフフレームの作成
        fig, ax = plt.subplots()
        # fig.subplots_adjust(right=0.75)
        # step2 y軸の作成
        twin1 = ax.twinx()
        # twin2 = ax.twinx()

        # twin2を右方向に動かします
        # twin2.spines['right'].set_position(('axes', 1.2))
        # step3 散布図の描画
        p1 = ax.scatter([0, 0.4, 0.8, 1, 1.3, 1.8, 2], [0, 8, 2, 1, 21, 14, 22], c='C0', label='Y1')
        p2 = twin1.scatter([0, 0.7, 0.9, 1, 1.2, 1.5, 2], [0, 34, 23, 23, 12, 8, 16], c='C1', label='Y2')
        # p3 = twin2.scatter([0, 0.6, 0.8, 1, 1.4, 1.8, 2], [22, 50, 23, 24, 95, 30, 15], c='C2', label='Y3')

        ax.set_xlabel('X label')
        ax.set_ylabel('Y1')
        twin1.set_ylabel('Y2')
        # twin2.set_ylabel('Y3')

        ax.set_title('scatter graph with 2 y-axes')
        ax.legend(handles=[p1, p2])

        plt.show()

if __name__ == '__main__':
    multi_format = MultiFormat()
    multi_format.plt_line()
    # multi_format.plt_scatter()