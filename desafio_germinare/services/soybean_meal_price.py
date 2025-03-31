from decimal import Decimal

from sqlalchemy import select

from desafio_germinare.database.models import SoybeanMealPrice
from desafio_germinare.schemas.soybean_meal_price import (
    FlatPriceRequest,
    SoybeanMealPricePatch,
    SoybeanMealPriceRequest,
)
from desafio_germinare.utils.dependencies import Session
from desafio_germinare.utils.exceptions import (
    ContractMonthNotFoundException,
    InternalServerError,
    InvalidBasisException,
    InvalidContractMonthException,
    SoybeanMealAlreadyExistsException,
    SoybeanMealNotFoundException,
)
from desafio_germinare.utils.sanitize import sanitize
from desafio_germinare.utils.validators import validate_contract_month

CONVERSION_FACTOR = 1.10231
BASIS_THRESHOLD = 50


def get_flat_prices_service(
    flat_price_request: FlatPriceRequest, session: Session
):
    basis = Decimal(flat_price_request.basis)

    try:
        flat_price_request.contract_months = [
            sanitize(contract_month)
            for contract_month in flat_price_request.contract_months
        ]

        for contract_month in flat_price_request.contract_months:
            validate_contract_month(contract_month)

        if basis > BASIS_THRESHOLD or basis < -BASIS_THRESHOLD:
            raise InvalidBasisException()

        query = select(SoybeanMealPrice).filter(
            SoybeanMealPrice.contract_month.in_(
                flat_price_request.contract_months
            )
        )

        soybean_meal_prices = session.scalars(query).all()

        if not soybean_meal_prices:
            raise ContractMonthNotFoundException()

        flat_prices = []

        conversion_factor = Decimal(CONVERSION_FACTOR)

        for soybean_meal_price in soybean_meal_prices:
            cbot_price = Decimal(soybean_meal_price.price)

            # Flat Price = (Preço Futuro (CBOT) + Basis)*Fator de conversão
            flat_price = (cbot_price + basis) * conversion_factor

            formatted_cbot_price = f'{float(cbot_price):.2f}'
            formatted_basis = f'{basis:.2f}'

            flat_prices.append(
                {
                    'contract_month': soybean_meal_price.contract_month,
                    'cbot_price': formatted_cbot_price,
                    'basis': formatted_basis,
                    'flat_price': round(float(flat_price), 2),
                }
            )

        return flat_prices

    except InvalidContractMonthException as e:
        raise e

    except InvalidBasisException as e:
        raise e

    except ContractMonthNotFoundException as e:
        raise e

    except Exception:
        raise InternalServerError


def create_soybean_meal_price_service(
    soybean_meal_price: SoybeanMealPriceRequest, session: Session
):
    sanitized_contract_month = sanitize(soybean_meal_price.contract_month)
    validate_contract_month(sanitized_contract_month)

    existing_soybean_meal_price = (
        session.query(SoybeanMealPrice)
        .filter(
            SoybeanMealPrice.contract_month
            == soybean_meal_price.contract_month,
            SoybeanMealPrice.price == soybean_meal_price.price,
        )
        .first()
    )

    if existing_soybean_meal_price:
        raise SoybeanMealAlreadyExistsException()

    db_soybean_meal_price = SoybeanMealPrice(
        contract_month=sanitized_contract_month,
        price=soybean_meal_price.price,
    )

    session.add(db_soybean_meal_price)
    session.commit()
    session.refresh(db_soybean_meal_price)

    return db_soybean_meal_price


def list_soybean_meal_price_service(session: Session):
    query = select(SoybeanMealPrice)

    soybean_meal_prices = session.scalars(query).all()

    return {'soybean_meal_prices': soybean_meal_prices}


def read_soybean_meal_price_service(
    soybean_meal_price_id: int, session: Session
):
    db_soybean_meal_price = session.scalar(
        select(SoybeanMealPrice).where(
            SoybeanMealPrice.id == soybean_meal_price_id
        )
    )

    if not db_soybean_meal_price:
        raise SoybeanMealNotFoundException()

    return db_soybean_meal_price


def patch_soybean_meal_price_service(
    soybean_meal_price_id: int,
    soybean_meal_price: SoybeanMealPricePatch,
    session: Session,
):
    db_soybean_meal_price = session.scalar(
        select(SoybeanMealPrice).where(
            SoybeanMealPrice.id == soybean_meal_price_id
        )
    )

    if not db_soybean_meal_price:
        raise SoybeanMealNotFoundException()

    for key, value in soybean_meal_price.model_dump(
        exclude_unset=True
    ).items():
        sanitized_value = value
        if key in {'contract_month'}:
            sanitized_value = sanitize(value)

        setattr(db_soybean_meal_price, key, sanitized_value)

        validate_contract_month(db_soybean_meal_price.contract_month)

    session.add(db_soybean_meal_price)
    session.commit()
    session.refresh(db_soybean_meal_price)

    return db_soybean_meal_price


def delete_soybean_meal_price_service(
    soybean_meal_price_id: int,
    session: Session,
):
    db_soybean_meal_price = session.scalar(
        select(SoybeanMealPrice).where(
            SoybeanMealPrice.id == soybean_meal_price_id
        )
    )

    if not db_soybean_meal_price:
        raise SoybeanMealNotFoundException()

    session.delete(db_soybean_meal_price)
    session.commit()

    return {'message': 'Soybean Meal Price has been deleted successfully.'}
