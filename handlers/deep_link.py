from aiogram import Router, F
from aiogram.types import Message
from baza.anime import get_anime_by_hesh, get_anime_by_title
from baza.users import add_user

router = Router()

@router.message(F.text.startswith("/start"))
async def f(message: Message):
    # /start dan keyingi parametrni olish
    args = message.text.split(maxsplit=1)  # ['/start', 'param']
    param = args[1] if len(args) > 1 else None

    if param:
        try:
            await add_user(message.from_user.id)
            anime = await get_anime_by_hesh(param)
            anime_by_title = await get_anime_by_title(param)
            if anime:
                channel_id, message_id = anime
                await message.bot.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=int(channel_id),
                message_id=int(message_id)
            )
            elif anime_by_title:
                for h in anime_by_title:
                    await message.bot.copy_message(
                    chat_id=message.from_user.id,
                    from_chat_id=int(h[0]),
                    message_id=int(h[1])
                    )
            else:
                await message.answer("❌ Anime topilmadi")
                return

            
        except Exception as e:
            print(e)
            await message.answer("❌ Anime topilmadi")

    else:
        await add_user(message.from_user.id)
        await message.answer("Botga xush kelibsiz!!!")
