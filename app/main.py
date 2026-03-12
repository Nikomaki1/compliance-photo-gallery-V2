from fastapi import FastAPI

app = FastAPI(title="Compliance Photo Gallery")

@app.get("/")
async def root():
    return {"message": "Welcome to the Compliance Photo Gallery API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
