# horizontal
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barh.html#sphx-glr-gallery-lines-bars-and-markers-barh-py
# label demo
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html#sphx-glr-gallery-lines-bars-and-markers-bar-label-demo-py


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
        plt.rcParams['errorbar.capsize'] = 3
        self.line_styles = ['-', '--', '-.', ':']
        self.markers = ['o', ',', '.', 'v', '^', '<', '>', '1', '2', '3', '.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3']
    
    def plt_hori(self):
        # Fixing random state for reproducibility
        np.random.seed(19680801)


        plt.rcdefaults()
        fig, ax = plt.subplots()

        # Example data
        people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
        y_pos = np.arange(len(people))
        performance = 3 + 10 * np.random.rand(len(people))
        error = np.random.rand(len(people))

        ax.barh(y_pos, performance, xerr=error, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(people)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Performance')
        ax.set_title('How fast do you want to go today?')

        plt.show()

    def plt_hori_label(self):
        np.random.seed(19680801)

        plt.rcdefaults()
        fig, ax = plt.subplots()

        # Example data
        people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
        y_pos = np.arange(len(people))
        performance = 3 + 10 * np.random.rand(len(people))
        error = np.random.rand(len(people))

        hbars = ax.barh(y_pos, performance, xerr=error, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(people)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Performance')
        ax.set_title('How fast do you want to go today?')

        # Label with specially formatted floats
        ax.bar_label(hbars, fmt='%.2f')
        ax.set_xlim(right=15)  # adjust xlim to fit labels

        plt.show()

    def plt_hori_label_ad(self):
        np.random.seed(19680801)

        plt.rcdefaults()
        fig, ax = plt.subplots()

        # Example data
        people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
        y_pos = np.arange(len(people))
        performance = 3 + 10 * np.random.rand(len(people))
        error = np.random.rand(len(people))
        hbars = ax.barh(y_pos, performance, xerr=error, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(people)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Performance')
        ax.set_title('How fast do you want to go today?')

        # Label with given captions, custom padding and annotate options
        ax.bar_label(hbars, labels=['±%.2f' % e for e in error],
                    padding=8, color='b', fontsize=14)
        ax.set_xlim(right=16)

        plt.show()


if __name__ == '__main__':
    thesis_format = ThesisFormat()
    thesis_format.plt_hori()
    thesis_format.plt_hori_label()
    thesis_format.plt_hori_label_ad()