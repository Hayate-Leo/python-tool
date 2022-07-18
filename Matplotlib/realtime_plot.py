# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html
# https://matplotlib.org/3.2.2/api/_as_gen/matplotlib.axes.Axes.remove.html

import numpy as np
import matplotlib.pyplot as plt


class RealTime:
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
        xs = []
        y1 = []
        y2 = []
        fig, ax = plt.subplots()

        for x in np.linspace(0, 10, 100):
            xs.append(x)
            y1.append(4 + 2 * np.sin(2 * x))
            y2.append(4 + 2 * np.cos(2 * x))

            line1, = ax.plot(xs, y1, linestyle=self.line_styles[0], label='Sample1')
            line2, = ax.plot(xs, y2, linestyle=self.line_styles[1], label='Sample2')

            
            ax.set_xlim(0, 8)
            ax.set_ylim(0, 8)
            ax.set_xlabel('Time [$sec$]')
            ax.set_ylabel('Frequency [$Hz$]')
            ax.legend()

            plt.pause(0.001)
            line1.remove()
            line2.remove()


if __name__ == '__main__':
    real_time = RealTime()
    real_time.plt_line()