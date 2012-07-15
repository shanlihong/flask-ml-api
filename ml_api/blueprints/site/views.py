from . import site
from flask.templating import render_template

@site.route('/', methods=['GET'])
def index():
    """
    Home page
    """
    context = dict()
    return render_template('index.html', **context)


@site.route('help')
def help():
    """
    Help page
    """
    context = dict()
    return render_template('help.html', **context)


@site.route('training', methods=['GET'])
def training():
    """
    Allow users to train a sample set
    """
    context = dict()
    return render_template('training.html', **context)


@site.route('prediction', methods=['GET'])
def training():
    """
    Allow users to make a prediction on data
    not in the training set
    """
    context = dict()
    return render_template('prediction.html', **context)