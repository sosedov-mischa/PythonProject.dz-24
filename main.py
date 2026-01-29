from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram.utils.formatting import Text

from Keyboar import *

bot_token = "8504316835:AAE0Fablv1zhVcQy7NJB0-Nc9NOr_GxA2HE"
bot = Bot(token=bot_token)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer("Привет я телеграмм бот. Помогающий подобрать лучший подарок для друзей и близких.")
    await message.answer("Инструкция: \n"
                        "1. Вы говорите для кого подарок (Маме, Папе, Сестре, и т.д.) \n"
                        "2. Вы говорите то сколько денег вы готовы потратить на подарок.\n"
                        "3. Я подберу подходящие для вас варианты.")
    await message.answer(text="↓ клавиатура 1 ↓", reply_markup=keyword1)



@dp.message(Command(commands=["глав._меню"]))
async def process_start_command_1(message: Message):
    await message.answer(text="↓ клавиатура 1 ↓", reply_markup=keyword1)

@dp.message(Command(commands=["меню_мама"]))
async def process_start_command_2(message: Message):
    await message.answer(text="↓ клавиатура 2 ↓", reply_markup=keyword2)

@dp.message(Command(commands=["меню_папа"]))
async def process_start_command_2(message: Message):
    await message.answer(text="↓ клавиатура 2 ↓", reply_markup=keyword2_1)

@dp.message(Command(commands=["меню_брат"]))
async def process_start_command_2(message: Message):
    await message.answer(text="↓ клавиатура 2 ↓", reply_markup=keyword2_3)

@dp.message(Command(commands=["меню_сестра"]))
async def process_start_command_2(message: Message):
    await message.answer(text="↓ клавиатура 2 ↓", reply_markup=keyword2_4)

@dp.message(Command(commands=["меню_друг"]))
async def process_start_command_2(message: Message):
    await message.answer(text="↓ клавиатура 2 ↓", reply_markup=keyword2_5)

@dp.message(Command(commands=["меню_подруга"]))
async def process_start_command_2(message: Message):
    await message.answer(text="↓ клавиатура 2 ↓", reply_markup=keyword2_6)

# ----------------------------------------------------------------------------------------------Маме------
# ---------------------------------------------------------------------------------------------------------

@dp.message(Command(commands=["Маме"]))
async def process_start_command_3(message: Message):
    await message.answer("Сколько денег вы готовы потратить на подарок.")
    await message.answer(text="↓ клавиатура 2 ↓", reply_markup=keyword2)


