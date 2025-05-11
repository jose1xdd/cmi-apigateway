from fastapi import FastAPI
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    print("pinga")
    name = os.getenv("NAME", "Valor por defecto")
    return {"name": name}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))  # Usa 8000 si PORT no está definido
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
