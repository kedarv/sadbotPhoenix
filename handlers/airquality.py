import os
import requests
import json


def aqi_command(update, context):
    """Send a message when the command /aqi is issued."""
    zip_code = "94117"
    if len(context.args):
        zip_code = context.args[0]
    observation_url = "http://www.airnowapi.org/aq/observation/zipCode/current/"

    parameter_map = {
        "PM2.5": "fine particulate matter",
        "PM10": "particulate matter",
        "O3": "ozone",
    }

    data = requests.get(
        observation_url,
        params={
            "API_KEY": os.environ.get("AIRNOW_KEY"),
            "distance": 25,
            "zipCode": zip_code,
            "format": "application/json",
        },
    ).content
    observations = json.loads(data.decode("utf-8"))
    texts = []
    for observation in observations:
        title = "{} ({})".format(
            observation["ParameterName"],
            parameter_map[observation["ParameterName"]],
        )
        text = "{} - {}".format(observation["AQI"], observation["Category"]["Name"])
        texts.append(title + "\n" + text)

    update.message.reply_text("\n\n".join(texts), quote=False)