⟜꯭͓❤⃪꯭ฺฺ͓ٖٖٖٖٖٖٖٖٖٖٖٖ𝗥⃪꯭͓𝗼⃪꯭͓𝗺⃪꯭͓𝗮⃪꯭͓⃔𝗮⃪꯭͓𝗻⃪꯭ฺฺฺฺ͓ٖٖٖٖٖٖٖٖٖٖٖٖٖٖ:
import time
import os, logging, asyncio, random
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

from config import BOT_TOKEN as bot_token, API_ID as api_id, API_HASH as api_hash

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(name)

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)


spam_chats = []


@client.on(events.NewMessage(pattern="^/htag ?(.*)"))
async def mention_all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "This command can be used in groups and channels!"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐓𝐨 𝐀𝐥𝐥 𝐁𝐚𝐛𝐲...")
    
    if event.pattern_match.group(1):
        return await event.respond("/htag  👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐎𝐤 𝐅𝐨𝐫 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..")
    else:
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
        if msg is None:
            return await event.respond(
                "/htag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐎𝐫 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞..."
            )

    spam_chats.append(chat_id)
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        user_id = usr.id
        mention_text = f"[{usr.first_name}](tg://user?id={user_id}) {random.choice(TAGMES)}"
        await client.send_message(chat_id, mention_text)
        time.sleep(5)
        
    try:
        spam_chats.remove(chat_id)
    except:
        pass
        



EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]
  
@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mention_all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "This command can be used in groups and channels!"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐓𝐨 𝐀𝐥𝐥 𝐁𝐚𝐛𝐲...")

if event.pattern_match.group(1):
        return await event.respond("/etag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐎𝐤 𝐅𝐨𝐫 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..")
    else:
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
        if msg is None:
            return await event.respond(
                "/etag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐎𝐫 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞..."
            )

    spam_chats.append(chat_id)
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        user_id = usr.id
        mention_text = f"[ {random.choice(EMOJI)} ](tg://user?id={usr.id})"
        await client.send_message(chat_id, mention_text)
        time.sleep(5)
        
    try:
        spam_chats.remove(chat_id)
    except:
        pass
         
 
                   
                          
