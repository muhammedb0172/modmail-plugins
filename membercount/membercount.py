import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

Cog = getattr(commands, 'Cog', object)


class Membercount(Cog):
    """Shows you the amount of people that are in the currwnt server!"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def membercount(self, ctx):
        """Shows you how many members there are in this server."""

        mc = ctx.guild.member_count
        embed = discord.Embed(
            title="Members",
            color=discord.Color.red(),
            description = f"{mc} amount of people are in the server!"
        )
        embed.add_field(name="Q: Who made this?",value="A: By AshyHi#2158")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Membercount(bot))
