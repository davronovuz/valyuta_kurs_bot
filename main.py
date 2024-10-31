import logging
import requests
from aiogram import Bot,Dispatcher,types,executor



API_TOKEN='7609932894:AAGOXqskuv8E-rZG_M_XIaiHQlSQHGxahzo'


logging.basicConfig(level=logging.INFO)


bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)






#start komandasi uchun handler
@dp.message_handler(commands='start')
async def start_handler(message:types.Message):
    username=message.from_user.full_name
    text=f"Assalomu alaykum {username}\n\n"
    text+=f"Valyuta kurslari telegram botiga xush kelibsiz "
    await message.answer(text,parse_mode='Markdown')



@dp.message_handler(commands='valyuta')
async def valyuta_course(message:types.Message):

    request=requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
    response=request.json()

    text=f"Sana: {response[0]['Date']}\n\n"
    CURRENSY=['USD','EUR','RUB','EGP']

    for i in response:
        if i['Ccy'] in CURRENSY:
            text+=f"1 {i['CcyNm_UZC']} ~ {i['Rate']} so'm\n"
    await message.answer(text)



@dp.message_handler(commands='dog')
async def valyuta_course(message:types.Message):

    request=requests.get('https://dog.ceo/api/breeds/image/random')
    response=request.json()

    await message.answer_photo()











if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)







