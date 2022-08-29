import openpyxl
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

token = "5774510211:AAEV7NSqrpXLOSf8KMLCm1zrPlvV_RD91dU"

# Initialize bot and dispatcher
bot = Bot(token=token)
dp = Dispatcher(bot)
    

wb = openpyxl.load_workbook('test6.xlsx')  
sheet = wb.active 

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['Almaty', 'Nur-Sultan']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Please select a City', reply_markup=keyboard)

@dp.message_handler(Text(equals='Almaty'))
async def almaty(message: types.Message):
    await message.answer('Please select type phone....')
    
    # case = ['Iphone']
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(*case)
    # @dp.message_handler(Text(equals='Iphone'))
    # async def Iphone(message: types.Message):
    #     cells = sheet['A2':'B13']
    #     for i1,i2 in cells:  
    #         await message.answer("{0:8} {1:8}".format(i1.value,i2.value))

@dp.message_handler(Text(equals='Nur-Sultan'))
async def nur_sultan(message: types.Message):
    await message.answer('Please waiting....')
    chat_id = message.chat.id

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)