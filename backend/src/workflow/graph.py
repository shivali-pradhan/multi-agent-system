from langgraph.graph import StateGraph, START, END
from backend.src.workflow.state import State
from backend.src.workflow.nodes.rag_node import rag_node
from backend.src.workflow.nodes.sql_node import sql_node
from backend.src.workflow.nodes.router_node import router_node, router_condition

graph = StateGraph(State)

# Nodes
graph.add_node('router', router_node)
graph.add_node('rag_agent', rag_node)
graph.add_node('sql_agent', sql_node)

# Edges
graph.add_edge(START, 'router')
graph.add_conditional_edges('router', router_condition)
graph.add_edge('rag_agent', END)
graph.add_edge('sql_agent', END)

workflow = graph.compile()
