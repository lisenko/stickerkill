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
    if update.message.sticker.is_animated == True or update.message.sticker.is_video == True:
        bot.delete_message(update.message.chat.id, update.message.message_id)

def main():
    TOKEN = os.environ['telegram_token']
    NAME = os.environ['app_name']

    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Port is given by Heroku
    PORT = os.environ.get('PORT')

    # delete animated stickers
    dispatcher.add_handler(MessageHandler(Filters.sticker, stickerkill))

    # uncomment this if you don't want to use heroku/webhooks
    #updater.start_polling()

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                      port=int(PORT),
                      url_path=TOKEN,
                      webhook_url = "https://{}.herokuapp.com/{}".format(NAME, TOKEN))

    updater.idle()


if __name__ == '__main__':
    main()