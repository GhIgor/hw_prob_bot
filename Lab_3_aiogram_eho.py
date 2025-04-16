from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from aiogram import F

# токен вашего бота, полученный у @BotFather
BOT_TOKEN = '7963539181:AAGt_4IIW1bVMRkUk9B_AbVOEMQp6CWjeOU'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )

# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)

dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)

# Этот хэндлер будет срабатывать на отправку боту стикер
async def send_photo_echo(message: Message):
    print(message)
    await message.reply_sticker(message.sticker.file_id)

dp.message.register(send_photo_echo, F.content_type == ContentType.STICKER)

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text) # отличие от метода message.answer - в ответе на сообщение


if __name__ == '__main__':
    dp.run_polling(bot)