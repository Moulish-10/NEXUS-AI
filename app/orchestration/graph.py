from langgraph.graph import StateGraph, START, END

from app.orchestration.state import AgentState
from app.agents.planner import create_plan


def planner_node(state: AgentState):

    try:
        plan = create_plan(
            state["user_request"]
        )

        return {
            "execution_plan": plan.model_dump(),
            "status": "planned",
            "error": ""
        }

    except Exception as e:

        return {
            "status": "failed",
            "error": str(e)
        }


def build_planner_graph():

    workflow = StateGraph(AgentState)

    workflow.add_node(
        "planner",
        planner_node
    )

    workflow.add_edge(
        START,
        "planner"
    )

    workflow.add_edge(
        "planner",
        END
    )

    return workflow.compile()


planner_graph = build_planner_graph()