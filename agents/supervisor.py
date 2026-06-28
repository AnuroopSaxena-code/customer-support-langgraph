from llm import llm


def supervisor_agent(state):

    prompt = f"""
Improve this response.

Keep it polite.

Do not change the meaning.

Do NOT include any introductory, explanatory, or concluding text (such as "Here is an improved version of the response:", "Changes made:", or notes). Output ONLY the polished response text directly.

Response:
{state["response"]}
"""

    state["response"] = llm.invoke(prompt).content

    return state

