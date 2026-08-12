from fastapi import FastAPI
from routes import store

app = FastAPI()

app.include_router(store.router)

@app.get("/")
def read_root():
    return {"message": "Frostreats inventory system is running"}