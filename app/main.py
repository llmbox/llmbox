from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .routers import assistants
from .routers.threads import threads, messages, runs, run_steps

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(assistants.router)
app.include_router(threads.router)
app.include_router(messages.router)
app.include_router(runs.router)
app.include_router(run_steps.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
