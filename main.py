# # from pydantic import BaseModel,validate_call,ValidationError,StringConstraints,Field
# # from typing import Annotated
# # from fastapi import FastAPI

# # class item(BaseModel):
# #     name:str= Field(..., min_leng=4)
# #     description: str | None=None
# #     price:float
    
# # @validate_call
# # def validate_name(name: Annotated[str,StringConstraints(min_length=)]):
# #     return name

# # try:
# #     name=validate_name(name="md rashid")
# #     print("name is valid")
# # except ValidationError as error: 
# #     print(f"name is invalid{error}")

# # try:
# #     product=item(name="md_rashid", price=100.01)
# #     # print("name is valid")
# #     product_without_price=product.model_dump(exclude={'price'})
# #     print(product_without_price)
# # except ValidationError as error:
# #     print(f"name is invalid {error}")# name is valid

# # app=FastAPI()

# # @app.post("/items")
# # def create_item(items:item):
# #     return items

# # async def create_item(
# #     name:str=Body(None),
# #     description:str= Body(None),
# #     price:float=Body(...),
# #     offer:float=Body(None)
# # ):
# #     item={"name":name, "price":price}
# #     if description:
# #         item[description]=description
# #     if offer:
# #         item[offer]=offer
# #     return item     








# from fastapi import FastAPI, Depends,Header,Path,HTTPException,status
# from typing import Annotated,Any,Dict,Type
# from pydantic import BaseModel
# from datetime import date
# app=FastAPI()

# async def get_db_session():
#     print("db session> start")
#     session={"data":{1:{"name":"item one"},2:{"name":"item tow"}}}
#     try:
#         yield session
#     finally:
#         print("db session< teardown")

# Dbsession=Annotated[dict, Depends(get_db_session)]

# async def get_user(token: Annotated[str|None,Header()]=None):
#     print("checking auth..")
#     user={"username": "test_user"}
#     return user

# CurrentUser=Annotated[dict,Depends(get_user)]

# class ItemCreate(BaseModel):
#     name:str
#     price:float| None=None
    
# @app.post("/item")
# async def create_item(item:ItemCreate, db:Dbsession,user:CurrentUser):  
#     print(f"User{user['username']} creating item")
#     new_id=max(db["data"].keys()or [0])+1
#     db["data"][new_id]=item.model_dump
#     return{"id":new_id,**item.model_dump}

# @app.get()("/item{item_id}")
# async def read_item(item_id: Annotated[int,Path(ge=1)], db:Dbsession):
#     print("reading Items")
#     if item_id not in db["data"]:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item is not present")
#     return{"id": item_id, **db["data"][item_id]}







# #in a real ERP, this comes from your database(e.g, a productcategory table)
# CATEGORY_DEFINITIONS={
#     1:{"name":"laptop",
#        "fields":{"cpu_type":(str,...),"ram_gb":(int,...)}},
#     2:{"name": "t-shirt",
#        "fields":{"color":(str,...),"size":(str,"m")}},
#     3:{"name":"equipment",
#        "fields":{"voltage":(int,220),"warranty_expires_on":(date,...)}}
# }

# #create method which can generatged dynamic model
# def get_product_model_for_category(category_id: int) -> Type[BaseModel]:
#     """ Dependency: creates a dynamin pydantic model based on the cateogry."""
#     category=CATEGORY_DEFINITIONS.get(category_id)
#     if not category:
#         raise HTTPException(status_code=404,detail=f"product category {category_id} not found")
#     #base fields common to all products
#     base_fields={
#         'sku':(str,...),
#         'price':(float, Field(..., gt=0))
#     }
#     #add category specific fields
#     all_fields={**base_fields,**category["fields"]}
#     #use create model to build the class
#     ProductModel=create_model(
#         f'Dynamic{category["name"]}Model',
#         **all_fields
#     )
#     return ProductModel
    
# app.post("/products/{category_id}")
# async def create_dynamic_product(
#         category_id:int,
#         request_body:dict[str,any]):
    
#     Model= get_product_model_for_category(category_id)
#     try:
#         validate_product=Model(**request_body)
#     except Exception as error:
#         raise HTTPException(status_code=422,detail=error)
#     return{
#         "message":"product created successfully",
#         "product": validate_product.model_dump()
#     }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


# #whatis sqlmodel?



words=['apple','banana','apple','banana','orange','apple']
word_count={}
# word_count['hey']
for word in words:
    word_count[word]=word_count.get(word,0)+1
print(word_count)