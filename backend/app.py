from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from random import randint


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешите доступ только с вашего React-приложения
    allow_credentials=True,
    allow_methods=["*"],  # Разрешите все методы
    allow_headers=["*"],  # Разрешите все заголовки
)


@app.get("/")
async def start(request: Request) -> int:
    first = randint(1, 25)
    second = randint(1, 25)
    fird = randint(1, 25)
    while first == second or second == fird or first == fird:
        if first == second:
            second = randint(1, 25)
        elif second == fird:
            fird = randint(1, 25)
        elif first == fird:
            first = randint(1, 25)
    return JSONResponse(content={"data": [first, second, fird]})


if __name__ == "__main__":
    uvicorn.run(app=app)
