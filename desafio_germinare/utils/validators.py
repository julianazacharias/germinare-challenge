import re

from .exceptions import InvalidContractMonthException


def validate_contract_month(contract_month: str):
    """
    Valid if contract_month follows the right format:
    [Month] + [Year 2 last digits].
    Example: JAN24, FEB25, etc.

    Raise InvalidContractMonthException if the value is incorrect.
    """
    month_year_pattern = re.compile(
        r'^(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\d{2}$'
    )

    if not month_year_pattern.match(contract_month):
        raise InvalidContractMonthException()

    return True
