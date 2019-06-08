import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

Cog = getattr(commands, 'Cog', object)


class Information(Cog):
    """Information plugin"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def information(self, ctx):
        """Information about this server."""

        embed = discord.Embed(
            title="Information",
            color=discord.Color.blue(),
            description="Welcome to The Xtreme Comminuty!"

Links that are not posted in this channel are not approved or official. Please also follow following rules:

| Do not be rude to anyone. Respect everyone the way you want to be respected.

| Do not spamm or swear in the entire server.

| Do not ping any staff or High Ranks unless it is necesarry.

| To be able to talk please join the roblox group.",
        )
        embed.add_field(name="Links",value="Coming soon!")
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
