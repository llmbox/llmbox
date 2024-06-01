from fastapi import APIRouter
from pydantic import BaseModel
from openai.types.beta.threads.run import Run
from openai.types.beta.threads.run_submit_tool_outputs_params import RunSubmitToolOutputsParamsBase
from openai.pagination import SyncCursorPage

router = APIRouter(
    tags=["threads/runs"],
    responses={404: {"description": "Not found"}},
)


@router.get("/v1/threads/{thread_id}/runs")
async def create_runs(thread_id: str, run: Run) -> Run:
    return {
        "id": "run_abc123",
        "object": "thread.run",
        "created_at": 1699063290,
        "assistant_id": "asst_abc123",
        "thread_id": "thread_abc123",
        "status": "queued",
        "started_at": 1699063290,
        "expires_at": None,
        "cancelled_at": None,
        "failed_at": None,
        "completed_at": 1699063291,
        "last_error": None,
        "model": "gpt-4-turbo",
        "instructions": None,
        "incomplete_details": None,
        "tools": [{"type": "code_interpreter"}],
        "metadata": {},
        "usage": None,
        "temperature": 1.0,
        "top_p": 1.0,
        "max_prompt_tokens": 1000,
        "max_completion_tokens": 1000,
        "truncation_strategy": {"type": "auto", "last_messages": None},
        "response_format": "auto",
        "tool_choice": "auto",
    }


@router.post("/v1/threads/{thread_id}/runs")
async def create_thread_and_run(thread_id: str, run: Run) -> Run:
    return {
        "id": "run_abc123",
        "object": "thread.run",
        "created_at": 1699076792,
        "assistant_id": "asst_abc123",
        "thread_id": "thread_abc123",
        "status": "queued",
        "started_at": None,
        "expires_at": 1699077392,
        "cancelled_at": None,
        "failed_at": None,
        "completed_at": None,
        "required_action": None,
        "last_error": None,
        "model": "gpt-4-turbo",
        "instructions": "You are a helpful assistant.",
        "tools": [],
        "tool_resources": {},
        "metadata": {},
        "temperature": 1.0,
        "top_p": 1.0,
        "max_completion_tokens": None,
        "max_prompt_tokens": None,
        "truncation_strategy": {"type": "auto", "last_messages": None},
        "incomplete_details": None,
        "usage": None,
        "response_format": "auto",
        "tool_choice": "auto",
    }


@router.get("/v1/threads/{thread_id}/runs")
async def list_runs(thread_id: str) -> SyncCursorPage[Run]:
    return {
        "object": "list",
        "data": [
            {
                "id": "run_abc123",
                "object": "thread.run",
                "created_at": 1699075072,
                "assistant_id": "asst_abc123",
                "thread_id": "thread_abc123",
                "status": "completed",
                "started_at": 1699075072,
                "expires_at": None,
                "cancelled_at": None,
                "failed_at": None,
                "completed_at": 1699075073,
                "last_error": None,
                "model": "gpt-4-turbo",
                "instructions": None,
                "incomplete_details": None,
                "tools": [{"type": "code_interpreter"}],
                "tool_resources": {
                    "code_interpreter": {"file_ids": ["file-abc123", "file-abc456"]}
                },
                "metadata": {},
                "usage": {
                    "prompt_tokens": 123,
                    "completion_tokens": 456,
                    "total_tokens": 579,
                },
                "temperature": 1.0,
                "top_p": 1.0,
                "max_prompt_tokens": 1000,
                "max_completion_tokens": 1000,
                "truncation_strategy": {"type": "auto", "last_messages": None},
                "response_format": "auto",
                "tool_choice": "auto",
            },
            {
                "id": "run_abc456",
                "object": "thread.run",
                "created_at": 1699063290,
                "assistant_id": "asst_abc123",
                "thread_id": "thread_abc123",
                "status": "completed",
                "started_at": 1699063290,
                "expires_at": None,
                "cancelled_at": None,
                "failed_at": None,
                "completed_at": 1699063291,
                "last_error": None,
                "model": "gpt-4-turbo",
                "instructions": None,
                "incomplete_details": None,
                "tools": [{"type": "code_interpreter"}],
                "tool_resources": {
                    "code_interpreter": {"file_ids": ["file-abc123", "file-abc456"]}
                },
                "metadata": {},
                "usage": {
                    "prompt_tokens": 123,
                    "completion_tokens": 456,
                    "total_tokens": 579,
                },
                "temperature": 1.0,
                "top_p": 1.0,
                "max_prompt_tokens": 1000,
                "max_completion_tokens": 1000,
                "truncation_strategy": {"type": "auto", "last_messages": None},
                "response_format": "auto",
                "tool_choice": "auto",
            },
        ],
        "first_id": "run_abc123",
        "last_id": "run_abc456",
        "has_more": False,
    }


# curl https://api.openai.com/v1/threads/thread_abc123/runs/run_abc123 \
#   -H "Authorization: Bearer $OPENAI_API_KEY" \
#   -H "OpenAI-Beta: assistants=v2"


