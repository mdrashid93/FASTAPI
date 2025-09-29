from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel,Field
from  typing import Dict,Any,Type,List,Literal
from pydantic import create_model
from datetime import date
app=FastAPI()

CATEGORY_DEFINATIONS={
    1:{"name":"laptop","fields":{"cpu_type":(str,...),"ram_gb":(int,...)}},
    2:{"name":"phone","fields":{"carrier":(str,...),"num_of_sims":(int,1)}},
    3:{"name":"T-shirt","fields":{"color":(str,...),"size":(Literal['s','m','l','xl'],...)}},
    4:{"name":"Equipment","fields":{"volatage":(int,220),"warranty_expires_on":(date,...)}}
}

#create method whic can genearate dynamic model
def get_product_model(category_id:int) -> type[BaseModel]:
    """Dependency:Create dynamic model based on category_id"""
    category=CATEGORY_DEFINATIONS.get(category_id)
    if not category:
        raise HTTPException(status_code=404,detail=f"prodcut category {category_id} not found")
    #basw fields common to all products
    base_fields={
        'sku':(str,...),
        'price':(float,Field(...,gt=0))}
    #add category specific fields
    all_fields={**base_fields,**category['fields']}
    #use create_model to build dynamic model class
    ProdductModel=create_model(
        f'DynamicProductModel_{category["name"]}Model',
        **all_fields
    )
    return ProdductModel

#post request
@app.post("/products/{category_id}")
async def create_dynamic_product(
    category_id:int,
    request_body:Dict[str,Any]
):
    Model=get_product_model(category_id)
    try:
        validate_product=Model(**request_body)
    except Exception as error:
        raise HTTPException(status_code=400,detail=error)
    return{
        "message":"product created successfully",
        "product":validate_product.model_dump()
    }
product_database={ 1:{"category_id":1,"sku":"LAP123","price":999.99,"cpu_type":"Intel i7","ram_gb":16},
        2:{"category_id":2,"sku":"PHN456","price":699.99,"carrier":"Verizon","num_of_sims":2},
        3:{"category_id":3,"sku":"TSH789","price":19.99,"color":"Blue","size":"L"},
        4:{"category_id":4,"sku":"EQP101","price":49.99,"volatage":220,"warranty_expires_on":"2025-12-31"}
    }    

@app.get("/products/{product_id}")
async def get_product(product_id):
    #dummy product data
    product_data=product_database[int(product_id)]
    if not product_data:
        raise HTTPException(status_code=404,detail=f"product {product_id} not found")
    category_id=product_data["category_id"]
    ResponseModel=get_product_model(category_id)
    response_data={
        "sku":product_data["sku"],
        "price":product_data["price"],
        **product_data["attributes"]
    }
    try:
        return ResponseModel(**response_data)
    except Exception as error:
        raise HTTPException(status_code=500,detail=f"{error}")

@app.get("/products/", response_model=list[Dict[str,Any]])
async def list_products():
    return list(product_database.values())
    
        