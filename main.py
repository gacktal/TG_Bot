
from telegram.ext import (
    Application,
    CommandHandler,
    filters,
    MessageHandler
)
from settings import tg_token
from handlers import *

def main() -> None:

    application = Application.builder().token(tg_token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("FAQ", Faq))
    application.add_handler(CommandHandler("1", first))
    application.add_handler(CommandHandler("2",second))
    application.add_handler(CommandHandler("3", third))
    application.add_handler(MessageHandler(filters.Regex('FAQ'), Faq))
    application.add_handler(MessageHandler(filters.Regex('back'), start))
    application.add_handler(MessageHandler(filters.Regex('one'), first))
    application.add_handler(MessageHandler(filters.Regex('two'), second))
    application.add_handler(MessageHandler(filters.Regex('three'), third))
    application.run_polling()

if __name__ == "__main__":
    main()