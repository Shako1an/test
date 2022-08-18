import requests
from config import exchange_rate_url


def get_exchange_rate(city):
    try:
        result = requests.get(
            f"{exchange_rate_url}?city={city}"
        )
        data = result.json()
        return format_exchange_rate(data[0])
    except Exception as ex:
        print(ex)
        return "Что-то пошло не так! Проверьте правильно ли вы ввели город."


def format_exchange_rate(data):
    output = "<b>покупка    продажа    </b>\n"
    output += "<b>-------------    -------------</b>\n"
    output += f"{data['USD_in']}        {data['USD_out']}       $ 🇺🇸\n"
    output += f"{data['EUR_in']}        {data['EUR_out']}       € 🇪🇺\n"
    output += f"{data['RUB_in']}        {data['RUB_out']}       ₽ 🇷🇺 (100 ед.)\n"

    return output
