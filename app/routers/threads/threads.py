from fastapi import APIRouter
from openai.types.beta.thread import Thread

router = APIRouter(
    tags=["threads"],
    responses={404: {"description": "Not found"}},
)


@router.get("/v1/threads")
async def create_thread(thread: Thread) -> Thread:
    return {
        "id": "thread_abc123",
        "object": "thread",
        "created_at": 1699012949,
        "metadata": {},
        "tool_resources": {},
    }


@router.get("/v1/threads/{thread_id}")
async def get_thread(thread_id: str) -> Thread:
    return {
        "id": "thread_abc123",
        "object": "thread",
        "created_at": 1699012949,
        "metadata": {},
        "tool_resources": {},
    }


@router.post("/v1/threads/{thread_id}")
async def modify_thread(thread_id: str, thread: Thread):
    return {
        "id": "thread_abc123",
        "object": "thread",
        "created_at": 1699014083,
        "metadata": {"modified": "true", "user": "abc123"},
        "tool_resources": {},
    }


@router.delete("/v1/threads/{thread_id}")
async def delete_thread(thread_id: str):
    return {"id": "thread_abc123", "object": "thread.deleted", "deleted": True}
