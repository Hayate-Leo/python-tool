# https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_demo.html#sphx-glr-gallery-images-contours-and-fields-contour-demo-py
# https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_imag.html#sphx-glr-gallery-images-contours-and-fields-contour-image-py
# https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_demo.html#sphx-glr-gallery-images-contours-and-fields-contourf-demo-py


import matplotlib.pyplot as plt
import numpy as np

class ThesisContour:
    def __init__(self) -> None:
        self.plt_style()
        self.plt_data()
    
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
    
    def plt_data(self):
        delta = 0.025
        x = np.arange(-3.0, 3.0, delta)
        y = np.arange(-2.0, 2.0, delta)
        X, Y = np.meshgrid(x, y)
        Z1 = np.exp(-X**2 - Y**2)
        Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
        Z = (Z1 - Z2) * 2
        self.X = X
        self.Y = Y
        self.Z = Z

    def plt_contour(self):
        fig, ax = plt.subplots()
        CS = ax.contour(self.X, self.Y, self.Z)
        ax.clabel(CS, inline=True)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_title('Simple Contour')
        plt.show()
    
    def plt_contourf(self):
        fig, ax = plt.subplots()
        CS = ax.contourf(self.X, self.Y, self.Z)

        fig.colorbar(CS)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_title('Simple Contourf')
        plt.show()
    
    def plt_levels(self):
        fig, axs = plt.subplots(1, 2, constrained_layout=True)

        CS1 = axs[0].contour(self.X, self.Y, self.Z)
        CS2 = axs[1].contour(self.X, self.Y, self.Z, levels=13)

        axs[0].clabel(CS1, inline=True)
        axs[1].clabel(CS2, inline=True)

        for ax in axs.flat:
            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')

        axs[0].set_title('Levels default')
        axs[1].set_title('Levels 13')

        plt.show()

    def plt_colors(self):
        fig, axs = plt.subplots(2, 2, constrained_layout=True)

        axs[0, 0].contour(self.X, self.Y, self.Z)
        axs[0, 1].contour(self.X, self.Y, self.Z, colors='red')
        axs[1, 0].contour(self.X, self.Y, self.Z, colors=['red', 'black'])
        axs[1, 1].contour(self.X, self.Y, self.Z, colors='red', alpha=0.5)

        for ax in axs.flat:
            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')

        axs[0, 0].set_title('Colors Blank')
        axs[0, 1].set_title('Colors Red')
        axs[1, 0].set_title('Colors Red & Black')
        axs[1, 1].set_title('Colors Red Alpha=0.5')

        plt.show()
    
    def plt_cmap(self):
        fig, axs = plt.subplots(2, 2, constrained_layout=True)

        cmaps = ['viridis', 'Greys', 'winter', 'bwr']

        count = 0
        for col in range(2):
            for row in range(2):
                cmap = cmaps[count]
                ax = axs[row, col]
                CS = ax.contourf(self.X, self.Y, self.Z, cmap=cmap)
                fig.colorbar(CS, ax=ax)

                ax.set_xlabel('X Label')
                ax.set_ylabel('Y Label')
                ax.set_title('Cmap '+cmap)

                count += 1

        plt.show()
    
    def plt_thesis_contour(self):
        fig, ax = plt.subplots()
        # 等高線のラベル
        CS = ax.contour(self.X, self.Y, self.Z, colors='black')
        ax.clabel(CS, inline=True)

        # 等高線の塗りつぶし
        CSf = ax.contourf(self.X, self.Y, self.Z)

        # カラーバーの設定
        cbar = fig.colorbar(CSf)
        cbar.ax.set_ylabel('Z Label')
        cbar.add_lines(CS)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_title('Contour for Thesis')
        plt.show()
    
    def plt_3d(self):
        fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
        # 3Dグラフ
        SF = ax.plot_surface(self.X, self.Y, self.Z, cmap='viridis')

        # カラーバーの設定
        cbar = fig.colorbar(SF, aspect=8)
        cbar.ax.set_ylabel('Z Label')

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_title('3D Contour by 3D surface')
        plt.show()
    

if __name__ == '__main__':
    thesis_contour = ThesisContour()
    # thesis_contour.plt_contour()
    # thesis_contour.plt_contourf()
    # thesis_contour.plt_levels()
    # thesis_contour.plt_colors()
    # thesis_contour.plt_cmap()
    # thesis_contour.plt_thesis_contour()
    thesis_contour.plt_3d()
    