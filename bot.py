import discord

# ⚠ استبدل التوكن بتاعك هنا، بس تأكد إنه مش مرفوع على GitHub علنيًا!
TOKEN = "MTM0NTQ5MTQyNjQ0Nzk4MjY5Mw.GGguU6.eX0I641lsSla5sa_wMGgX-VQk9BcpvWh6_WhQ4"

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ البوت شغال! الاسم: {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "جوجو" in message.content:
        await message.channel.send("أنا هنا! 🤖")

client.run(TOKEN)