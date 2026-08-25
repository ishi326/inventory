from fastapi import FastAPI
from routes import store, admin

app = FastAPI()

app.include_router(store.router)
app.include_router(admin.router)

@app.get("/")
def read_root():
    return {"message": "Frostreats inventory system is running"}