import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import os


def plot_points(x,y,xlabel,ylabel,title):
    fig =plt.figure(figsize=(20,10))
    plt.plot(x,y,'bo-')
    plt.title(f'{title}', fontsize=36)
    plt.xlabel(f'{xlabel}', fontsize=20)
    plt.ylabel(f'{ylabel}', fontsize=20)

    my_path = os.path.abspath(os.path.dirname(__file__))+ '/static/graph_images/'

    plot_name = 'plot_name.png'
    url = my_path + plot_name
    fig.savefig(url)
    return plot_name
