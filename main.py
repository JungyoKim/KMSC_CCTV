from fastapi import FastAPI
import uvicorn
import socket

app = FastAPI()

@app.get("/")
async def root():
    data = open("memory.txt", "r").read()
    return {"img": data}

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)