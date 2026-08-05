from pydantic_settings import BaseSettings
class Settings(BaseSettings):
 MONGODB_URI:str=""
 DATABASE_NAME:str="stepsolar"
settings=Settings()
