import asyncio

from . import CMD_HELP, catmemes
from .utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(outgoing=True, pattern="abuse$"))
@bot.on(sudo_cmd(pattern="abuse$", allow_sudo=True))
async def abusing(abused):
    index = random.randint(0, len(catmemes.ABUSE_STRINGS) - 1)
    reply_text = catmemes.ABUSE_STRINGS[index]
    await edit_or_reply(abused, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="abusehard$"))
@bot.on(sudo_cmd(pattern="abusehard$", allow_sudo=True))
async def fuckedd(abusehard):
    index = random.randint(0, len(catmemes.ABUSEHARD_STRING) - 1)
    reply_text = catmemes.ABUSEHARD_STRING[index]
    await edit_or_reply(abusehard, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="rape$"))
@bot.on(sudo_cmd(pattern="rape$", allow_sudo=True))
async def raping(raped):
    index = random.randint(0, len(catmemes.RAPE_STRINGS) - 1)
    reply_text = catmemes.RAPE_STRINGS[index]
    await edit_or_reply(raped, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="fuck$"))
@bot.on(sudo_cmd(pattern="fuck$", allow_sudo=True))
async def chutiya(fuks):
    index = random.randint(0, len(catmemes.CHU_STRINGS) - 1)
    reply_text = catmemes.FUK_STRINGS[index]
    await edit_or_reply(fuks, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="thanos$"))
@bot.on(sudo_cmd(pattern="thanos$", allow_sudo=True))
async def thanos(thanos):
    index = random.randint(0, len(catmemes.THANOS_STRINGS) - 1)
    reply_text = catmemes.THANOS_STRINGS[index]
    await edit_or_reply(thanos, reply_text)


@bot.on(admin_cmd(outgoing=True, pattern="kiss$"))
@bot.on(sudo_cmd(pattern="kiss$", allow_sudo=True))
async def _(event):
    catevent = await edit_or_reply(event, "`kiss`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵💋👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@bot.on(admin_cmd(outgoing=True, pattern="fuk$"))
@bot.on(sudo_cmd(pattern="fuk$", allow_sudo=True))
async def _(event):
    catevent = await edit_or_reply(event, "`fuking....`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["👉       ✊️", "👉     ✊️", "👉  ✊️", "👉✊️💦"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@bot.on(admin_cmd(outgoing=True, pattern="sex$"))
@bot.on(sudo_cmd(pattern="sex$", allow_sudo=True))
async def _(event):
    catevent = await edit_or_reply(event, "`sex`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵👼👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


CMD_HELP.update(
    {
        "gali": "**plugin : **`gali`\
        \n\n**Commands :**\
        \n  •  `abuse`\
        \n  •  `abusehard`\
        \n  •  `rape`\
        \n  •  `fuck`\
        \n  •  `thanos`\
        \n  •  `kiss`\
        \n  •  `fuk`\
        \n  •  `sex`\
        \n\n**Function :**\
        \n__First 5 are random gali string generaters__\
        \n__Last 3 are animations\
        "
    }
)
