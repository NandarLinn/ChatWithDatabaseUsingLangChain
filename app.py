from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from db import engine
from apis import api_router
import models


models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Chat With Database Using Landchain")
app.include_router(api_router, prefix="/api/v1")
