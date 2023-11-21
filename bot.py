import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, KeyboardButton
from aiogram.types import URLInputFile
from aiogram.types import InputFile

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Диспетчер
dp = Dispatcher()



# Для записей с типом Secret* необходимо 
# вызывать метод get_secret_value(), 
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")






# Хэндлер на команду /start - начальное меню
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
       [
           types.KeyboardButton(text="/students"),
           types.KeyboardButton(text="/schedule") 
       ],
       [
           types.KeyboardButton(text="/help"),
           types.KeyboardButton(text="/start")
        ]
   ]
    keyboard1 = types.ReplyKeyboardMarkup(keyboard=kb,row_width=0.5)
 
    await message.reply("<b><i>Мы вас приветсвуем, мы рады что вы реши нами воспользоваться)))</i></b>", reply_markup=keyboard1)

    buttons = [
        [
            types.InlineKeyboardButton(text="Беседа ИКТ-37", url="https://t.me/+plICg8WcSl8zNTNi")
        ],
        [
            types.InlineKeyboardButton(text="Написать разработчику", url="https://t.me/just_danya_kr")
        ],
        [
            types.InlineKeyboardButton(text="Помощь",  callback_data="help") 
        ]
    ]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer(
        "<b><u>Выбирите, что вы хотите сделать:</u></b>",
        reply_markup=keyboard
    )

#Хендлер на команду students
@dp.message(Command('students'))
async def cmd_students(message: types.Message):
    buttons = [
        [ 
        types.InlineKeyboardButton(text="Аврамова К.Р.", callback_data="1"),
        types.InlineKeyboardButton(text="Аминджонов А.Х.", callback_data="2")
        ],
        [ 
        types.InlineKeyboardButton(text="Ашкенов Т.Т.", callback_data="3"),
        types.InlineKeyboardButton(text="Балтиев В.А.", callback_data="4")
        ],
        [ 
        types.InlineKeyboardButton(text="Барамохин Н.С.", callback_data="5"),
        types.InlineKeyboardButton(text="Барановский Е.Д.", callback_data="6")
        ],
        [ 
        types.InlineKeyboardButton(text="Богданов А.П.", callback_data="7"),
        types.InlineKeyboardButton(text="Вященко К.Л.", callback_data="8")
        ],
        [ 
        types.InlineKeyboardButton(text="Габбасов А.", callback_data="9"),
        types.InlineKeyboardButton(text="Гусейнов Э.Д.", callback_data="10")
        ],
        [ 
        types.InlineKeyboardButton(text="Кинель А.С.", callback_data="11"),
        types.InlineKeyboardButton(text="Краснянский Д.М.", callback_data="12")
        ],
        [ 
        types.InlineKeyboardButton(text="Кувшинов А.И.", callback_data="13"),
        types.InlineKeyboardButton(text="Левченко Ф.А.", callback_data="14")
        ],
        [ 
        types.InlineKeyboardButton(text="Майдан А.А.", callback_data="15"),
        types.InlineKeyboardButton(text="Макаров Д.И.", callback_data="16")
        ],
        [ 
        types.InlineKeyboardButton(text="Мовчан А.О.", callback_data="17"),
        types.InlineKeyboardButton(text="Мосунов Е.А.", callback_data="18")
        ],
        [ 
        types.InlineKeyboardButton(text="Новикова А.Н.", callback_data="19"),
        types.InlineKeyboardButton(text="Савченко А.К.", callback_data="20")
        ],
        [ 
        types.InlineKeyboardButton(text="Солдатов Е.И.", callback_data="21"),
        types.InlineKeyboardButton(text="Судакова А.С.", callback_data="22")
        ],
        [ 
        types.InlineKeyboardButton(text="Третьяков И.Е.", callback_data="23"),
        types.InlineKeyboardButton(text="Умнов В.О.4", callback_data="24")
        ],
        [ 
        types.InlineKeyboardButton(text="Хадиятов Р.У.", callback_data="25"),
        types.InlineKeyboardButton(text="Шматов К.Д.", callback_data="26")
        ]
        ]
        
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    image = URLInputFile('https://sun9-37.userapi.com/impg/W9ND4OuspTYr8WqLZh3qir8yzJcHSLxErSNj8g/aUzMBOMnNQs.jpg?size=668x1107&quality=95&sign=0e2afb36f43dc6bb42e27cf0b92fd452&type=album')
    await bot.send_photo(message.chat.id, image , caption='<b><i>Выберите про кого вы хотите узнать информацию:</i></b>', reply_markup=keyboard)