TAGMES = [ " 𝐇𝐞𝐲 𝐁𝐚𝐛𝐲 𝐊𝐚𝐡𝐚 𝐇𝐨🥱 ",
           " 𝐎𝐲𝐞 𝐒𝐨 𝐆𝐲𝐞 𝐊𝐲𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚𝐨😊 ",
           " 𝐕𝐜 𝐂𝐡𝐚𝐥𝐨 𝐁𝐚𝐭𝐞𝐧 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧 𝐊𝐮𝐜𝐡 𝐊𝐮𝐜𝐡😃 ",
           " 𝐊𝐡𝐚𝐧𝐚 𝐊𝐡𝐚 𝐋𝐢𝐲𝐞 𝐉𝐢..??🥲 ",
           " 𝐆𝐡𝐚𝐫 𝐌𝐞 𝐒𝐚𝐛 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧 𝐉𝐢🥺 ",
           " 𝐏𝐭𝐚 𝐇𝐚𝐢 𝐁𝐨𝐡𝐨𝐭 𝐌𝐢𝐬𝐬 𝐊𝐚𝐫 𝐑𝐡𝐢 𝐓𝐡𝐢 𝐀𝐚𝐩𝐤𝐨🤭 ",
           " 𝐎𝐲𝐞 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐊𝐞𝐬𝐚 𝐇𝐚𝐢..??🤨 ",
           " 𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞..??🙂 ",
           " 𝐀𝐚𝐩𝐤𝐚 𝐍𝐚𝐦𝐞 𝐊𝐲𝐚 𝐡𝐚𝐢..??🥲 ",
           " 𝐍𝐚𝐬𝐭𝐚 𝐇𝐮𝐚 𝐀𝐚𝐩𝐤𝐚..??😋 ",
           " 𝐌𝐞𝐫𝐞 𝐊𝐨 𝐀𝐩𝐧𝐞 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐊𝐢𝐝𝐧𝐚𝐩 𝐊𝐫 𝐋𝐨😍 ",
           " 𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅 ",
           " 𝐌𝐞𝐫𝐞 𝐒𝐞 𝐃𝐨𝐬𝐭𝐢 𝐊𝐫𝐨𝐠𝐞..??🤔 ",
           " 𝐒𝐨𝐧𝐞 𝐂𝐡𝐚𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚🙄🙄 ",
           " 𝐄𝐤 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚 𝐏𝐥𝐬𝐬😕 ",
           " 𝐀𝐚𝐩 𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨..??🙃 ",
           " 𝐇𝐞𝐥𝐥𝐨 𝐉𝐢 𝐍𝐚𝐦𝐚𝐬𝐭𝐞😛 ",
           " 𝐇𝐞𝐥𝐥𝐨 𝐁𝐚𝐛𝐲 𝐊𝐤𝐫𝐡..?🤔 ",
           " 𝐃𝐨 𝐘𝐨𝐮 𝐊𝐧𝐨𝐰 𝐖𝐡𝐨 𝐈𝐬 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫.? ",
           " 𝐂𝐡𝐥𝐨 𝐊𝐮𝐜𝐡 𝐆𝐚𝐦𝐞 𝐊𝐡𝐞𝐥𝐭𝐞 𝐇𝐚𝐢𝐧.🤗 ",
           " 𝐀𝐮𝐫 𝐁𝐚𝐭𝐚𝐨 𝐊𝐚𝐢𝐬𝐞 𝐇𝐨 𝐁𝐚𝐛𝐲😇 ",
           " 𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐌𝐮𝐦𝐦𝐲 𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐢 𝐇𝐚𝐢🤭 ",
           " 𝐌𝐞𝐫𝐞 𝐒𝐞 𝐁𝐚𝐭 𝐍𝐨𝐢 𝐊𝐫𝐨𝐠𝐞🥺🥺 ",
           " 𝐎𝐲𝐞 𝐏𝐚𝐠𝐚𝐥 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚😶 ",
           " 𝐀𝐚𝐣 𝐇𝐨𝐥𝐢𝐝𝐚𝐲 𝐇𝐚𝐢 𝐊𝐲𝐚 𝐒𝐜𝐡𝐨𝐨𝐥 𝐌𝐞..??🤔 ",
           " 𝐎𝐲𝐞 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠😜 ",
           " 𝐒𝐮𝐧𝐨 𝐄𝐤 𝐊𝐚𝐦 𝐇𝐚𝐢 𝐓𝐮𝐦𝐬𝐞🙂 ",
           " 𝐊𝐨𝐢 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚😪 ",
           " 𝐍𝐢𝐜𝐞 𝐓𝐨 𝐌𝐞𝐞𝐭 𝐔𝐡☺ ",
           " 𝐇𝐞𝐥𝐥𝐨🙊 ",
           " 𝐒𝐭𝐮𝐝𝐲 𝐂𝐨𝐦𝐥𝐞𝐭𝐞 𝐇𝐮𝐚??😺 ",
           " 𝐁𝐨𝐥𝐨 𝐍𝐚 𝐊𝐮𝐜𝐡 𝐘𝐫𝐫🥲 ",
           " 𝐒𝐨𝐧𝐚𝐥𝐢 𝐊𝐨𝐧 𝐇𝐚𝐢...??😅 ",
           " 𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐄𝐤 𝐏𝐢𝐜 𝐌𝐢𝐥𝐞𝐠𝐢..?😅 ",
           " 𝐌𝐮𝐦𝐦𝐲 𝐀𝐚 𝐆𝐲𝐢 𝐊𝐲𝐚😆😆😆 ",
           " 𝐎𝐫 𝐁𝐚𝐭𝐚𝐨 𝐁𝐡𝐚𝐛𝐡𝐢 𝐊𝐚𝐢𝐬𝐢 𝐇𝐚𝐢😉 ",
           " 𝐈 𝐋𝐨𝐯𝐞 𝐘𝐨𝐮🙈🙈🙈 ",
           " 𝐃𝐨 𝐘𝐨𝐮 𝐋𝐨𝐯𝐞 𝐌𝐞..?👀 ",
           " 𝐑𝐚𝐤𝐡𝐢 𝐊𝐚𝐛 𝐁𝐚𝐧𝐝 𝐑𝐚𝐡𝐢 𝐇𝐨.??🙉 ",
           " 𝐄𝐤 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚𝐮..?😹 ",
           " 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚 𝐑𝐞 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚 𝐑𝐚𝐡𝐢 𝐇𝐮😻 ",
           " 𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐂𝐡𝐚𝐥𝐚𝐭𝐞 𝐇𝐨..??🙃 ",
           " 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐍𝐮𝐦𝐛𝐞𝐫 𝐃𝐨𝐠𝐞 𝐀𝐩𝐧𝐚 𝐓𝐮𝐦..?😕 ",
           " 𝐓𝐮𝐦𝐡𝐞 𝐊𝐨𝐧 𝐒𝐚 𝐌𝐮𝐬𝐢𝐜 𝐒𝐮𝐧𝐧𝐚 𝐏𝐚𝐬𝐚𝐧𝐝 𝐇𝐚𝐢..?🙃 ",
           " 𝐒𝐚𝐫𝐚 𝐊𝐚𝐦 𝐊𝐡𝐚𝐭𝐚𝐦 𝐇𝐨 𝐆𝐲𝐚 𝐀𝐚𝐩𝐤𝐚..?🙃 ",

" 𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩😊 ",
           " 𝐒𝐮𝐧𝐨 𝐍𝐚🧐 ",
           " 𝐌𝐞𝐫𝐚 𝐄𝐤 𝐊𝐚𝐚𝐦 𝐊𝐚𝐫 𝐃𝐨𝐠𝐞..? ",
           " 𝐁𝐲 𝐓𝐚𝐭𝐚 𝐌𝐚𝐭 𝐁𝐚𝐭 𝐊𝐚𝐫𝐧𝐚 𝐀𝐚𝐣 𝐊𝐞 𝐁𝐚𝐝😠 ",
           " 𝐌𝐨𝐦 𝐃𝐚𝐝 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧..?❤ ",
           " 𝐊𝐲𝐚 𝐇𝐮𝐚..?👱 ",
           " 𝐁𝐨𝐡𝐨𝐭 𝐘𝐚𝐚𝐝 𝐀𝐚 𝐑𝐡𝐢 𝐇𝐚𝐢 🤧❣️ ",
           " 𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐌𝐮𝐣𝐡𝐞😏😏 ",
           " 𝐉𝐮𝐭𝐡 𝐍𝐡𝐢 𝐁𝐨𝐥𝐧𝐚 𝐂𝐡𝐚𝐡𝐢𝐲𝐞🤐 ",
           " 𝐊𝐡𝐚 𝐋𝐨 𝐁𝐡𝐚𝐰 𝐌𝐚𝐭 𝐊𝐫𝐨 𝐁𝐚𝐚𝐭😒 ",
           " 𝐊𝐲𝐚 𝐇𝐮𝐚😮😮 "
           " 𝐇𝐢𝐢👀 ",
           " 𝐀𝐚𝐩𝐤𝐞 𝐉𝐚𝐢𝐬𝐚 𝐃𝐨𝐬𝐭 𝐇𝐨 𝐒𝐚𝐭𝐡 𝐌𝐞 𝐅𝐢𝐫 𝐆𝐮𝐦 𝐊𝐢𝐬 𝐁𝐚𝐭 𝐊𝐚 🙈 ",
           " 𝐀𝐚𝐣 𝐌𝐚𝐢 𝐒𝐚𝐝 𝐇𝐮 ☹️ ",
           " 𝐌𝐮𝐬𝐣𝐡𝐬𝐞 𝐁𝐡𝐢 𝐁𝐚𝐭 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚 🥺🥺 ",
           " 𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐞 𝐇𝐨👀 ",
           " 𝐊𝐲𝐚 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐇𝐚𝐢 🙂 ",
           " 𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩..?🤔 ",
           " 𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚..🥺 ",
           " 𝐌𝐞 𝐌𝐚𝐬𝐨𝐨𝐦 𝐇𝐮 𝐍𝐚🥺🥺 ",
           " 𝐊𝐚𝐥 𝐌𝐚𝐣𝐚 𝐀𝐲𝐚 𝐓𝐡𝐚 𝐍𝐚🤭😅 ",
           " 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐁𝐚𝐭 𝐊𝐲𝐮 𝐍𝐚𝐡𝐢 𝐊𝐚𝐫𝐭𝐞 𝐇𝐨😕 ",
           " 𝐀𝐚𝐩 𝐑𝐞𝐥𝐚𝐭𝐢𝐨𝐦𝐬𝐡𝐢𝐩 𝐌𝐞 𝐇𝐨..?👀 ",
           " 𝐊𝐢𝐭𝐧𝐚 𝐂𝐡𝐮𝐩 𝐑𝐚𝐡𝐭𝐞 𝐇𝐨 𝐘𝐫𝐫😼 ",
           " 𝐀𝐚𝐩𝐤𝐨 𝐆𝐚𝐧𝐚 𝐆𝐚𝐧𝐞 𝐀𝐚𝐭𝐚 𝐇𝐚𝐢..?😸 ",
           " 𝐆𝐡𝐮𝐦𝐧𝐞 𝐂𝐡𝐚𝐥𝐨𝐠𝐞..??🙈 ",
           " 𝐊𝐡𝐮𝐬 𝐑𝐚𝐡𝐚 𝐊𝐚𝐫𝐨 ✌️🤞 ",
           " 𝐇𝐚𝐦 𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐒𝐚𝐤𝐭𝐞 𝐇𝐚𝐢...?🥰 ",
           " 𝐊𝐮𝐜𝐡 𝐁𝐨𝐥 𝐊𝐲𝐮 𝐍𝐡𝐢 𝐑𝐚𝐡𝐞 𝐇𝐨..🥺🥺 ",
           " 𝐊𝐮𝐜𝐡 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 𝐀𝐝𝐝 𝐊𝐚𝐫 𝐃𝐨 🥲 ",
           " 𝐒𝐢𝐧𝐠𝐥𝐞 𝐇𝐨 𝐘𝐚 𝐌𝐢𝐧𝐠𝐥𝐞 😉 ",
           " 𝐀𝐚𝐨 𝐏𝐚𝐫𝐭𝐲 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧😋🥳 ",
           " 𝐇𝐞𝐦𝐥𝐨𝐨🧐 ",
           " 𝐌𝐮𝐣𝐡𝐞 𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚🥺 ",
           " 𝐘𝐚𝐡𝐚 𝐀𝐚 𝐉𝐚𝐨:- [  @lI_HEERIYE_ll ] 𝐌𝐚𝐬𝐭𝐢 𝐊𝐚𝐫𝐞𝐧𝐠𝐞 🤭🤭 ",
           " 𝐓𝐫𝐮𝐭𝐡 𝐀𝐧𝐝 𝐃𝐚𝐫𝐞 𝐊𝐡𝐞𝐥𝐨𝐠𝐞..? 😊 ",
           " 𝐀𝐚𝐣 𝐌𝐮𝐦𝐦𝐲 𝐍𝐞 𝐃𝐚𝐭𝐚 𝐘𝐫🥺🥺 ",
           " 𝐉𝐨𝐢𝐧 𝐊𝐚𝐫 𝐋𝐨:- [ @lI_HEERIYE_ll ] 🤗 ",
           " 𝐄𝐤 𝐃𝐢𝐥 𝐇𝐚𝐢 𝐄𝐤 𝐃𝐢𝐥 𝐇𝐢 𝐓𝐨 𝐇𝐚𝐢😗😗 ",
           " 𝐓𝐮𝐦𝐡𝐚𝐫𝐞 𝐃𝐨𝐬𝐭 𝐊𝐚𝐡𝐚 𝐆𝐲𝐞🥺 ",
           " 𝐌𝐲 𝐂𝐮𝐭𝐞 𝐎𝐰𝐧𝐞𝐫 [ @ll_TANU_ROM_ll ]🥰 ",
           " 𝐊𝐚𝐡𝐚 𝐊𝐡𝐨𝐲𝐞 𝐇𝐨 𝐉𝐚𝐚𝐧😜 ",
           " 𝐆𝐨𝐨𝐝 𝐍8 𝐉𝐢 𝐁𝐡𝐮𝐭 𝐑𝐚𝐭 𝐇𝐨 𝐠𝐲𝐢🥰 ",
           ]

