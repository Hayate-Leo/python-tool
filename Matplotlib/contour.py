# https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_demo.html#sphx-glr-gallery-images-contours-and-fields-contour-demo-py
# https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_imag.html#sphx-glr-gallery-images-contours-and-fields-contour-image-py
# https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_demo.html#sphx-glr-gallery-images-contours-and-fields-contourf-demo-py


import matplotlib.pyplot as plt
import numpy as np
from thesis_format import ThesisFormat

class ThesisContour(ThesisFormat):
    def __init__(self) -> None:
        super().__init__()
    
    def plt_data(self):
        delta = 0.025
        x = np.arange(-3.0, 3.0, delta)
        y = np.arange(-2.0, 2.0, delta)
        X, Y = np.meshgrid(x, y)
        Z1 = np.exp(-X**2 - Y**2)
        Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
        Z = (Z1 - Z2) * 2
        return X, Y, Z

    def plt_contour(self):
        # step1 3次元データの呼び出し
        X, Y, Z = self.plt_data()
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 等高線グラフの描画
        CS = ax.contour(X, Y, Z)
        # step4 等高線グラフのラベル表示
        ax.clabel(CS, inline=True)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_title('Simple Contour')
        plt.show()
    
    def plt_contourf(self):
        # step1 3次元データの呼び出し
        X, Y, Z = self.plt_data()
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 塗りつぶし等高線グラフの描画
        CS = ax.contourf(X, Y, Z)
        # step4 カラーバーの表示
        fig.colorbar(CS)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_title('Simple Contourf')
        plt.show()
    
    def plt_levels(self):
        X, Y, Z = self.plt_data()
        fig, ax = plt.subplots()

        CS = ax.contour(X, Y, Z, levels=13)

        ax.clabel(CS, inline=True)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_title('Levels 13')

        plt.show()

    def plt_colors(self):
        X, Y, Z = self.plt_data()
        fig, ax = plt.subplots()

        # ax.contour(X, Y, Z, colors='red')
        # ax.contour(X, Y, Z, colors=['red', 'black'])
        ax.contour(X, Y, Z, colors='#0097a7', alpha=0.5)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')

        # ax.set_title('Colors Red')
        # ax.set_title('Colors Red & Black')
        ax.set_title('Colors="#0097a7" Alpha=0.5')

        plt.show()
    
    def plt_cmap(self):
        X, Y, Z = self.plt_data()
        fig, ax = plt.subplots()

        cmaps = ['viridis', 'Greys', 'bwr']
        cmap=cmaps[2]
        CS = ax.contourf(X, Y, Z, cmap=cmap)
        fig.colorbar(CS, ax=ax)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_title('Cmap '+cmap)

        plt.show()
    
    def plt_thesis_contour(self):
        # step1 3次元データの呼び出し
        X, Y, Z = self.plt_data()
        # step2 グラフフレームの作成
        fig, ax = plt.subplots()
        # step3 等高線グラフの描画
        CS = ax.contour(X, Y, Z, colors='black')
        # step4 等高線グラフのラベル表示
        ax.clabel(CS, inline=True)

        # step5 等高線の塗りつぶし
        CSf = ax.contourf(X, Y, Z)

        # step6 カラーバーの設定
        cbar = fig.colorbar(CSf)
        cbar.ax.set_ylabel('Z Label')
        cbar.add_lines(CS)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_title('Contour for Thesis')
        plt.show()
    
    def plt_3d(self):
        X, Y, Z = self.plt_data()
        fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
        # 3Dグラフ
        SF = ax.plot_surface(X, Y, Z, cmap='viridis')

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
    thesis_contour.plt_cmap()
    # thesis_contour.plt_thesis_contour()
    # thesis_contour.plt_3d()
    