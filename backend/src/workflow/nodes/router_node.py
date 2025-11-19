from langchain.messages import SystemMessage, HumanMessage
from backend.src.workflow.state import State
from backend.src.models.router_model import router_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.messages import SystemMessage, HumanMessage
from pydantic import BaseModel
from typing import Literal

class RouterResponse(BaseModel):
  route: Literal['rag', 'sql']

router_parser = PydanticOutputParser(pydantic_object=RouterResponse)

# Configure the behaviour of LLM for grounds of classification of query into RAG or SQL
# Also send some knowledge about the database like its schema, so the LLM can match context/keywords from query
ROUTER_SYSTEM_MESSAGE = SystemMessage(
  content="""
  You are a routing agent. Determine which type of processing the user query requires.
  Options:
  - rag : For information retrieval, explanations from documents.
  - sql : For structured database queries, analytics, metrics, filters, chart visualization.
  """
)


def router_node(state: State):
  query = state['query']
  template = PromptTemplate(
    template="""
    Classify this user query as a RAG query or SQL query. 
    Follow the system message strictly for decision making.
    Query: {query}
    {format_instruction}
    """,
    input_variables=['query'],
    partial_variables={'format_instruction': router_parser.get_format_instructions()} 
  )
  prompt = template.invoke({'query': query})
  messages = [
    ROUTER_SYSTEM_MESSAGE,
    HumanMessage(content=prompt.text),  
  ]
  raw_output = router_model.invoke(messages).content
  parsed_output = router_parser.parse(raw_output)
  decision = parsed_output.route.upper()
  
  return {'route': decision}


def router_condition(state: State):
  print("LLM decision: ", state['route'])
  if state['route'] == 'RAG':
    return "rag_agent"
  elif state['route'] == 'SQL':
    return "sql_agent"
  