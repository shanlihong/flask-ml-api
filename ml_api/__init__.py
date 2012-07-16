"""
Provides methods to initialize and run the full application.
"""

import sys

def register_api(app, view, endpoint, url, pk='id', pk_type='string'):
    """
    Helper method to generate the URLs and methods
    """
    view_func = view.as_view(endpoint)

    if pk:
        app.add_url_rule(url, defaults={pk: None}, view_func=view_func, methods=['GET', 'DELETE'])
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
                                             ClassesAPI,
                                             TrainingAPI,
                                             ClassificationsAPI)

    register_api(app, BaseAPI, 'base_api', '/api/v1/')

    register_api(app, ClassesAPI,
        'classes_api', '/api/v1/classes/', pk='id')

    register_api(app, TrainingAPI,
        'training_api', '/api/v1/training/', pk='id')

    register_api(app, ClassificationsAPI,
        'classifications_api', '/api/v1/classifications/', pk='id')

    # Setup a db connection
    app.db = dict(
        classes=list(),
        training=list(),
        classifications=list())

    # Return the app
    return app

# Prevent create_app from being called twice when running in development or
# being called at all during setup.py, etc.
if not any(arg in sys.argv[0] for arg in ('runserver', 'setup.py', 'nosetests')):
    app = create_app()
