from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import os
load_dotenv()
TOKEN = os.getenv("TOKEN")
PDF_FILES = {
    "VishMat_Lec1": r"C:\Users\artem\Desktop\TgBot\VishMat\lec1.pdf",
    "VishMat_Lec2": r"C:\Users\artem\Desktop\TgBot\VishMat\lec2.pdf"
}

def main_keyboard():
    keyboard = [
        [InlineKeyboardButton("Вища математика", callback_data='VishMat')]
    ]
    return InlineKeyboardMarkup(keyboard)

def back_to_topics_keyboard():
    keyboard = [
        [InlineKeyboardButton("⬅️ Назад до тем", callback_data='back_to_topics')]
    ]
    return InlineKeyboardMarkup(keyboard)

def topics_keyboard():
    keyboard = [
        [InlineKeyboardButton("Тема 1. ВИЗНАЧНИКИ. МАТРИЦІ", callback_data='VishMat_Lec1')],
        [InlineKeyboardButton("Тема 2. (СЛАР)", callback_data='VishMat_Lec2')],
        [InlineKeyboardButton("Тема 3. ВЕКТОРНА АЛГЕБРА", callback_data='VishMat_Lec3')],
        [InlineKeyboardButton("Тема 4. Аналітична геометрія на площині", callback_data='VishMat_Lec4')],
        [InlineKeyboardButton("Тема 5. Аналітична геометрія в тривимірному просторі", callback_data='VishMat_Lec5')],
        [InlineKeyboardButton("Тема 6. Вступ до математичного аналізу", callback_data='VishMat_Lec6')],
        [InlineKeyboardButton("Тема 7. Чудові границі Неперервність функції", callback_data='VishMat_Lec7')],
        [InlineKeyboardButton("Тема 8. Диференціальне числення", callback_data='VishMat_Lec8')],
        [InlineKeyboardButton("Назад", callback_data='back_to_subjects')]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update, context):
    await update.message.reply_text("Привіт! Я бот для збереження твоїх конспектів 📚.")
    await update.message.reply_text("Ось доступні предмети:", reply_markup=main_keyboard())

async def show_subjects(update, context):
    await update.message.reply_text("Ось доступні предмети:", reply_markup=main_keyboard())

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id

    async def safe_edit(text, reply_markup=None):
        try:
            await query.edit_message_text(text=text, reply_markup=reply_markup)
        except Exception:
            await context.bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)

    if query.data == "VishMat":
        await safe_edit("Ви обрали Вищу математику. Оберіть тему:", reply_markup=topics_keyboard())

    elif query.data == "back_to_subjects":
        await safe_edit("Ось доступні предмети:", reply_markup=main_keyboard())

    elif query.data == "back_to_topics":
        await safe_edit("Ви обрали Вищу математику. Оберіть тему:", reply_markup=topics_keyboard())

    elif query.data in PDF_FILES:
        file_path = PDF_FILES[query.data]
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                await context.bot.send_document(chat_id=chat_id, document=f)

            await context.bot.send_message(
                chat_id=chat_id,
                text="⬅️ Повернутись до списку тем:",
                reply_markup=back_to_topics_keyboard()
            )
        else:
            await context.bot.send_message(chat_id=chat_id, text="Файл не знайдено 😢")

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("list", show_subjects))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Бот запущено...")
    app.run_polling()
