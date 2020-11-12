import matplotlib
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import io
import urllib, base64

matplotlib.use('Agg')

def generate_normal_distribution(hypothesis):
    data =  [float(x) for x in hypothesis.split(';')]

    mean, std = scipy.stats.norm.fit(data)

    x_min = mean - 3*std
    x_max = mean + 3*std

    x = np.linspace(x_min, x_max, 100)

    y = scipy.stats.norm.pdf(x, mean, std)

    #----------------------------------------------------------------------------------------#
    # fill area 1

    pt1 = mean + std
    plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean, std)], color='white')

    pt2 = mean - std
    plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean, std)], color='white')

    ptx = np.linspace(pt1, pt2, 10)
    pty = scipy.stats.norm.pdf(ptx,mean,std)

    plt.fill_between(ptx, pty, color='#0b559f', alpha=1.0)

    #----------------------------------------------------------------------------------------#
    # fill area 2

    pt1 = mean + std
    plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean, std)], color='white')

    pt2 = mean + 2.0 * std
    plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean, std)], color='white')

    ptx = np.linspace(pt1, pt2, 10)
    pty = scipy.stats.norm.pdf(ptx,mean,std)

    plt.fill_between(ptx, pty, color='#2b7bba', alpha=1.0)

    #----------------------------------------------------------------------------------------#
    # fill area 3

    pt1 = mean - std
    plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean, std)], color='white')

    pt2 = mean - 2.0 * std
    plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean, std)], color='white')

    ptx = np.linspace(pt1, pt2, 10)
    pty = scipy.stats.norm.pdf(ptx,mean,std)

    plt.fill_between(ptx, pty, color='#2b7bba', alpha=1.0)

    #----------------------------------------------------------------------------------------#
    # fill area 4

    pt1 = mean + 2.0 * std
    plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean, std)], color='white')

    pt2 = mean + 3.0 * std
    plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean, std)], color='white')

    ptx = np.linspace(pt1, pt2, 10)
    pty = scipy.stats.norm.pdf(ptx,mean,std)

    plt.fill_between(ptx, pty, color='#539ecd', alpha=1.0)

    #----------------------------------------------------------------------------------------#
    # fill area 5

    pt1 = mean - 2.0 * std
    plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean, std)], color='white')

    pt2 = mean - 3.0 * std
    plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean, std)], color='white')

    ptx = np.linspace(pt1, pt2, 10)
    pty = scipy.stats.norm.pdf(ptx,mean,std)

    plt.fill_between(ptx, pty, color='#539ecd', alpha=1.0)

    #----------------------------------------------------------------------------------------#
    # fill area 6

    pt1 = mean + 3.0 * std
    plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean, std)], color='white')

    pt2 = mean + 10.0 *std
    plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean, std)], color='white')

    ptx = np.linspace(pt1, pt2, 10)
    pty = scipy.stats.norm.pdf(ptx,mean,std)

    plt.fill_between(ptx, pty, color='#89bedc', alpha=1.0)

    #----------------------------------------------------------------------------------------#
    # fill area 7

    pt1 = mean - 3.0 * std
    plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean, std)], color='white')

    pt2 = mean - 10.0 * std
    plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean, std)], color='white')

    ptx = np.linspace(pt1, pt2, 10)
    pty = scipy.stats.norm.pdf(ptx,mean,std)

    plt.fill_between(ptx, pty, color='#89bedc', alpha=1.0)

    #----------------------------------------------------------------------------------------#
    plt.plot(x,y, color='black')

    for x in data:
        plt.scatter(x, 0.0, color='red') 

    plt.xlim(x_min, x_max)

    plt.title('',fontsize=10)

    plt.xlabel('x')
    plt.ylabel('Normal Distribution')

    fig = plt.gcf()
    plt.close(fig)
    plt.ioff()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string

def func(x, pos):
    return format(x).replace("-", "").replace(".0", "")

def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # We want to show all ticks...
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)
    plt.xlabel('Question\'s number', fontsize=10)
    plt.ylabel('Answer\'s number', fontsize=10)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels())

    # Turn spines off and create grey grid.
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="#f5f5ef", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=True, left=False)

    return im, cbar

def annotate_heatmap(im, data=None, valfmt="{x:i}",
                     textcolors=["black", "white"],
                     threshold=None, **textkw):

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts

def getHeatmap(answers_data):
    answers_numbers = range(4, 0, -1)
    questions = range(1, len(answers_data)+1)

    arr = np.full((4, len(answers_data)), np.nan)

    for i in range(len(answers_data)):
        for j in range(len(answers_data[i])):
            arr[len(answers_data)-1-j][i] = answers_data[i][j]

    data = arr
    print(answers_data)
    print(type(data[3][1]))
    print(data)

    fig, ax = plt.subplots()

    im, cbar = heatmap(data, answers_numbers, questions, ax=ax,
                    cmap="magma_r", cbarlabel="Answers frequency per question")

    valfmt=matplotlib.ticker.FuncFormatter(func)
    texts = annotate_heatmap(im, valfmt=valfmt)

    fig = plt.gcf()
    plt.close(fig)
    plt.ioff()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string