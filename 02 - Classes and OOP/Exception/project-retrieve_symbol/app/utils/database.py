# database.py
import json


__all__ = ["load_data_base"]

def load_data_base(database_location):
    """

    Args:
        database_location (str): file location

    Returns:
        json dictionary

    """
    with open(database_location, 'r') as f:
        data = json.load(f)
    return data