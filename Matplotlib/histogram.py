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
    
    def plt_simple(self):
        # step1 再現性のある乱数発生器を作成
        rng = np.random.default_rng(19680801)

        # step2 データの作成
        N_points = 100000
        n_bins = 20
        dist1 = rng.standard_normal(N_points)

        # step3 グラフフレームを作成
        fig, ax = plt.subplots()

        # step4 ヒストグラムを描画
        ax.hist(dist1, bins=n_bins)
        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.set_title(r'A Simple Histogram')
        plt.show()
    
    def plt_patch(self):
        # step1 再現性のある乱数発生器を作成
        rng = np.random.default_rng(19680801)
        # step2 データの作成
        N_points = 100000
        n_bins = 20
        dist1 = rng.standard_normal(N_points)
        # step3 グラフフレームを作成
        fig, ax = plt.subplots()

        # step4 ヒストグラムを描画
        # Nは各ビン数，binsはビンの下限値
        N, bins, patches = ax.hist(dist1, bins=n_bins)

        # step5 色設定のための準備
        # 高さで色分け
        fracs = N / N.max()
        # カラーマップの全範囲でデータを0〜1に正規化
        norm = colors.Normalize(fracs.min(), fracs.max())

        # step6 オブジェクトをループして，それぞれの色を設定
        for thisfrac, thispatch in zip(fracs, patches):
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
        # 再現性のある乱数発生器の作成
        rng = np.random.default_rng(19680801)

        N_points = 100000
        n_bins = 20

        # 正規分布を生成する
        dist1 = rng.standard_normal(N_points)

        fig, ax = plt.subplots()

        ax.hist(dist1, bins=n_bins, histtype='step')
        ax.set_title('histtype=step')

        plt.show()
    
    def plt_datasets(self):
        # 再現性のある乱数発生器の作成
        rng = np.random.default_rng(19680801)

        N_points = 100000
        n_bins = 20

        # 正規分布を生成する
        dist1 = rng.standard_normal(size=(N_points, 3))

        fig, ax = plt.subplots()

        # ax.hist(dist1, bins=n_bins, histtype='barstacked')
        # ax.set_title('multiple datasets by barstacked')
        # ax.hist(dist1, bins=n_bins)
        # ax.set_title('multiple datasets by bar')
        ax.hist(dist1, bins=n_bins, histtype='step', stacked=True)
        ax.set_title('multiple datasets by step')

        plt.show()


if __name__ == '__main__':
    histogarm = HistoGram()
    # histogarm.plt_simple()
    # histogarm.plt_patch()
    # histogarm.plt_percentage()
    # histogarm.plt_2d()
    # histogarm.plt_types()
    histogarm.plt_datasets()
