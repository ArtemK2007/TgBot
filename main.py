from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import os
base_dir = os.path.abspath(os.path.dirname(__file__))
base_path = os.path.join(base_dir, "VishMat")
load_dotenv()
TOKEN = os.getenv("TOKEN")
PDF_FILES = {
    f"VishMat_Lec{i}": os.path.join(base_path, f"lec{i}.pdf")
    for i in range(1, 33)
}
#-----------------------------------------------------------------------------------------------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! 👋 Я бот для збереження твоїх конспектів 📚✨.")
    await update.message.reply_text("📋 Список доступних команд: /help 🛠️")
    await update.message.reply_text("🎓 Ось доступні предмети:", reply_markup=main_keyboard())
#-----------------------------------------------------------------------------------------------------------------------
async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = (
        "👋 Привіт! Я бот для збереження конспектів 📚\n\n"
        "Тут ти можеш швидко знаходити та завантажувати лекції з різних предметів.\n"
        "Команди:\n"
        "/start — почати роботу з ботом\n"
        "/list — список доступних предметів\n"
        "/help — допомога по командам\n"
        "/about — інформація про бота\n\n"
        "Створено з ❤️ для твого зручного навчання!"
    )
    await update.message.reply_text(about_text)
# -----------------------------------------------------------------------------------------------------------------------
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⬅️ В головне меню", callback_data='main_keyboard')]
    ]
    help_text = (
        "📋 Список доступних команд:\n"
        "/list — список доступних предметів\n"
        "/help — список команд\n"
        "/about — інформація про бота 💡"
    )
    await update.message.reply_text(help_text, reply_markup=InlineKeyboardMarkup(keyboard))
#-----------------------------------------------------------------------------------------------------------------------
async def show_subjects(update, context):
    await update.message.reply_text("Ось доступні предмети: 📚", reply_markup=main_keyboard())
#-----------------------------------------------------------------------------------------------------------------------
def main_keyboard():
    keyboard = [
        [InlineKeyboardButton("Вища математика📐", callback_data='VishMat')],
        [InlineKeyboardButton("Потрібна допомога?🆘", callback_data='help_command')],
    ]
    return InlineKeyboardMarkup(keyboard)
#-----------------------------------------------------------------------------------------------------------------------
def back_to_topics_keyboard_vishmat():
    keyboard = [
        [InlineKeyboardButton("⬅️ Назад до тем", callback_data='back_to_topics')]
    ]
    return InlineKeyboardMarkup(keyboard)
#-----------------------------------------------------------------------------------------------------------------------
def topics_keyboard_vishmat():
    keyboard = [
        [InlineKeyboardButton("📌Тема 1. ВИЗНАЧНИКИ. МАТРИЦІ", callback_data='VishMat_Lec1')],
        [InlineKeyboardButton("📌Тема 2. (СЛАР)", callback_data='VishMat_Lec2')],
        [InlineKeyboardButton("📌Тема 3. ВЕКТОРНА АЛГЕБРА", callback_data='VishMat_Lec3')],
        [InlineKeyboardButton("📌Тема 4. Аналітична геометрія на площині", callback_data='VishMat_Lec4')],
        [InlineKeyboardButton("📌Тема 5. Аналітична геометрія в тривимірному просторі", callback_data='VishMat_Lec5')],
        [InlineKeyboardButton("📌Тема 6. Вступ до математичного аналізу", callback_data='VishMat_Lec6')],
        [InlineKeyboardButton("📌Тема 7. Чудові границі Неперервність функції", callback_data='VishMat_Lec7')],
        [InlineKeyboardButton("📌Тема 8. Диференціальне числення", callback_data='VishMat_Lec8')],
        [InlineKeyboardButton("➡️Наступна сторінка", callback_data='topics_keyboard_vishmat2')],
        [InlineKeyboardButton("⬅️Назад", callback_data='back_to_subjects')],
        [InlineKeyboardButton("⬅️В головне меню", callback_data='main_keyboard')]
    ]
    return InlineKeyboardMarkup(keyboard)
