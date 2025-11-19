from fastapi import FastAPI
from pydantic import BaseModel
from backend.src.workflow.graph import workflow

app = FastAPI(
  title="Multi-Agent System"
)

# API request and response schemas --> temporarily here, then shift them to organised files later
class QueryRequest(BaseModel):
  query: str

class QueryResponse(BaseModel):
  result: dict

@app.post("/query", response_model=QueryResponse)
async def query_endpoint(payload: QueryRequest):
  result = workflow.invoke({'query': payload.query})
  print("Result: ", result)
  return QueryResponse(result=result)