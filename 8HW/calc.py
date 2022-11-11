from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def min_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} - {y} = {x-y}')

async def prod_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} * {y} = {x*y}')

async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} / {y} = {x/y}')