# OrbitDesk AI Support Agent

An AI-powered customer support agent built for the OrbitDesk AI Engineer Internship Assignment.

## Features

- LangGraph-based workflow
- Local Hugging Face language model
- FAISS vector search for retrieval
- Knowledge Base question answering
- Structured JSON responses
- Source references for every answer
- Multiple routing paths:
  - Answerable
  - Requires Clarification
  - Requires Escalation
  - Out of Scope

## Tech Stack

- Python 3
- LangGraph
- LangChain
- Hugging Face Transformers
- Sentence Transformers
- FAISS
- JSON Schema

## Project Structure

```
AI-Support-Agent/
│
├── app.py
├── graph.py
├── triage.py
├── retrieval.py
├── generator.py
├── verifier.py
├── state.py
├── config.py
├── knowledge_base/
├── resolved_cases.json
├── sample_questions.json
├── output_schema.json
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Support-Agent.git
cd AI-Support-Agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Workflow

```
User Question
        │
        ▼
     Triage
        │
        ▼
    Retrieval
        │
        ▼
    Generator
        │
        ▼
     Verifier
        │
        ▼
 Structured JSON Response
```

## Sample Output

```json
{
  "classification": "answerable",
  "answer": "...",
  "sources": [
    {
      "source_id": "...",
      "passage": "..."
    }
  ],
  "confidence": 0.95,
  "requires_human": false,
  "reason": "Answer verified using retrieved documentation."
}
```

## Notes

- Uses only the supplied knowledge base.
- Does not provide refunds, legal advice, or unsupported actions.
- Designed to answer both the provided sample questions and new natural-language questions.
