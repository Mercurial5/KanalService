from bs4 import BeautifulSoup
import requests

from datetime import datetime


def get_usd_currency() -> int:
    current_date = datetime.now()
    link = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={current_date.strftime("%d/%m/%Y")}'

    response = requests.get(link)
    soup = BeautifulSoup(response.text, features='xml')

    valute = soup.find('Valute', {'ID': 'R01235'})
    usd_currency = valute.find('Value').text
    usd_currency = float(usd_currency.replace(',', '.'))

    return usd_currency
