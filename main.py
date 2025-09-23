from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Agora meu arquivo tá funcionando bem!"}