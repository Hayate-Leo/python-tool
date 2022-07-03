# https://matplotlib.org/stable/api/matplotlib_configuration_api.html?highlight=rcparams#matplotlib.rcParams
# https://qiita.com/qsnsr123/items/325d21621cfe9e553c17


import matplotlib.pyplot as plt
import numpy as np

class ThesisFormat:
    def __init__(self) -> None:
        self.plt_style()
    
    def plt_style(self):
        plt.rcParams['font.family'] ='Times New Roman'
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        plt.rcParams['font.size'] = 12
        plt.rcParams['axes.linewidth'] = 1.0
        plt.rcParams['lines.markersize'] = 7
        self.line_styles = ['-', '--', '-.', ':']
        self.markers = ['o', ',', '.', 'v', '^', '<', '>', '1', '2', '3', '.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3']

    def plt_line(self):
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)

        fig, ax = plt.subplots()

        ax.plot(x, y1, linestyle=self.line_styles[0], label='Sample 1')
        ax.plot(x, y2, linestyle=self.line_styles[1], label='Sample 2')
        
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        ax.set_xlabel('Time [$sec$]')
        ax.set_ylabel('Frequency [$Hz$]')
        ax.legend()

        plt.show()
    
    def plt_scatter(self):
        x = 4 + np.random.normal(0, 2, 24)
        y1 = 4 + np.random.normal(0, 2, len(x))
        y2 = 4 + np.random.normal(0, 2, len(x))

        fig, ax = plt.subplots()

        ax.scatter(x, y1, label='Sample 1', marker=self.markers[0], vmin=0, vmax=100)
        ax.scatter(x, y2, label='Sample 2', marker=self.markers[1],vmin=0, vmax=100)

        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        ax.set_xlabel('Time [$sec$]')
        ax.set_ylabel('Frequency [$Hz$]')
        ax.legend()

        plt.show()
    
    def plt_bar(self):
        np.random.seed(3)
        x = 0.5 + np.arange(8)
        y = np.random.uniform(2, 7, len(x))

        fig, ax = plt.subplots()

        ax.bar(x, y, label='Sample 1')

        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        ax.set_xlabel('Time [$sec$]')
        ax.set_ylabel('Frequency [$Hz$]')  
        ax.legend()

        plt.show()
    
    def plt_step(self):
        np.random.seed(3)
        x = 0.5 + np.arange(8)
        y = np.random.uniform(2, 7, len(x))

        fig, ax = plt.subplots()

        ax.step(x, y, label='Sample 1')

        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        ax.set_xlabel('Time [$sec$]')
        ax.set_ylabel('Frequency [$Hz$]')  
        ax.legend()

        plt.show()

if __name__ == '__main__':
    thesis_format = ThesisFormat()
    thesis_format.plt_line()
    # thesis_format.plt_scatter()
    # thesis_format.plt_bar()
    # thesis_format.plt_step()