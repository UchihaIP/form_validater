from fastapi import FastAPI
import uvicorn

from database.connection import Settings
from routes.forms import form_router

app = FastAPI()
settings = Settings()

app.include_router(form_router)


@app.on_event("startup")
async def init_db():
    """При запуске приложения заполняет БД тестовыми данными, если их нет."""
    if checking_data := await settings.check_existence_of_data_in_database():
        return
    await settings.initialize_database()


@app.get("/")
async def home():
    return {"Greetings": "Hello, friend"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0",
                port=8080, reload=True)
