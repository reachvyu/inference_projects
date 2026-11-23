from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def healthCheck():
    return {"message" : "Hello World I am healthy"}
