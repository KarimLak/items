from typing import List
from fastapi import Depends, FastAPI, HTTPException
from app.schemas.items import ItemCreate, ItemResponse, ItemUpdate
from app.service.item import ItemService, get_item_service
from app.routes.items import router
app = FastAPI()

app.include_router(router)
    



