
import logging

from django.core.management.base import BaseCommand

from django.conf import settings
from telegram import Update, ForceReply

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
updater = Updater(token='', use_context=True)
from app.models import For_Bot

p, _ = For_Bot.objects.get_or_create(
    user_id=chat_id,
    defaults={
    'name': update.message.from_user.username,
    'tel': update.message.from_user,
    'user_name': update.message.from_user,
    'inf': update.message.from_user,
}
)

# Включить ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)






