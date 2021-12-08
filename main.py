import discord
from discord.ext import commands
import keep_alive
import traceback

owner_id = 445887034473578506

intents = discord.Intents.all()

help_command = commands.DefaultHelpCommand(no_category = 'Bot owner')

bot = commands.Bot(command_prefix='cat?', intents = intents, help_command= help_command)

embed_color = 0xffe070

ext = ['Cmd','Event','管理權限']

print(traceback)

@bot.event
async def on_ready():
    print('>Bot is online<')
    myid = '<@445887034473578506>'
    embed=discord.Embed(title="開始運行",color=embed_color)
    embed.add_field(name="等一等 不可以已上線", value= myid, inline=True)
    channel = bot.get_channel(904611397462261830)
    await channel.send(embed=embed)

#-----------------------------------

@bot.command()
async def reload(ctx, extension):
  bot.reload_extension(extension)
  embed= discord.Embed(title='Reload done...', color= embed_color)
  await ctx.send(embed= embed)

if __name__ == "__main__":
  for extension in ext:
    bot.load_extension(extension)
  keep_alive.keep_alive()
  bot.run('OTA0NjA3NDM1NzQ5MjAzOTc4.YX9_Uw.ohWRTxqFfD9NPLnyC9FbBjwrYdA')