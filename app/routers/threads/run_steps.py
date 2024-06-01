from fastapi import APIRouter
from pydantic import BaseModel
from openai.types.beta.threads.runs.run_step import RunStep
from openai.pagination import SyncCursorPage

router = APIRouter(
    tags=["threads/runs/steps"],
    responses={404: {"description": "Not found"}},
)


# curl https://api.openai.com/v1/threads/thread_abc123/runs/run_abc123/steps/step_abc123 \
#   -H "Authorization: Bearer $OPENAI_API_KEY" \
#   -H "Content-Type: application/json" \
#   -H "OpenAI-Beta: assistants=v2"
@router.get("/v1/threads/{thread_id}/runs/{run_id}/steps/{step_id}")
async def retrieve_run_step(thread_id: str, run_id: str, step_id: str) -> RunStep:
    return {
        "id": "step_abc123",
        "object": "thread.run.step",
        "created_at": 1699063291,
        "run_id": "run_abc123",
        "assistant_id": "asst_abc123",
        "thread_id": "thread_abc123",
        "type": "message_creation",
        "status": "completed",
        "cancelled_at": None,
        "completed_at": 1699063291,
        "expired_at": None,
        "failed_at": None,
        "last_error": None,
        "step_details": {
            "type": "message_creation",
            "message_creation": {"message_id": "msg_abc123"},
        },
        "usage": {"prompt_tokens": 123, "completion_tokens": 456, "total_tokens": 579},
    }
