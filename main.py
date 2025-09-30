from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Teste para a apresentação!"}
