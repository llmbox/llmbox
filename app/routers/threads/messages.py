from fastapi import APIRouter
from pydantic import BaseModel
from openai.types.beta.threads import Message
from openai.pagination import SyncCursorPage

router = APIRouter(
    tags=["threads/messages"],
    responses={404: {"description": "Not found"}},
)





@router.post("/v1/threads/{thread_id}/messages")
async def create_message(thread_id: str, message: Message):
    return {
        "id": "msg_abc123",
        "object": "thread.message",
        "created_at": 1713226573,
        "assistant_id": None,
        "thread_id": "thread_abc123",
        "run_id": None,
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": {
                    "value": "How does AI work? Explain it in simple terms.",
                    "annotations": [],
                },
            }
        ],
        "attachments": [],
        "metadata": {},
    }


@router.get("/v1/threads/{thread_id}/messages")
async def list_messages(thread_id: str) -> SyncCursorPage[Message]:
    return {
        "object": "list",
        "data": [
            {
                "id": "msg_abc123",
                "object": "thread.message",
                "created_at": 1699016383,
                "assistant_id": None,
                "thread_id": "thread_abc123",
                "run_id": None,
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": {
                            "value": "How does AI work? Explain it in simple terms.",
                            "annotations": [],
                        },
                    }
                ],
                "attachments": [],
                "metadata": {},
            },
            {
                "id": "msg_abc456",
                "object": "thread.message",
                "created_at": 1699016383,
                "assistant_id": None,
                "thread_id": "thread_abc123",
                "run_id": None,
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": {"value": "Hello, what is AI?", "annotations": []},
                    }
                ],
                "attachments": [],
                "metadata": {},
            },
        ],
        "first_id": "msg_abc123",
        "last_id": "msg_abc456",
        "has_more": False,
    }


@router.get("/v1/threads/{thread_id}/messages/{message_id}")
async def retrieve_message(thread_id: str, message_id: str)-> Message:
    return {
        "id": "msg_abc123",
        "object": "thread.message",
        "created_at": 1699017614,
        "assistant_id": null,
        "thread_id": "thread_abc123",
        "run_id": null,
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": {
                    "value": "How does AI work? Explain it in simple terms.",
                    "annotations": [],
                },
            }
        ],
        "attachments": [],
        "metadata": {},
    }


@router.patch("/v1/threads/{thread_id}/messages/{message_id}")
async def modify_message(thread_id: str, message_id: str, message: Message):
    return {
        "id": "msg_abc123",
        "object": "thread.message",
        "created_at": 1699017614,
        "assistant_id": None,
        "thread_id": "thread_abc123",
        "run_id": None,
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": {
                    "value": "How does AI work? Explain it in simple terms.",
                    "annotations": [],
                },
            }
        ],
        "file_ids": [],
        "metadata": {"modified": "true", "user": "abc123"},
    }


@router.delete("/v1/threads/{thread_id}/messages/{message_id}")
async def delete_message(thread_id: str, message_id: str):
    return {"id": "msg_abc123", "object": "thread.message.deleted", "deleted": True}
