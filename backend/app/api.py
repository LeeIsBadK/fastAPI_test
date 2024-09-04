from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 

# Add CORS middleware to allow requests from the frontend
origins = [
    "http://localhost:3000",
    "localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get Route
@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Hello World"}