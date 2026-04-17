from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1, max_length=255)
    price: float = Field(..., gt = 0)

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int
    model_config = ConfigDict(
        from_attribute=True
    )

class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str]  = Field(None, min_length=1, max_length=255)
    price: Optional[float]  = Field(None, gt = 0)
