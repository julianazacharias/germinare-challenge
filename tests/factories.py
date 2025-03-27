from datetime import datetime
from decimal import Decimal

import factory
import factory.fuzzy

from desafio_germinare.database.models import SoybeanMealPrice


class SoybeanMealPriceFactory(factory.Factory):
    class Meta:
        model = SoybeanMealPrice

    month_names = [
        'JAN',
        'FEB',
        'MAR',
        'APR',
        'MAY',
        'JUN',
        'JUL',
        'AUG',
        'SEP',
        'OCT',
        'NOV',
        'DEC',
    ]
    current_year = (
        datetime.now().year % 100
    )  # Pega os dois últimos dígitos do ano atual

    contract_month = factory.Sequence(
        lambda n: f'{SoybeanMealPriceFactory.month_names[n % 12]}{
            SoybeanMealPriceFactory.current_year + (n // 12)
        }'
    )

    contract_month = factory.Sequence(lambda n: f'test{n}')
    price = factory.Sequence(lambda n: Decimal(f'{round(n * 0.01, 2)}'))
