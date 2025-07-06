import asyncio
from aiogram import Bot, Dispatcher
from handlers import router
import os
from dotenv import load_dotenv
from aiohttp import web

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start_bot():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

async def handle_root(request):
    return web.Response(text="Bot is alive")


async def init_app():
    app = web.Application()
    app.router.add_get("/", handle_root)
    return app


async def main():
    bot_task = asyncio.create_task(start_bot())

    # Start the aiohttp server
    app = await init_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get("PORT", 8000)))
    await site.start()

    print("Bot and server are running...")

    await bot_task

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is offline")
