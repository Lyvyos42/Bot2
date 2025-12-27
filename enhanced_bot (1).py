#!/usr/bin/env python3
import os
import sys
from telegram.ext import Application, CommandHandler, ContextTypes
import logging

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    print("❌ Set BOT_TOKEN in Railway: railway variables set BOT_TOKEN=your_token")
    sys.exit(1)

async def start(update, context):
    await update.message.reply_text("🤖 Serie AI Bot is online!")

async def predict(update, context):
    await update.message.reply_text("⚽ Prediction feature active!")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("predict", predict))
    print("🚀 Bot ready for Railway deployment")
    app.run_polling()

if __name__ == "__main__":
    main()