# Хендлер help и для кнопки start - о командах бота
@dp.message(Command('help'))
async def help(message: types.Message):
    await message.reply('/start - для начального меню \n'
                        '/help - тут описаны все важные команды\n'
                        '/information - информация о боте\n'
                        '/students - про студентов IKT-37\n'
                        '/schedule - расписание')
@dp.callback_query(F.data == 'help')
async def help(callback: types.CallbackQuery):
    await callback.message.answer('/start - для начала использования бота \n'
                        '/help - тут описаны все важные команды\n'
                        '/information - информация о боте\n'
                        '/students - про студентов IKT-37\n'
                        '/schedule - расписание')
    await callback.answer()





# Хендлер information - информация о боте
@dp.message(Command('information'))
async def help(message: types.Message):
    image = URLInputFile('https://sun9-34.userapi.com/impg/wARHgJ5H368qnfFmpJpIY_mAqsQj7HGPi6sQjA/pWJXTxwyUH8.jpg?size=1440x2160&quality=95&sign=d8a86351a8cb61bc636e9e2217e7eed9&type=album')

    await bot.send_photo(message.chat.id, image , caption='<i><u><b>Разработчик бота</b> - Краснянский Даниил Михайлович</u>\n'
    'Этот бот создан для того чтобы лучше узнать, как кого зовут! Я выполнял этого бота для тренировки себя в программирование.</i>\n'
    'В этом боте рассказано про каждого студента группы IKT-37.')

# Хендлер на /schedule
@dp.message(Command('schedule'))
async def sch(message: types.Message):
    buttons = [
        [ 
        types.InlineKeyboardButton(text="Ноябрь", callback_data="n")
        ],
        [ 
        types.InlineKeyboardButton(text="Декабрь", callback_data="d")
        ],
        ]
        
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer(
        "<b><u>На какой месяц вы хотите расписание?</u></b>",
        reply_markup=keyboard)
# калбеки для ноября
@dp.callback_query(F.data == 'n')
async def n(callback: types.CallbackQuery):
    image1 = types.URLInputFile('https://sun9-42.userapi.com/impg/RRzILMAvE3-AayFLqp6m6ruZJU-oZRfeIVgIJA/CDttjYBcE9M.jpg?size=970x1563&quality=96&sign=fc72a61dfc9eed231f630543ce1fb6b7&type=album')
    await callback.message.reply_photo(image1, '<b>Расписание на НОЯБРЬ</b>' )
    await callback.answer()
# кэлбэк для декабря
@dp.callback_query(F.data == 'd')
async def n(callback: types.CallbackQuery):
    image1 = types.URLInputFile('https://sun9-5.userapi.com/impg/wmB3olC2Wtxaexrof9tFkMGSdrtCi_PVVlaGBA/YIIk-FzQoD8.jpg?size=966x1530&quality=96&sign=8fa50bcdb465bba2d259589c1d892b42&type=album')
    await callback.message.reply_photo(image1, '<b>Расписание на ДЕКАБРЬ</b>' )
    await callback.answer()