@dp.message(Command(commands=["50-100р"]))                                       #1
async def process_start_command_4(message: Message):
    await message.answer("1) Подставка для смартфона - 78 рубей.")
    await message.answer("2) Антистресс 'лапка' - 83 руб.")
    await message.answer("3) Сладкий подарок - 87 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword3)


@dp.message(Command(commands="1m"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'Подставка для смартфона' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="2m"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'Антистресс 'лапка'' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="3m"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш 'Сладкий подарок' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)

# --------------

@dp.message(Command(commands=["100-200р"]))                                       #2
async def process_start_command_8(message: Message):
    await message.answer("1) указка с пальцем - 120 руб.")
    await message.answer("2) настольный пенал - 150 руб.")
    await message.answer("3) копилка - 175 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword12)


@dp.message(Command(commands="4m"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'указка с пальцем' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="5m"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'настольный пенал' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="6m"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'копилка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)

# --------------

@dp.message(Command(commands=["200-500р"]))                                       #3
async def process_start_command_9(message: Message):
    await message.answer("1) кружка на заказ - 250 руб.")
    await message.answer("2) ночник - 400 руб.")
    await message.answer("3) семейное фото - 450 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword13)

@dp.message(Command(commands="7m"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'кружка на заказ' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="8m"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'ночник' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="9m"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш 'семейное фото' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)

# --------------

@dp.message(Command(commands=["500-1000р"]))                                       #4
async def process_start_command_10(message: Message):
    await message.answer("1) картина - 600 руб.")
    await message.answer("2) статуэтка - 750 руб.")
    await message.answer("3) ваза - 800 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword14)

@dp.message(Command(commands="10m"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'картина' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="11m"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'статуэтка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="12m"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'ваза' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)

# --------------

@dp.message(Command(commands=["1000-2000р"]))                                       #5
async def process_start_command_11(message: Message):
    await message.answer("1) духи - 1000 руб.")
    await message.answer("2) косметика - 1500 руб.")
    await message.answer("3) футболка с именем мамы - 2000 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword15)

@dp.message(Command(commands="13m"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'духи' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="14m"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'косметика' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="15m"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'футболка с именем мамы' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)

# --------------

@dp.message(Command(commands=["2000-5000р"]))                                       #6
async def process_start_command_12(message: Message):
    await message.answer("1) сумка - 2500 руб.")
    await message.answer("2) платёж в спорт-клуб - 3000 руб.")
    await message.answer("3) корзина продуктов - 5000 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword16)

@dp.message(Command(commands="16m"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'сумка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="17m"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'платёж в спорт-клуб' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="18m"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваша 'корзина продуктов' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)

# ----------------------------------------------------------------------------------------------Папе------
# ---------------------------------------------------------------------------------------------------------

@dp.message(Command(commands=["Папе"]))
async def process_start_command_13(message: Message):
    await message.answer("Сколько денег вы готовы потратить на подарок.")
    await message.answer(text="↓ клавиатура 2 ↓", reply_markup=keyword2_1)


@dp.message(Command(commands=["50-101р"]))  # 1
async def process_start_command_4(message: Message):
    await message.answer("1) Подставка для смартфона - 78 руб.")
    await message.answer("2) коллекционная машинка - 100 руб.")
    await message.answer("3) Сладкий подарок - 87 руб.")
    await message.answer(text="↓ клавиатура 17 ↓", reply_markup=keyword17)


@dp.message(Command(commands="1p"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'Подставка для смартфона' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="2p"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'коллекционная машинка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="3p"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш 'Сладкий подарок' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["100-201р"]))  # 2
async def process_start_command_8(message: Message):
    await message.answer("1) указка с пальцем - 120 руб.")
    await message.answer("2) настольный пенал - 150 руб.")
    await message.answer("3) копилка - 175 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword18)


@dp.message(Command(commands="4p"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'Подставка для смартфона' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="5p"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'настольный пенал' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="6p"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваша 'копилка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["200-501р"]))  # 3
async def process_start_command_9(message: Message):
    await message.answer("1) кружка на заказ - 250 руб.")
    await message.answer("2) ночник 'белый' - 400 руб.")
    await message.answer("3) семейное фото - 450 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword19)


@dp.message(Command(commands="7p"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'кружка на заказ' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="8p"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'ночник' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="9p"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш 'семейное фото' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["500-1001р"]))  # 4
async def process_start_command_10(message: Message):
    await message.answer("1) картина - 600 руб.")
    await message.answer("2) статуэтка - 750 руб.")
    await message.answer("3) повербанк ГИГАНТ - 800 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword110)


@dp.message(Command(commands="10p"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'картина' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="11p"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'статуэтка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="12p"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'повербанк' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["1000-2001р"]))  # 5
async def process_start_command_11(message: Message):
    await message.answer("1) духи - 1000 руб.")
    await message.answer("2) логотип его машины - 1500 руб.")
    await message.answer("3) футболка с именем папы - 2000 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword111)


@dp.message(Command(commands="13p"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'духи' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="14p"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'логотип его машины' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="15p"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш 'футболка с именем папы' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["2000-5001р"]))  # 6
async def process_start_command_12(message: Message):
    await message.answer("1) сумка - 2500 руб.")
    await message.answer("2) платёж в спорт-клуб - 3000 руб.")
    await message.answer("3) беспров.наушники - 5000 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword112)


@dp.message(Command(commands="16p"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'сумка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="17p"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'платёж в спорт-клуб' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)



@dp.message(Command(commands="18p"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'беспров.наушники' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)



# ---------------------------------------------------------------------------------------------Сестре------
# ---------------------------------------------------------------------------------------------------------

@dp.message(Command(commands=["Сестре"]))
async def process_start_command_17(message: Message):
    await message.answer("Сколько денег вы готовы потратить на подарок.")
    await message.answer(text="↓ клавиатура 2 ↓", reply_markup=keyword2_3)


@dp.message(Command(commands=["51-100р"]))  # 1
async def process_start_command_4(message: Message):
    await message.answer("1) Подставка для смартфона - 78 руб.")
    await message.answer("2) Антистресс 'лапка' - 83 руб.")
    await message.answer("3) Сладкий подарок - 87 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword113)


@dp.message(Command(commands="1s"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'Подставка для смартфона' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="2s"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'Антистресс 'лапка'' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="3s"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш 'Сладкий подарок' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["101-200р"]))  # 2
async def process_start_command_8(message: Message):
    await message.answer("1) указка с пальцем - 120 руб.")
    await message.answer("2) настольный пенал - 150 руб.")
    await message.answer("3) копилка - 175 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword114)


@dp.message(Command(commands="4s"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'указка с пальцем' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="5s"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'настольный пенал' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="6s"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'копилка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["201-500р"]))  # 3
async def process_start_command_9(message: Message):
    await message.answer("1) кружка на заказ - 250 руб.")
    await message.answer("2) ночник 'розовый' - 400 руб.")
    await message.answer("3) семейное фото - 450 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword115)


@dp.message(Command(commands="7p"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'кружка на заказ' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="8s"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'ночник' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="9s"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'семейное фото' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["501-1000р"]))  # 4
async def process_start_command_10(message: Message):
    await message.answer("1) картина - 600 руб.")
    await message.answer("2) статуэтка - 750 руб.")
    await message.answer("3) камин на батарейках - 800 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword116)


@dp.message(Command(commands="10s"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'картина' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="11s"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'статуэтка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="12s"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'камин' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["1001-2000р"]))  # 5
async def process_start_command_11(message: Message):
    await message.answer("1) духи - 1000 руб.")
    await message.answer("2) косметика - 1500 руб.")
    await message.answer("3) футболка с именем сестры - 2000 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword117)


@dp.message(Command(commands="13s"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'духи' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="14s"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'косметика' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="15s"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш 'футболка с именем сестры' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["2001-5000р"]))  # 6
async def process_start_command_12(message: Message):
    await message.answer("1) сумка - 2500 руб.")
    await message.answer("2) серёжки - 3000 руб.")
    await message.answer("3) смарт-часы - 5000 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword118)


@dp.message(Command(commands="16s"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'сумка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="17s"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'серёжки' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)



@dp.message(Command(commands="18s"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'смарт-часы' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# ---------------------------------------------------------------------------------------------Брату------
# ---------------------------------------------------------------------------------------------------------

@dp.message(Command(commands=["Брату"]))
async def process_start_command_17(message: Message):
    await message.answer("Сколько денег вы готовы потратить на подарок.")
    await message.answer(text="↓ клавиатура 2 ↓", reply_markup=keyword2_4)


@dp.message(Command(commands=["50-102р"]))  # 1
async def process_start_command_4(message: Message):
    await message.answer("1) Подставка для смартфона - 78 руб.")
    await message.answer("2) Антистресс 'лапка' - 83 руб.")
    await message.answer("3) Сладкий подарок - 87 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword119)


@dp.message(Command(commands="1b"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'Подставка для смартфона' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="2b"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'Антистресс 'лапка'' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="3b"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш 'Сладкий подарок' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["100-202р"]))  # 2
async def process_start_command_8(message: Message):
    await message.answer("1) указка с пальцем - 120 руб.")
    await message.answer("2) настольный пенал - 150 руб.")
    await message.answer("3) копилка - 175 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword120)


@dp.message(Command(commands="4b"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'указка с пальцем' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="5b"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'настольный пенал' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="6b"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'копилка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["200-502р"]))  # 3
async def process_start_command_9(message: Message):
    await message.answer("1) кружка на заказ - 250 руб.")
    await message.answer("2) ночник - 400 руб.")
    await message.answer("3) семейное фото - 450 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword121)


@dp.message(Command(commands="7b"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'кружка на заказ' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="8b"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'ночник' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="9b"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'семейное фото' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["500-1002р"]))  # 4
async def process_start_command_10(message: Message):
    await message.answer("1) картина - 600 руб.")
    await message.answer("2) статуэтка - 750 руб.")
    await message.answer("3) неон маска - 800 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword122)


@dp.message(Command(commands="10b"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'картина' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="11b"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'статуэтка персонажа' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="12b"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'неон маска' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["1000-2002р"]))  # 5
async def process_start_command_11(message: Message):
    await message.answer("1) автомат игрушечный - 1000 руб.")
    await message.answer("2) духи - 1500 руб.")
    await message.answer("3) футболка с именем брата - 2000 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword123)


@dp.message(Command(commands="13b"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'автомат игрушечный' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="14b"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'духи' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="15b"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'футболка с именем брата' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["2000-5002р"]))  # 6
async def process_start_command_12(message: Message):
    await message.answer("1) мини-принтер - 2500 руб.")
    await message.answer("2) колонка bluetooth - 3000 руб.")
    await message.answer("3) дрифт машинка на радио-управлении - 5000 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword124)


@dp.message(Command(commands="16b"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'мини-принтер' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="17b"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'колонка bluetooth' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)



@dp.message(Command(commands="18b"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш 'дрифт машинка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# ----------------------------------------------------------------------------------------------Другу------
# ---------------------------------------------------------------------------------------------------------


@dp.message(Command(commands=["Другу"]))
async def process_start_command_18(message: Message):
    await message.answer("Сколько денег вы готовы потратить на подарок.")
    await message.answer(text="↓ клавиатура 2 ↓", reply_markup=keyword2_5)


@dp.message(Command(commands=["52-100р"]))  # 1
async def process_start_command_4(message: Message):
    await message.answer("1) Подставка для смартфона - 78 руб.")
    await message.answer("2) Антистресс 'лапка' - 83 руб.")
    await message.answer("3) Сладкий подарок - 87 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword131)


@dp.message(Command(commands="1d"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'Подставка для смартфона' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="2d"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'Антистресс 'лапка'' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="3d"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш 'Сладкий подарок' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["102-200р"]))  # 2
async def process_start_command_8(message: Message):
    await message.answer("1) указка с пальцем - 120 руб.")
    await message.answer("2) настольный пенал - 150 руб.")
    await message.answer("3) копилка - 175 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword132)


@dp.message(Command(commands="4d"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'указка с пальцем' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="5d"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'настольный пенал' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="6d"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'копилка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["202-500р"]))  # 3
async def process_start_command_9(message: Message):
    await message.answer("1) кружка на заказ - 250 руб.")
    await message.answer("2) ночник - 400 руб.")
    await message.answer("3) ваше фото - 450 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword133)


@dp.message(Command(commands="7d"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'кружка на заказ' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="8d"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'ночник' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="9d"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'ваше фото' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["502-1000р"]))  # 4
async def process_start_command_10(message: Message):
    await message.answer("1) картина - 600 руб.")
    await message.answer("2) статуэтка - 750 руб.")
    await message.answer("3) камин на батарейках - 800 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword134)


@dp.message(Command(commands="10d"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'картина' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="11d"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'статуэтка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="12d"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'камин на батарейках' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["1002-2000р"]))  # 5
async def process_start_command_11(message: Message):
    await message.answer("1) лего - 1000 руб.")
    await message.answer("2) фингерборд + скейт-парк - 1500 руб.")
    await message.answer("3) футболка с именем друга - 2000 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword135)


@dp.message(Command(commands="13d"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'лего' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="14d"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'фингерборд + скейт-парк' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="15d"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'футболка с именем друга' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["2002-5000р"]))  # 6
async def process_start_command_12(message: Message):
    await message.answer("1) сумка - 2500 руб.")
    await message.answer("2) дрифт машинка - 3000 руб.")
    await message.answer("3) автомат игрушечный - 5000 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword136)


@dp.message(Command(commands="16d"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'сумка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="17d"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'дрифт машинка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)



@dp.message(Command(commands="18d"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'автомат игрушечный' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# ----------------------------------------------------------------------------------------------Подруге---
# ---------------------------------------------------------------------------------------------------------


@dp.message(Command(commands=["Подруге"]))
async def process_start_command_19(message: Message):
    await message.answer("Сколько денег вы готовы потратить на подарок.")
    await message.answer(text="↓ клавиатура 2 ↓", reply_markup=keyword2_6)


@dp.message(Command(commands=["51-101р"]))  # 1
async def process_start_command_4(message: Message):
    await message.answer("1) Подставка для смартфона - 78 руб.")
    await message.answer("2) Антистресс 'лапка' - 83 руб.")
    await message.answer("3) Сладкий подарок - 87 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword125)


@dp.message(Command(commands="1s"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'Подставка для смартфона' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="2s"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'Антистресс 'лапка'' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="3s"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш 'Сладкий подарок' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["101-201р"]))  # 2
async def process_start_command_8(message: Message):
    await message.answer("1) указка с пальцем - 120 руб.")
    await message.answer("2) настольный пенал - 150 руб.")
    await message.answer("3) копилка - 175 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword126)


@dp.message(Command(commands="4s"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'указка с пальцем' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="5s"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'настольный пенал' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="6s"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'копилка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["201-501р"]))  # 3
async def process_start_command_9(message: Message):
    await message.answer("1) кружка на заказ - 250 руб.")
    await message.answer("2) ночник 'розовый' - 400 руб.")
    await message.answer("3) ваше фото - 450 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword127)


@dp.message(Command(commands="7p"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'кружка на заказ' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="8s"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'ночник' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="9s"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'ваше фото' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["501-1001р"]))  # 4
async def process_start_command_10(message: Message):
    await message.answer("1) картина - 600 руб.")
    await message.answer("2) статуэтка - 750 руб.")
    await message.answer("3) камин на батарейках - 800 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword128)


@dp.message(Command(commands="10s"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'картина' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="11s"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'статуэтка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="12s"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'камин' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["1001-2001р"]))  # 5
async def process_start_command_11(message: Message):
    await message.answer("1) духи - 1000 руб.")
    await message.answer("2) косметика - 1500 руб.")
    await message.answer("3) футболка с именем подруги - 2000 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword129)


@dp.message(Command(commands="13s"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'духи' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="14s"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'косметика' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="15s"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш 'футболка с именем подруги' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# --------------

@dp.message(Command(commands=["2001-5001р"]))  # 6
async def process_start_command_12(message: Message):
    await message.answer("1) сумка - 2500 руб.")
    await message.answer("2) серёжки - 3000 руб.")
    await message.answer("3) смарт-часы - 5000 руб.")
    await message.answer(text="↓ клавиатура 3 ↓", reply_markup=keyword130)


@dp.message(Command(commands="16s"))
async def process_gift_stand_5(message: Message):
    await message.answer("Ваш подарок 'сумка' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


@dp.message(Command(commands="17s"))
async def process_gift_stand_6(message: Message):
    await message.answer("Ваш подарок 'серёжки' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)



@dp.message(Command(commands="18s"))
async def process_gift_stand_7(message: Message):
    await message.answer("Ваш подарок 'смарт-часы' готовится")
    await message.answer(text="Выберите, кому еще хотите подарить:", reply_markup=keyword1)


# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------


@dp.message()
async def process_start_command(message: Message):
    await message.answer("Я не знаю такой команды")

dp.run_polling(bot)
