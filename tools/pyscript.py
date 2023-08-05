import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plt_style():
    # step1 グラフのフォーマット
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.figsize'] = [6.4, 4.8]
    plt.rcParams['font.family'] ='serif'
    plt.rcParams['font.size'] = 12
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['axes.linewidth'] = 1.0
    plt.rcParams['errorbar.capsize'] = 6
    plt.rcParams['lines.markersize'] = 6
    plt.rcParams['lines.markerfacecolor'] = 'white'
    plt.rcParams['mathtext.fontset'] = 'cm'

def data():
    # step2 データの作成
    x = np.linspace(0, 10, 100)
    y1 = 4 + 2 * np.sin(2 * x)
    y2 = 4 + 2 * np.cos(2 * x)
    return x, y1, y2
  
def plot(x, y1, y2):
    # step3 グラフフレームの作成
    fig, ax = plt.subplots()
    # step4 グラフの描画
    ax.plot(x, y1, linestyle='-', label='Sample 1')
    ax.plot(x, y2, linestyle='--', label='Sample 2')
  
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    ax.set_xlabel('X label')
    ax.set_ylabel('Y label')
    ax.legend()
    ax.set_title('Simple line')
    # step5 HTML上にグラフ表示
    # display(fig)
    plt.show()

# 各関数の実行
plt_style()
x, y1, y2 = data()
plot(x, y1, y2)