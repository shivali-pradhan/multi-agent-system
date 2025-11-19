from backend.src.workflow.state import State

# Dummy function for RAG node

def rag_node(state: State):
  query = state['query']
  print("RAG node input query: ", query)
  return state