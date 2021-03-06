from nonebot.rule import to_me
from nonebot.typing import Event
from nonebot.plugin import on_startswith
from nonebot.adapters.cqhttp import Bot
from nonebot.adapters.ding import Bot as DingBot, Event as DingEvent
from nonebot.permission import GROUP_ADMIN

test_command = on_startswith("hello", to_me(), permission=GROUP_ADMIN)


@test_command.handle()
async def test_handler(bot: Bot, event: Event, state: dict):
    await test_command.finish("cqhttp hello")


@test_command.handle()
async def test_handler(bot: DingBot, event: DingEvent, state: dict):
    await test_command.finish("ding hello")
