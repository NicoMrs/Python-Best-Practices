# paths_manager.py

import os
from os.path import dirname as up

__all__ = [
    "Path"
]

class Path:

    base_dir = up(up(__file__))

    @classmethod
    def database(cls):
        return os.path.join(cls.base_dir, 'database')

    @classmethod
    def api_keys(cls):
        return os.path.join(cls.database(), 'api_keys.json')

    @classmethod
    def data(cls):
        return os.path.join(cls.database(), 'database.json')