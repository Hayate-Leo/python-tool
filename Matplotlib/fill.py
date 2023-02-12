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
        # グラフのフォーマット整形
        plt.rcParams['figure.autolayout'] = True
        plt.rcParams['figure.figsize'] = [6.4, 4.8]
        plt.rcParams['font.family'] ='Times New Roman'
        plt.rcParams['font.size'] = 12
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        plt.rcParams['axes.linewidth'] = 1.0
        plt.rcParams['errorbar.capsize'] = 6
        plt.rcParams['lines.markersize'] = 6
        plt.rcParams['lines.markerfacecolor'] = 'white'
        plt.rcParams['mathtext.fontset'] = 'cm'
        self.line_styles = ['-', '--', '-.', ':']
        self.markers = ['o', 's', '^', 'D', 'v', '<', '>', '1', '2', '3']
    
    def plt_line(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.sin(2 * x)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 グラフの描画
        # ax.plot(x, y1, label=r'$y1 = 2sin(2x)$')
        # ax.plot(x, y2, label=r'$y2 = y1+4$')
        # ax.fill_between(x, y1, label=r'$y1 = 2sin(2x)$')
        # ax.fill_between(x, y1, 1, label=r'$y1 = 2sin(2x)$')
        ax.fill_between(x, y1, y2, label=r'$y1 = 2sin(2x), y2 = y1+4$')

        # ax.set_title(r'plot y1, y2')
        # ax.set_title(r'fill between y1 and 0')
        # ax.set_title(r'fill between y1 and 1')
        ax.set_title(r'fill between y1 and y2')

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_ylim(-3, 8)
        ax.legend()

        plt.show()
    
    def plt_bands(self):
        # step1 データの作成
        x = np.linspace(0, 10, 11)
        y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1,  9.9, 13.9, 15.1, 12.5]

        # step2 予測線と誤差範囲の推定
        a, b = np.polyfit(x, y, deg=1)
        y_est = a * x + b
        y_err = x.std() * np.sqrt(1/len(x) +
                                (x - x.mean())**2 / np.sum((x - x.mean())**2))
        # step3 グラフフレームの作成
        fig, ax = plt.subplots()
        # step4 グラフの描画
        # 予測線
        ax.plot(x, y_est)
        # 予測線の信頼区間
        ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
        # 実際のデータ
        ax.scatter(x, y)

        ax.set_title(r'Confidence bands')
        plt.show()
    
    def plt_where(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        y1 = 2 * np.sin(2 * x)
        y2 = 2 * np.cos(2 * x)
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 グラフの描画
        ax.plot(x, y1, '--')
        ax.plot(x, y2, '--')
        # ax.fill_between(x, y1, y2, where=y2 >= y1)
        # ax.fill_between(x, y1, y2, where=y2 <= y1)
        ax.fill_between(x, y1, y2, where=y2 >= y1, color='C0')
        ax.fill_between(x, y1, y2, where=y2 <= y1, color='C1')

        # ax.set_title(r'plot y1 and y2')
        # ax.set_title(r'where = y2 >= y1')
        # ax.set_title(r'where = y2 <= y1')
        ax.set_title(r'fill between y1 and y2')
        
        plt.show()
    
    def plt_interpolation(self):
        # step1 データの作成
        x = np.array([0, 1, 2, 3])
        y1 = np.array([0.8, 0.8, 0.2, 0.2])
        y2 = np.array([0, 0, 1, 1])
        # step2 グラフフレームの作成   
        fig, ax = plt.subplots()
        # step3 グラフの描画
        ax.plot(x, y1, 'o--')
        ax.plot(x, y2, 'o--')
        ax.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3,
                        interpolate=True)
        ax.fill_between(x, y1, y2, where=(y1 <= y2), color='C1', alpha=0.3,
                        interpolate=True)

        ax.set_title('interpolation=True')
        plt.show()
    
    def plt_xline(self):
        # step1 データの作成
        y = np.linspace(0, 10, 100)
        x1 = 2 * np.sin(2 * y)
        x2 = 4 + 2 * np.sin(2 * y)

        # step2 グラフフレームの作成   
        fig, ax = plt.subplots()

        # step3 グラフの描画
        ax.plot(x1, y, '--', label=r'$x1 = 2sin(2y)$')
        ax.plot(x2, y, '--', label=r'$x1 = x2+4$')
        ax.fill_betweenx(y, x1, x2, alpha=0.5)

        # ax.set_title(r'plot x1 and x2')
        ax.set_title(r'fill between X x1 and x2')
        ax.set_xlim(-3, 10)
        ax.legend()
        plt.show()

if __name__ == '__main__':
    fill_area = FillArea()
    # fill_area.plt_line()
    # fill_area.plt_bands()
    # fill_area.plt_where()
    # fill_area.plt_interpolation()
    fill_area.plt_xline()