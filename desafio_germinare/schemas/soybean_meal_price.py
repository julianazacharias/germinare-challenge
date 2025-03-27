from typing import List

from pydantic import BaseModel, ConfigDict


class SoybeanMealPriceRequest(BaseModel):
    contract_month: str
    price: float


class SoybeanMealPriceResponse(BaseModel):
    id: int
    contract_month: str
    price: float
    model_config = ConfigDict(from_attributes=True)


class SoybeanMealPricePatch(BaseModel):
    contract_month: str | None = None
    price: float | None = None


class SoybeanMealPriceList(BaseModel):
    soybean_meal_prices: list[SoybeanMealPriceResponse]


class FlatPriceRequest(BaseModel):
    basis: float
    contract_months: List[str]


class FlatPriceResponse(BaseModel):
    contract_month: str
    cbot_price: float
    basis: float
    flat_price: float
    model_config = ConfigDict(from_attributes=True)


class FlatPriceResponseList(BaseModel):
    results: List[FlatPriceResponse]
