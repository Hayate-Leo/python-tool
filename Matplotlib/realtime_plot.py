# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html
# https://matplotlib.org/3.2.2/api/_as_gen/matplotlib.axes.Axes.remove.html

import numpy as np
import matplotlib.pyplot as plt
from thesis_format import ThesisFormat

class RealTime(ThesisFormat):
    def __init__(self) -> None:
        super().__init__()

    def plt_line(self):
        xs = []
        y1 = []
        y2 = []
        fig, ax = plt.subplots()

        for x in np.linspace(0, 10, 100):
            xs.append(x)
            y1.append(4 + 2 * np.sin(2 * x))
            y2.append(4 + 2 * np.cos(2 * x))

            line1, = ax.plot(xs, y1, color='C0', linestyle=self.line_styles[0], label='Sample1')
            line2, = ax.plot(xs, y2, color='C1',linestyle=self.line_styles[1], label='Sample2')

            ax.set_xlabel('X label')
            ax.set_ylabel('Y label')
            ax.legend()

            plt.pause(0.001)
            line1.remove()
            line2.remove()


if __name__ == '__main__':
    real_time = RealTime()
    real_time.plt_line()