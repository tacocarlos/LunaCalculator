from fastapi import APIRouter
import numpy as np
from .eigen.value import power

router = APIRouter()

@router.get("/matrix/random")
async def rand_matrix(width: int = 3, height: int = 3):
    return {
        "matrix": np.random.rand(width, height).tolist()
    }

router.include_router(power.router)