#-----------------------------------------------------------------------------------------------------------------------
def topics_keyboard_vishmat2():
    keyboard = [
        [InlineKeyboardButton("📌Тема 9. Похідні і диференціали вищих порядків", callback_data='VishMat_Lec9')],
        [InlineKeyboardButton("📌Тема 10. Побудова граф. функц. з повним дослідженням", callback_data='VishMat_Lec10')],
        [InlineKeyboardButton("📌Тема 11. Функція багатьох змінних", callback_data='VishMat_Lec11')],
        [InlineKeyboardButton("📌Тема 12. Екстремуми функцій багатьох змінних", callback_data='VishMat_Lec12')],
        [InlineKeyboardButton("📌Тема 13. Невизначений інтеграл", callback_data='VishMat_Lec13')],
        [InlineKeyboardButton("📌Тема 14. Методи інтегрування", callback_data='VishMat_Lec14')],
        [InlineKeyboardButton("📌Тема 15. Визначений інтеграл", callback_data='VishMat_Lec15')],
        [InlineKeyboardButton("📌Тема 16. Застосування визначених інтегралів до розв'язання задач", callback_data='VishMat_Lec16')],
        [InlineKeyboardButton("➡️Наступна сторінка", callback_data='topics_keyboard_vishmat3')],
        [InlineKeyboardButton("⬅️Назад", callback_data='back_to_topics')],
        [InlineKeyboardButton("⬅️В головне меню", callback_data='main_keyboard')]
    ]
    return InlineKeyboardMarkup(keyboard)
#-----------------------------------------------------------------------------------------------------------------------
def topics_keyboard_vishmat3():
    keyboard = [
        [InlineKeyboardButton("📌Тема 17. Основні поняття теорії диференціальних рівнянь", callback_data='VishMat_Lec17')],
        [InlineKeyboardButton("📌Тема 18. Типи ДР та способи їх розв'язку Рівняня Бернуллі", callback_data='VishMat_Lec18')],
        [InlineKeyboardButton("📌Тема 19. ЛНДР 2-го та вищих порядків зі спеціальною правою частиною", callback_data='VishMat_Lec19')],
        [InlineKeyboardButton("📌Тема 20. Системи ДР", callback_data='VishMat_Lec20')],
        [InlineKeyboardButton("📌Тема 21. Подвійні інтеграли", callback_data='VishMat_Lec21')],
        [InlineKeyboardButton("📌Тема 22. Потрійні інтеграли", callback_data='VishMat_Lec22')],
        [InlineKeyboardButton("📌Тема 23. Криволінійні інтеграли", callback_data='VishMat_Lec23')],
        [InlineKeyboardButton("📌Тема 24. Поверхневі інтеграли", callback_data='VishMat_Lec24')],
        [InlineKeyboardButton("➡️Наступна сторінка", callback_data='topics_keyboard_vishmat4')],
        [InlineKeyboardButton("⬅️Назад", callback_data='topics_keyboard_vishmat2')],
        [InlineKeyboardButton("⬅️В головне меню", callback_data='main_keyboard')]
    ]
    return InlineKeyboardMarkup(keyboard)
