import discord
from discord.ext import commands
from core import Cog_core
from re import search

embed_color = 0xffe070

class Event(Cog_core):
  
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    def error_return():
      raise error
    if hasattr(ctx.command,'on_error'):
      return error_return()

    if isinstance(error, commands.errors.CommandNotFound):
      await ctx.send('該指令不存在！')
    elif isinstance(error, commands.errors.MissingRequiredArgument):
      await ctx.send('遺失參數！')
    elif isinstance(error, commands.errors.MissingPermissions):
      await ctx.send('權限不足！')
    
    raise error

  @commands.Cog.listener()
  async def on_member_join(self, member: discord.Member):
    channel =  self.bot.get_channel(904625191588597780)
    await channel.send(f'{member.mention} 歡迎加入 {member.guild}~')
  #-----------------------------------------------

  @commands.Cog.listener()
  async def on_raw_reaction_add(self, data):
      print(data)
      channel = (904691820557127700)
      if str(data.emoji) == '<:Padko_love:904695152893906974>':
          if str(channel) == str(data.channel_id):
              guild = self.bot.get_guild(data.guild_id)
              role = guild.get_role(904558856238161920)
              await data.member.add_roles(role)
          else:
              return
      if str(data.emoji) == '<:Padko_hentai:904697666158616628>':
          if str(channel) == str(data.channel_id):
              guild = self.bot.get_guild(data.guild_id)
              role = guild.get_role(904678824640389171)
              await data.member.add_roles(role)
          else:
              return
      if str(data.emoji) == '<:Padko_kusa:904694407545106472>':
          if str(channel) == str(data.channel_id):
              guild = self.bot.get_guild(data.guild_id)
              role = guild.get_role(899724815521423401)
              await data.member.add_roles(role)
          else:
              return

      channel_bus = 917001779097530409
      if str(data.emoji) == '<:wryyy:904694011128844318>':
        if str(channel_bus) == str(data.channel_id):
            guild = self.bot.get_guild(data.guild_id)
            role = guild.get_role(917000904010510357)
            await data.member.add_roles(role)
        else:
            return

  #-----------------------------------------------
  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, data):
      channel = 904691820557127700
      if str(data.emoji) == '<:Padko_love:904695152893906974>':
          if str(channel) == str(data.channel_id):
              guild = self.bot.get_guild(data.guild_id)
              user = guild.get_member(data.user_id)
              role = guild.get_role(904558856238161920)
              await user.remove_roles(role)
          else:
              return
      if str(data.emoji) == '<:Padko_hentai:904697666158616628>':
          if str(channel) == str(data.channel_id):
              guild = self.bot.get_guild(data.guild_id)
              user = guild.get_member(data.user_id)
              role = guild.get_role(904678824640389171)
              await user.remove_roles(role)
          else:
              return
      if str(data.emoji) == '<:Padko_kusa:904694407545106472>':
          if str(channel) == str(data.channel_id):
              guild = self.bot.get_guild(data.guild_id)
              user = guild.get_member(data.user_id)
              role = guild.get_role(899724815521423401)
              await user.remove_roles(role)
          else:
              return

      channel_bus = 917001779097530409
      if str(data.emoji) == '<:wryyy:904694011128844318>':
        if str(channel_bus) == str(data.channel_id):
            guild = self.bot.get_guild(data.guild_id)
            user = guild.get_member(data.user_id)
            role = guild.get_role(917000904010510357)
            await user.remove_roles(role)
        else:
            return

  #-----------------------------------------------
  @commands.Cog.listener()
  async def on_voice_state_update(self, member, before, after):
      if after:
          if after.channel:
              if after.channel.id == 906065818855563264:
                  print(f'{member} 已連接')
                  guild = self.bot.get_guild(836167095288332309)
                  maincategory = discord.utils.get(guild.categories, id=906065669206986753)
                  overwrites = {
                      member: discord.PermissionOverwrite(connect=True, mute_members=True, move_members=True,
                                                          manage_channels=True)
                  }
                  channel2 = await guild.create_voice_channel(name=f'{member.display_name}',
                                                              category=maincategory, overwrites=overwrites)

                  await member.move_to(channel2)

                  def check(x, y, z):
                      return len(channel2.members) == 0

                  await self.bot.wait_for('voice_state_update', check=check)
                  await channel2.delete()

  #-----------------------------------------------
  @commands.Cog.listener()
  async def on_message(self, msg):
    msg_content = msg.content.lower()

    link_word = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

    curseWord = ['Free Nitro', 'Discord Free Nitro','free nitro','nitro','Nitro']
    
    reason = '發送詐騙訊息，予以永久驅除之處分！'

    if any(word in msg_content for word in curseWord) and search(link_word, msg.content):
      await msg.delete()
      await msg.channel.send(f'{msg.author.mention}發送詐騙訊息，予以永久驅除之處分！')
      await msg.author.ban(reason=reason)
    #----------------------------------------------------------
    if msg.content.startswith('呀'):
      await msg.add_reaction(":wryyy:904694011128844318")
      await msg.add_reaction(":WHAT_GIF:905115626740260986")


      

def setup(bot):
  bot.add_cog(Event(bot))