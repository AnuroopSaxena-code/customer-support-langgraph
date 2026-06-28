from llm import llm


def supervisor_agent(state):

    prompt = f"""
Improve this response.

Keep it polite.

Do not change the meaning.

Response:

{state["response"]}
"""

    state["response"] = llm.invoke(prompt).content

    return state
