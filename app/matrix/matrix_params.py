from pydantic import BaseModel

class Matrix(BaseModel):
    width: int
    height: int
    data: list[list[float]]