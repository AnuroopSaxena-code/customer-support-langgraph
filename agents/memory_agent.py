from memory.memory import recall_last_issue, save_memory

def memory_agent(state):

    # Save the current query so it counts as the latest query in database history
    save_memory(
        state["conversation_id"],
        state["customer_name"],
        state["query"],
        ""
    )

    issue = recall_last_issue(
        state["conversation_id"]
    )

    state["memory_result"] = issue

    state["response"] = (
        f"Your previous support issue was:\n\n{issue}"
    )

    return state

