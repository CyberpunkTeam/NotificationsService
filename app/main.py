from fastapi import FastAPI
from .routers import notifications, state


app = FastAPI()


app.include_router(notifications.router)
app.include_router(state.router)
