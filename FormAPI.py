from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from python_modules import user_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_origins=["*"],
    allow_headers=["*"]
)

app.include_router(user_router.router)