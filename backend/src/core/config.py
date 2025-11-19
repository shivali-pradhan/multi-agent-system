from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  HUGGINGFACEHUB_API_TOKEN: str
  ROUTER_MODEL_NAME: str

  class Config:
    env_file = ".env"

settings = Settings()