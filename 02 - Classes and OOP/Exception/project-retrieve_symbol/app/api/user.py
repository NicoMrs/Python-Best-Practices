""" Define user class """

import json
import os
from ..utils import Path
from ..utils import NameNotFound

__all__ = ['User']

class User:
    """ user class """

    def __init__(self, name):
        self.name = name

        if not os.path.isfile(Path.api_keys()):
            raise FileNotFoundError(f"File {Path.api_keys()} not found.")

        self.api_key_json = Path.api_keys()
        self._api_key = None

    @property
    def api_key(self):
        """ retrieve api from json file then store it"""
        if self._api_key is None:
            self._api_key = self.retrieve_api_key()['api_key']
        return self._api_key

    def retrieve_api_key(self):
        """ retrieve api key """
        with open(self.api_key_json) as f:
            data = json.load(f)
        api_key = data.get(self.name, None)

        if api_key is None:
            raise NameNotFound(f"No api_key available for name:{self.name!r}")
        return api_key

if __name__ == "__main__":
    user = User(name='Nicolas')
    print(user.api_key)