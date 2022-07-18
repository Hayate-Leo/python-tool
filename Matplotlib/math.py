# https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_demo.html
# https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_examples.html
# https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_fontfamily_example.html

from turtle import color
import matplotlib.pyplot as plt
import numpy as np

class MathText:
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


    def plt_line(self):
        x = np.linspace(0, 10, 100)
        y1 = 4 + 2 * np.sin(2 * x)
        y2 = 4 + 2 * np.cos(2 * x)
        y3 = 6 + 2 * np.sin(2 * x)

        fig, ax = plt.subplots()

        ax.plot(x, y1, linestyle=self.line_styles[0], label='Sample 1')
        ax.plot(x, y2, linestyle=self.line_styles[1], label='Sample 2')

        tex1 = r'$4+2{\rm sin}(2x)$'
        tex2 = r'$4+2{\rm cos}(2x)$'

        ax.text(0.2, 1, tex1, color='C0')
        ax.text(0.2, 0.2, tex2, color='C1')
        
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        ax.set_xlabel('Time [sec]')
        ax.set_ylabel('Frequency [Hz]')
        ax.legend()

        plt.show()
    
    def plt_text(self):
        fig, ax = plt.subplots()

        subscripts_superscripts = [
            'alpha > beta', 
            r'$\alpha > \beta$', 
            r'$\alpha^{ic} > \beta_{ic}$', 
            r'$\sum_{i=0}^\infty x_i$'
        ]

        fractions = [
            r'$\frac{3}{4} \binom{3}{4} \genfrac{}{}{0}{}{3}{4}$',
            r'$\frac{5 - \frac{1}{x}}{4}$',
            r'$(\frac{5 - \frac{1}{x}}{4})$',
            r'$\left(\frac{5 - \frac{1}{x}}{4}\right)$'
        ]

        radicals = [
            r'$\sqrt{2}$',
            r'$\sqrt[3]{x}$'
        ]

        for i, tex in enumerate(radicals):
            ax.text(0.5, i*1.5+2, tex, size=18)
        
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)

        plt.show()

if __name__ == '__main__':
    math_text = MathText()
    # math_text.plt_line()
    math_text.plt_text()
