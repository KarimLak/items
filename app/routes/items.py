from typing import List
from fastapi import APIRouter, Depends, FastAPI, HTTPException
from app.database import get_db
from app.schemas.items import ItemCreate, ItemResponse, ItemUpdate
from app.service.item import ItemService, get_item_service

router = APIRouter()

@router.get("/items", response_model= List[ItemResponse])
def read_items(service : ItemService = Depends(get_item_service), db=Depends(get_db)):
    return service.get_all_items(db)

@router.get("/items/{item_id}", response_model = ItemResponse)
def read_items(item_id: int, service : ItemService = Depends(get_item_service)):
    return service.get_item(item_id)

@router.post("/items", response_model = ItemResponse)
def create_item(payload: ItemCreate, service : ItemService = Depends(get_item_service)):
    return service.new_item(payload)
    
@router.patch("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, payload: ItemUpdate, service : ItemService = Depends(get_item_service)):
    return service.modify_item(item_id, payload)

@router.delete("/items/{item_id}", response_model = ItemResponse)
def delete_item(item_id: int, service : ItemService = Depends(get_item_service)):
    return service.remove_item(item_id)
