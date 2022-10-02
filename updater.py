"""
This script is intended to update data from sheets.

May be used with crontab.
"""

from dotenv import load_dotenv

load_dotenv()

from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert

from utils import return_sheet_rows
from utils import get_usd_currency
from utils import str_to_date
from utils import usd_to_rub

from models import engine, Orders


def main():
    sheet_rows = return_sheet_rows()

    with Session(engine) as session:
        currency = get_usd_currency()
        orders = [
            Orders(id=row[1], cost_usd=row[2], cost_rub=usd_to_rub(currency, row[2]),
                   date=str_to_date(row[3])).serialize()
            for row in sheet_rows[1:]]

        # This way I don't need to check for duplicates (https://docs.python.org/3/glossary.html#term-EAFP)
        # https://stackoverflow.com/questions/63556777/sqlalchemy-add-all-ignore-duplicate-key-integrityerror
        session.execute(insert(Orders).values(orders).on_conflict_do_nothing())
        session.commit()


if __name__ == '__main__':
    main()
