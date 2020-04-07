from telethon import TelegramClient
import time

api_hash = '20e0059a476a0472781f6e42c333c084'
api_id = 766231

client = TelegramClient('test_tg',api_id,api_hash)
async def main():
    # me = await client.get_me()
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if dialog.title == 'GU_BigData_305 (02.11.2019)':
            await dialog.send_message('Hello!')
            async for msg in client.iter_messages(dialog):
                print(msg.date, msg.text)
                time.sleep(1)
                if msg.media:
                    await msg.download_media()
                    # if 'document' in msg.media:
                    #     print(f'Файл {msg.media.document.attributes[0].file_name} скачан!')



    #         members = await client.get_participants(dialog)
    # for member in members:
    #     print(member.first_name)

    pass




with client:
    client.loop.run_until_complete(main())
