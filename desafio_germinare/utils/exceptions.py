from http import HTTPStatus

from fastapi import HTTPException


class SoybeanMealAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=HTTPStatus.CONFLICT,
            detail='Soybean Meal Price is already included in the database',
        )


class PriceNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Price not found',
        )


class SoybeanMealNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Soybean Meal Price not found',
        )


class ContractMonthNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Contract month not found',
        )


class InvalidBasisException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Basis must be a number between -50 and 50',
        )


class InvalidContractMonthException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='One or more contract months are in an invalid format.'
            'Must be a valid month and a valid year.',
        )


class InsertABasisException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Insert a valid basis value',
        )


class InternalServerError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail='Unexpected server erro',
        )
