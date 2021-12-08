import discord
from discord.ext import commands
from core import Cog_core

embed_color = 0xffe070

class 管理員指令(Cog_core):
  @commands.command(kick_member=True) 
  @commands.has_any_role('機器人管理員','耳膜保護協會 會長','等一等，不可以')
  async def kick(self, ctx, member: discord.Member, *, reason= None):
        await member.kick(reason= reason)
        embed= discord.Embed(title=f'{member.display_name}已被踢出',color=embed_color)
        embed.add_field(name='原因',value=reason,inline=True)
        embed.set_footer(text=f"by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
  @kick.error
  async def kick_error(self, ctx, error):
    if isinstance(error , commands.errors.MissingAnyRole):
      await ctx.send('你沒有管理身分組執行Kick指令')
    elif isinstance(error, commands.errors.MissingRequiredArgument):
      kick_error_embed= discord.Embed(title='遺失參數！',description='使用方法：<cat?kick (@成員)>', color= embed_color)
      await ctx.send(embed= kick_error_embed)
      

  @commands.command(ban_member =True)
  @commands.has_any_role('機器人管理員','耳膜保護協會 會長','等一等，不可以')
  async def ban(self, ctx, member: discord.Member, *, reason= None):
        await member.ban(reason= reason)
        embed= discord.Embed(title=f'{member.display_name} 被永久驅逐',color=embed_color)
        embed.add_field(name='原因:',value=reason,inline=True)
        embed.set_footer(text=f"by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
  @ban.error
  async def ban_error(self, ctx, error):
    if isinstance(error, commands.errors.MissingAnyRole):
      await ctx.send('你沒有管理身分組執行Ban指令')
    elif isinstance(error, commands.errors.MissingRequiredArgument):
      ban_error_embed= discord.Embed(title='遺失參數！',description='使用方法：<cat?ban (@成員)>', color= embed_color)
      await ctx.send(embed= ban_error_embed)

def setup(bot):
  bot.add_cog(管理員指令(bot))