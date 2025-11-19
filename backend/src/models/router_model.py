from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from backend.src.core.config import settings

llm = HuggingFaceEndpoint(
  repo_id = settings.ROUTER_MODEL_NAME,
  task = "text-generation",
  huggingfacehub_api_token = settings.HUGGINGFACEHUB_API_TOKEN
)
router_model = ChatHuggingFace(llm=llm)
 