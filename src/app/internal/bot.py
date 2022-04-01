# import sqlite3
# from telegram.ext import Updater

# !/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Простой бот для ответа на сообщения Telegram.
Во-первых, определены несколько функций-обработчиков. Затем эти функции передаются
Диспетчеру и зарегистрировались по своим местам.
Затем бот запускается и работает до тех пор, пока мы не нажмем Ctrl-C в командной строке.
Использование:
Базовый пример Echobot, повторяет сообщения.
Нажмите Ctrl-C в командной строке или отправьте сигнал процессу, чтобы остановить
бот.
"""

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Включить ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Определите несколько обработчиков команд. Обычно они принимают два аргумента update и
# контекст.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main() -> None:


# Запустить бота
# Создайте средство обновления и передайте ему токен вашего бота.

    updater = Updater('')

# Заставить диспетчер зарегистрировать обработчики
    dispatcher = updater.dispatcher

# по разным командам - ответ в Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

# в некомандном, т.е. сообщении - эхо сообщения в Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Запускаем бота
    updater.start_polling()

# Запускаем бота, пока не нажмем Ctrl-C или процесс не получит SIGINT,
# SIGTERM или SIGABRT. Это следует использовать в большинстве случаев, так как
# start_polling() не блокирует и изящно остановит бота.
    updater.idle()

if __name__ == '__main__':
    main()

# 5292815147:AAHtRZbacBuVDCP8Y2S-lwhXgX7ugyKHRYc
