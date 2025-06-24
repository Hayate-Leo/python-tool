# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_constrained_layout.html#sphx-glr-gallery-subplots-axes-and-figures-demo-constrained-layout-py


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
from thesis_format import ThesisFormat


class LayoutFormat(ThesisFormat):
    def __init__(self) -> None:
        super().__init__()
    

    def plt_line(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, axs = plt.subplots(2, 2, figsize=(8, 6), layout='constrained')
        # step3 グラフの描画
        # axs[0].plot(x, y1)
        # axs[0].plot(x, y2)
        # axs[1].plot(x, y1, color='red')
        # axs[1].plot(x, y2, color='gray')
        # # step4 軸ラベルとタイトルの設定
        # axs[0].set_xlabel('X1 label')
        # axs[0].set_ylabel('Y1 label')
        # axs[0].set_title('Title 1')
        # axs[1].set_xlabel('X2 label')
        # axs[1].set_ylabel('Y2 label')
        # axs[1].set_title('Title 2')

        # 4×4
        # axs[0, 0].plot(x, y1)
        # axs[0, 1].plot(x, y2, color='green')
        # axs[1, 0].plot(x, y1, color='red')
        # axs[1, 1].plot(x, y2, color='gray')
        # # step4 軸ラベルとタイトルの設定
        # axs[0, 0].set_xlabel('X1 label')
        # axs[0, 0].set_ylabel('Y1 label')
        # axs[0, 0].set_title('Title 1')
        # axs[0, 1].set_xlabel('X2 label')
        # axs[0, 1].set_ylabel('Y2 label')
        # axs[0, 1].set_title('Title 2')        
        # axs[1, 0].set_xlabel('X3 label')
        # axs[1, 0].set_ylabel('Y3 label')
        # axs[1, 0].set_title('Title 3')        
        # axs[1, 1].set_xlabel('X4 label')
        # axs[1, 1].set_ylabel('Y4 label')
        # axs[1, 1].set_title('Title 4')
        for i, ax in enumerate(axs.flat):
            ax.plot(x, y1, color='C'+str(2*i), label='ax'+str(2*i+1))
            ax.plot(x, y2, color='C'+str(2*i+1), label='ax'+str(2*i+2))

            ax.set_xlabel('X'+str(i+1)+' label')
            ax.set_ylabel('Y'+str(i+1)+' label')
            ax.set_title('Title '+str(i+1))
            # ax.legend()
        fig.legend()
        # step5 Figureの呼び出し
        plt.show()
    
    def plt_grid(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig = plt.figure(constrained_layout=True)
        gs0 = gridspec.GridSpec(1, 2, figure=fig)

        # step3 グラフの描画
        gs1 = gridspec.GridSpecFromSubplotSpec(3, 1, subplot_spec=gs0[0])
        for n in range(3):
            ax = fig.add_subplot(gs1[n])
            ax.plot(x, y1, color='C'+str(n), label='ax'+str(n+1))
            # ax.legend()

        gs2 = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=gs0[1])
        for n in range(2):
            ax = fig.add_subplot(gs2[n])
            ax.scatter(x, y1, color='C'+str(n+3), label='ax'+str(n+4))
            # ax.legend()

        # gs = gridspec.GridSpec(3, 3, figure=fig)
        # step3 グラフの描画
        # ax1 = fig.add_subplot(gs[0, :])
        # ax1.plot(x, y1, color='C0', label='ax1')

        # ax2 = fig.add_subplot(gs[1, :-1])
        # ax2.plot(x, y1, color='C1', label='ax2')

        # ax3 = fig.add_subplot(gs[1:, -1])
        # ax3.plot(x, y1, color='C2', label='ax3')

        # ax4 = fig.add_subplot(gs[2, 0])
        # ax4.plot(x, y1, color='C3', label='ax4')

        # ax5 = fig.add_subplot(gs[2, 1])
        # ax5.plot(x, y1, color='C4', label='ax5')

        # step4 タイトルの設定
        fig.suptitle('GridSpec 1×2 with GridSpecFromSubplotSpec')
        fig.legend()

        # step5 Figureの呼び出し
        plt.show()


if __name__ == '__main__':
    layout_format = LayoutFormat()
    layout_format.plt_line()
    # layout_format.plt_grid()