# https://matplotlib.org/stable/gallery/specialty_plots/radar_chart.html

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D


def radar_factory(num_vars, frame='circle'):
    """

    num_vars（int型）の軸を持つレーダーチャートを作成する．

    この関数は，RadarAxesプロジェクションを作成し，登録する．

    Parameters
    ----------
    num_vars : int
        レーダーチャート用の変数の数
    frame : {'circle', 'polygon'}
        軸を囲む枠の形状

    """
    # 軸角を均等にする
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)

    class RadarTransform(PolarAxes.PolarTransform):

        def transform_path_non_affine(self, path):
            # 非単位の補間ステップを持つパスはグリッドラインに対応し,
            # （PolarTransformの円弧への自動変換を無効にするために）補間を強制する
            if path._interpolation_steps > 1:
                path = path.interpolated(num_vars)
            return Path(self.transform(path.vertices), path.codes)

    class RadarAxes(PolarAxes):

        name = 'radar'
        # 指定した点間を1本の線分で結ぶ
        RESOLUTION = 1
        PolarTransform = RadarTransform

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # 第一軸が上になるようにプロットを回転させる
            self.set_theta_zero_location('N')

        def fill(self, *args, closed=True, **kwargs):
            """fillを上書きし、デフォルトで行を閉じるようにする"""
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """デフォルトで線が閉じるようにplotを上書きする"""
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: x[0],y[0]のマーカーが2倍になる
            if x[0] != x[-1]:
                x = np.append(x, x[0])
                y = np.append(y, y[0])
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            # Axesパッチは軸座標で (0.5, 0.5) を中心とし，半径 0.5である必要がある
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((0.5, 0.5), num_vars,
                                      radius=.5, edgecolor="k")
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                # spine_typeは必ず'left'/'right'/'top'/'bottom'/'circle'
                spine = Spine(axes=self,
                              spine_type='circle',
                              path=Path.unit_regular_polygon(num_vars))
                # unit_regular_polygon は (0, 0) を中心とする半径 1 の多角形を与える
                # しかし 軸座標で(0.5, 0.5)を中心とする半径0.5の多角形が欲しい
                spine.set_transform(Affine2D().scale(.5).translate(.5, .5)
                                    + self.transAxes)
                return {'polar': spine}
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta


def example_data():
    data = [
        ['Sulfate', 'Nitrate', 'EC', 'OC1', 'OC2', 'OC3', 'OP'],
        ('Basecase', [
            [0.88, 0.01, 0.03, 0.03, 0.00, 0.06, 0.01],
            [0.07, 0.95, 0.04, 0.05, 0.00, 0.02, 0.01],
            [0.01, 0.01, 0.02, 0.71, 0.74, 0.70, 0.00]])
    ]
    return data


if __name__ == '__main__':
    N = 7
    theta = radar_factory(N, frame='polygon')

    data = example_data()
    spoke_labels = data.pop(0)

    fig, ax = plt.subplots(figsize=(9, 9), nrows=1, ncols=1,
                            subplot_kw=dict(projection='radar'))
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

    colors = ['b', 'r', 'g', 'm', 'y']
    # 例題データからの1つめのケースのみ取り出し
    title, case_data = data[0]
    ax.set_rgrids([0.2, 0.4, 0.6, 0.8])
    ax.set_title(title, weight='bold', size='medium', position=(0.5, 1.1),
                    horizontalalignment='center', verticalalignment='center')
    for d, color in zip(case_data, colors):
        ax.plot(theta, d, color=color)
        ax.fill(theta, d, facecolor=color, alpha=0.25, label='_nolegend_')
    ax.set_varlabels(spoke_labels)

    # 左上のプロットに相対的な凡例を追加
    labels = ('Factor 1', 'Factor 2', 'Factor 3')
    legend = ax.legend(labels, loc=(0.9, .95),
                              labelspacing=0.1, fontsize='small')

    fig.text(0.5, 0.965, '3-Factor Solution Profiles in 7-Elements',
             horizontalalignment='center', color='black', weight='bold',
             size='large')

    plt.show()

