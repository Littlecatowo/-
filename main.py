import discord
from discord.ext import commands
import keep_alive
import os

from Music_123 import config
from Music_123.audiocontroller import AudioController
from Music_123.settings import Settings
from Music_123 import utils
from Music_123.utils import guild_to_audiocontroller, guild_to_settings

from general import General

owner_id = 445887034473578506

intents = discord.Intents.all()

help_command = commands.DefaultHelpCommand(no_category = 'Bot owner')

bot = commands.Bot(command_prefix='cat?', intents = intents, help_command= help_command, case_insensitive=True)

embed_color = 0xffe070

ext = ['Cmd','Event','管理權限','music','general', 'button']

@bot.event
async def on_ready():

    print(config.STARTUP_MESSAGE)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Music, type {}help".format(config.BOT_PREFIX)))

    for guild in bot.guilds:
        await register(guild)
        print("Joined {}".format(guild.name))

    print(config.STARTUP_COMPLETE_MESSAGE)

    print('>Bot is online<')
    myid = '<@445887034473578506>'
    embed=discord.Embed(title="開始運行",color=embed_color)
    embed.add_field(name="等一等 不可以已上線", value= myid, inline=True)
    channel = bot.get_channel(904611397462261830)
    await channel.send(embed=embed)

@bot.event
async def on_guild_join(guild):
    print(guild.name)
    await register(guild)


async def register(guild):

    guild_to_settings[guild] = Settings(guild)
    guild_to_audiocontroller[guild] = AudioController(bot, guild)

    sett = guild_to_settings[guild]

    await guild.me.edit(nick=sett.get('default_nickname'))

    if config.GLOBAL_DISABLE_AUTOJOIN_VC == True:
        return

    vc_channels = guild.voice_channels

    if sett.get('vc_timeout') == False:
        if sett.get('start_voice_channel') == None:
            try:
                await guild_to_audiocontroller[guild].register_voice_channel(guild.voice_channels[0])
            except Exception as e:
                print(e)

        else:
            for vc in vc_channels:
                if vc.id == sett.get('start_voice_channel'):
                    try:
                        await guild_to_audiocontroller[guild].register_voice_channel(vc_channels[vc_channels.index(vc)])
                    except Exception as e:
                        print(e)

#-----------------------------------

@bot.command()
async def reload(ctx, extension):
  bot.reload_extension(extension)
  embed= discord.Embed(title='Reload done...', color= embed_color)
  await ctx.send(embed= embed)

if __name__ == "__main__":
  config.ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
  config.COOKIE_PATH = config.ABSOLUTE_PATH + config.COOKIE_PATH

  for extension in ext:
    bot.load_extension(extension)
  keep_alive.keep_alive()
  bot.run('OTA0NjA3NDM1NzQ5MjAzOTc4.YX9_Uw.ohWRTxqFfD9NPLnyC9FbBjwrYdA', bot=True, reconnect=True)