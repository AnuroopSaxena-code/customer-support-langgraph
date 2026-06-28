def human_review(state):

    if state["approval_required"]:

        print("\n===================")
        print("HUMAN APPROVAL")
        print("===================")

        print(state["response"])

        choice = input(
            "\nApprove? (y/n): "
        )

        state["approved"] = (
            choice.lower() == "y"
        )

        if not state["approved"]:

            state["response"] = (
                "Request rejected by supervisor."
            )

    return state
