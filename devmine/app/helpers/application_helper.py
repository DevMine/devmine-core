import json
from sqlalchemy.ext.declarative import DeclarativeMeta


def obj_to_json(obj):
    """
    Serialize an object to JSON.
    """
    fields = {}
    attrs = [x for x in obj.__dict__.keys() if not x.startswith('_')]
    for field in attrs:
        data = obj.__getattribute__(field)
        if hasattr(data, 'isoformat'):
            data = data.isoformat()
        json.dumps(data)
        fields[field] = data
    return fields


class AlchemyEncoder(json.JSONEncoder):
    """
    Extend JSONENcoder class in order to be able to convert objects gotten from
    SQLAlchemy requests to JSON.
    """
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            return obj_to_json(obj)
        return json.JSONEncoder.default(self, obj)
