from llm import llm

KEYWORD_MAP = {
    "Billing": [
        "refund",
        "invoice",
        "payment",
        "billing",
        "subscription",
        "cancel subscription",
        "compensation"
    ],

    "Account": [
        "password",
        "login",
        "account",
        "profile",
        "activate",
        "deactivate"
    ],

    "Technical": [
        "crash",
        "error",
        "bug",
        "upload",
        "install",
        "configuration",
        "technical"
    ],

    "Sales": [
        "price",
        "pricing",
        "plan",
        "subscription plans",
        "purchase",
        "buy"
    ]
}


MEMORY_KEYWORDS = [
    "previous issue",
    "previous support",
    "last issue",
    "remember",
    "earlier"
]


def classifier(state):

    query = state["query"].lower()

    # Detect memory requests
    if any(word in query for word in MEMORY_KEYWORDS):
        state["intent"] = "Memory"
        return state

    # Fast deterministic routing
    for intent, keywords in KEYWORD_MAP.items():
        if any(word in query for word in keywords):
            state["intent"] = intent
            return state


    # Fall back to the LLM
    prompt = f"""
Classify the customer query into exactly one of:

Sales
Technical
Billing
Account
Memory

Reply with ONLY the category.

Query:
{state["query"]}
"""

    state["intent"] = llm.invoke(prompt).content.strip()

    return state

