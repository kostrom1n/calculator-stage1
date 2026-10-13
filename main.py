from math import isfinite
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query


app = FastAPI(title="API-калькулятор")

# Принимаем только конечные числа: без NaN и бесконечности.
Number = Annotated[float, Query(allow_inf_nan=False)]


def make_response(result: float) -> dict[str, float]:
    if not isfinite(result):
        raise HTTPException(status_code=400, detail="Результат слишком велик")
    return {"result": result}


@app.get("/add")
async def add(a: Number, b: Number):
    return make_response(a + b)


@app.get("/subtract")
async def subtract(a: Number, b: Number):
    return make_response(a - b)


@app.get("/multiply")
async def multiply(a: Number, b: Number):
    return make_response(a * b)


@app.get("/divide")
async def divide(a: Number, b: Number):
    if b == 0:
        raise HTTPException(status_code=400, detail="Деление на ноль невозможно")
    return make_response(a / b)
