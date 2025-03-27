from http import HTTPStatus

from fastapi import APIRouter

from desafio_germinare.schemas.message import Message
from desafio_germinare.schemas.soybean_meal_price import (
    FlatPriceRequest,
    FlatPriceResponseList,
    SoybeanMealPriceList,
    SoybeanMealPricePatch,
    SoybeanMealPriceRequest,
    SoybeanMealPriceResponse,
)
from desafio_germinare.services.soybean_meal_price import (
    create_soybean_meal_price_service,
    delete_soybean_meal_price_service,
    get_flat_prices_service,
    list_soybean_meal_price_service,
    patch_soybean_meal_price_service,
    read_soybean_meal_price_service,
)
from desafio_germinare.utils.dependencies import Session

router = APIRouter(prefix='/api', tags=['apis'])


@router.post(
    '/flat_price',
    status_code=HTTPStatus.CREATED,
    response_model=FlatPriceResponseList,
)
def get_flat_prices(flat_price_request: FlatPriceRequest, session: Session):
    results = get_flat_prices_service(flat_price_request, session)
    return FlatPriceResponseList(results=results)


@router.post(
    '/',
    status_code=HTTPStatus.CREATED,
    response_model=SoybeanMealPriceResponse,
)
def create_soybean_meal_price(
    soybean_meal_price: SoybeanMealPriceRequest, session: Session
):
    soybean_meal_price = create_soybean_meal_price_service(
        soybean_meal_price, session
    )
    return soybean_meal_price


@router.get('/', response_model=SoybeanMealPriceList)
def list_soybean_meal_prices(session: Session):
    list = list_soybean_meal_price_service(session)
    return list


@router.get(
    '/{soybean_meal_price_id}', response_model=SoybeanMealPriceResponse
)
def read_soybean_meal_price(soybean_meal_price_id: int, session: Session):
    soybean_meal_price = read_soybean_meal_price_service(
        soybean_meal_price_id, session
    )
    return soybean_meal_price


@router.patch(
    '/{soybean_meal_price_id}', response_model=SoybeanMealPriceResponse
)
def patch_soybean_meal_price(
    soybean_meal_price_id: int,
    soybean_meal_price: SoybeanMealPricePatch,
    session: Session,
):
    soybean_meal_price = patch_soybean_meal_price_service(
        soybean_meal_price_id, soybean_meal_price, session
    )

    return soybean_meal_price


@router.delete('/{soybean_meal_price_id}', response_model=Message)
def delete_soybean_meal_price(
    soybean_meal_price_id: int,
    session: Session,
):
    soybean_meal_price = delete_soybean_meal_price_service(
        soybean_meal_price_id, session
    )
    return soybean_meal_price