@router.get("/v1/threads/{thread_id}/runs/{run_id}")
async def retrieve_run(thread_id: str, run_id: str) -> Run:
    return {
        "id": "run_abc123",
        "object": "thread.run",
        "created_at": 1699075072,
        "assistant_id": "asst_abc123",
        "thread_id": "thread_abc123",
        "status": "completed",
        "started_at": 1699075072,
        "expires_at": None,
        "cancelled_at": None,
        "failed_at": None,
        "completed_at": 1699075073,
        "last_error": None,
        "model": "gpt-4-turbo",
        "instructions": None,
        "incomplete_details": None,
        "tools": [{"type": "code_interpreter"}],
        "metadata": {},
        "usage": {"prompt_tokens": 123, "completion_tokens": 456, "total_tokens": 579},
        "temperature": 1.0,
        "top_p": 1.0,
        "max_prompt_tokens": 1000,
        "max_completion_tokens": 1000,
        "truncation_strategy": {"type": "auto", "last_messages": None},
        "response_format": "auto",
        "tool_choice": "auto",
    }


# curl https://api.openai.com/v1/threads/thread_abc123/runs/run_abc123 \
#   -H "Authorization: Bearer $OPENAI_API_KEY" \
#   -H "Content-Type: application/json" \
#   -H "OpenAI-Beta: assistants=v2" \
#   -d '{
#     "metadata": {
#       "user_id": "user_abc123"
#     }
#   }'
@router.patch("/v1/threads/{thread_id}/runs/{run_id}")
async def modify_run(thread_id: str, run_id: str, run: Run) -> Run:
    return {
        "id": "run_abc123",
        "object": "thread.run",
        "created_at": 1699075072,
        "assistant_id": "asst_abc123",
        "thread_id": "thread_abc123",
        "status": "completed",
        "started_at": 1699075072,
        "expires_at": None,
        "cancelled_at": None,
        "failed_at": None,
        "completed_at": 1699075073,
        "last_error": None,
        "model": "gpt-4-turbo",
        "instructions": None,
        "incomplete_details": None,
        "tools": [{"type": "code_interpreter"}],
        "tool_resources": {
            "code_interpreter": {"file_ids": ["file-abc123", "file-abc456"]}
        },
        "metadata": {"user_id": "user_abc123"},
        "usage": {"prompt_tokens": 123, "completion_tokens": 456, "total_tokens": 579},
        "temperature": 1.0,
        "top_p": 1.0,
        "max_prompt_tokens": 1000,
        "max_completion_tokens": 1000,
        "truncation_strategy": {"type": "auto", "last_messages": None},
        "response_format": "auto",
        "tool_choice": "auto",
    }


# curl https://api.openai.com/v1/threads/thread_123/runs/run_123/submit_tool_outputs \
#   -H "Authorization: Bearer $OPENAI_API_KEY" \
#   -H "Content-Type: application/json" \
#   -H "OpenAI-Beta: assistants=v2" \
#   -d '{
#     "tool_outputs": [
#       {
#         "tool_call_id": "call_001",
#         "output": "70 degrees and sunny."
#       }
#     ]
#   }'


@router.post("/v1/threads/{thread_id}/runs/{run_id}/submit_tool_outputs")
async def submit_tool_outputs( thread_id: str, run_id: str, tool_outputs) -> Run:
    return {
        "id": "run_123",
        "object": "thread.run",
        "created_at": 1699075592,
        "assistant_id": "asst_123",
        "thread_id": "thread_123",
        "status": "queued",
        "started_at": 1699075592,
        "expires_at": 1699076192,
        "cancelled_at": None,
        "failed_at": None,
        "completed_at": None,
        "last_error": None,
        "model": "gpt-4-turbo",
        "instructions": None,
        "tools": [
            {
                "type": "function",
                "function": {
                    "name": "get_current_weather",
                    "description": "Get the current weather in a given location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "unit": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                            },
                        },
                        "required": ["location"],
                    },
                },
            }
        ],
        "metadata": {},
        "usage": None,
        "temperature": 1.0,
        "top_p": 1.0,
        "max_prompt_tokens": 1000,
        "max_completion_tokens": 1000,
        "truncation_strategy": {"type": "auto", "last_messages": None},
        "response_format": "auto",
        "tool_choice": "auto",
    }

@router.post("/v1/threads/{thread_id}/runs/{run_id}/cancel")
async def cancel_run(thread_id: str, run_id: str) -> Run:
    return {
  "id": "run_abc123",
  "object": "thread.run",
  "created_at": 1699076126,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "cancelling",
  "started_at": 1699076126,
  "expires_at": 1699076726,
  "cancelled_at": None,
  "failed_at": None,
  "completed_at": None,
  "last_error": None,
  "model": "gpt-4-turbo",
  "instructions": "You summarize books.",
  "tools": [
    {
      "type": "file_search"
    }
  ],
  "tool_resources": {
    "file_search": {
      "vector_store_ids": ["vs_123"]
    }
  },
  "metadata": {},
  "usage": None,
  "temperature": 1.0,
  "top_p": 1.0,
  "response_format": "auto"
}

