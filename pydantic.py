from fastapi import FastAPI,Body
from pydantic import BaseModel,Field

app=FastAPI()

class Item(BaseModel):
    name:str=Field(...,min_length=4)
    description:str| None=None
    price:float
    
class offer(BaseModel):
    offer:str

@app.post("/item")
async def create_item(
    item:Item=Body(...),
    offer:offer=Body(...)):
    return {"item":item,"offer":offer}

# @app.post("/item")
# async def create_item(item:Item):
#     return item

#body met
# @app.post('/items')
# async def create_item(
#     name:str=Body(...),
#     description:str=Body(None),
#     price:float=Body(...),
#     offer:float=Body(None)
# ):
#     item={"name":name,"price":price }
#     if description:
#         item['description']=description
#     if offer:
#         item['offer']=offer
#     return item