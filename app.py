import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import os
from handlers.airquality import aqi_command
from handlers.magic8 import magic8_command

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


def main():
    updater = Updater(os.environ.get("TELEGRAM_TOKEN"), use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("aqi", aqi_command))
    dp.add_handler(CommandHandler("8ball", magic8_command))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
