#!/usr/bin/env python
# pylint: disable=W0613, C0116
# type: ignore[union-attr]

import logging, os

from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

bot = Bot(os.environ['telegram_token'])

def stickerkill(update: Update, context: CallbackContext) -> None:
    if update.message.sticker.is_animated == True:
        bot.delete_message(update.message.chat.id, update.message.message_id)

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(os.environ['telegram_token'])

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # delete animated stickers
    dispatcher.add_handler(MessageHandler(Filters.sticker, stickerkill))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()