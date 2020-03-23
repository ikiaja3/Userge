import asyncio
from userge import userge
from pyrogram import Message

LOG = userge.getLogger(__name__)


@userge.on_cmd('restart', about="__Restarts the bot and reload all plugins__")
async def restart_cmd_handler(m: Message):
    ack_message = await m.reply(
        text=f"Restarting Userge Services", reply_to_message_id=m.message_id)

    LOG.info(f"USERGE Services - Restart initiated")
    asyncio.create_task(restart(userge, ack_message))


async def restart(c, m):
    await c.restart()
    await m.edit(f"USERGE Services have been Restarted!")
    LOG.info(f"USERGE - Restarted")