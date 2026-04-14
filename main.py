from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from exceptions.custom_exceptions import TodoNotFound
from fastapi import FastAPI
from routes import todo_routes

app = FastAPI()
app.include_router(todo_routes.router)

@app.middleware("http")
async def logger(request , call_next):
    print("I am from middleware - start")

    response = await call_next(request)

    print("I am from middleware - end")
    return response

@app.exception_handler(TodoNotFound)
async def exceptionHandler(req : Request , exc : TodoNotFound):
    return JSONResponse(
        status_code=404,
        content={
            "status" :"error",
            "message" : str(exc)
        }
    )
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://127.0.0.1:5500"] if using Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)