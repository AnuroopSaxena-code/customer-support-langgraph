from graph import build_graph


graph = build_graph()


def main():

    print("=" * 60)

    print("Customer Support Automation System")

    print("=" * 60)

    while True:

        query = input("\nCustomer: ")

        if query.lower() == "exit":
            break

        state = {
            "customer_name": "David",
            "query": query,
            "intent": "",
            "department": "",
            "retrieved_context": "",
            "approval_required": False,
            "approved": False,
            "response": "",
            "conversation_id": "demo-user",
            "memory_result": None
        }

        result = graph.invoke(state)

        print(f"\nDetected Intent : {result['intent']}")
        print(f"Approval Needed : {result['approval_required']}")

        if result.get("retrieved_context"):
            print("\nRetrieved Context:")
            print(result["retrieved_context"])
            print("-" * 40)

        print("\nAssistant:")
        print(result["response"])



if __name__ == "__main__":

    main()
