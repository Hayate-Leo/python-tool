# https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_demo.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_betweenx_demo.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html


import matplotlib.pyplot as plt
import numpy as np


class FillArea:
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
    
    def plt_line(self):
        x = np.linspace(0, 10, 100)
        y1 = 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.sin(2 * x)

        fig, axs = plt.subplots(2, 2, sharex=True, constrained_layout=True)

        axs[0, 0].plot(x, y1)
        axs[0, 0].plot(x, y2)
        axs[0, 1].fill_between(x, y1)
        axs[1, 0].fill_between(x, y1, 1)
        axs[1, 1].fill_between(x, y1, y2)

        axs[0, 0].set_title(r'plot y1 and y2')
        axs[0, 1].set_title(r'fill between y1 and 0')
        axs[1, 0].set_title(r'fill between y1 and 1')
        axs[1, 1].set_title(r'fill between y1 and y2')

        for ax in axs.flat:
            ax.set_xlabel(r'Time [$sec$]')
            ax.set_ylabel(r'Frequency [$Hz$]')
        
        fig.suptitle(r'Plot vs Fill Between, $y1 = 2sin(2x) | y2 = y1+4$')
        plt.show()
    
    def plt_bands(self):
        x = np.linspace(0, 10, 11)
        y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1,  9.9, 13.9, 15.1, 12.5]

        # 一次曲線にフィットし，のy値とその誤差を推定する
        a, b = np.polyfit(x, y, deg=1)
        y_est = a * x + b
        y_err = x.std() * np.sqrt(1/len(x) +
                                (x - x.mean())**2 / np.sum((x - x.mean())**2))

        fig, ax = plt.subplots()
        # 予測線
        ax.plot(x, y_est)
        # 予測線の信頼区間
        ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
        # 実際のデータ
        ax.scatter(x, y)

        fig.suptitle(r'Confidence bands')
        plt.show()
    
    def plt_where(self):
        x = np.linspace(0, 10, 100)
        y1 = 2 * np.sin(2 * x)
        y2 = 2 * np.cos(2 * x)
        fig, axs = plt.subplots(2, 2, sharex=True, constrained_layout=True)

        axs[0, 0].plot(x, y1)
        axs[0, 0].plot(x, y2)
        axs[0, 1].fill_between(x, y1, y2, where=y2 >= y1, facecolor='C0')
        axs[0, 1].fill_between(x, y1, y2, where=y2 <= y1, facecolor='C1')
        axs[1, 0].fill_between(x, y1, y2, where=y2 >= y1, facecolor='C0')
        axs[1, 1].fill_between(x, y1, y2, where=y2 <= y1, facecolor='C1')

        axs[0, 0].set_title(r'plot y1 and y2')
        axs[0, 1].set_title(r'fill between y1 and y2')
        axs[1, 0].set_title(r'where = y2 >= y1')
        axs[1, 1].set_title(r'where = y2 <= y1')
        
        fig.suptitle(r'How to use where of Fill Between, $y1 = 2sin(2x) | y2 = 2cos(2x)$')
        plt.show()
    
    def plt_interpolation(self):
        x = np.array([0, 1, 2, 3])
        y1 = np.array([0.8, 0.8, 0.2, 0.2])
        y2 = np.array([0, 0, 1, 1])

        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, constrained_layout=True)

        ax1.set_title('interpolation=False')
        ax1.plot(x, y1, 'o--')
        ax1.plot(x, y2, 'o--')
        ax1.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3)
        ax1.fill_between(x, y1, y2, where=(y1 < y2), color='C1', alpha=0.3)

        ax2.set_title('interpolation=True')
        ax2.plot(x, y1, 'o--')
        ax2.plot(x, y2, 'o--')
        ax2.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3,
                        interpolate=True)
        ax2.fill_between(x, y1, y2, where=(y1 <= y2), color='C1', alpha=0.3,
                        interpolate=True)
        plt.show()
    
    def plt_xline(self):
        y = np.linspace(0, 10, 100)
        x1 = 2 * np.sin(2 * y)
        x2 = 4 + 2 * np.sin(2 * y)

        fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, constrained_layout=True)

        ax1.plot(x1, y)
        ax1.plot(x2, y)
        ax2.fill_betweenx(y, x1, x2)

        ax1.set_title(r'plot x1 and x2')
        ax2.set_title(r'fill between X x1 and x2')
        
        fig.suptitle(r'Plot vs Fill Between X, $x1 = 2sin(2y) | x2 = x1+4$')
        plt.show()

if __name__ == '__main__':
    fill_area = FillArea()
    # fill_area.plt_line()
    # fill_area.plt_bands()
    # fill_area.plt_where()
    # fill_area.plt_interpolation()
    fill_area.plt_xline()