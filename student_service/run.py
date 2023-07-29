from fastapi import FastAPI
from auth.routers import router as auth_router

app = FastAPI(
    title='student_service'
)

app.include_router(auth_router)