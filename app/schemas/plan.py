from typing import Literal
from pydantic import BaseModel, Field


AgentType = Literal[
    "knowledge",
    "researcher",
    "executor",
    "reviewer",
    "response"
]


class PlanStep(BaseModel):
    step_number: int = Field(ge=1)
    assigned_agent: AgentType
    description: str
    expected_output: str


class ExecutionPlan(BaseModel):
    objective: str
    steps: list[PlanStep] = Field(min_length=1, max_length=10)
    requires_human_approval: bool
    reasoning: str