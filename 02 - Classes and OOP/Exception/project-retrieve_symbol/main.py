""" main.py """

from app.api import User, StockApi
from app.utils import load_data_base, Path
from app.utils import NameNotFound, NoSymbolFound

if __name__ == '__main__':

    # try name with no api
    print('Try incorrect name')
    try:
        api_key = User("John").api_key
    except NameNotFound as ex:
        print(ex.log())

    user = User("Nicolas")

    # try invalid symbol
    print('\nTry invalid symbol')
    try:
        res = StockApi.get_symbol_info('AAAAL', user)
    except NoSymbolFound as ex:
        print(repr(ex))

    # valid symbol
    print('\nValid Symbol')
    print(StockApi.get_symbol_info('MXT', user))

    try:
        symbol = "MXTRF"
        api_key = User("MacKohnley").api_key
    except NameNotFound as ex:
        print(f"{type(ex).__name__} falls back to database")
        db = load_data_base(Path.data())

        for data in db:
            if data.get("symbol", None) == symbol:
                print(data)
