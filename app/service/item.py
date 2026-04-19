from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.models.items import Item
from app.schemas.items import ItemCreate, ItemResponse, ItemUpdate

class ItemService:

    def get_all_items(self, db:Session)-> List[ItemResponse]:
        try: 
            result = db.execute(select(Item))
            return result.scalars().all()
        except Exception as e:
            raise HTTPException(status_code=404, detail=e)
            
    def get_item(self, item_id: int, db:Session) -> ItemResponse:
        try:
            result = db.get(Item, item_id)
            return result
        except Exception as e:
            raise HTTPException(status_code=404, detail=e)
    
    def new_item(self, payload: ItemCreate, db:Session) -> ItemResponse:
        try:
            new_item = Item(**payload.model_dump())
            db.add(new_item)
            db.commit()
            db.refresh(new_item)
            result = db.execute(select(Item).order_by(desc(Item.id)).limit(1))
            return result.scalars().first()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=404, detail=e)
    
    def modify_item(self, item_id: int, payload: ItemUpdate, db:Session) -> ItemResponse:
        try:
            result = db.execute(
                select(Item).where(Item.id == item_id)
            )
            item = result.scalars().first()
            if not item:
                raise HTTPException(status_code=404, detail="Item not found")
            update_data = payload.model_dump(exclude_none=True)
            for key, value in update_data.items():
                setattr(item, key, value)
            db.commit()
            db.refresh(item)
            return ItemResponse.model_validate(item)
        except Exception as e:
          db.rollback()
          raise HTTPException(status_code=404, detail=e)
    
    def remove_item(self, item_id: int, db:Session) -> ItemResponse:
        try : 
            obj = db.get(Item, item_id)
            db.delete(obj)
            db.commit()
            db.refresh(obj)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=404, detail=e)

def get_item_service() -> ItemService:
    return ItemService()




