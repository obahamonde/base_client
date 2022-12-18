from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def api():
    return "Welcome!"

