import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

Cog = getattr(commands, 'Cog', object)


class Serverinfo(Cog):
    """Info of your current server!"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def serverinfo(self, ctx):
        """Shows you a little info your server!"""

        mc = ctx.guild.member_count
        rc = len()ctx.guild.roles
        embed = discord.Embed(
            title="Serverinfo!",
            color=discord.Color.red(),
            description = f"{mc} amount of people are in the server!\n{rc} amount of roles are in the server!"
            
        )
        embed.add_field(name="Q: Who made this?",value="A: By AshyHi#2158")
        embed.add_field(name="Are there coming more stuff?",value="Yes! Ofcourse! But you just need to wait!")
        embed.add_field(name="Links?",value="Please wait. And update the bot daily and use the command to when the link is here!")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Serverinfo(bot))
