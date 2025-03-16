# model.py

__all__ = ["Model"]


class BaseModel:
    def __init__(self):
        print("Base Model")


class Model(BaseModel):

    def __init__(self):
        super().__init__()
        print("Standard Model")

    pass
