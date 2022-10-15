import matplotlib.pyplot as plt
import numpy as np


def plt_default():
    x = np.linspace(0, 10, 100)
    y1 = 4 + 2 * np.sin(2 * x)
    y2 = 4 + 2 * np.cos(2 * x)

    fig, ax = plt.subplots()

    ax.plot(x, y1, 'o--', label='Sample 1')
    ax.plot(x, y2, 'D--', label='Sample 2')

    plt.show()

def plt_title():
    x = np.linspace(0, 10, 100)
    y1 = 4 + 2 * np.sin(2 * x)
    y2 = 4 + 2 * np.cos(2 * x)

    fig, ax = plt.subplots()

    ax.plot(x, y1, 'o--', label='Sample 1')
    ax.plot(x, y2, 'D--', label='Sample 2')

    # Axes.set_title(label, fontdict, loc, pad, y)
    ax.set_title('Ax Title')
    # Figure.suptitle(t, x, y, ha, va, size, weight)
    fig.suptitle('Fig Title')

    plt.show()

def plt_label():
    x = np.linspace(0, 10, 100)
    y1 = 4 + 2 * np.sin(2 * x)
    y2 = 4 + 2 * np.cos(2 * x)

    fig, ax = plt.subplots()

    ax.plot(x, y1, 'o--', label='Sample 1')
    ax.plot(x, y2, 'D--', label='Sample 2')

    ax.set_title('Ax Title')
    fig.suptitle('Fig Title')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    # fig.supxlabel('Sup X Label')
    # fig.supylabel('Sup Y Label')

    plt.show()

def plt_legend():
    x = np.linspace(0, 10, 100)
    y1 = 4 + 2 * np.sin(2 * x)
    y2 = 4 + 2 * np.cos(2 * x)

    fig, ax = plt.subplots()

    ax.plot(x, y1, 'o--', label='Sample 1')
    ax.plot(x, y2, 'D--', label='Sample 2')

    ax.set_title('Default')
    fig.suptitle('Legend')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    
    ax.legend()

    plt.show()

def plt_legend_handles():
    x = np.linspace(0, 10, 100)
    y1 = 4 + 2 * np.sin(2 * x)
    y2 = 4 + 2 * np.cos(2 * x)

    fig, ax = plt.subplots()

    line1, = ax.plot(x, y1, 'o--', label='Sample 1')
    line2, = ax.plot(x, y2, 'D--', label='Sample 2')

    ax.set_title('handles')
    fig.suptitle('Legend')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    
    ax.legend(handles=[line1, line2])

    plt.show()

def plt_legend_labels():
    x = np.linspace(0, 10, 100)
    y1 = 4 + 2 * np.sin(2 * x)
    y2 = 4 + 2 * np.cos(2 * x)

    fig, ax = plt.subplots()

    ax.plot(x, y1, 'o--')
    ax.plot(x, y2, 'D--')

    ax.set_title('labels')
    fig.suptitle('Legend')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    
    ax.legend(labels=['Sample 1', 'Sample 2'])

    plt.show()

def plt_legend_loc():
    x = np.linspace(0, 10, 100)
    y1 = 4 + 2 * np.sin(2 * x)
    y2 = 4 + 2 * np.cos(2 * x)

    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)

    locs = ['best', 'lower right', 'center', 'upper left']
    for ax, loc in zip(axs.flat, locs):
        ax.plot(x, y1, 'o--', label='Sample 1')
        ax.plot(x, y2, 'D--', label='Sample 2')

        ax.set_title(loc)
        ax.legend(loc=loc)

    fig.suptitle('Legend')
    fig.supxlabel('X label')
    fig.supylabel('Y label')
    
    plt.show()

def plt_legend_bbox():
    x = np.linspace(0, 10, 100)
    y1 = 4 + 2 * np.sin(2 * x)
    y2 = 4 + 2 * np.cos(2 * x)

    fig, ax = plt.subplots()

    ax.plot(x, y1, 'o--', label='Sample 1')
    ax.plot(x, y2, 'D--', label='Sample 2')

    ax.set_title('Bbox')
    fig.suptitle('Legend')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    plt.show()

def plt_lim():
    x = np.linspace(0, 10, 100)
    y1 = 4 + 2 * np.sin(2 * x)
    y2 = 4 + 2 * np.cos(2 * x)

    fig, ax = plt.subplots()

    ax.plot(x, y1, 'o--', label='Sample 1')
    ax.plot(x, y2, 'D--', label='Sample 2')

    ax.set_title('Default')
    fig.suptitle('Lim')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    
    ax.legend()

    plt.show()

def plt_scale():
    x = np.linspace(0, 10, 100)
    y1 = np.exp(x) + 2 * np.sin(2 * x)
    y2 = np.exp(x) + 2 * np.cos(2 * x)

    fig, axs = plt.subplots(1, 2, sharex=True)

    for ax in axs.flat:
        ax.plot(x, y1, label='Sample 1')
        ax.plot(x, y2, label='Sample 2')
        ax.legend()

    axs[0].set_title('linear')
    axs[1].set_title('log')

    fig.suptitle('scale')
    fig.supxlabel('X label')
    fig.supylabel('Y label')

    axs[1].set_yscale('log')

    plt.show()

if __name__ == '__main__':
    # plt_default()
    # plt_title()
    # plt_label()
    # plt_legend()
    # plt_legend_handles()
    # plt_legend_labels()
    # plt_legend_loc()
    # plt_legend_bbox()
    # plt_lim()
    plt_scale()