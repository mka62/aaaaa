
import discord
import asyncio

TOKEN = "MTMyNTMyMTk5NTk1MjQ1OTc3Nw.GvAKft.89NfoNZ5da__d8OM1HU5GgK36HPIsCOriPeBhc"
VOICE_CHANNEL_ID = 1379089098995798106

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    for guild in bot.guilds:
        channel = guild.get_channel(VOICE_CHANNEL_ID)
        if channel:
            try:
                vc = await channel.connect()
                await vc.guild.change_voice_state(channel=channel, self_mute=True, self_deaf=False)
                print("Connected and muted in voice channel.")
            except Exception as e:
                print(f"Failed to connect: {e}")
        else:
            print("Voice channel not found.")

bot.run(TOKEN)
