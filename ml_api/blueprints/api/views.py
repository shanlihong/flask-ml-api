from . import api
from flask.views import MethodView
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


class TrainingSetsAPI(MethodView):
    """
    Training Sets API
    """

    def get(self, ts_id):
        try:
            return ok([])
        except Exception as e:
            return server_error([e.message])

    def post(self):
        try:
            return ok("id")
        except Exception as e:
            return server_error([e.message])

    def put(self, ts_id):
        try:
            return empty()
        except Exception as e:
            return server_error([e.message])

    def delete(self, ts_id):
        try:
            return empty()
        except Exception as e:
            return server_error([e.message])


class PredictionsAPI(MethodView):
    """
    Predictions API
    """

    def get(self, p_id):
        try:
            return ok([])
        except Exception as e:
            return server_error([e.message])

    def post(self):
        try:
            return ok("id")
        except Exception as e:
            return server_error([e.message])

    def put(self, p_id):
        try:
            return empty()
        except Exception as e:
            return server_error([e.message])

    def delete(self, p_id):
        try:
            return empty()
        except Exception as e:
            return server_error([e.message])