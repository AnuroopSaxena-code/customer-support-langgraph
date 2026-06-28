from llm import llm
from rag.retriever import retrieve
from memory.memory import save_memory


HIGH_RISK = [
    "refund",
    "cancel subscription",
    "compensation"
]


def billing_agent(state):

    query = state["query"].lower()

    state["approval_required"] = any(
        word in query for word in HIGH_RISK
    )

    context = retrieve(state["query"])
    state["retrieved_context"] = context

    prompt = f"""
You are Billing Support.

Use ONLY the following company documents.

<context>
{context}
</context>

Customer:
{state["query"]}
"""

    state["response"] = llm.invoke(prompt).content

    save_memory(
        state["conversation_id"],
        state["customer_name"],
        state["query"],
        state["response"]
    )

    return state


