from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class ProductSpecs(BaseModel):
    size_value: str = Field(..., description="Размер товара")
    color_value: str = Field(..., description="Цвет товара")
    material_type: str = Field(..., description="Материал изготовления товара")


class ProductCreateRequest(BaseModel):
    product_name: str = Field(..., description="Наименование товара")
    product_price: float = Field(..., gt=0, description="Стоимость товара (положительное число)")
    product_specs: ProductSpecs = Field(..., description="Спецификации товара")


class BasicProductResponse(BaseModel):
    product_name: str = Field(..., description="Наименование товара")
    product_price: float = Field(..., gt=0, description="Стоимость товара (положительное число)")
    item_id: int = Field(...)


class FullProductInfo(BaseModel):
    item_id: int = Field(...)
    product_name: str = Field(..., description="Наименование товара")
    product_price: float = Field(..., gt=0, description="Стоимость товара (положительное число)")
    product_specs: ProductSpecs = Field(..., description="Спецификации товара")
    

@app.get("/items/{item_identifier}", response_model=FullProductInfo)
async def retrieve_product(item_identifier: int) -> FullProductInfo:
    target_item = None
    for current_item in product_collection:
        if current_item["item_id"] == item_identifier:
            target_item = current_item
            break
    
    if target_item is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    
    return target_item


@app.get("/items", response_model=List[BasicProductResponse])
async def fetch_all_products() -> List[BasicProductResponse]:
    return product_collection


@app.post("/items")
async def create_new_product(product_data: ProductCreateRequest):
    global item_counter
    product_dict = product_data.dict()
    product_dict["item_id"] = item_counter
    item_counter += 1
    product_collection.append(product_dict)
    return product_dict
# END