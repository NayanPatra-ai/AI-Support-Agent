from typing import TypedDict, List, Optional


class Source(TypedDict):
    source_id: str
    passage: str


class AgentState(TypedDict):
    question: str
    classification: str

    retrieved_docs: list

    answer: str

    sources: List[Source]

    confidence: float

    requires_human: bool

    reason: str

    clarification_question: Optional[str]

    warnings: List[str]

    verified: bool