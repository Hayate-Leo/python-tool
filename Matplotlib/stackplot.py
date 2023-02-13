import matplotlib.pyplot as plt
import numpy as np
from thesis_format import ThesisFormat

class StackPlot(ThesisFormat):
    def __init__(self) -> None:
        super().__init__()

    def plt_simple(self):
        # step1 データの作成
        x = np.linspace(0, 10, 100)
        dict_y = {
            'y1': x**1.5,
            'y2': x**2,
            'y3': x**2.1,
            'y4': np.exp(0.4*x),
            'y5': np.exp(0.4*x)+np.sin(x),
        }
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 積み上げ面グラフの描画
        ax.stackplot(x, dict_y.values(), labels=dict_y.keys())

        ax.set_xlabel('X label')
        ax.set_ylabel('Y label')
        ax.legend(loc='upper left')

        ax.set_title('Simple Stackplot')

        plt.show()

    def plt_sym(self):
        x = np.linspace(0, 10, 100)
        dict_y = {
            'y1': x**1.5,
            'y2': x**2,
            'y3': x**2.1,
            'y4': np.exp(0.4*x),
            'y5': np.exp(0.4*x)+np.sin(x),
        }

        fig, ax = plt.subplots()

        ax.stackplot(x, dict_y.values(), labels=dict_y.keys(), baseline='sym')
        ax.axhline(0, color='black', ls='--')
        
        ax.set_title('baseline = Sym')

        plt.show()

    def plt_stream(self):
        x = np.linspace(0, 10, 100)
        dict_y = {
            'y1': np.sin(x)+np.cos(0.5*x),
            'y2': np.sin(2+x)+np.cos(1.2*x),
            'y3': np.sin(0.5+x)+np.cos(3*x),
            'y4': np.sin(4*x)+np.cos(2*x),
            'y5': np.sin(3+x)+np.cos(0.7*x),
        }

        fig, ax = plt.subplots()
        
        ax.stackplot(x, dict_y.values(), labels=dict_y.keys(), baseline='wiggle')
        ax.axhline(0, color='black', ls='--')

        ax.set_title('baseline = wiggle')
        fig.suptitle('Streamgraph')
        plt.show()

    def plt_baseline(self):
        x = np.linspace(0, 10, 100)
        dict_y = {
            'y1': np.sin(x)+np.cos(0.5*x),
            'y2': np.sin(2+x)+np.cos(1.2*x),
            'y3': np.sin(0.5+x)+np.cos(3*x),
            'y4': np.sin(4*x)+np.cos(2*x),
            'y5': np.sin(3+x)+np.cos(0.7*x),
        }

        fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
        
        baselines = ['zero', 'sym', 'wiggle', 'weighted_wiggle']
        for ax, baseline in zip(axs.flat, baselines):
            ax.stackplot(x, dict_y.values(), labels=dict_y.keys(), baseline=baseline)
            ax.axhline(0, color='black', ls='--')
            ax.set_title(baseline)
        
        fig.supxlabel('X label')
        fig.supylabel('Y label')
        fig.suptitle('baseline in Stackplot')

        plt.show()

    def plt_colors(self):
        x = np.linspace(0, 10, 100)
        dict_y = {
            'y1': x**1.5,
            'y2': x**2,
            'y3': x**2.1,
            'y4': np.exp(0.4*x),
            'y5': np.exp(0.4*x)+np.sin(x),
        }

        fig, ax = plt.subplots()

        colors = ['forestgreen', 'limegreen', 'aquamarine', 'cyan', 'skyblue']
        ax.stackplot(x, dict_y.values(), labels=dict_y.keys(), colors=colors)
        
        ax.set_title('Colors in  Stackplot')

        plt.show()

if __name__ == '__main__':
    stack_plot = StackPlot()
    # stack_plot.plt_simple()
    stack_plot.plt_sym()
    # stack_plot.plt_stream()
    # stack_plot.plt_baseline()
    # stack_plot.plt_colors()