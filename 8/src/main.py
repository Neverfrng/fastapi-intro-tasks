from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class ProductSpecifications(BaseModel):
    size: str = Field(...)
    color: str = Field(...)
    material: str = Field(...)

class Product(BaseModel):
    name: str = Field(...)
    price: float = Field(...)
    specifications: ProductSpecifications

@app.post("/product")
async def create_product(product: Product):
    global product_id_counter, product_list
    if not product.price or product.price <= 0:
        raise HTTPException(status_code=422, detail=[{"msg": "ensure this value is greater than 0"}])
    if not product.specifications.size or not product.specifications.color or not product.specifications.material:
        raise HTTPException(status_code=422, detail=[{"msg": "specifications fields cannot be empty"}])
    product_dict = product.dict()
    product_dict["id"] = product_id_counter
    product_id_counter += 1
    product_list.append(product_dict)
    return {"message": "Product added successfully", "product": product_dict}

@app.get("/products")
async def get_products():
    return {"products": product_list}
# END
