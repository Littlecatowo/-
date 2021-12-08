import discord
from discord.ext import commands
from core import Cog_core
import asyncio

embed_color = 0xffe070



class cmd(Cog_core):
  
  @commands.command(help='刪除語音頻道')
  async def vcdt(self, ctx, channel: discord.VoiceChannel):
    if channel.id == 906065818855563264:
      await ctx.send('You can\'t delete this channel')
    else:
      await channel.delete()
      await ctx.message.delete()
  @vcdt.error
  async def vcdt_error(self, ctx, error):
    if isinstance(error, commands.errors.ChannelNotFound):
      vcdt_embed= discord.Embed(title='頻道不存在！', color= embed_color)
      await ctx.send(embed= vcdt_embed)

  #-----------------------------------------------
  @commands.command()
  async def vcedit(self, ctx, channel: discord.VoiceChannel, *, new_name):
      if channel.name == '點我創建owo':
          await ctx.send('你無法編輯此頻道名稱')
      else:
        if channel.name == ' ':
          pass
        await channel.edit(name=new_name)
        await ctx.message.delete()
        embed= discord.Embed(title=f'已更改為{new_name}',color= embed_color) 
        await ctx.send(embed= embed)

  #-----------------------------------------------
  @commands.command(help='移動成員')
  async def move(self, ctx, channel : discord.VoiceChannel,*members: discord.Member):
      

      for member in members:
          asyncio.sleep(0.5)
          await member.move_to(channel)
          if member == " ":
              return

      await ctx.send('移動結束')
  
  #-----------------------------------------------
  @commands.command(name='math', help='計算數學')
  async def math(self , ctx, *, msg):
      await ctx.message.delete()
      embed= discord.Embed(title='計算中...', color = embed_color)
      message_math = await ctx.send(embed= embed)
      w = eval(msg)
      _embed=discord.Embed(title="題目",description= msg,color=embed_color)
      _embed.add_field(name="Results", value= w, inline=True)
      _embed.set_footer(text=f"by {ctx.author.display_name}",                     icon_url=ctx.author.avatar_url)
      await message_math.edit(embed = _embed)
  @math.error
  async def math_error(self , ctx , error):
    if isinstance(error, commands.errors.CommandInvokeError):
      math_error_embed= discord.Embed(title='參數錯誤！', color= embed_color)
      await ctx.send(embed=math_error_embed)
    elif isinstance(error, commands.errors.MissingRequiredArgument):
      math_error_embed= discord.Embed(title='遺失參數！',description='使用方法：<cat?math 計算式>', color= embed_color)
      await ctx.send(embed= math_error_embed)

  #-----------------------------------------------
  @commands.command(help='覆誦訊息')
  async def say(self, ctx, *, msg):
      await ctx.message.delete()
      embed= discord.Embed(title= msg,color=embed_color)
      await ctx.send(embed=embed)
  @commands.command(help='覆誦訊息 without Embed')
  async def sayy(self, ctx, *, msg):
      await ctx.message.delete()
      await ctx.send(msg)


  #-----------------------------------------------
  @commands.command(help='顯示延遲')
  async def ping(self, ctx):
      embed=discord.Embed(title="延遲",description= (f'{round(self.bot.latency*1000)}(ms)') ,color=embed_color)
      await ctx.send(embed=embed)
      await ctx.message.delete()

  #-----------------------------------------------
  @commands.command(help='清理訊息')
  async def clean(self, ctx, num: int):
      await ctx.channel.purge(limit=num + 1)
  @clean.error
  async def clean_error(self , ctx , error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
      embed= discord.Embed(title='遺失參數！',description='使用方法：<cat?clean 刪除數量>', color= embed_color)
      await ctx.send(embed=embed)

  #-----------------------------------------------


def setup(bot):
  bot.add_cog(cmd(bot))