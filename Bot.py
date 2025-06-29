bot.py import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.environ["BOT_TOKEN"]  # Token aman via Render

# === Perintah /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Bot kamu aktif 24 jam! 🚀 Ketik /menu")

# === /menu ===
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("ℹ️ Info", callback_data="info")],
        [InlineKeyboardButton("📷 Gambar", callback_data="gambar")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Menu utama:", reply_markup=reply_markup)

# === Tombol inline ===
async def tombol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        await query.edit_message_text("🤖 Ini bot canggih aktif 24 jam.")
    elif query.data == "gambar":
        await query.message.reply_photo("https://i.imgur.com/ExdKOOz.png", caption="Ini gambar dari bot!")

# === Auto-reply ===
async def autoreply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "halo" in text:
        await update.message.reply_text("👋 Hai juga!")
    else:
        await update.message.reply_text(f"Kamu bilang: {update.message.text}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CallbackQueryHandler(tombol))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, autoreply))
    app.run_polling()

if __name__ == "__main__":
    main()
