import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

Cog = getattr(commands, 'Cog', object)


class Member Count(Cog):
    """Information plugin"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def membercount(self, ctx):
        """How many members there are in this server."""

        mc = ctx.guild.member_count
        embed = discord.Embed(
            title="Members",
            color=discord.Color.red(),
            description = "mc amount of people are in the server!"
        )
        embed.add_field(name="Links",value="Coming soon!")
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
