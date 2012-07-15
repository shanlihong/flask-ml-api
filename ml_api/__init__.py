"""
Provides methods to initialize and run the full application.
"""

import sys

def register_api(app, view, endpoint, url, pk='id', pk_type='int'):
    """
    Helper method to generate the URLs and methods
    """
    view_func = view.as_view(endpoint)

    if pk:
        app.add_url_rule(url, defaults={pk: None}, view_func=view_func, methods=['GET'])
        app.add_url_rule(url, view_func=view_func, methods=['POST',])
        app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk),
            view_func=view_func, methods=['GET', 'PUT', 'DELETE'])
    else:
        app.add_url_rule(url, defaults={pk: None}, view_func=view_func,
            methods=['GET', 'HEAD', 'POST', 'PUT', 'OPTIONS', 'DELETE'])


def create_app(debug=False):
    """
    Dynamically create a flask app.
    """
    from flask import Flask

    app = Flask(__name__,
        template_folder='templates',
        static_folder='assets',
        instance_relative_config=True)

    # Default settings
    app.config.from_object('ml_api.settings')
    app.debug = debug

    # Blueprints
    from .blueprints.site.views import site
    app.register_blueprint(site, url_prefix='/')

    # Register API classes
    from ml_api.blueprints.api.views import (BaseAPI,
                                             TrainingSetsAPI,
                                             PredictionsAPI)

    register_api(app, BaseAPI, 'base_api', '/api/v1/')

    register_api(app, TrainingSetsAPI,
        'training_sets_api', '/api/v1/training-sets/', pk='ts_id')

    register_api(app, PredictionsAPI,
        'predictions_api', '/api/v1/predictions/', pk='p_id')

    # Setup a db connection
    app.db = None

    # Return the app
    return app

# Prevent create_app from being called twice when running in development or
# being called at all during setup.py, etc.
if not any(arg in sys.argv[0] for arg in ('runserver', 'setup.py', 'nosetests')):
    app = create_app()
