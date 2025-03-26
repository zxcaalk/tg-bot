from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Укажи свой токен от BotFather
TOKEN = '8087376904:AAHHg3XouTQFRm9co5TOF_GR5KrBcps4jzA'  # Заменить на свой токен

# Функция для создания клавиатуры главного меню
def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("📖 Каталог", callback_data='catalog')],
        [InlineKeyboardButton("✍️ Оставить заявку", callback_data='request')],
        [InlineKeyboardButton("💬 Связаться с менеджером", url='https://t.me/itm_9043')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Функция для создания клавиатуры каталога
def catalog_keyboard():
    keyboard = [
        [InlineKeyboardButton("📸 Фоточки ножек", callback_data='photo_legs')],
        [InlineKeyboardButton("📸 Фоточки киски", callback_data='photo_kiss')],
        [InlineKeyboardButton("📸 Фоточки попы", callback_data='photo_butt')],
        [InlineKeyboardButton("📸 Фоточки груди", callback_data='photo_breast')],
        [InlineKeyboardButton("📸 Фоточки всё вместе", callback_data='photo_all')],
        [InlineKeyboardButton("💞 Кружки ножек", callback_data='cup_legs')],
        [InlineKeyboardButton("💞 Кружки киски", callback_data='cup_kiss')],
        [InlineKeyboardButton("💞 Кружки попы", callback_data='cup_butt')],
        [InlineKeyboardButton("💞 Кружки груди", callback_data='cup_breast')],
        [InlineKeyboardButton("💞 Кружки все вместе", callback_data='cup_all')],
        [InlineKeyboardButton("🎥 Видео ножек", callback_data='video_legs')],
        [InlineKeyboardButton("🎥 Видео киски", callback_data='video_kiss')],
        [InlineKeyboardButton("🎥 Видео попы", callback_data='video_butt')],
        [InlineKeyboardButton("🎥 Видео груди", callback_data='video_breast')],
        [InlineKeyboardButton("🎥 Видео все вместе", callback_data='video_all')],
        [InlineKeyboardButton("🥵💖 Приват навсегда", callback_data='private')],
        [InlineKeyboardButton("📞 Видео звонок", callback_data='video_call')]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    # Отправляем приветственное сообщение с клавишами главного меню
    await update.message.reply_text(f"Привет, {user.first_name}!", reply_markup=main_menu_keyboard())

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Подтверждаем нажатие кнопки

    # Обработка нажатия на кнопку "Каталог"
    if query.data == 'catalog':
        catalog_text = """
📸 *Фоточки*:
- Ножки
- Киска
- Попа
- Грудь
- Всё вместе

💞 *Кружки*:
- Ножки
- Киска
- Попа
- Грудь
- Всё вместе

🎥 *Видео*:
- Ножки
- Киска
- Попа
- Грудь
- Всё вместе

🥵💖 *Приват навсегда*

📞 *Видео звонок*
        """
        # Отправляем текст с каталогом и клавишами каталога
        await query.message.reply_text(catalog_text, reply_markup=catalog_keyboard())

    # Обработка заявки
    elif query.data == 'request':
        # Здесь будет сообщение о заявке
        await query.message.reply_text("Оставьте свою заявку, и мы с вами свяжемся. Напишите ваш запрос.")

    # Здесь можно добавить обработку других кнопок для показа информации о товаре или услуги.
    elif query.data == 'photo_legs':
        await query.message.reply_text("📸 *Фоточки ножек* - 40 грн / 40 ₽ (30 фото)")
    elif query.data == 'photo_kiss':
        await query.message.reply_text("📸 *Фоточки киски* - 40 грн / 40 ₽ (30 фото)")
    elif query.data == 'photo_butt':
        await query.message.reply_text("📸 *Фоточки попы* - 40 грн / 40 ₽ (30 фото)")
    elif query.data == 'photo_breast':
        await query.message.reply_text("📸 *Фоточки груди* - 40 грн / 40 ₽ (30 фото)")
    elif query.data == 'photo_all':
        await query.message.reply_text("📸 *Фоточки всё вместе* - 80 грн / 80 ₽")
    elif query.data == 'cup_legs':
        await query.message.reply_text("💞 *Кружки ножек* - 60 грн / 60 ₽ (40 кружков)")
    elif query.data == 'cup_kiss':
        await query.message.reply_text("💞 *Кружки киски* - 60 грн / 60 ₽ (40 кружков)")
    elif query.data == 'cup_butt':
        await query.message.reply_text("💞 *Кружки попы* - 60 грн / 60 ₽ (40 кружков)")
    elif query.data == 'cup_breast':
        await query.message.reply_text("💞 *Кружки груди* - 60 грн / 60 ₽ (40 кружков)")
    elif query.data == 'cup_all':
        await query.message.reply_text("💞 *Кружки все вместе* - 120 грн / 120 ₽")
    elif query.data == 'video_legs':
        await query.message.reply_text("🎥 *Видео ножек* - 90 грн / 90 ₽ (40 видео)")
    elif query.data == 'video_kiss':
        await query.message.reply_text("🎥 *Видео киски* - 90 грн / 90 ₽ (40 видео)")
    elif query.data == 'video_butt':
        await query.message.reply_text("🎥 *Видео попы* - 90 грн / 90 ₽ (40 видео)")
    elif query.data == 'video_breast':
        await query.message.reply_text("🎥 *Видео груди* - 90 грн / 90 ₽ (40 видео)")
    elif query.data == 'video_all':
        await query.message.reply_text("🎥 *Видео все вместе* - 180 грн / 180 ₽")
    elif query.data == 'private':
        await query.message.reply_text("🥵💖 *Приват навсегда* - 385 грн")
    elif query.data == 'video_call':
        await query.message.reply_text("📞 *Видео звонок* - 5 минут — 85 грн / 85 ₽, 10 минут — 170 грн / 170 ₽")

def main():
    # Создание экземпляра приложения
    app = ApplicationBuilder().token(TOKEN).build()

    # Обработчики команд и кнопок
    app.add_handler(CommandHandler("start", start))  # Обработчик команды /start
    app.add_handler(CallbackQueryHandler(button_handler))  # Обработчик нажатий на кнопки

    # Запуск бота
    app.run_polling()

if __name__ == '__main__':
    main()
