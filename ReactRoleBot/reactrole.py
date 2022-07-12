import discord
from discord.ext import commands

roles = {
  "<emoji 1>":"<Role 1>", 
  "<emoji 2>":"<Role 2>", 
  "<emoji 3>":"<Role 3>", 
  "<emoji 4>":"<Role 4>", 
  "<emoji 5>":"<Role 5>",
  "<emoji 6>":"<Role 6>",
  "<emoji 7>":"<Role 7>",
  "<emoji 8>":"<Role 8>"
  }

class Reactrole(commands.Cog):
  def __init__ (self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
        print('Bot is online. -React Role')

  @commands.Cog.listener()
  async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
      if guild.id == <enter server ID>:
        msg = f'Welcome {member.mention} to {guild.name} <add emojis here>! \n Head over to <channel id of react-role channel>to get some roles'
        await guild.system_channel.send(msg)

  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    if payload.message_id == <enter message ID of react role message/take from database>:
    
      chn = self.client.get_channel(<enter channel ID of react role channel>)

      serverID = payload.guild_id
      server = discord.utils.find(lambda g : g.id == serverID, self.client.guilds)
    
      member = payload.member

      role = None
      if str(payload.emoji) in roles.keys():
        role = discord.utils.get(server.roles, name = roles[str(payload.emoji)])
      if member is not None:
        if role is not None:
          await member.add_roles(role)
          await chn.send(f"Added {role} role to <@!{payload.user_id}>", delete_after = 30)
    
  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, payload):
    if payload.message_id == <enter message ID of react role message/take from database>:
    
      chn = self.client.get_channel(<enter channel ID of react role channel>)

      serverID = payload.guild_id
      server = discord.utils.find(lambda g : g.id == serverID, self.client.guilds)

      role = None

      if str(payload.emoji) in roles.keys():
        role = discord.utils.get(server.roles, name = roles[str(payload.emoji)])
    
      member = discord.utils.find(lambda m: m.id == payload.user_id, server.members)
      if member is not None:
        if role is not None:
          await member.remove_roles(role)
          await chn.send(f"Removed {role} role from <@!{payload.user_id}>", delete_after = 30)

  @commands.command()
  async def reactinit(self, ctx):
    if ctx.author.id != 719886641401036861:
      await ctx.message('Denied!')
      return
    channel = self.client.get_channel(<enter channel id of react role channel>)
    msg = "React to get yourself the following roles:\n"
    for key in roles.keys():
      msg += f"{key} - {roles[key]} \n"

    message = await channel.send(msg)

    for key in roles.keys():
      await message.add_reaction(key)
  

def setup(client):
  client.add_cog(Reactrole(client))
