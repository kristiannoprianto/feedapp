from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import feedback

apps = FastAPI()

origins = ["*"]

apps.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@apps.get("/")
def root():
    return {"message": "Welcome!"}


apps.include_router(feedback.router)
