from app.services.retrieval_service import retrieve_context

query = "What is CSS?"

results = retrieve_context(query)

print(results)