from typing import List,Optional
from sqlmodel import Field,Relationship,SQLModel

class User(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    username:str =Field(index=True, unique=True)

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    category: "Category"=Relationship(back_populates="products")
    reviews: List["Review"]=Relationship(back_populates="product")

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    product: List[Product] = Relationship(back_populates="category")

class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    rating: int = Field(foreign_key="user.id")
    user: User = Field(back_populates="reviews")
    product_id: int = Field(foreign_key="product.id")
    product: Product = Relationship(back_populates="reviews")   
    