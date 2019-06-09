mc = ctx.guild.member_count
em = discord.Embed(color=bot.main_color, description=mc, title="Current Members")
em.set_footer(text="This is how many members we have currently!")
await ctx.send(embed=em)
