import json

from graph import graph


def main():

    print("=" * 60)
    print("🚀 OrbitDesk AI Support Agent")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:

        question = input("\nAsk a question: ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        state = {
            "question": question,
            "classification": "",
            "retrieved_docs": [],
            "answer": "",
            "sources": [],
            "confidence": 0.0,
            "requires_human": False,
            "reason": "",
            "clarification_question": None,
            "warnings": [],
            "verified": False
        }

        result = graph.invoke(state)

        response = {
            "classification": result["classification"],
            "answer": result["answer"],
            "sources": result["sources"],
            "confidence": result["confidence"],
            "requires_human": result["requires_human"],
            "reason": result["reason"],
            "clarification_question": result["clarification_question"],
            "warnings": result["warnings"]
        }

        print("\nResponse:\n")
        print(json.dumps(response, indent=4))


if __name__ == "__main__":
    main()