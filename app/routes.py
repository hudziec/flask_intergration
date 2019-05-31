from app import app
from flask import render_template
from app.data import getStats
from app.parser import getPoem
from app.graph import plot_points


@app.route('/')
@app.route('/index')
def index():
    url = 'http://www.arthurleej.com/e-love.html'
    response = getPoem(url)
    return render_template('index.html', response=response)


@app.route('/dataframe')
def dataframe():
    response = getStats()
    return render_template('dataframe.html', response=response)


@app.route('/graph')
def graph():
    x = [1, 2, 3, 4]
    y = [10, 12.2, 18.6, 8.5]

    xlabel = 'X Axis'
    ylabel = 'Y Axis'
    title = 'Flask Integrated Graph'

    name = plot_points(x, y, xlabel, ylabel, title)

    return render_template('graph.html', name=name)
