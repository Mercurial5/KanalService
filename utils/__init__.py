from utils.google_sheets_api import return_sheet_rows
from utils.currency_exchange import get_usd_currency

from datetime import datetime, date
from math import ceil


def usd_to_rub(currency: int, usd: int) -> int:
    if isinstance(usd, str):
        usd = int(usd)

    return ceil(currency * usd)


def str_to_date(str_date: str) -> date:
    d = datetime.strptime(str_date, '%d.%m.%Y')
    return date(d.year, d.month, d.day)
