from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router

import uvicorn

app = FastAPI()

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")



if __name__ == "__main__":
    uvicorn.run("main:app", port=8080)