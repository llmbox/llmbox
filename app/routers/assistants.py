from fastapi import APIRouter
from openai.types.beta.assistant import Assistant
from openai.pagination import SyncCursorPage

router = APIRouter(
    tags=["assistants"],
    responses={404: {"description": "Not found"}},
)

@router.post("/v1/assistants")
async def create_assistant(asssistant: Assistant) -> Assistant:
    return {
        "id": "asst_abc123",
        "object": "assistant",
        "created_at": 1698984975,
        "name": "Math Tutor",
        "description": None,
        "model": "gpt-4-turbo",
        "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
        "tools": [{"type": "code_interpreter"}],
        "metadata": {},
        "top_p": 1.0,
        "temperature": 1.0,
        "response_format": "auto",
    }


@router.get("/v1/assistants")
async def list_assistants() -> SyncCursorPage[Assistant]:
    return {
        "object": "list",
        "data": [
            {
                "id": "asst_abc123",
                "object": "assistant",
                "created_at": 1698982736,
                "name": "Coding Tutor",
                "description": None,
                "model": "gpt-4-turbo",
                "instructions": "You are a helpful assistant designed to make me better at coding!",
                "tools": [],
                "tool_resources": {},
                "metadata": {},
                "top_p": 1.0,
                "temperature": 1.0,
                "response_format": "auto",
            },
            {
                "id": "asst_abc456",
                "object": "assistant",
                "created_at": 1698982718,
                "name": "My Assistant",
                "description": None,
                "model": "gpt-4-turbo",
                "instructions": "You are a helpful assistant designed to make me better at coding!",
                "tools": [],
                "tool_resources": {},
                "metadata": {},
                "top_p": 1.0,
                "temperature": 1.0,
                "response_format": "auto",
            },
            {
                "id": "asst_abc789",
                "object": "assistant",
                "created_at": 1698982643,
                "name": None,
                "description": None,
                "model": "gpt-4-turbo",
                "instructions": None,
                "tools": [],
                "tool_resources": {},
                "metadata": {},
                "top_p": 1.0,
                "temperature": 1.0,
                "response_format": "auto",
            },
        ],
        "first_id": "asst_abc123",
        "last_id": "asst_abc789",
        "has_more": False,
    }


@router.get("/v1/assistants/{assistant_id}")
async def get_assistant(assistant_id: str) -> Assistant:
    return {
        "id": "asst_abc123",
        "object": "assistant",
        "created_at": 1699009709,
        "name": "HR Helper",
        "description": None,
        "model": "gpt-4-turbo",
        "instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies.",
        "tools": [{"type": "file_search"}],
        "metadata": {},
        "top_p": 1.0,
        "temperature": 1.0,
        "response_format": "auto",
    }


@router.post("v1/assistants/{assistant_id}")
async def modify_assistant(assistant_id: str, assistant: Assistant):
    return {
        "id": "asst_123",
        "object": "assistant",
        "created_at": 1699009709,
        "name": "HR Helper",
        "description": None,
        "model": "gpt-4-turbo",
        "instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies. Always response with info from either of the files.",
        "tools": [{"type": "file_search"}],
        "tool_resources": {"file_search": {"vector_store_ids": []}},
        "metadata": {},
        "top_p": 1.0,
        "temperature": 1.0,
        "response_format": "auto",
    }


@router.delete("/v1/assistants/{assistant_id}")
async def delete_assistant(assistant_id: str):
    return {"id": "asst_abc123", "object": "assistant.deleted", "deleted": True}
