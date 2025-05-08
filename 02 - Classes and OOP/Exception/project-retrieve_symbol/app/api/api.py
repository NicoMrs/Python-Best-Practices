""" Api requests """

import requests
from ..utils import NoSymbolFound

__all__ = ['StockApi']

class StockApi:

    base_url = 'https://financialmodelingprep.com/stable/'

    @classmethod
    def get_symbol_info(cls, symbol, user):
        url = f'{cls.base_url}search-symbol?query={symbol}&apikey={user.api_key}'
        res = requests.get(url).json()

        if not res:
            raise NoSymbolFound(f"No symbol found for {symbol!r}")
        return res


if __name__ == '__main__':

    from user import User
    user = User("Nicolas")