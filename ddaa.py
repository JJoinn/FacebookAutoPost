from telethon import TelegramClient, errors
from telethon.tl.types import MessageMediaDocument
import os
import re
from datetime import datetime

api_id = 26999820 # appId
api_hash = '543409a3f49aefe58771040830925246' # app密钥
client = TelegramClient('anon', api_id, api_hash)


async def main():
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)
    download_folder = 'downloaded_media'
    os.makedirs(download_folder, exist_ok=True)
    count = 0
    channel = await client.get_entity(频道id)
    async for message in client.iter_messages(channel, reverse=True):
        count += 1
        if message.media is not None and isinstance(message.media, MessageMediaDocument):
            document = message.media.document
            if document.mime_type.startswith('video'):
                print(f"{datetime.now()} - 第{count}条 - {message.text}")
                print(message)
                file_name = message.text
                if len(message.text) >= 50:
                    print(f"{datetime.now()} - '{file_name}' ,消息文本超过50字,怀疑是广告,跳过下载.")
                    continue
                if document.attributes[0].duration < 15:
                    print(f"{datetime.now()} - '{file_name}' ,时长{document.attributes[0].duration}少于15s,跳过下载.")
                    continue
                if not file_name:
                    file_name = str(message.id)

                if not file_name.endswith(".mp4"):
                    file_name += ".mp4"

                file_name = file_name.replace("📣 频道 @HTPorn01", "")
                illegal_chars = r'[<>:"/\\|?*\x00-\x1F]'
                file_name = re.sub(illegal_chars, ' ', file_name)
                file_name = file_name.strip()[:255]
                file_path = os.path.join('D:/downloaded_media', file_name)

                # 检查文件是否已存在，如果存在就跳过下载
                if os.path.exists(file_path):
                    print(f"{datetime.now()} - '{file_name}' ,已经存在,跳过下载.")
                else:
                    print(f"{datetime.now()} - 开始下载'{file_name}'")
                    try:
                        # 下载视频文件
                        path = await message.download_media(file="D:/downloaded_media/" + file_name)
                    except errors.rpcerrorlist.FileReferenceExpiredError as e:
                        print(f"文件已过期'{file_name}',无法下载:", e)
                        continue

                    # 构建新的文件路径，避免重名
                    new_file_path = os.path.join('D:/downloaded_media', file_name)

                    # 重命名文件
                    os.rename(path, new_file_path)

                    print(f"{datetime.now()} - File saved to '{new_file_path}'")  # 下载完成后打印路径


with client:
    client.loop.run_until_complete(main())
