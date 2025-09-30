from pydanticic import BaseModel
from typing import List

#review schemas\
class ReviewBase(BaseModel):
    text:str
    rating:int
class ReviewCreate(ReviewBase):
    pass
class Review(ReviewBase):
    id:int
    user_id:int
    class Config:
        from_attributes=True
#user schemas
class UserBase(BaseModel):
    username:str
class UserCreate(UserBase):
    password:str
class User(UserBase):
    id:int
    role:str
    reviews:List[Review]=[]
    class Config:
        from_attributes=True 