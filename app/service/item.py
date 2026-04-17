from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.items import Item
from app.schemas.items import ItemCreate, ItemResponse, ItemUpdate

def get_item_service() -> ItemService:
    return ItemService()

class ItemService:

    def get_all_items(self, db:Session)-> List[ItemResponse]:
        result = db.execute(select(Item))
        return result.scalars().all()

    
    def get_item(self, item_id: int) -> ItemResponse:
        for item in self.ITEMS:
            if (item.get("id") == item_id):
                return item
        raise HTTPException(status_code = 401)
    
    def new_item(self, payload: ItemCreate) -> ItemResponse:
        id = self.ITEMS[-1]["id"] + 1
        self.ITEMS.append({"id": id, **payload.model_dump()})
        return self.ITEMS[-1]
    
    def modify_item(self, item_id: int, payload: ItemUpdate) -> ItemResponse:
        for item in self.ITEMS:
            if (item.get("id") == item_id):
                item.update(payload.model_dump(exclude_none=True))
                return item
        raise HTTPException(status_code = 401)
    
    def remove_item(self, item_id: int) -> ItemResponse:
        for index, item in enumerate(self.ITEMS):
            if (item.get("id") == item_id):
                self.ITEMS.pop(index)
                return item
        raise HTTPException(status_code = 401)




