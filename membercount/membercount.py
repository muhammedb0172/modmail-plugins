import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

Cog = getattr(commands, 'Cog', object)


class Membercount(Cog):
    """Membercount plugin"""
    
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
        embed.add_field(name="Links",value="Coming soon!")
        embed.footer(text="Thank you for supporting us!")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Membercount(bot))
