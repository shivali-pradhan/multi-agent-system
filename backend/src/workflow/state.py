from typing import Literal, TypedDict, Annotated, Optional
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class State(TypedDict):
  query: str
  # messages: Annotated[list[BaseMessage], add_messages]
  route: Optional[Literal['RAG', 'SQL']]
  rag_result: Optional[str]
  sql_result: Optional[str]
