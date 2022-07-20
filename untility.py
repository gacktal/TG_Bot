from telegram import *
from telegram.ext import *

def get_first_keyboard():
    first_keyboard = [KeyboardButton("FAQ")]
    return first_keyboard
def get_FAQ_keyboard():
    FAQ_keyboard = [KeyboardButton('one'),KeyboardButton('two'),KeyboardButton('three'), KeyboardButton("Back")]
    return FAQ_keyboard