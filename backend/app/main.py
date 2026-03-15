from fastapi import FastAPI
from app.controllers import job_controller

app = FastAPI()

app.include_router(job_controller.router)

@app.get("/")
def root():
    return {"message": "AI Job Application Optimizer Backend Running"}