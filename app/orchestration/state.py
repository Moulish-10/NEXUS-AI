from typing import TypedDict, Any


class AgentState(TypedDict, total=False):

    user_request: str

    execution_plan: dict[str, Any]

    status: str

    error: str