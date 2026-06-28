from langgraph.graph import StateGraph
from langgraph.graph import END

from state import CustomerSupportState

from agents.classifier import classifier

from agents.sales import sales_agent
from agents.technical import technical_agent
from agents.billing import billing_agent
from agents.account import account_agent
from agents.supervisor import supervisor_agent
from agents.memory_agent import memory_agent
from agents.human_review import human_review


def router(state):

    intent = state["intent"].lower()

    if "sales" in intent:
        return "sales"

    if "technical" in intent:
        return "technical"

    if "billing" in intent:
        return "billing"

    if "account" in intent:
        return "account"

    if "memory" in intent:
        return "memory"

    return "supervisor"


def approval_router(state):

    if state["approval_required"]:
        return "review"

    return "supervisor"


workflow = StateGraph(CustomerSupportState)

workflow.add_node("classifier", classifier)

workflow.add_node("sales", sales_agent)
workflow.add_node("technical", technical_agent)
workflow.add_node("billing", billing_agent)
workflow.add_node("account", account_agent)

workflow.add_node("memory", memory_agent)
workflow.add_node("review", human_review)

workflow.add_node("supervisor", supervisor_agent)

workflow.set_entry_point("classifier")

workflow.add_conditional_edges(
    "classifier",
    router
)

workflow.add_edge("sales", "supervisor")
workflow.add_edge("technical", "supervisor")

workflow.add_conditional_edges(
    "billing",
    approval_router
)

workflow.add_conditional_edges(
    "account",
    approval_router
)

workflow.add_edge("review", "supervisor")
workflow.add_edge("memory", END)

workflow.add_edge("supervisor", END)


def build_graph():

    return workflow.compile()

