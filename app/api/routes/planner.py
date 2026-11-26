from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.orchestration.graph import planner_graph


router = APIRouter()


class PlannerRequest(BaseModel):

    message: str = Field(
        min_length=5,
        max_length=10000
    )


@router.post("/plan")
async def generate_plan(request: PlannerRequest):

    try:

        result = await planner_graph.ainvoke({
            "user_request": request.message,
            "status": "pending"
        })

        if result["status"] == "failed":
            raise HTTPException(
                status_code=502,
                detail="Planner execution failed"
            )

        return {
            "success": True,
            "status": result["status"],
            "plan": result["execution_plan"]
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=502,
            detail="Unable to generate execution plan"
        )