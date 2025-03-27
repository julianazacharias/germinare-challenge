from http import HTTPStatus

from fastapi import HTTPException

SoybeanMealAlreadyExistsException = HTTPException(
    status_code=HTTPStatus.CONFLICT,
    detail='Soybean Meal Price is already included in the database',
)

PriceNotFoundException = HTTPException(
    status_code=HTTPStatus.NOT_FOUND, detail='Price not found'
)

SoybeanMealNotFoundException = HTTPException(
    status_code=HTTPStatus.NOT_FOUND, detail='Soybean Meal Price not found'
)

ContractMonthNotFoundException = HTTPException(
    status_code=HTTPStatus.NOT_FOUND, detail='Contract month not found'
)

InvalidBasisException = HTTPException(
    status_code=HTTPStatus.BAD_REQUEST,
    detail='Basis must be a number between -50 and 50',
)

InternalServerErrorException = HTTPException(
    status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
    detail='Unexpected server error',
)
