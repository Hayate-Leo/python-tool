# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_constrained_layout.html#sphx-glr-gallery-subplots-axes-and-figures-demo-constrained-layout-py


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

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

    def plt_line(self):
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)

        fig, axs = plt.subplots(2, 2, constrained_layout=True)

        for ax in axs.flat:
            ax.plot(x, y1, linestyle=self.line_styles[0], label='Sample 1')
            ax.plot(x, y2, linestyle=self.line_styles[1], label='Sample 2')
        
            ax.set_xlabel('Time [$sec$]')
            ax.set_ylabel('Frequency [$Hz$]')

        plt.show()
    
    def plt_grid(self):
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)

        fig = plt.figure(constrained_layout=True)

        gs0 = gridspec.GridSpec(1, 2, figure=fig)

        gs1 = gridspec.GridSpecFromSubplotSpec(3, 1, subplot_spec=gs0[0])
        for n in range(3):
            ax = fig.add_subplot(gs1[n])
            ax.plot(x, y1, color='C'+str(n), label='ax'+str(n+1))
            ax.legend()


        gs2 = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=gs0[1])
        for n in range(2):
            ax = fig.add_subplot(gs2[n])
            ax.scatter(x, y1, color='C'+str(n+3), label='ax'+str(n+4))
            ax.legend()

        # gs = gridspec.GridSpec(3, 3, figure=fig)
        # ax1 = fig.add_subplot(gs[0, :])
        # ax1.plot(x, y1, color='C0', label='ax1')
        # ax1.legend()

        # ax2 = fig.add_subplot(gs[1, :-1])
        # ax2.plot(x, y1, color='C1', label='ax2')
        # ax2.legend()

        # ax3 = fig.add_subplot(gs[1:, -1])
        # ax3.plot(x, y1, color='C2', label='ax3')
        # ax3.legend()

        # ax4 = fig.add_subplot(gs[2, 0])
        # ax4.plot(x, y1, color='C3', label='ax4')
        # ax4.legend()

        # ax5 = fig.add_subplot(gs[2, 1])
        # ax5.plot(x, y1, color='C4', label='ax5')
        # ax5.legend()


        fig.suptitle('GridSpec 1×2')

        plt.show()

if __name__ == '__main__':
    thesis_format = ThesisFormat()
    # thesis_format.plt_line()
    thesis_format.plt_grid()