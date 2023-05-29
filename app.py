import os
import discord
from dotenv import load_dotenv
import azure_openai

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(f"目前登入身份： {client.user}")

@client.event
async def on_message(message):
    print(f"使用者發送的訊息：{message.content}")
    if message.author == client.user:
        return
    await message.channel.send(azure_openai.openai_prompt(message.content))
    
client.run(os.getenv('DISCORD_TOKEN'))