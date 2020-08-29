import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Hi!")


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Help!")


def aqi_command(update, context):
    """Send a message when the command /help is issued."""
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

    update.message.reply_text("\n\n".join(texts), default_quote=False)


def main():
    updater = Updater(os.environ.get("TELEGRAM_TOKEN"), use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("aqi", aqi_command))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()