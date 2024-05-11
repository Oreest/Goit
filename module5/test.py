import asyncio
from datetime import datetime, timedelta
import logging
from pprint import pp as print
from aiohttp import ClientSession, ClientConnectorError

URL_PB = 'https://api.privatbank.ua/p24api/exchange_rates?json'
URL_NBU = 'https://bank.gov.ua/NBU_Exchange/exchange?json'
CURRENCY = ['USD', 'EUR']


async def request(url: str):
    async with ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.ok:
                    r = await resp.json()
                    return r
                logging.error(f"Error status: {resp.status} for {url}")
                return None
        except ClientConnectorError as err:
            logging.error(f"Connection error: {str(err)}")
            return None


def pb_handler(data):
    date = data['date']
    print(f'{date}:')
    for rate in data['exchangeRate']:
        if rate['currency'] in CURRENCY:
            print(f'{rate["currency"]} SALE: {rate["saleRate"]} BUY: {rate["purchaseRate"]}')


def nbu_handler(result):
    return result[0:]


async def get_exchange(url, handler, days=0):
    dates = [(datetime.now() - timedelta(days=x)).strftime('%d.%m.%Y') for x in range(days + 10)]
    exchange_rate_data = [request(f'{url}&date={date}') for date in dates]
    results = await asyncio.gather(*exchange_rate_data)
    for result in results:
        return handler(result)
    return "Failed to retrieve data"


def parse_currency(exchange_rate):
    for item in exchange_rate:
        print(item['CurrencyCodeL'])
        print(item['Amount'])


if __name__ == '__main__':
    # result1 = asyncio.run(get_exchange(URL_NBU, nbu_handler))
    result2 = asyncio.run(get_exchange(URL_PB, pb_handler))
    #print(result2)
    # parse_currency(result1)
