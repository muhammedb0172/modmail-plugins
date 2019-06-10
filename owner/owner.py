import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

Cog = getattr(commands, 'Cog', object)


class Owner(Cog):
    """Info of your the bot his owner!\nAre you interested in the Owner?\nThen use this command right here, right **NOW**!"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def owner(self, ctx):
        """Shows you a little info of the bot his owner!\nWith links! [BETA]"""

        embed = discord.Embed(
            title="Owner of the bot his little info.",
            color=discord.Color.green(),
            description="Look under this sentence!\nAll the link are listed under here!"
            
        )
        embed.add_field(name="Q: Who made this?",value="A: By AshyHi#2158")
        embed.add_field(name="UTube",value="[Click Here](https://www.youtube.com/channel/UCs71Z0iOVIMko0-EbFtuSSg)")
        embed.add_field(name="TTV",value="[Click Here](https://twitch.tv/nofailstudios)")
        embed.add_field(name="Coming soon.",value="Wait pls!")
        embed.set_footer(text="Do before baby shark eats you KID")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Owner(bot))
