# https://matplotlib.org/stable/gallery/lines_bars_and_markers/vline_hline_demo.html
# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axhspan_demo.html

import matplotlib.pyplot as plt
import numpy as np

class HVLines:
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
        plt.rcParams['mathtext.fontset'] = 'cm'
        self.line_styles = ['-', '--', '-.', ':']
        self.markers = ['o', ',', '.', 'v', '^', '<', '>', '1', '2', '3', '.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3']
    
    def plt_hlines(self):
        t = np.arange(0.0, 5.0, 0.1)
        s = np.exp(-t) + np.sin(2 * np.pi * t) + 1

        fig, ax = plt.subplots()

        ax.plot(s, t, '^')
        ax.hlines(t, 0, s, lw=2)

        ax.set_xlabel('time (s)')
        ax.set_title('Horizontal lines demo')

        plt.show()
    
    def plt_vlines(self):
        t = np.arange(0.0, 5.0, 0.1)
        s = np.exp(-t) + np.sin(2 * np.pi * t) + 1

        fig, ax = plt.subplots()

        ax.plot(t, s, '^')
        ax.vlines(t, 0, s, lw=2)

        ax.set_xlabel('time (s)')
        ax.set_title('Vertical lines demo')

        plt.show()
    
    def plt_axlines(self):
        fig, axs = plt.subplots(2, 2, constrained_layout=True)

        threshold = 0.75
        axs[0, 0].axhline(threshold, color='C0', lw=2)
        axs[0, 1].axvline(threshold, color='C1', lw=2)
        axs[1, 0].axline((0, 0), (4, 8), color='C2', lw=2)
        axs[1, 1].axline((0, 0), slope=0.5, color='C2', lw=2)

        axs[0, 0].set_title('Axhline')
        axs[0, 1].set_title('Axvline')
        axs[1, 0].set_title(r'Axline $(0, 0) (4, 8)$')
        axs[1, 1].set_title(r'Axline $y=0.5x$')

        for ax in axs.flat:
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)

        plt.show()
    
    def plt_axspan(self):
        fig, axs = plt.subplots(1, 2, constrained_layout=True)

        min_value = 5
        max_value = 8
        axs[0].axhspan(min_value, max_value, color='C0', alpha=0.7)
        axs[1].axvspan(min_value, max_value, color='C1', alpha=0.7)

        axs[0].set_title('Axhspan')
        axs[1].set_title('Axvspan')

        for ax in axs.flat:
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 10)

        plt.show()

if __name__ == '__main__':
    h_v_lines = HVLines()
    # h_v_lines.plt_hlines()
    h_v_lines.plt_vlines()
    # h_v_lines.plt_axlines()
    # h_v_lines.plt_axspan()
    
