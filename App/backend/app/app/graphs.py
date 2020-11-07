import matplotlib
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import io
import urllib, base64

def generate_normal_distribution(hypothesis):
    matplotlib.use('Agg')
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