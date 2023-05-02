from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from python_modules import userRouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_origins=["*"],
    allow_headers=["*"]
)

app.include_router(userRouter.router)