from llm import llm
from rag.retriever import retrieve
from memory.memory import save_memory


def account_agent(state):

    query = state["query"].lower()

    if "close account" in query:

        state["approval_required"] = True

    context = retrieve(state["query"])
    state["retrieved_context"] = context

    prompt = f"""
You are Account Support.

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