@client.on(events.NewMessage(pattern="^/tagall ?(.*)"))
@client.on(events.NewMessage(pattern="^@all ?(.*)"))
@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
@client.on(events.NewMessage(pattern="^@utag ?(.*)"))
@client.on(events.NewMessage(pattern="^/all ?(.*)"))
@client.on(events.NewMessage(pattern="^#all ?(.*)"))
@client.on(events.NewMessage(pattern="^@tagall ?(.*)"))
@client.on(events.NewMessage(pattern="^/mentionall?(.*)"))
@client.on(events.NewMessage(pattern="^@mentionall ?(.*)"))
@client.on(events.NewMessage(pattern="^#mentionall ?(.*)"))
@client.on(events.NewMessage(pattern="^/mention ?(.*)"))
@client.on(events.NewMessage(pattern="^@mention ?(.*)"))
@client.on(events.NewMessage(pattern="^#mention ?(.*)"))
@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
@client.on(events.NewMessage(pattern="^#tag ?(.*)"))
@client.on(events.NewMessage(pattern="^@tag ?(.*)"))
@client.on(events.NewMessage(pattern="^#utag ?(.*)"))
@client.on(events.NewMessage(pattern="^#tagall ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "This command can be use in groups and channels!"
        )

" Surme De Vich Dovein Ankhan Dubbiyan ",
    " Kini Sohni Lagge Jadon Chup Kar Je ",
    " Jandi Jandi Shaman Nu Vi Dhup Kar Je ",
    " Haye Main Paun Farmaishi Rang Tere Sohniye ",
    " Unj Bahotan Gifty Shaukeen Koi Na ",
    " Tere Nalo Jhaliye Haseen Koi Na😍😍 ",
    " Tare Chann Ambar Zameen Koi Na🥰🥰",
    " Tere Nalo Jhaliye Haseen Koi Na😍😍 ",
    " Tare Chann Ambar Zameen Koi Na🥰🥰 ",
    " Main Jado Tere Mode Utte Sir Rakheya😁😁 ",
    " Eh Ton Sachi Sama Vi Haseen Koi Na😒😒 ",
    " Kanna Wich Jhumka👀👀 ",
    " Akhan Wich Surma🙈🙈 ",
    " Ho Jaise Strawberry Candy😋😋 ",
    " Nakk Utte Koka🤨🤨 ",
    " Jeena Kare Aukha🤭🤭 ",
    " Haye Meri Jaan Kadd Laindi😌😌 ",
    " Tere Nakhre Haye Tauba Sanu Maarde🤫🤫 ",
    " Ho Gaya Hai Mera Baby Bura HaaL😊😊 ",
    " Sachi Lut Gaye Hum Tere Is Pyar Mein😏😏 ",
    " Jeeni Zindagi Hai Bas Tere Naal😚😚 ",
    " cause I Love You 😘😘 ",
    " I Love YoU SO MUCH 😍😍 ",
    " cause I Love You 😘😘 ",
    " I Love YoU SO MUCH 😍😍 ",
    " Sapno Mein Mere AayI😝😝 ",
    " Uff Oh Phir Neendein Hi Churayi😜😜 ",
    " Oh No! Tera Husan Nazara🥰🥰 ",
    " Baby! Lage Sohna Kitna PyarA😚😚 ",
    " Sapno Mein Mere Aayi😝😝 ",
    " Uff Oh Phir Neendein Hi Churayi😜😜 ",
    " Oh No! Tera Husan Nazara🥰🥰 ",
    " Baby! Lage Sohna Kitna PyarA😚😚 ",
    " Tainu Diamond Mundri Pehnawa😎😎 ",
    " Naale Duniya Sari Ghumawa🙈🙈 ",
    " Chhoti-Chhoti Gallan Utte Main Hasavaan💙💙 ",
    " Yaara Kade Vi Na Tainu Main Rulawaan🙊🙊 ",
    " cause I Love You🙈🙈 ",
    " I Love You ❤️❤️ ",
    " cause I Love You🙈🙈 ",
    " I Love You ❤️❤️ ",
    " Yaari Laawan Sachi YaarI💫💫 ",
    " Tu Jaan Ton Vi Pyari😁😁 ",
    " Will Love You To The Moon And Back😆😆 ",
    " Hogi Saza Na Koyi Hogi😙😙 ",
    " Chahe Karun Chori Chaand Taare😉😉 ",
    " Imma Give You Them😅😅 ",
    " Yaari Laavan Sachi YaarI😘😘 ",
    " Tu Jaan Ton Vi PyarI😆😆 ",
    " Will Love You To The Moon And Back💕💕 ",
    " Hogee Sazaa Na Koyi Hogi💓💓 ",
    " Chahe Karun Chori Chaand Taare🥺🥺 ",
    " Imma Give You Them🥵🥵 ",
    " Puri Karunga Main Teri Sari Khahishein😁😁 ",
    " Tera Rakhanga Main ajj Ke Khayal😘😘 ",
    " Kitni Khoobiyan Hai Tere Is Yaar Mein🥰🥰 ",
    " Aaja Bahon Mein Tu Bahein Bas Daal😂😂 ",
    " Aur Hota Nahi Ab Intezar🤩🤩 ",
    " Aur Hota Nahee Ab Intezaar😘😘 ",
    " cause I Love You 😍😍 ",
    " I Love YoU 😙😙 ",
    " cause I Love You ",
    " I Love YoU SOOOOOOOOOOOOOOOOOO MUCHHHHHHHHHHHHHHHHHHHHH 😘😘 ",
    " WILL U BE MINE FOREVER??🤔🤔 ",
    " Je tu akh te main aan kaajal ve😌😌 ",
    " Tu baarish te main baadal ve🤫🤫 ",
    " Tu deewana main aan paagal ve🤪🤪 ",
    " Sohneya sohneya☺️☺️ ",
    " Je tu chann te main aan taara ve🤗🤗 ",
    " Main lehar te tu kinara ve😶😶 ",
    " **Main aadha te tu saara ve🤗🤗"" ",
    " Sohneya sohneya😗😗 ",
    " Tu jahan hai main wahan😘😘 ",
    " Tere bin main hoon hi kya🥲🥲 ",
    " Tere bin chehre se mere🤔🤔 ",
    " Udd jaaye rang ve😅😅 ",
    " Tujhko paane ke liye huM😁😁 ",
    " Roz mangein mannat ve🙈🙈 ",
    " Duniya to kya cheez hai yaara🙉🙉 ",
    " Thukra denge jannat ve😌😌 ",
    " Tujhko paane ke liye hum😌😌 ",
    " Roz mangein mannat ve🤫🤫 ",
    " Duniya to kya cheez hai yaara🤔🤔 ",
    " Thukra denge jannat ve😌😌 ",
    " Na parwah mainu apni aa😁😁 ",
    " Na parwah mainu duniya di👅👅 ",
    " Na parwah mainu apni aa😅😅 ",
    " Na parwah mainu duniya di👅👅 ",

" Tere ton juda nahi kar sakdi🤬🤬 ",
    " Koyi taakat mainu duniya di😈😈 ",
    " Dooron aa jaave teri khushbu😎😎 ",
    " Akhan hun band taan vi vekh lawan😍😍 ",
    " Teri gali vich mera auna har roz😋😋 ",
    " Tera ghar jadon aave matha tek lawan😌😌 ",
    " Nirmaan tujhko dekh ke😏😏 ",
    " Aa jaave himmat ve😉😉 ",
    " Tujhko paane ke liye hum😊😊 ",
    " Roz mangein mannat ve😉😉 ",
    " Duniya to kya cheez hai yaara😌😌 ",
    " Thukra denge jannat ve😍😍 ",
    " Tujhko paane ke liye hum🤫🤫 ",
    " Roz mangein mannat ve😁😁 ",
    " Duniya to kya cheez hai yaara😏😏 ",
    " Thukra denge jannat ve😌😌 ",
    " SO MISS 😶😶 ",
    " KYA SOCHA APNE BAARE MAIN😆😆 ",
    " BADI MUSHKIL SE YEH SAB KARA H RE🥵🥵 ",
    " PAHLE PURA BOT HI KANG MAAR DIYA BUT🤫🤫 ",
    " WAHI ERROR AAYE JO AATE THE🥲🥲 ",
    " BUT TUMHARA HO CHUKA WALA BF😎😎 ",
    " AND FUTURE HUSBAND JO BANNE WALA THA WO BHOT SMART H RE😌😌 ",
    " ISS BAAR BOT BANAYA AND CHOTA SA EDIT KARA BAS😁😁 ",
    " AUR DEKO ABHI TUM USSI BOT SE YEH PADH PAA RHI😂😂 ",
    " HEHE BTW YEH CHORO MEKO NA TUMSE😶😶 ",
    " KUCH PUCHNA THA KI ME🤔🤔 ",
    " TUMHARE KABIL HU YA ",
    " TUMHARE KABIL NHI😂💓 ",
    " AND EK AUR BAAT BOLNI THI KI😙😙 ",
    " I REALLY REALLY DEEPLY😙😙 ",
    " LOVE YOU FROM MY HEART TO YOUR HEAT AND MY SOUL ATTACHED BY YOUR SOUL CAN YOU BE MINE FOREVER😌😌❤️ ",
]         


