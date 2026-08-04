from state import AgentState


def triage(state: AgentState) -> AgentState:
    question = state["question"].lower().strip()

    # Out of scope
    if any(keyword in question for keyword in [
        "refund",
        "legal advice",
        "lawsuit",
        "subscription refund"
    ]):
        state["classification"] = "out_of_scope"
        state["answer"] = (
            "I can't issue refunds or provide legal advice. "
            "Please contact OrbitDesk support for billing or legal requests."
        )
        state["confidence"] = 1.0
        state["requires_human"] = True
        state["reason"] = (
            "The request is outside the supported capabilities of this assistant."
        )
        return state

    # Requires clarification
    if (
        "data sync" in question
        and "error" not in question
        and "connection" not in question
        and "refresh" not in question
    ):
        state["classification"] = "requires_clarification"
        state["answer"] = "More information is required before troubleshooting."
        state["clarification_question"] = (
            "Could you provide the connection type, error message, or the latest sync status?"
        )
        state["confidence"] = 0.45
        state["requires_human"] = False
        state["reason"] = "The request is too broad to provide accurate troubleshooting."
        return state

    # Requires escalation
    if (
        "render_failed" in question
        or "failed with render_failed" in question
        or "two export runs" in question
    ):
        state["classification"] = "requires_escalation"
        state["answer"] = (
            "This issue should be escalated to the support team after collecting diagnostic information."
        )
        state["confidence"] = 0.90
        state["requires_human"] = True
        state["reason"] = (
            "The documented troubleshooting steps have already been completed."
        )
        return state

    # Default
    state["classification"] = "answerable"
    return state