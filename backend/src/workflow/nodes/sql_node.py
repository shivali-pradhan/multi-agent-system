from backend.src.workflow.state import State

# Dummy function for SQL node

def sql_node(state: State):
  query = state['query']
  print("SQL node input query: ", query)
  return state