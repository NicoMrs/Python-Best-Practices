# utils.py

def run_from(func):
    def inner(*args, **kwargs):
        print(f"{func.__name__!r}")
        return func(*args, **kwargs)
    return inner
