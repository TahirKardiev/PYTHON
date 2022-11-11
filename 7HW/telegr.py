from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import time_command, help_command, sum_command, hello

app = ApplicationBuilder().token("5690321800:AAFWVK1MJdXr9QWFJzue9IcjeuBwPRibCpY").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

app.run_polling()