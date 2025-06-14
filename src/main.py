import uvicorn
from fastapi import FastAPI
from src.router import router as main_router
from src.library import router as library_router

app = FastAPI()
app.include_router(main_router)
app.include_router(library_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)