""" exception management

 - UserException
    - ApiKeyNotFound
    - InvalidApiKey
    - NameNotFound
 - ApiException
     - SymbolNotFound
"""

from http import HTTPStatus

__all__ = [
    "MyBaseException",
    "UserException",
    "ApiKeyNotFound",
    "NameNotFound",
    "InvalidApiKey",
    "ApiException",
    "NoSymbolFound"
]


class MyBaseException(Exception):
    https_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_message = "There is a system error"
    user_message = None

    def __init__(self, *args):
        if args:
            self.user_message = args[0]
            super().__init__(args[1:])

    def log(self):
        data = {
            'name': type(self).__name__,
            'status': self.https_status,
            'internal message': self.internal_message,
            'user message': self.user_message
        }
        return data

    def __repr__(self):
        cls_name = type(self).__name__
        base_message = f"{cls_name}(status={self.https_status.value}"

        if self.user_message is not None:
            base_message += f", message={self.user_message!r}"
        return  base_message+')'


class UserException(MyBaseException):
    https_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_message = "There is an error on your end"

class NameNotFound(UserException):
    internal_message = "Name not found"

class ApiKeyNotFound(UserException):
    internal_message = "Api key has not been found"

class InvalidApiKey(UserException):
    internal_message = "Api key is not valid"

class ApiException(MyBaseException):
    https_status = HTTPStatus.BAD_REQUEST
    internal_message = "There is an error on our end"

class NoSymbolFound(ApiException):
    internal_message = "No symbol found"

if __name__ == '__main__':

    try:
        wrong_api_key = '??????'
        raise InvalidApiKey(f"Api found {wrong_api_key}", 1,2,3)
    except MyBaseException as err:
        print(err.log())
        print(repr(err))
        print(err.args)