from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from calc import min_command, prod_command, div_command, sum_command

app = ApplicationBuilder().token("5690321800:AAFWVK1MJdXr9QWFJzue9IcjeuBwPRibCpY").build()

app.add_handler(CommandHandler("min", min_command))
app.add_handler(CommandHandler("prod", prod_command))
app.add_handler(CommandHandler("div", div_command))
app.add_handler(CommandHandler("sum", sum_command))

app.run_polling()