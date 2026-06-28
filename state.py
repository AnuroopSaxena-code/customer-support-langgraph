from typing import TypedDict, Optional


class CustomerSupportState(TypedDict):

    customer_name: str

    query: str

    intent: str

    department: str

    retrieved_context: str

    approval_required: bool

    approved: bool

    response: str

    conversation_id: str

    memory_result: Optional[str]
