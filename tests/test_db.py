from sqlalchemy import select

from desafio_germinare.database.models import SoybeanMealPrice


def test_create_soybean_meal_price(session):
    new_soybean_meal_price = SoybeanMealPrice(
        contract_month='MAY24', price='450.00'
    )
    session.add(new_soybean_meal_price)
    session.commit()

    soybean_meal_price = session.scalar(
        select(SoybeanMealPrice).where(
            SoybeanMealPrice.contract_month == 'MAY24'
        )
    )

    assert soybean_meal_price.contract_month == 'MAY24'