# калбеки для стюдентс
#1
@dp.callback_query(F.data == '1')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/+79605264208")
        )
    image = URLInputFile('https://sun9-30.userapi.com/impg/jlzu0paH6iL3wHe9A99WsQCTGHAuzrk1i6TxkA/CX2bqkh9kvg.jpg?size=1200x1600&quality=96&sign=094d33de7bd9fd68f81cb49c2105aa76&type=album')
    await callback.message.answer_photo(image,'<b><u>Аврамова Ксения Романовна</u></b> \n<i><b>Родилась: 09.05.2005\n Интерисуется програмированием. \nРаньше занималась карате.\n'
                                        'Её вариант - 1</b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#2
@dp.callback_query(F.data == '2')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('https://sun9-48.userapi.com/impg/K3vvVhtJ4ynj0dollq3MlocZdOSKKmdcYXwkRw/rVwM_BNjkMM.jpg?size=1200x1600&quality=96&sign=72e69bb953767bc1a4db7cc9561d3e84&type=album')
    await callback.message.answer_photo(image,'<b><u>Амиджонов Амирджон Хушбахтович</u></b> \n<i><b>Родился 08.10.2006\nХобби: комп игры , футбол да и все \nЕго вариант - 2</b></i>',reply_markup=builder.as_markup())
    await callback.answer()
#3
@dp.callback_query(F.data == '3')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('https://sun9-55.userapi.com/impg/q8CK0l3fv2OP-2TQ4uYyIISPu5nlDUONQdzEcw/H9IsShMI3cI.jpg?size=2560x1919&quality=95&sign=fca18f4175a8e8448dd969919466c602&type=album')
    await callback.message.answer_photo(image,'<b><u>Ташкенов Тимур Талгатбекович</u></b> \n<i><b>Родился: 01.12.2005 в городе Алматы\n'
                                        'Rогда рожали все менты дрожали по идее, а так четкий прямой чувак. Всем мир\n'
                                        'Его вариант - 3</b></i>',reply_markup=builder.as_markup())
    await callback.answer()
#4
@dp.callback_query(F.data == '4')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('https://sun9-40.userapi.com/impg/JmdQMaCxBfhnziGoL2-j0mClZ3RC7J5NRxwYbA/w62EHD1cF_E.jpg?size=1620x2160&quality=96&sign=8dc095b8b34115894c07088cbdef97fc&type=album')
    await callback.message.answer_photo(image,'<b><u>Балтиев Владимир Алексанлрович</u></b> \n<i><b>Родился: 02.12.2005\nЕго вариант - 4</b></i>',reply_markup=builder.as_markup())
    await callback.answer()
#5
@dp.callback_query(F.data == '5')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('https://sun9-17.userapi.com/impg/FF7pqaLIok7pJzCv2rjJYaso7vUJZGS_RQx1ZQ/wF74q02-hyM.jpg?size=1620x2160&quality=96&sign=3076d1bee3a8a4fe915643fa27962893&type=album')
    await callback.message.answer_photo(image,'<b><u>Барамохин Никита Сергеевич</u></b> \n<i><b>Родился^ 01.07.2005\nОн по жизни спортик\nЕго вариант - 5</b></i>',reply_markup=builder.as_markup())
    await callback.answer()
#6
@dp.callback_query(F.data == '6')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('https://sun9-12.userapi.com/impg/VbJ4gZlVjPbm9mm00ny_tcxlir0VezM3rWZwmw/0XTDIzWYEmI.jpg?size=1620x2160&quality=95&sign=536af6ac70a4fa72712d08f06867647e&type=album')
    await callback.message.answer_photo(image,'<b><u>Барановский Егор Дмитревич</u></b> \n<i><b>Хобби:валяюсь на кровати. А также интерисуется програмированием и инвестициями.\n'
                                        'Его вариант 6</b></i>',reply_markup=builder.as_markup())
    await callback.answer()
#7
@dp.callback_query(F.data == '7')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('https://sun9-8.userapi.com/impg/J-_fyo3xa8D-DICgY0qD8kd-91M9gPr_ocXWhA/ADYpo-VHbu0.jpg?size=1200x1600&quality=96&sign=d4d590a6507f0d09b712f516e7d1edbb&type=album')
    await callback.message.answer_photo(image,'<b><u>Богданов Артём Павлович</u></b> \n<i><b>Родился: 17.08.2005\nИграет в CS и Dota\nЕго вариант - 7</b></i>',reply_markup=builder.as_markup())
    await callback.answer()
#8
@dp.callback_query(F.data == '8')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('https://actomrussia.ru/images/2020/11/16/2816616767.jpg')
    await callback.message.answer_photo(image,'<b><u>Вященко Константин Леонидович</u></b> \n<i><b>Родился: 04.03.2005\nХобби сидеть кайфовать\nЕго вариант - 8</b></i>',reply_markup=builder.as_markup())
    await callback.answer()
#9
@dp.callback_query(F.data == '9')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('https://sun9-15.userapi.com/impg/IJ01YqqmjajFNSwrWyAQX-0j2MNiXg-KGVsN-Q/uPG_60uYvTM.jpg?size=640x640&quality=95&sign=aa2598fd328815af088bb68925232d1c&type=album')
    await callback.message.answer_photo(image,'<b><u>Габбасов Алишер</u></b> \n<i><b>Родился 22.10.2004\Хобби писать книги\nЕго вариант - 9</b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#10
@dp.callback_query(F.data == '10')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('https://sun9-67.userapi.com/impg/hd5_mt4O704ZqRzn70JsG-_R1pwdAAgb_f3LZg/eZ-f5N8WVOU.jpg?size=1215x2160&quality=95&sign=e3ddfa7f05aaa64c68c9c90c2ed54ba3&type=album')
    await callback.message.answer_photo(image,'<b><u>Гусейнов Эльдар Джавидович</u></b> \n<i><b>Родился: 16.08.2005\n Увлекаюсь битмейкингом и немного программированием, люблю смотреть аниме заниматься прокрастинацией\nЕго вариант - 10</b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#11
@dp.callback_query(F.data == '11')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('https://actomrussia.ru/images/2020/11/16/2816616767.jpg')
    await callback.message.answer_photo(image,'<b><u>Кинель Алексей Сергеевич</u></b> \n<i><b>Родился: 13.08.2005\nХобби: комп.игры, чтение книг. \nИнтересуюсь: автомобилями, сборками пк.\nЕго вариант - 11</b></i>',reply_markup=builder.as_markup())
    await callback.answer()
#12
@dp.callback_query(F.data == '12')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('https://sun9-34.userapi.com/impg/wARHgJ5H368qnfFmpJpIY_mAqsQj7HGPi6sQjA/pWJXTxwyUH8.jpg?size=1440x2160&quality=95&sign=d8a86351a8cb61bc636e9e2217e7eed9&type=album')
    await callback.message.answer_photo(image,'<b><u>Краснянский Даниил Михайлови:</u></b> \n<i><b>Родился: 08.10.2005 \nЗаместитель старосты группы ИКТ 37. \nЕго вариант - 12\n'
                                  'Хобби - программирование, монтаж видеороликов, плаванье и другие.</b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#13
@dp.callback_query(F.data == '13')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('https://sun9-17.userapi.com/impg/5reTtZbThL89GchIhU0ZOMtCD6kiF_c6KpWxdA/85hCgSXizxo.jpg?size=960x1280&quality=95&sign=85899a0753e087f44b53b1c44507c6c0&type=album')
    await callback.message.answer_photo(image,'<b><u>Кувшинов Александр Игоревич</u></b> \n<i><b>Родился: 05.12.2004\nЛюблю рок-музыку (в частности метал), обожаю костюмы и люблю смеяться.\nЕго вариант - 13</b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#14
@dp.callback_query(F.data == '14')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('https://sun9-12.userapi.com/impg/k1dju9O3gXS8kYVHI0IjluD87fWSWPQjyNzdXw/AolTiK2vbwM.jpg?size=2560x1920&quality=95&sign=ac211a90f472930e542c64e6058782bb&type=album')
    await callback.message.answer_photo(image,'<b><u>Левченко Фёдор Андреевич</u></b> \n<i><b>Родился: 24.04.2004\nЯвляется старостой группы ИКТ-37\nУвличения тачки, комп\nЕго вариант - 14</b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#15
@dp.callback_query(F.data == '15')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('')
    await callback.message.answer_photo(image,'<b><u>Майдан Анна Алексеевна</u></b> \n<i><b></b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#16
@dp.callback_query(F.data == '16')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('')
    await callback.message.answer_photo(image,'<b><u>Макаров Даниил Игоревич</u></b> \n<i><b></b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#17
@dp.callback_query(F.data == '17')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('')
    await callback.message.answer_photo(image,'<b><u>Мовчан Алёна Олеговна</u></b> \n<i><b></b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#18
@dp.callback_query(F.data == '18')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('')
    await callback.message.answer_photo(image,'<b><u>Мосунов Егор Андреевич</u></b> \n<i><b></b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#19
@dp.callback_query(F.data == '19')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('')
    await callback.message.answer_photo(image,'<b><u>Новикова Анастасия Николаевна</u></b> \n<i><b></b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#20
@dp.callback_query(F.data == '20')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('')
    await callback.message.answer_photo(image,'<b><u>Савченко Алиса Константиновна</u></b> \n<i><b></b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#21
@dp.callback_query(F.data == '21')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/+79116847149")
        )
    image = URLInputFile('https://sun9-52.userapi.com/impg/wcAEYm269FZNhN32GgxHHV1_dHUqGOU9c7LfwQ/hju8ReP7Y1s.jpg?size=1200x1600&quality=95&sign=0e75495f8e56ca56b5a8466e71946532&type=album')
    await callback.message.answer_photo(image,'<b><uСолдатов Егор Игоревичu></b> \n<i><b>Родился: 21.01.2005\nУвлечения армрестлинг, кс\nЕго вариант - 21</b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#22
@dp.callback_query(F.data == '22')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('')
    await callback.message.answer_photo(image,'<b><u>Судокова Александра Сергеевна</u></b> \n<i><b></b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#23
@dp.callback_query(F.data == '23')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('')
    await callback.message.answer_photo(image,'<b><u>Третьеков Иван Евгеньевич</u></b> \n<i><b></b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#24
@dp.callback_query(F.data == '24')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('')
    await callback.message.answer_photo(image,'<b><u>Умнов Вадим Олегович</u></b> \n<i><b></b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#25
@dp.callback_query(F.data == '25')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('')
    await callback.message.answer_photo(image,'<b><u>Хадиятов Родион Уралович</u></b> \n<i><b></b></i>', reply_markup=builder.as_markup())
    await callback.answer()
#26
@dp.callback_query(F.data == '26')
async def help(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать", 
        url="https://t.me/")
        )
    image = URLInputFile('')
    await callback.message.answer_photo(image,'<b><u>Шматов Константин Денисович</u></b> \n<i><b></b></i>', reply_markup=builder.as_markup())
    await callback.answer()



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())