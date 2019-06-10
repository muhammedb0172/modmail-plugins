import asyncio
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

Cog = getattr(commands, 'Cog', object)


class Purger(Cog):
    """Delete multiple messages at a time.
    More info: __[click here]__(https://github.com/muhammedb0172/modmail-plugins/tree/master/purger)
    """

    def __init__(self, bot):
        self.bot = bot
        asyncio.create_task(self.api_post())

    async def api_post(self):

        async with self.bot.session.post(
            "https://papiersnipper.herokuapp.com/modmail-plugins/purger/"
            + str(self.bot.user.id)
        ):
            pass


    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def purge(self, ctx, amount: str):
        """Delete the specified amount of messages."""

        try:
            try:
                amount = int(amount)
            except Exception:
                return await ctx.send('That\'s not a valid amount of messages to delete.')

            if amount > 1 and amount < 1000:
                await ctx.channel.purge(limit=amount + 1)
                delete_message = await ctx.send(f'I successfully deleted {amount} messages!')

                await asyncio.sleep(3)
                await delete_message.delete()
            else:
                return await ctx.send('The number of messages to delete has been be between 1 and 1000.')

        except discord.Forbidden:
            return await ctx.send('I don\'t have the proper permissions to delete messages.')


def setup(bot):
    bot.add_cog(Purger(bot))