#-----------------------------------------------------------------------------------------------------------------------
def topics_keyboard_vishmat4():
    keyboard = [
        [InlineKeyboardButton("📌Тема 25. Теорія поля", callback_data='VishMat_Lec25')],
        [InlineKeyboardButton("📌Тема 26. Числові ряди. Знакододатні числові ряди", callback_data='VishMat_Lec26')],
        [InlineKeyboardButton("📌Тема 27. Знакопереміжні та знакозмінні числові ряди", callback_data='VishMat_Lec27')],
        [InlineKeyboardButton("📌Тема 28. Функціональні і степеневі ряди", callback_data='VishMat_Lec28')],
        [InlineKeyboardButton("📌Тема 29. Ряди Фур'є", callback_data='VishMat_Lec29')],
        [InlineKeyboardButton("📌Тема 30. Основи теорії ймовірностей", callback_data='VishMat_Lec30')],
        [InlineKeyboardButton("📌Тема 31. Послідовність випробувань. Схема Бернуллі", callback_data='VishMat_Lec31')],
        [InlineKeyboardButton("📌Тема 32. Дискретні і неперервні випадкові величини", callback_data='VishMat_Lec32')],
        [InlineKeyboardButton("⬅️Назад", callback_data='topics_keyboard_vishmat3')],
        [InlineKeyboardButton("⬅️В головне меню", callback_data='main_keyboard')]
    ]
    return InlineKeyboardMarkup(keyboard)
#-----------------------------------------------------------------------------------------------------------------------
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id

    async def replace_message(query, context, text, reply_markup=None):
        try:
            await query.message.delete()
        except:
            pass
        await context.bot.send_message(chat_id=query.message.chat.id, text=text, reply_markup=reply_markup)
# -----------------------------------------------------------------------------------------------------------------------
    if query.data == "VishMat":
        await replace_message(query, context, "Ви обрали Вищу математику 📐 Оберіть тему (показані перші 8 тем):", reply_markup=topics_keyboard_vishmat())
# -----------------------------------------------------------------------------------------------------------------------
    elif query.data == "main_keyboard":
        await replace_message(query, context, "Ось доступні предмети: 🔍", reply_markup=main_keyboard())
# -----------------------------------------------------------------------------------------------------------------------
    elif query.data == "back_to_subjects":
        await replace_message(query, context, "Ось доступні предмети: 🔍", reply_markup=main_keyboard())
# -----------------------------------------------------------------------------------------------------------------------
    elif query.data == "back_to_topics":
        await replace_message(query, context, "Ви обрали Вищу математику. Оберіть тему: 🔍", reply_markup=topics_keyboard_vishmat())
# -----------------------------------------------------------------------------------------------------------------------
    elif query.data == "topics_keyboard_vishmat2":
        await replace_message(query, context, "Теми 9-16 📝", reply_markup=topics_keyboard_vishmat2())
# -----------------------------------------------------------------------------------------------------------------------
    elif query.data == "topics_keyboard_vishmat3":
        await replace_message(query, context, "Теми 17-24 📝", reply_markup=topics_keyboard_vishmat3())
# -----------------------------------------------------------------------------------------------------------------------
    elif query.data == "topics_keyboard_vishmat4":
        await replace_message(query, context, "Теми 25-32 📝", reply_markup=topics_keyboard_vishmat4())
# -----------------------------------------------------------------------------------------------------------------------
    elif query.data == "help_command":
        await replace_message(query, context,         "📋 Список доступних команд:\n"
        "/list — список доступних предметів\n"
        "/help — список команд\n"
        "/about — інформація про бота 💡",
                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ В головне меню", callback_data='main_keyboard')]]))
# -----------------------------------------------------------------------------------------------------------------------
    elif query.data in PDF_FILES:
        file_path = PDF_FILES[query.data]
        if os.path.exists(file_path):
            try:
                with open(file_path, 'rb') as f:
                    await context.bot.send_document(chat_id=chat_id, document=f)
            except Exception as e:
                await context.bot.send_message(chat_id=chat_id, text=f"Сталася помилка при відправці файлу❌⚠️{e}")
                # ------------------------------------------------------------------------------------------------------
            await context.bot.send_message(
                chat_id=chat_id,
                text="⬅️ Повернутись до списку тем:",
                reply_markup=back_to_topics_keyboard_vishmat()
            )
        else:
            await context.bot.send_message(chat_id=chat_id, text="Файл не знайдено 😢❌")
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CommandHandler("list", show_subjects))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Бот запущено...")
    app.run_polling()
#-----------------------------------------------------------------------------------------------------------------------