from langgraph.graph import StateGraph, END

from state import AgentState
from triage import triage
from retrieval import retrieve
from generator import generate_answer
from verifier import verify


def retrieval_node(state: AgentState) -> AgentState:
    """Retrieve relevant documents."""

    docs = retrieve(state["question"])

    state["retrieved_docs"] = docs

    state["sources"] = [
        {
            "source_id": doc.metadata.get("source", "Unknown"),
            "passage": doc.page_content[:200]
        }
        for doc in docs
    ]

    return state


def generator_node(state: AgentState) -> AgentState:
    """Generate answer using retrieved documents."""

    answer = generate_answer(
        state["question"],
        state["retrieved_docs"]
    )

    state["answer"] = answer

    return state


def route_question(state: AgentState):
    """
    Decide the next node based on triage classification.
    """
    return state["classification"]


# Build Graph
builder = StateGraph(AgentState)

# Nodes
builder.add_node("triage", triage)
builder.add_node("retrieval", retrieval_node)
builder.add_node("generator", generator_node)
builder.add_node("verifier", verify)

# Entry point
builder.set_entry_point("triage")

# Conditional Routing
builder.add_conditional_edges(
    "triage",
    route_question,
    {
        "answerable": "retrieval",
        "requires_clarification": END,
        "requires_escalation": END,
        "out_of_scope": END,
        "safe_failure": END,
    },
)

# Normal flow
builder.add_edge("retrieval", "generator")
builder.add_edge("generator", "verifier")
builder.add_edge("verifier", END)

# Compile graph
graph = builder.compile()