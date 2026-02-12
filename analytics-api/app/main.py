from fastapi import FastAPI
import routes

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "FastAPI is running"}

app.include_router(routes.router)