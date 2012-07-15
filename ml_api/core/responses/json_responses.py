"""
Helpers for constructing JSON responses
"""
import json
from flask.helpers import make_response


def _response(content, code=200):
    """
    Base helper to construct a JSON response
    """
    response = make_response(json.dumps(content, indent=4))
    response.content_type = 'application/json'
    response.status_code = code
    return response


def ok(content):
    """
    Construct a JSON success response
    """
    return _response(content)


def empty():
    """
    Construct an empty JSON success response
    """
    return _response("", 204)


def bad_request(errors):
    """
    Construct a bad request JSON response
    """
    content = dict()
    content['errors'] = errors
    return _response(content, 400)


def not_found(errors):
    """
    Construct a not found JSON response
    """
    content = dict()
    content['errors'] = errors
    return _response(content, 404)


def server_error(errors):
    """
    Construct a server error JSON response
    """
    content = dict()
    content['errors'] = errors
    return _response(content, 500)
