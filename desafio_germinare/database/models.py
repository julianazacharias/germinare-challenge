from datetime import datetime
from typing import Optional

from sqlalchemy import Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class SoybeanMealPrice:
    __tablename__ = 'soybean_meal_prices'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    contract_month: Mapped[str] = mapped_column(String(10))
    price: Mapped[float] = mapped_column(Numeric(10, 2))
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    update_at: Mapped[Optional[datetime]] = mapped_column(
        init=False, onupdate=func.now()
    )