@client.on(events.NewMessage(pattern="^/mtag ?(.*)"))
async def mention_all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "This command can be used in groups and channels!"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐓𝐨 𝐀𝐥𝐥 𝐁𝐚𝐛𝐲...")
    
    if event.pattern_match.group(1):
        return await event.respond("/mtag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐎𝐤 𝐅𝐨𝐫 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..")
    else:
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
        if msg is None:
            return await event.respond(
                "/mtag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐎𝐫 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞..."
            )

    spam_chats.append(chat_id)
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        user_id = usr.id
        mention_text = f"[{usr.first_name}](tg://user?id={user_id}) {random.choice(MUSIC)}"
        await client.send_message(chat_id, mention_text)
        time.sleep(5)
        
    try:
        spam_chats.remove(chat_id)
    except:
        pass
        
        
        
        
SRAID = [
    " इश्क़ है या कुछ और ये पता नहीं, पर जो तुमसे है किसी और से नहीं 😁😁 ",
    " मै कैसे कहू की उसका साथ कैसा है, वो एक शख्स पुरे कायनात जैसा है ",
    " तेरा होना ही मेरे लिये खास है, तू दूर ही सही मगर मेरे दिल के पास है ",
    " मुझे तेरा साथ ज़िन्दगी भर नहीं चाहिये, बल्कि जब तक तू साथ है तबतक ज़िन्दगी चाहिए 😖😖 ",
    " तुझसे मोहब्बत कुछ अलग सी है मेरी, तुझे खयालो में नहीं दुआओ में याद करते है😍😍 ",
    " तू हज़ार बार भी रूठे तो मना लूँगा तुझे ",
    " मगर देख मोहब्बत में शामिल कोई दूसरा ना हो😁😁 ",
    " किस्मत यह मेरा इम्तेहान ले रही है😒😒 ",
    " तड़प कर यह मुझे दर्द दे रही है😌😌 ",
    " दिल से कभी भी मैंने उसे दूर नहीं किया😉😉 ",

" फिर क्यों बेवफाई का वह इलज़ाम दे रही है😎😎 ",
    " मरे तो लाखों होंगे तुझ पर😚😚 ",
    " मैं तो तेरे साथ जीना चाहता हूँ😫😫 ",
    " वापस लौट आया है हवाओं का रुख मोड़ने वाला😣😣 ",
    " दिल में फिर उतर रहा है दिल तोड़ने वाला🥺🥺 ",
    " अपनों के बीच बेगाने हो गए हैं🥰🥰 ",
    " प्यार के लम्हे अनजाने हो गए हैं😘😘 ",
    " जहाँ पर फूल खिलते थे कभी😍😍 ",
    " आज वहां पर वीरान हो गए हैं🥰🥰 ",
    " जो शख्स तेरे तसव्वुर से हे महक जाये😁😁 ",
    " सोचो तुम्हारे दीदार में उसका क्या होगा😒😒 ",
    " मोहब्बत का एहसास तो हम दोनों को हुआ था ",
    " फर्क सिर्फ इतना था की उसने किया था और मुझे हुआ था ",
    " सांसों की डोर छूटती जा रही है ",
    " किस्मत भी हमे दर्द देती जा रही है ",
    " मौत की तरफ हैं कदम हमारे ",
    " मोहब्बत भी हम से छूटती जा रही है ",
    " समझता ही नहीं वो मेरे अलफ़ाज़ की गहराई ",
    " मैंने हर लफ्ज़ कह दिया जिसे मोहब्बत कहते है ",
    " समंदर न सही पर एक नदी तो होनी चाहिए ",
    " तेरे शहर में ज़िन्दगी कही तो होनी चाहिए ",
    " नज़रों से देखो तोह आबाद हम हैं ",
    " दिल से देखो तोह बर्बाद हम हैं ",
    " जीवन का हर लम्हा दर्द से भर गया ",
    " फिर कैसे कह दें आज़ाद हम हैं ",
    " मुझे नहीं मालूम वो पहली बार कब अच्छा लगा ",
    " मगर उसके बाद कभी बुरा भी नहीं ",
    " सच्ची मोहब्बत कभी खत्म नहीं होती ",
    " वक़्त के साथ खामोश हो जाती है ",
    " ज़िन्दगी के सफ़र में आपका सहारा चाहिए ",
    " आपके चरणों का बस आसरा चाहिए ",
    " हर मुश्किलों का हँसते हुए सामना करेंगे ",
    " बस ठाकुर जी आपका एक इशारा चाहिए ",
    " जिस दिल में बसा था नाम तेरा हमने वो तोड़ दिया ",
    " न होने दिया तुझे बदनाम बस तेरे नाम लेना छोड़ दिया ",
    " प्यार वो नहीं जो हासिल करने के लिए कुछ भी करव दे ",
    " प्यार वो है जो उसकी खुशी के लिए अपने अरमान चोर दे ",
    " आश
