# https://matplotlib.org/stable/gallery/lines_bars_and_markers/vline_hline_demo.html
# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axhspan_demo.html

import matplotlib.pyplot as plt
import numpy as np
from thesis_format import ThesisFormat


class HVLines(ThesisFormat):
    def __init__(self) -> None:
        super().__init__()
    
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
        # step1 グラフフレームの作成
        fig, ax = plt.subplots()
        # step2 Axes.axhlineとAxes.axvlineによる直線の表示
        threshold = 0.75
        # ax.axhline(threshold, color='C0', lw=2)
        # ax.set_title('Axhline')

        # ax.axvline(threshold, color='C1', lw=2)
        # ax.set_title('Axvline')
        
        # ax.axline((0, 0), (4, 8), color='red', lw=2)
        # ax.set_title(r'Axline $(0, 0) (4, 8)$')

        ax.axline((0, 0), slope=0.5, color='#0097a7', lw=2)
        ax.set_title(r'Axline $y=0.5x$')

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xlabel('Xlabel')
        ax.set_ylabel('Ylabel')

        plt.show()
    
    def plt_axspan(self):
        # step1 データの作成
        min_value = 5
        max_value = 8
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 Axes.hspanによる水平帯線の表示
        # ax.axhspan(min_value, max_value, color='C0', alpha=0.7)
        # ax.set_title('Axhspan')
        # step3 Axes.vspanによる垂直帯線の表示
        ax.axvspan(min_value, max_value, color='C1', alpha=0.7)
        ax.set_title('Axvspan')

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_xlabel('Xlabel')
        ax.set_ylabel('Ylabel')

        plt.show()

if __name__ == '__main__':
    h_v_lines = HVLines()
    # h_v_lines.plt_hlines()
    # h_v_lines.plt_vlines()
    # h_v_lines.plt_axlines()
    h_v_lines.plt_axspan()
    
