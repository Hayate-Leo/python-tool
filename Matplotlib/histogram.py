# https://matplotlib.org/stable/gallery/statistics/hist.html
# https://matplotlib.org/stable/gallery/statistics/histogram_histtypes.html
# https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

class HistoGram:
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
        plt.rcParams['mathtext.fontset'] = 'dejavuserif'
        self.line_styles = ['-', '--', '-.', ':']
        self.markers = ['o', ',', '.', 'v', '^', '<', '>', '1', '2', '3', '.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3']
    
    def plt_simple(self):
        # 再現性のある乱数発生器の作成
        rng = np.random.default_rng(19680801)

        N_points = 100000
        n_bins = 20

        # 正規分布を生成する
        dist1 = rng.standard_normal(N_points)

        fig, ax = plt.subplots()

        # キーワード引数 *bins* でビンの数を設定
        ax.hist(dist1, bins=n_bins)
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title(r'A Simple Histogram')
        plt.show()
    
    def plt_patch(self):
        # 再現性のある乱数発生器の作成
        rng = np.random.default_rng(19680801)

        N_points = 100000
        n_bins = 20

        # 正規分布を生成する
        dist1 = rng.standard_normal(N_points)

        fig, ax = plt.subplots()

        # Nは各ビン数，binsはビンの下限値
        N, bins, patches = ax.hist(dist1, bins=n_bins)

        # ここでは高さで色分けしているが，任意のスカラー値を使用することも可能
        fracs = N / N.max()

        # カラーマップの全範囲でデータを0〜1に正規化する必要があります
        norm = colors.Normalize(fracs.min(), fracs.max())
        # オブジェクトをループして，それぞれの色を設定
        for thisfrac, thispatch in zip(fracs, patches):
            print(norm(thisfrac))
            color = plt.cm.viridis(norm(thisfrac))
            thispatch.set_facecolor(color)

        plt.show()
        

    def plt_percentage(self):
        # 再現性のある乱数発生器の作成
        rng = np.random.default_rng(19680801)

        N_points = 100000
        n_bins = 20

        # 正規分布を生成する
        dist1 = rng.standard_normal(N_points)

        fig, ax = plt.subplots()

        # カウントの総数で入力を正規化することも可能
        ax.hist(dist1, bins=n_bins, density=True)

        # Y軸をパーセンテージ表示にフォーマット
        ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))

        plt.show()
    
    def plt_2d(self):
        # 再現性のある乱数発生器の作成
        rng = np.random.default_rng(19680801)

        N_points = 100000

        # 正規分布を生成する
        dist1 = rng.standard_normal(N_points)
        dist2 = 0.4 * rng.standard_normal(N_points) + 5

        fig, ax = plt.subplots()
        ax.hist2d(dist1, dist2)

        plt.show()
    
    def plt_types(self):
        np.random.seed(19680801)

        mu_x = 200
        sigma_x = 25
        x = np.random.normal(mu_x, sigma_x, size=100)

        fig, axs = plt.subplots(nrows=1, ncols=2)

        axs[0].hist(x, 20, density=True, histtype='stepfilled', facecolor='g',
                    alpha=0.75)
        axs[0].set_title('stepfilled')

        axs[1].hist(x, 20, density=True, histtype='step', facecolor='g',
                    alpha=0.75)
        axs[1].set_title('step')

        fig.tight_layout()
        plt.show()
    
    def plt_datasets(self):
        np.random.seed(19680801)

        n_bins = 10
        x = np.random.randn(1000, 3)

        fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)

        colors = ['red', 'tan', 'lime']
        ax0.hist(x, n_bins, density=True, histtype='bar', color=colors, label=colors)
        ax0.legend(prop={'size': 10})
        ax0.set_title('bars with legend')

        ax1.hist(x, n_bins, density=True, histtype='bar', stacked=True)
        ax1.set_title('stacked bar')

        ax2.hist(x, n_bins, histtype='step', stacked=True, fill=False)
        ax2.set_title('stack step (unfilled)')

        # 長さの異なるデータセットのヒストグラムを作成
        x_multi = [np.random.randn(n) for n in [10000, 5000, 2000]]
        ax3.hist(x_multi, n_bins, histtype='bar')
        ax3.set_title('different sample sizes')

        fig.tight_layout()
        plt.show()


if __name__ == '__main__':
    histogarm = HistoGram()
    # histogarm.plt_simple()
    # histogarm.plt_patch()
    # histogarm.plt_percentage()
    # histogarm.plt_2d()
    histogarm.plt_types()
    # histogarm.plt_datasets()
