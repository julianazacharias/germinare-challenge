from fastapi import FastAPI

from desafio_germinare.config.settings import Settings
from desafio_germinare.routers import soybean_meal_price

settings = Settings()

app = FastAPI()

app.include_router(soybean_meal_price.router)


@app.get('/')
def read_root():
    return {'message': 'Hello World!'}
