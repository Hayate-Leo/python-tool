# https://matplotlib.org/stable/gallery/spines/multiple_yaxis_with_spines.html

import matplotlib.pyplot as plt

class MultiFormat:
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
        fig, ax = plt.subplots()
        fig.subplots_adjust(right=0.75)

        twin1 = ax.twinx()
        twin2 = ax.twinx()

        # twin2を右方向に動かします
        twin2.spines['right'].set_position(('axes', 1.2))

        p1, = ax.plot([0, 1, 2], [0, 1, 2], 'C0', label='Y1')
        p2, = twin1.plot([0, 1, 2], [0, 3, 2], 'C1', label='Y2')
        p3, = twin2.plot([0, 1, 2], [50, 30, 15], 'C2', label='Y3')

        ax.set_xlim(0, 2)
        ax.set_ylim(0, 2)
        twin1.set_ylim(0, 4)
        twin2.set_ylim(1, 65)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y1')
        twin1.set_ylabel('Y2')
        twin2.set_ylabel('Y3')

        ax.yaxis.label.set_color(p1.get_color())
        twin1.yaxis.label.set_color(p2.get_color())
        twin2.yaxis.label.set_color(p3.get_color())

        ax.tick_params(axis='y', colors=p1.get_color())
        twin1.tick_params(axis='y', colors=p2.get_color())
        twin2.tick_params(axis='y', colors=p3.get_color())

        ax.legend(handles=[p1, p2, p3])

        plt.show()
    
    def plt_scatter(self):
        fig, ax = plt.subplots()
        fig.subplots_adjust(right=0.75)

        twin1 = ax.twinx()
        twin2 = ax.twinx()

        # twin2を右方向に動かします
        twin2.spines['right'].set_position(('axes', 1.2))

        p1 = ax.scatter([0, 0.4, 0.8, 1, 1.3, 1.8, 2], [0, 8, 2, 1, 21, 14, 22], c='C0', label='Y1')
        p2 = twin1.scatter([0, 0.7, 0.9, 1, 1.2, 1.5, 2], [0, 34, 23, 23, 12, 8, 16], c='C1', label='Y2')
        p3 = twin2.scatter([0, 0.6, 0.8, 1, 1.4, 1.8, 2], [22, 50, 23, 24, 95, 30, 15], c='C2', label='Y3')

        ax.set_xlim(0, 2)
        ax.set_ylim(0, 30)
        twin1.set_ylim(0, 40)
        twin2.set_ylim(1, 100)

        ax.set_xlabel('X label')
        ax.set_ylabel('Y1')
        twin1.set_ylabel('Y2')
        twin2.set_ylabel('Y3')

        ax.legend(handles=[p1, p2, p3])

        plt.show()

if __name__ == '__main__':
    multi_format = MultiFormat()
    multi_format.plt_line()
    # multi_format.plt_scatter()