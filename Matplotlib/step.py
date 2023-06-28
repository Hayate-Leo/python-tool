import matplotlib.pyplot as plt
import numpy as np
from thesis_format import ThesisFormat


class StepFormat(ThesisFormat):
    def __init__(self) -> None:
        super().__init__()
    
    def plt_simple(self):
        # step1 データの作成
        x = np.arange(10)
        y = np.sin(x)

        # step2 グラフフレームの作成
        fig, ax = plt.subplots()

        # step3 階段グラフの描画
        ax.step(x, y, label='Sample 1')
        ax.step(x, y+2, label='Sample 2')

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')  
        ax.legend()
        ax.set_title('Step Line Chart')

        plt.show()

    def plt_fmt(self):
        # step1 データの作成
        x = np.arange(10)
        y = np.sin(x)

        # step2 グラフフレームの作成
        fig, ax = plt.subplots()

        # step3 階段グラフの描画
        # ax.step(x, y, 'og--' ,label='fmt="og--"')
        # ax.step(x, y+2, 'sr-.' ,label='fmt="sr-."')
        # ax.step(x, y+4, '*c:' ,label='fmt="*c:"')

        # マーカー
        # ax.step(x, y, 'o-' ,label='circle')
        # ax.step(x, y+2, 's-' ,label='square')
        # ax.step(x, y+4, '^-' ,label='triangle_up')

        # 線種
        # ax.step(x, y, '-' ,label='solid')
        # ax.step(x, y+2, '--' ,label='dashed')
        # ax.step(x, y+4, '-.' ,label='dash-dot')
        # ax.step(x, y+6, ':' ,label='dotted')
    
        # 色
        ax.step(x, y, 'm' ,label='Magenta')
        ax.step(x, y+2, '#0097a7' ,label='#0097a7')
        ax.step(x, y+4, 'tomato' ,label='tomato')

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')  
        ax.legend()
        ax.set_title('Step Line Chart')

        plt.show()

    def plt_where(self):
        # step1 データの作成
        x = np.arange(10)
        y = np.sin(x)

        # step2 グラフフレームの作成
        fig, ax = plt.subplots()

        # step3 階段グラフの描画
        ax.step(x, y, where='pre', label='pre (default)')
        ax.plot(x, y, 'o--', color='grey', alpha=0.4)
        ax.step(x, y+2, where='mid',label='mid')
        ax.plot(x, y+2, 'o--', color='grey', alpha=0.4)
        ax.step(x, y+4, where='post', label='post')
        ax.plot(x, y+4, 'o--', color='grey', alpha=0.4)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')  
        ax.legend()
        ax.set_title('Step Line Chart')

        plt.show()

if __name__ == '__main__':
    step_plt = StepFormat()
    # step_plt.plt_simple()
    step_plt.plt_fmt()
    # step_plt.plt_where()