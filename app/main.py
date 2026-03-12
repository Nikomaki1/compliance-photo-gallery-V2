from fastapi import FastAPI
from app.models.schemas import Property

app = FastAPI(title="Compliance Photo Gallery")

@app.get("/")
async def root():
    return {"message": "Welcome to the Compliance Photo Gallery API"}

@app.post("/properties/", response_model=Property)
async def create_property(property: Property):
    """
    Test endpoint to verify Property and ImagePair models.
    """
    return property

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
