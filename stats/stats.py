import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

#Cog = getattr(commands, 'Cog', object)

class Stats(commands.Cog):

    """Get useful stats directly in an embed about either the ModMail bot, a user or the server."""

    

    def __init__(self, bot):

        self.bot = bot
  
    @commands.group(name="stats", aliases=["stat"], invoke_without_command=True)
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def stats(self, ctx):
        """Get a cool embed with a lot of cool stats about your ModMail, server or a user"""

        await ctx.send_help(ctx.command)
        
   
    @stats.command(name="server")
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def server(self, ctx):
        """Get a cool embed with many useful stats about your server"""


        embed = discord.Embed(

            color=discord.Color.blue(),

            description=f"**Here are the stats for {ctx.guild.name}, enjoy them:**",

        )
                
        humans = 0
        bots = 0
        for m in ctx.guild.members:
          if m.bot:
             bots += 1
          else:
             humans += 1
                
        online = 0
        for m in ctx.guild.members:
          if m.status != discord.Status.offline:
             online += 1
          else:
             continue
                
        embed.add_field(name=f"Member Count",value=f"{ctx.guild.member_count}, {humans} are humans and {bots} are bots, {online} are online")
        embed.add_field(name="Guild ID",value=f"{ctx.guild.id}")
        embed.add_field(name="Categories",value=f"{len(ctx.guild.categories)}")
        embed.add_field(name="Text Channels",value=f"{len(ctx.guild.text_channels)}")
        embed.add_field(name="Voice Channels",value=f"{len(ctx.guild.voice_channels)}")
        embed.add_field(name="Roles",value=f"{len(ctx.guild.roles)}")
        embed.add_field(name="Server Region",value=f"{ctx.guild.region}")
        embed.add_field(name=f"Server Owner",value=f"{ctx.guild.owner.mention}")
        embed.add_field(name=f"Created",value=f"{ctx.guild.created_at:%a, %b %d, %Y %X}")
        embed.set_thumbnail(url=str(ctx.guild.icon_url))
        embed.set_footer(text=f'If you have suggestions for more stats, please use the command "?stat info" for more info on how you do it (COMING SOON)')
        embed.set_author(name=f"{ctx.guild.name} stats")

        await ctx.send(embed=embed)
        
    @stats.command(name="bot")
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def bot(self, ctx):

        """Get a neat embed with many useful stats about your ModMail bot"""
	
        #member = f"{self.bot.user.id}"

        embed = discord.Embed(

            color=discord.Color.blue(),

            description=f"**Here are the stats for {self.bot.user.name}, enjoy them:**",

        )
        embed.add_field(name=f"Invite Link For {self.bot.user.name}",value=f"[Invite your bot](https://discordapp.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=268443792&scope=bot)")
        embed.add_field(name="Bot User ID",value=f"`{self.bot.user.id}`")
        embed.add_field(name=f"Bot Prefix",value=f"`{self.bot.prefix}` or {self.bot.user.mention}")
        embed.add_field(name=f"Latency",value=f"{self.bot.latency * 1000:.2f} MilliSeconds / {self.bot.latency:.3f} Seconds")
        embed.add_field(name="Bot Uptime",value=f"{self.bot.uptime}")
        embed.add_field(name=f"Bot Created",value=f"{self.bot.user.created_at:%a, %b %d, %Y %X}")
        #embed.add_field(name=f"Bot Join Date",value=f"{member.joined_at:%a, %b %d, %Y %X}")
        embed.set_thumbnail(url=str(self.bot.user.avatar_url))
        embed.set_footer(text=f'If you have suggestions for more stats, please use the command "?stat info" for more info on how you do it (COMING SOON)')
        embed.set_author(name=f"{self.bot.user.name} stats")

        await ctx.send(embed=embed)
        
    @stats.command(name="all")
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def all(self, ctx):

        """Sends All Stats Embeds At Once"""

        await ctx.invoke(self.bot.get_command("stats bot"))
        await ctx.invoke(self.bot.get_command(f'stats server'))
        await ctx.invoke(self.bot.get_command("stats user"))
        
	
    @stats.command(name="user")
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def user(self, ctx, member: discord.Member = None):

        """Get A Cool Embed With Many Useful Stats About A User"""
		
        if member is None:
            member = ctx.author

        embed = discord.Embed(

            color=discord.Color.blue(),

            description=f"**Here are the stats for {member.name}, enjoy them:**",

        )
	
        roles = ""
        for r in ctx.author.roles:
            if r.name != "@everyone":
               roles += f"{r.mention} "

        embed.add_field(name=f"User Created",value=f"{member.created_at:%a, %b %d, %Y %X}")
        embed.add_field(name="User ID",value=f"`{member.id}`")
        embed.add_field(name="User Roles",value=f"{roles}")
        embed.add_field(name=f"User Joined",value=f"{member.joined_at:%a, %b %d, %Y %X}")
        embed.add_field(name="User Status",value=f"{member.status}")
        embed.set_thumbnail(url=str(member.avatar_url))
        embed.set_footer(text=f'If you have suggestions for more stats, please use the command "?stat info" for more info on how you do it (COMING SOON)')
        embed.set_author(name=f"{member.name}'s stats")

        await ctx.send(embed=embed)
        
def setup(bot):

    bot.add_cog(Stats(bot))
