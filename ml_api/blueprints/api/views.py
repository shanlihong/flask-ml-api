from . import api
from flask import current_app as app
from flask.globals import request
from flask.views import MethodView
from ml_api.blueprints.api.models import (select,
                                          insert,
                                          update,
                                          delete,
                                          delete_all)

from ml_api.core.responses.json_responses import (ok, empty, server_error)

class BaseAPI(MethodView):
    """
    Base API
    """

    def get(self, id):
        try:
            return ok([])
        except Exception as e:
            return server_error([e.message])


class RESTMixin(object):
    """
    Cover the basic RESTful operations
    """

    def get(self, id):
        try:
            if id:
                # Return the item
                cls = select(id, self.list)
                return ok(cls)
            else:
                # Return all items
                return ok(self.list)
        except Exception as e:
            return server_error([e.message])

    def post(self):
        try:
            # Store new item
            id = insert(request.json, self.list)

            # Return the new item id
            return ok(id)
        except Exception as e:
            return server_error([e.message])

    def put(self, id):
        try:
            # Update the existing item's field
            update(id, request.json['key'], request.json['value'], self.list)
            return empty()
        except Exception as e:
            return server_error([e.message])

    def delete(self, id):
        try:
            if id:
                # Delete the item
                delete(id, self.list)
            else:
                # Delete all items
                delete_all(self.list)
            return empty()
        except Exception as e:
            return server_error([e.message])

class ClassesAPI(MethodView, RESTMixin):
    """
    Classes API
    """

    def __init__(self):
        self.list = app.db['classes']

class TrainingAPI(MethodView, RESTMixin):
    """
    Training API
    """

    def __init__(self):
        self.list = app.db['training']


class ClassificationsAPI(MethodView, RESTMixin):
    """
    Classifications API
    """

    def __init__(self):
        self.list = app.db['classifications']

    def post(self):
        try:
            # Store new item
            id = insert(request.json, self.list)

            # Return the classification
            classification = dict(
                id=id,
                classification="FOO",
                confidence=0.9
            )

            return ok(classification)
        except Exception as e:
            return server_error([e.message])