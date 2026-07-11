import os  # เพิ่มบรรทัดนี้เข้ามาด้านบนสุด
import discord
from discord.ext import commands
from myserver import server_on

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

# กำหนด Prefix ให้เป็นเครื่องหมายตกใจ (!)
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ล็อกอินเรียบร้อยในชื่อ: {bot.user.name}")
    print("บอทพร้อมสิงห้อง voice แล้ว!")

# คำสั่งสำหรับเข้าห้องเสียง (!CB)
@bot.command(name="CB")
async def connect_bot(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"บอทเข้ามานั่ง AFK ในห้อง `{channel.name}` เรียบร้อยแล้วจ้า! 💤")
    else:
        await ctx.send("คุณต้องเข้าห้องพูดคุยก่อนสั่งผมนะ!")

# คำสั่งสำหรับออกห้องเสียง (!QB)
@bot.command(name="QB")
async def quit_bot(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("บ๊ายบาย ออกจากห้องเสียงแล้วครับ! 👋")
    else:
        await ctx.send("ตอนนี้ผมไม่ได้อยู่ในห้องเสียงไหนเลยนะ")

# เรียกใช้ฟังก์ชันเปิดเว็บเซอร์เวอร์ (เขียนให้ชิดซ้ายสุด ห้ามมีเว้นวรรค)
server_on()

# รันบอทด้วย Token จากระบบ Environment Variable
bot.run(os.getenv("DISCORD_TOKEN"))
