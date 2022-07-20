from telegram import *
from telegram.ext import *
from untility import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Inform user about what this bot can do"""
    await update.message.reply_text(
        "Здравствуйте"
    )
    message = "Чтобы узнать о компании больше, нажмите /FAQ"
    await update.effective_message.reply_text(message,
    reply_markup=get_FAQ_keyboard())

async def Faq(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    message = "Что вы хотите узнать? 1, 2, 3"
    update.effective_message.reply_text(message, reply_markup=get_first_keyboard())

async def first(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    message = "Some info"
    await update.effective_message.reply_text(message)


async def second(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    message = "Some info"
    await update.effective_message.reply_text(message)


async def third(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    message = "Some info"
    await update.effective_message.reply_text(message)


