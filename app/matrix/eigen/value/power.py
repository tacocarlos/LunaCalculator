import sys
from pydantic import BaseModel
from app.matrix.matrix_params import Matrix

from fastapi import APIRouter

import numpy as np


router = APIRouter()

class EigenvaluePowerMethodRequest(BaseModel):
    matrix: Matrix
    maxSteps: int = 20
    threshold: float = 0.0001

@router.post("/matrix/eigen/value/power")
async def power_method(request_data: EigenvaluePowerMethodRequest):
    A = np.array(request_data.matrix.data)
    return {
        'matrix': (A + 1).tolist()
    }