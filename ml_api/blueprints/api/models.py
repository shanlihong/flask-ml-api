"""
Methods for simulating DB calls
"""
import json
from flask import current_app as app
import uuid


def log():
    print
    print "*"*50
    print json.dumps(app.db, indent=4)
    print "*"*50
    print


def select(id, list):
    item = filter(lambda li: li['id'] == id, list)
    log()
    return item


def insert(data, list):
    id = str(uuid.uuid1())
    data['id'] = id

    # Store it, with id
    list.append(data)

    log()
    return id


def update(id, key, value, list):
    item = select(id, list)
    item[key] = value
    log()
    return


def delete(id, list):
    for item in list:
        if item['id'] == id:
            list.remove(item)
            break
    log()
    return


def delete_all(list):
    del list[0:len(list)]
    log()
    return