from requests import Session
from config import coinmarket


def get_data():
    try:
        session = Session()
        session.headers.update({
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': coinmarket["token"],
        })
        parameters = {
            'symbol': 'BTC'
        }
        result = session.get(coinmarket["url"], params=parameters)
        data = result.json()

        return f"Bitcoin price - {data['data']['BTC']['quote']['USD']['price']}"
    except Exception as ex:
        print(ex)
        return "Что-то пошло не так c коинмаркетом!"
