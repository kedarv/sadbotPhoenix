import os
import requests
import json

BASE_URL = "https://api.weatherbit.io/v2.0/current"


CODE_EMOJI_MAP = {
    200: "🌩️",
    201: "🌩️",
    202: "🌩️",
    230: "🌩️",
    231: "🌩️",
    232: "🌩️",
    233: "🌩️",
    300: "🌧️",
    301: "🌧️",
    302: "🌧️",
    500: "🌧️",
    501: "🌧️",
    502: "🌧️",
    511: "🌧️",
    521: "🌧️",
    522: "🌧️",
    600: "❄️",
    601: "❄️",
    602: "❄️",
    610: "❄️",
    611: "🌨️",
    612: "🌨️",
    621: "🌨️",
    622: "🌨️",
    700: "🌫️",
    711: "🌫️",
    721: "🌫️",
    731: "🌫️",
    741: "🌫️",
    751: "🌫️",
    800: "☀️",
    801: "🌤️",
    802: "🌤️",
    803: "☁️",
    804: "☁️",
    900: "🌫️",
}


def weather_command(update, context):
    """Send a message when the command /weather is issued."""
    params = {
        "key": os.environ.get("WEATHERBIT_KEY"),
        "units": "I",
        "postal_code": "94117",
    }

    if len(context.args):
        try:
            zip_code = int(context.args[0])
            params["postal_code"] = zip_code
        except Exception:
            cities_data = json.load(open("data/cities_20000.json", encoding="utf-8"))
            city_name = " ".join(context.args)
            for city in cities_data:
                if city["city_name"] == city_name and city['country_code'] == 'US':
                    params["postal_code"] = None
                    params["city_id"] = city["city_id"]
                    break
    
    print(f"{params=}")
    data = requests.get(
        BASE_URL,
        params=params,
    ).json()

    update.message.reply_text(
        "{} {}: Currently {} °F".format(
            CODE_EMOJI_MAP[int(data["data"][0]["weather"]["code"])],
            data["data"][0]["weather"]["description"],
            round(data["data"][0]["temp"]),
        ),
        quote=False,
    )
