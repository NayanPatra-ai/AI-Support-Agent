from retrieval import retrieve

question = "How do I schedule exports?"

results = retrieve(question)

for i, doc in enumerate(results, start=1):
    print(f"\n----- Document {i} -----")
    print(doc.metadata)
    print(doc.page_content[:500])